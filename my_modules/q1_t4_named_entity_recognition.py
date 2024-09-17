import csv
import os
import warnings
from collections import Counter

import spacy
import torch
from tqdm import tqdm
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline

warnings.simplefilter(action="ignore", category=FutureWarning)


class NERProcessor:
    """
    A class to perform Named Entity Recognition (NER) using either BioBERT or scispaCy models
    and extract counts of diseases and drugs from a text file.
    """

    def __init__(self, input_file, output_file, model_name, model_type):
        """
        Initialize the NERProcessor instance with the specified model.

        Args:
            input_file (str): Path to the text file to be tokenized.
            output_file (str): Path where the output CSV file will be saved.
            model_name (str): The pretrained model to use.
            model_type (str): The type of model ('biobert' or 'scispacy').
        """
        self.input_file = input_file
        self.output_file = output_file
        self.model_name = model_name
        self.model_type = model_type.lower()

        if self.model_type == "biobert":
            self.model, self.tokenizer = self.load_biobert_model_and_tokenizer()
            # Use the Hugging Face pipeline for token classification
            self.ner_pipeline = pipeline(
                "ner",
                model=self.model,
                tokenizer=self.tokenizer,
                device=0 if torch.cuda.is_available() else -1,
                batch_size=8,  # Adjust batch size as needed
            )
        elif self.model_type == "scispacy":
            self.ner_model = spacy.load(self.model_name)
            self.ner_model.max_length = 1500000  # Set the maximum length for processing
        else:
            raise ValueError("Invalid model_type. Choose 'biobert' or 'scispacy'.")

    def load_biobert_model_and_tokenizer(self):
        """
        Loads the tokenizer and model for the specified BioBERT model.

        Returns:
            model: The loaded model.
            tokenizer: The loaded tokenizer.
        """
        # Load the tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        model = AutoModelForTokenClassification.from_pretrained(self.model_name)

        # Move the model to GPU if available
        if torch.cuda.is_available():
            model = model.to("cuda")
            print("BioBERT model loaded on GPU")
        else:
            print("Running BioBERT model on CPU")

        return model, tokenizer

    def perform_ner(self):
        """
        Performs NER on the input file and saves the results to the output file.
        """
        # Check if the input file exists
        if not os.path.isfile(self.input_file):
            print(f"Error: The file '{self.input_file}' does not exist.")
            return

        # Check if the output directory exists; create it if not
        output_dir = os.path.dirname(self.output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created the output directory: {output_dir}")

        # Load the text from the file
        with open(self.input_file, "r", encoding="utf-8") as text_file:
            text = text_file.read()

        if self.model_type == "biobert":
            # Process the text using BioBERT
            diseases_counts, drugs_counts = self.process_text_biobert(text)
        elif self.model_type == "scispacy":
            # Process the text using scispaCy
            diseases_counts, drugs_counts = self.process_text_scispacy(text)
        else:
            raise ValueError("Invalid model_type. Choose 'biobert' or 'scispacy'.")

        # Save the results to a CSV file
        self.save_counts_to_csv(self.output_file, diseases_counts, drugs_counts)

    def process_text_biobert(self, text):
        """
        Processes the text using the BioBERT NER pipeline and extracts entities.

        Args:
            text (str): The text to process.

        Returns:
            tuple: Counters for diseases and drugs.
        """
        diseases_counts = Counter()
        drugs_counts = Counter()

        # Split the text into chunks of size 512 for processing
        chunk_size = 512
        text_chunks = [
            text[i : i + chunk_size] for i in range(0, len(text), chunk_size)
        ]

        for chunk in tqdm(
            text_chunks, desc="Processing Chunks with BioBERT", unit="chunk"
        ):
            # Run NER on the chunk
            ner_results = self.ner_pipeline(chunk)

            # Combine subword tokens into full entities
            combined_entities = self.combine_entities_biobert(ner_results)

            if combined_entities is None:
                continue  # Skip if there are no entities

            # Filter entities based on labels
            diseases = [
                entity[0] for entity in combined_entities if "Disease" in entity[1]
            ]
            drugs = [
                entity[0] for entity in combined_entities if "Chemical" in entity[1]
            ]

            # Update counters
            diseases_counts.update(diseases)
            drugs_counts.update(drugs)

        return diseases_counts, drugs_counts

    def combine_entities_biobert(self, ner_results):
        """
        Combines subword tokens (with '##') into full words for BioBERT.

        Args:
            ner_results (list): List of NER results from the BioBERT pipeline.

        Returns:
            list: A list of tuples containing the combined entity and its label.
        """
        entities = []
        current_entity = ""
        current_label = None

        for result in ner_results:
            word = result["word"]
            label = result["entity"]

            # Handle subword tokens
            if word.startswith("##"):
                current_entity += word[2:]
            else:
                if (
                    current_entity and current_label
                ):  # Safeguard against appending empty entities
                    entities.append((current_entity, current_label))
                current_entity = word
                current_label = label

        # Append the last entity if any
        if (
            current_entity and current_label
        ):  # Safeguard against appending empty entities
            entities.append((current_entity, current_label))

        return entities if entities else None  # Return None if no entities found

    def process_text_scispacy(self, text):
        """
        Processes the text using the scispaCy NER model and extracts entities.

        Args:
            text (str): The text to process.

        Returns:
            tuple: Counters for diseases and drugs.
        """
        diseases_counts = Counter()
        drugs_counts = Counter()

        # Split the text into chunks for processing
        chunk_size = 1500000  # As per original code
        text_chunks = [
            text[i : i + chunk_size] for i in range(0, len(text), chunk_size)
        ]

        print(f"Total number of chunks: {len(text_chunks)}")

        for chunk in tqdm(
            text_chunks, desc="Processing Chunks with scispaCy", unit="chunk"
        ):
            doc = self.ner_model(chunk)

            # Extract tokens and their entity types from the NER model output
            tokens_entities = [(token.text, token.ent_type_) for token in doc]

            # Separate diseases and drugs
            diseases = [token[0] for token in tokens_entities if token[1] == "DISEASE"]
            drugs = [token[0] for token in tokens_entities if token[1] == "CHEMICAL"]

            # Update counters
            diseases_counts.update(diseases)
            drugs_counts.update(drugs)

        return diseases_counts, drugs_counts

    def save_counts_to_csv(self, output_file_path, diseases_counts, drugs_counts):
        """
        Saves the disease and drug counts to a CSV file.

        Args:
            output_file_path (str): Path to save the CSV file.
            diseases_counts (Counter): Counter of disease entities.
            drugs_counts (Counter): Counter of drug entities.
        """
        with open(output_file_path, "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Entity Type", "Word", "Count"])

            # Write disease entries
            for word, count in diseases_counts.most_common():
                csv_writer.writerow(["Disease", word, count])

            # Write drug entries
            for word, count in drugs_counts.most_common():
                csv_writer.writerow(["Drug", word, count])

        print(f"Ordered word counts saved to {output_file_path}")
