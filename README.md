# HIT137-SoftwareNow-Assignment-2-CAS309

## Project Setup

### **Important: Download CSV Files**

Before running the project, you **must download the required CSV files** from the `datasets` folder link provided. After downloading, place all the CSV files into the `input/` folder within the repository. Without these files, the project will not function as expected.

1. **Dataset Link**: [Download CSV Files](https://drive.google.com/drive/folders/1Lgp7fhB6M6tdfv1Um46FzmsIDCD5g5fW?usp=sharing)

2. **Create an `input/` folder** in the root directory of the project if it doesn't exist:
   ```bash
   mkdir input
   ```

### Python Version

This project requires Python 3.10 or 3.11 to run. Ensure you have the correct Python version installed.

### Install Dependencies

#### Using a Virtual Environment (Recommended):

1. **Create a Virtual Environment**:
   - Run the following command to create a new virtual environment:
     ```bash
     python3 -m venv venv
     ```
2. **Activate the Virtual Environment**:

   - On macOS/Linux, use:
     ```bash
     source venv/bin/activate
     ```
   - On Windows, use:
     ```bash
     venv\Scripts\activate
     ```

3. **Upgrade `pip` (Optional but recommended)**:

   - Once the virtual environment is activated, it’s a good idea to upgrade `pip`:
     ```bash
     pip install --upgrade pip
     ```

4. **Install the Required Libraries**:

   - With the virtual environment activated, install the dependencies listed in `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

5. **Verify Installation**:

   - Ensure all packages are correctly installed by running:
     ```bash
     pip list
     ```

6. **Run the Project**:
   - Once the dependencies are installed, run the project:
     ```bash
     python main.py
     ```
