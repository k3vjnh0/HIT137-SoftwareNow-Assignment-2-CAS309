import os
import time

from PIL import Image


class ImageModifier:
    """
    A class to modify an image by adjusting its pixel values based on a generated number.
    """

    def __init__(self, input_file, output_file):
        """
        Initialize the ImageModifier instance.

        Args:
            input_file (str): Path to the input image file.
            output_file (str): Path where the modified image will be saved.
        """
        self.input_file = input_file
        self.output_file = output_file

    def modify_image(self):
        """
        Modifies the image by adjusting pixel values and saves the new image.
        Also calculates the sum of all red pixel values in the new image.
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

        # Generate the number based on the current time
        generated_number = (int(time.time()) % 100) + 50
        generated_number += 10 if generated_number % 2 == 0 else 0

        # Load and convert the image to RGB
        image = Image.open(self.input_file).convert("RGB")
        image_width, image_height = image.size
        pixels = image.load()

        # Create a new image to store modified pixels
        new_image = Image.new("RGB", (image_width, image_height))
        new_pixels = new_image.load()

        n = generated_number

        # Modify each pixel and calculate the sum of all red pixels simultaneously
        sum_red_pixels = 0
        for i in range(image_width):
            for j in range(image_height):
                r, g, b = pixels[i, j]

                # Adjust pixel values with wrapping around 256
                r = (r + n) % 256
                g = (g + n) % 256
                b = (b + n) % 256

                new_pixels[i, j] = (r, g, b)
                sum_red_pixels += r

        # Save the new image
        new_image.save(self.output_file)
        print(f"Image saved to {self.output_file}")
        print(f"The sum of all red pixels is: {sum_red_pixels}")
