import pandas as pd
# Specify the CSV file path
file_path = '/path/to/LargeFileUnreadable.csv'

# Define the chunk size (number of rows per smaller file)
chunk_size = 100000  # Adjust this as needed

# Set the counter for file parts
part_number = 1

try:
    # Read and split the file into chunks
    for chunk in pd.read_csv(file_path, chunksize=chunk_size, low_memory=False):
        # Define the output file name
        output_file = f'output_part_{part_number}.csv'
        
        # Save each chunk to a new CSV file
        chunk.to_csv(output_file, index=False)
        
        print(f'Created: {output_file}')
        part_number += 1
except FileNotFoundError:
    print(f"File not found: {file_path}")
except pd.errors.EmptyDataError:
    print(f"The file {file_path} is empty or corrupted.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
