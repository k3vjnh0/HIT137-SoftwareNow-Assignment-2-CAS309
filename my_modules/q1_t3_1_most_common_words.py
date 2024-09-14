import csv
import os
import re
from collections import Counter


class TopWordsExtractor:
    """
    A class to extract the top N most common words from a text file and save them to a CSV file.
    """

    def __init__(self, input_file, output_file, top_n):
        """
        Initialize the TopWordsExtractor instance.

        Args:
            input_file (str): Path to the text file to be tokenized.
            output_file (str): Path where the output CSV file will be saved.
            top_n (int): Number of top words to save.
        """
        self.input_file = input_file
        self.output_file = output_file
        self.top_n = top_n

    def extract_top_words(self):
        """
        Extracts the top N most common words from the input text file and saves them to the output CSV file.
        """
        # Check if the input file exists
        if not os.path.isfile(self.input_file):
            print(f"Error: The file '{self.input_file}' does not exist.")
            return

        # Check if the output directory exists, create it if not
        output_dir = os.path.dirname(self.output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created the output directory: {output_dir}")

        # Load and normalize the text
        with open(self.input_file, "r") as file:
            text = file.read().lower()

        # Count word occurrences
        words = re.findall(r"\b[a-z]+(?:-[a-z]+)?\b", text)
        word_counts = Counter(words)

        # Identify the top N most common words
        top_words = word_counts.most_common(self.top_n)

        # Write the results to a CSV file
        with open(self.output_file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Word", "Count"])  # Header
            writer.writerows(top_words)

        print(f"Top {self.top_n} words have been written to '{self.output_file}'.")
