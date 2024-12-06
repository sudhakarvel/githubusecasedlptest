# Process CSV File to expand row values

This script processes a CSV file, expanding rows where the `externalUsers` column contains semicolon-separated values into individual rows. It saves the processed data to a new CSV file.

---

## Prerequisites
Ensure the following are installed:
- Python 3.7+ 
- `pip3` (Python package manager)

---

## Steps to Use

### 1. Clone or Copy the Project
Save the script as `explode.py` and place it in a directory of your choice.

---

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

### 4. Prepare Input CSV File
Save your input file as `input.csv` in the same directory or specify its path in the script.

---

### 5. Run the Script
Execute the script with the following command:

```bash
python3 explode.py
```

---

### 6. Output
The script will:
- Read the input file (default: `input.csv`).
- Expand rows where the `externalUsers` column has semicolon-separated values into separate rows.
- Save the processed data to a file named `output.csv`.

A success message will confirm the output file's location.

---

## Example Input/Output

### Input (`input.csv`):
| Name     | externalUsers        |
|----------|----------------------|
| John Doe | user1@example.com;user2@example.com |

### Output (`output.csv`):
| Name     | externalUsers        |
|----------|----------------------|
| John Doe | user1@example.com    |
| John Doe | user2@example.com    |

---

## Notes
- Modify `input_file` and `output_file` variables in the script if needed.
- Ensure input files are formatted correctly with a column named `externalUsers`.

---



