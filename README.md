# Truecaller Bulk Search Script

## 1. Set Up Your Environment

- **Install Python**: Make sure Python is installed on your machine. Download it from [python.org](https://www.python.org/downloads/).
- **Install Pip**: Pip comes with Python. Verify by running `pip --version` in your command prompt or terminal.
- **Install Necessary Packages**:
  - Open a command prompt or terminal and run:
    ```bash
    pip install pandas openpyxl asyncio truecallerpy
    ```

## 2. Prepare the Excel File

- **Create an Excel File**:
  - Open Excel and create a new workbook.
  - Enter phone numbers in the first column (e.g., column A) without any country code or symbols.
  - Save the file as `phone_numbers.xlsx` in the same directory where the script will be located.

## 3. Set Up the Script

- **Download the Script**:
  - Copy the provided Python script into a text editor (e.g., Notepad++).
  - Save it as `truecaller_scrap.py` in the same directory as your `phone_numbers.xlsx` file.

## 4. Customize the Script

- **Installation ID**:
  - Replace the placeholder installation ID `'a1i0Y--ohnh2OF7VRIKww8gLfg3OBNIzyC26L-h5p5H_cyetVOEJnLSKC7O-lFum'` with your actual installation ID from Truecaller.
- **File Path**:
  - Ensure the `file_path` variable points to the correct location of your `phone_numbers.xlsx` file. If the script and Excel file are in the same directory, no changes are needed.

## 5. Run the Script

- **Execute the Script**:
  - Open a command prompt or terminal in the directory where your script and Excel file are located.
  - Run the script using Python:
    ```bash
    python truecaller_scrap.py
    ```
- **Wait for Completion**:
  - The script will process the phone numbers, perform a bulk search via the Truecaller API, and write the results back into the Excel file.
  - Once completed, the script will output a confirmation message: `Names have been successfully written to the Excel sheet.`
