import pandas as pd
import asyncio
from truecallerpy import bulk_search

file_path = './phone_numbers.xlsx'
installation_id = 'a1i0Y--ohnh2OF7VRIKww8gLfg3OBNIzyC26L-h5p5H_cyetVOEJnLSKC7O-lFum'

async def perform_bulk_search(phone_numbers, country_code, installation_id):
    response = await bulk_search(phone_numbers, country_code, installation_id)
    return response

def main():
    # Load the Excel file
    df = pd.read_excel(file_path, engine='openpyxl', dtype=str)  # Ensure numbers are read as strings

    # Construct a comma-separated string of phone numbers
    phone_numbers = ','.join(df.iloc[:, 0])

    # Define your country code and installation ID
    country_code = 'IN'

    # Perform bulk search
    response = asyncio.run(perform_bulk_search(phone_numbers, country_code, installation_id))

    # Extract results and write to the second column
    results = []
    if 'data' in response and 'data' in response['data']:
        data_entries = response['data']['data']
        data_dict = {entry['key']: entry['value'] for entry in data_entries}
        for number in df.iloc[:, 0]:
            number_str = number
            if number_str in data_dict:
                result = data_dict[number_str].get('name', 'No name available')
                results.append(result)
            else:
                results.append('No data found')
    else:
        # Handle case where the response does not contain the expected data
        results = ['No data found'] * len(df)

    df['Response'] = results

    # Save the updated DataFrame back to the Excel file
    df.to_excel(file_path, index=False, engine='openpyxl')

    # Print final confirmation message
    print("Names have been successfully written to the Excel sheet.")

if __name__ == "__main__":
    main()
