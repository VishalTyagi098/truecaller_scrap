
### 1. Set Up Your Environment

- **Install Python**: Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).
- **Install Pip**: Pip is usually installed with Python. Verify by running `pip --version` in your command prompt or terminal.
- **Install Necessary Packages**:
  - Open a command prompt or terminal and run the following commands:
    ```bash
    pip install pandas openpyxl asyncio truecallerpy
    ```

### 2. Prepare the Excel File

- **Create an Excel File**:
  - Open Excel and create a new workbook.
  - In the first column (e.g., column A), enter the phone numbers without any country code or symbols.
  - Save the file as `phone_numbers.xlsx` in the same directory where the script will be located.

### 3. Truecaller Login and InstallationId

- **Login**:
  - Log in to your Truecaller account using the following command:
    ```bash
    truecallerpy login
    ```
  - If you encounter any errors, try running the command with administrative privileges (e.g., `sudo truecallerpy login` on Linux or running the command prompt as administrator on Windows).

- **Get InstallationId**:
  - Retrieve your Truecaller InstallationId with the command:
    ```bash
    truecallerpy --installationid
    ```
  - Copy this InstallationId for use in the script.

### 4. Set Up the Script

- **Download the Script**:
  - Copy the provided Python script into a text editor (e.g., Notepad++) and save it with the name `truecaller_scrap.py` in the same directory as your `phone_numbers.xlsx`.

### 5. Customize the Script

- **Installation ID**:
  - Replace the placeholder InstallationId `'a1i0Y--ohnh2OF7VRIKww8gLfg3OBNIzyC26L-h5p5H_cyetVOEJnLSKC7O-lFum'` in the script with your actual InstallationId from Truecaller.
  
- **File Path**:
  - Ensure the `file_path` variable points to the correct location of your `phone_numbers.xlsx` file. If the script and Excel file are in the same directory, no changes are needed.

### 6. Run the Script

- **Execute the Script**:
  - Open a command prompt or terminal in the directory where your script and Excel file are located.
  - Run the script using Python:
    ```bash
    python truecaller_scrap.py
    ```
