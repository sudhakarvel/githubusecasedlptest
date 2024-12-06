import pandas as pd

input_file = "Book2.csv"  # Replace with your file path
output_file = "opoutput.csv"  # Specify output file path
df = pd.read_csv(input_file)
df_expanded = df.assign(
    externalUsers=df['externalUsers'].str.split(';')
).explode('externalUsers')
df_expanded.to_csv(output_file, index=False)
print(f"Data has been processed and saved to {output_file}")

