from setuptools import find_packages, setup

setup(
    name="hit137-assignment2-cas308",
    version="1.0",
    packages=find_packages(),
    python_requires=">=3.10, <3.12",  # Ensuring Python 3.10 or 3.11 is used
    install_requires=[
        # List your dependencies here, or use the requirements.txt method
    ],
    entry_points={
        "console_scripts": [
            "run-main = main:main",  # We have a main function in main.py
        ],
    },
)
