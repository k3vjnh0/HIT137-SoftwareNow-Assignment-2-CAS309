import csv
import os
import re
import warnings
from collections import Counter

from tqdm import tqdm
from transformers import AutoTokenizer

warnings.simplefilter(action="ignore", category=FutureWarning)


class UniqueTokenCounter:
    """
    A class to count unique tokens in a text file using a specified tokenizer model
    and save the top N tokens to a CSV file.
    """

    def __init__(self, input_file, output_file, model_name, top_n):
        """
        Initialize the UniqueTokenCounter instance.

        Args:
            input_file (str): Path to the text file to be tokenized.
            output_file (str): Path where the output CSV file will be saved.
            model_name (str): Pretrained model name for the tokenizer.
            top_n (int): Number of top tokens to save.
        """
        self.input_file = input_file
        self.output_file = output_file
        self.model_name = model_name
        self.top_n = top_n

    def count_unique_tokens(self):
        """
        Counts unique tokens in the input text file using the specified tokenizer
        and saves the top N tokens to the output CSV file.
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

        # Load the tokenizer with the fast implementation
        tokenizer = AutoTokenizer.from_pretrained(self.model_name, use_fast=True)

        # Initialize a Counter to keep track of unique tokens
        unique_tokens = Counter()

        # Regular expression for refining tokens
        token_pattern = re.compile(r"\b[a-z]+(?:-[a-z]+)?\b")

        # Determine the total size for progress bar
        total_size = os.path.getsize(self.input_file)

        # Process the text file in chunks to avoid loading the entire file into memory
        chunk_size = 1024 * 1024  # 1 MB chunks

        # Use a single with statement with multiple contexts
        with open(self.input_file, "r", encoding="utf-8") as f, tqdm(
            total=total_size, unit="B", unit_scale=True, desc="Processing File"
        ) as pbar:
            while True:
                text_chunk = f.read(chunk_size)
                if not text_chunk:
                    break

                # Tokenize the text chunk
                tokens = tokenizer.tokenize(text_chunk)

                # Refine tokens using the regular expression
                refined_tokens = []
                for token in tokens:
                    refined_tokens.extend(re.findall(token_pattern, token.lower()))

                # Update the counter with the refined tokens
                unique_tokens.update(refined_tokens)

                pbar.update(len(text_chunk.encode("utf-8")))

        # Get the top N most common tokens
        top_tokens = unique_tokens.most_common(self.top_n)

        # Write the results to the output CSV file
        with open(self.output_file, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Token", "Count"])
            writer.writerows(top_tokens)

        print(f"Top {self.top_n} tokens and counts saved to: {self.output_file}")
