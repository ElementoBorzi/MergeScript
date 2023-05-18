import csv
import os

race_id_filter = '5'

input_file_name = r'C:\Users\Rafae\OneDrive\Área de Trabalho\Mesa de Trabalhos\Python Scripts\CharacterFacialHairStylesHD.csv'
output_file_name = r'C:\Users\Rafae\OneDrive\Área de Trabalho\Mesa de Trabalhos\Python Scripts\CharacterFacialHairStylesCustom.csv'
temp_file_name = r'C:\Users\Rafae\OneDrive\Área de Trabalho\Mesa de Trabalhos\Python Scripts\Temp.csv'

columns = ["ID","RaceID","SexID","VariationID","Geoset_1","Geoset_2","Geoset_3","Geoset_4","Geoset_5"]

print("Starting the script...")

try:
    total_rows = sum(1 for row in open(input_file_name, 'r')) - 1
    print(f"Total number of lines in the input file: {total_rows}")
except Exception as e:
    print(f"Error opening the input file: {e}")
    input("\nPress Enter to close...")
    exit()

try:
    input_data = {}
    with open(input_file_name, 'r') as input_file:
        reader = csv.DictReader(input_file)
        for row in reader:
            if row['RaceID'] == race_id_filter:
                input_data[row['ID']] = row

    for id, data in input_data.items():
        print(f"ID: {id}, Data: {data}")

    is_output_file_empty = os.stat(output_file_name).st_size == 0

    with open(output_file_name, 'r') as output_file, open(temp_file_name, 'w', newline='') as temp_file:
        writer = csv.DictWriter(temp_file, fieldnames=columns, quoting=csv.QUOTE_ALL)

        writer.writeheader()

        if is_output_file_empty:
            for i, row in enumerate(input_data.values()):
                print(f"Writing to output: {row}")  
                writer.writerow(row)
                progress = (i + 1) / len(input_data) * 100
                print(f"Writing line {i+1} to the temporary file. Progress: {progress:.2f}%")
                print(f"Modified columns: {', '.join(columns)}\n")
        else:
            for i, row in enumerate(csv.DictReader(output_file)):
                print(f"Reading line {i+1} from the output file. RaceID: {row['RaceID']}")

                if row['RaceID'] == race_id_filter and row['ID'] in input_data:
                    row = input_data.get(row['ID'], row)
                    progress = (i + 1) / total_rows * 100
                    print(f"Writing to output: {row}")  
                    print(f"Writing line {i+1} to the temporary file. Progress: {progress:.2f}%")
                    print(f"Modified columns: {', '.join(columns)}\n")
                     # Write the row to the temporary file, regardless of its RaceID
                writer.writerow(row)

    # Rename the temporary file to replace the old output file
    os.remove(output_file_name)
    os.rename(temp_file_name, output_file_name)

    print("Script finished successfully.")
    print(r'''

███████╗██╗░░░░░███████╗███╗░░░███╗███████╗███╗░░██╗████████╗░█████╗░░░░░░░██████╗░░█████╗░██████╗░███████╗██╗
██╔════╝██║░░░░░██╔════╝████╗░████║██╔════╝████╗░██║╚══██╔══╝██╔══██╗░░░░░░██╔══██╗██╔══██╗██╔══██╗╚════██║██║
█████╗░░██║░░░░░█████╗░░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░██║░░██║█████╗██████╦╝██║░░██║██████╔╝░░███╔═╝██║
██╔══╝░░██║░░░░░██╔══╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░██║░░██║╚════╝██╔══██╗██║░░██║██╔══██╗██╔══╝░░██║
███████╗███████╗███████╗██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░╚█████╔╝░░░░░░██████╦╝╚█████╔╝██║░░██║███████╗██║
╚══════╝╚══════╝╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝
''')

except Exception as e:
    print(f"An error occurred: {e}")

print("\nPress Enter to close...")
input()