

# CSV Splitter Utility

This Python script splits large CSV files into smaller chunks based on a specified number of rows per chunk.

## Features
- Handles large CSV files efficiently using pandas.
- Configurable chunk size.
- Handles columns with mixed data types.

## Prerequisites
Ensure the following are installed:
- Python 3.7+ 
- `pip3` (Python package manager)

---

## Steps to Use

### 1. Clone or Copy the Project
Clone or download this repository.


### 2. Create a Python Virtual Environment
Run the following commands to create and activate a virtual environment:


Create and activate the virtual environment

```
python3 -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

---

### 3. Install Required Packages


```bash
pip3 install -r requirements.txt
```

---



## Usage

1. Specify the path to your CSV file in the script (`file_path`).
2. Adjust the `chunk_size` variable as needed to set the number of rows per chunk.
3. Run the script:
   ```bash
   python3 chunk.py
   ```
4. The script will create output files in the same directory, named `output_part_<part_number>.csv`.

## Example

If your CSV file path is `/data/large_file.csv` and you want to split it into chunks of 100,000 rows:

1. Set `file_path = '/data/large_file.csv'` in the script.
2. Run the script as instructed.

### Output
The output files will be named sequentially, e.g., `output_part_1.csv`, `output_part_2.csv`, etc.
