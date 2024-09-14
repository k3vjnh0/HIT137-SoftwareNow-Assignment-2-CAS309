import os

import pandas as pd


class CSVTextExtractor:
    """
    A class to extract text from CSV files in a directory and write it to an output file.
    """

    def __init__(self, input_file, output_file, text_cols=None):
        """
        Initialize the CSVTextExtractor instance.

        Parameters:
        - input_file: Directory containing CSV files.
        - output_file: Path for the extracted text to be written.
        - text_cols: A list of columns to extract text from. If None, all columns will be extracted.
        """
        self.input_file = input_file
        self.output_file = output_file
        self.text_cols = text_cols

    def extract_text_from_csv_files(self):
        """
        Extract text from CSV files and write it to an output file.
        """
        # Check if the input directory exists
        if not os.path.isdir(self.input_file):
            print(f"Error: The directory '{self.input_file}' does not exist.")
            return

        # Check if the output directory exists, create it if not
        output_dir = os.path.dirname(self.output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created the output directory: {output_dir}")

        # Open the output file for writing
        with open(self.output_file, "w") as f:
            for file in os.listdir(self.input_file):
                if file.endswith(".csv"):
                    file_path = os.path.join(self.input_file, file)

                    try:
                        # Read the CSV file
                        df = pd.read_csv(file_path)

                        # If text_cols is provided, check which of the specified columns exist
                        if self.text_cols:
                            available_cols = [
                                col for col in self.text_cols if col in df.columns
                            ]

                            if not available_cols:
                                print(
                                    f"Warning: None of the specified columns {self.text_cols} were found in {file}. Skipping this file."
                                )
                                continue
                        else:
                            # If text_cols is None, extract all columns
                            available_cols = df.columns

                        # Combine the available columns into a single text column
                        df["combined_text"] = df[available_cols].apply(
                            lambda row: " ".join(row.dropna().astype(str)), axis=1
                        )

                        # Write the combined text to the output file
                        df["combined_text"].dropna().to_csv(
                            f, header=False, index=False
                        )

                    except Exception as e:
                        print(f"Error processing {file}: {e}")

        print(f"Text extracted successfully to {self.output_file}")
