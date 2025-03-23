# pyCCDA

A lightweight Python library for parsing raw C-CDA (Consolidated Clinical Document Architecture) documents without the need to understand the entire specification. If you're using [BlueButton.js](https://github.com/blue-button/bluebutton.js/) this maintains much of the same functionality.

Test documents from various vendors available [here](https://github.com/jmandel/sample_ccdas).

## Features

- Parse CCDA documents into Python objects
- Extract structured data from CCDA documents
- Access common clinical data elements (allergies, medications, problems, etc.)
- Python 3 compatible

## Installation

```bash
pip install pyCCDA
```

## Usage

### Basic Usage

```python
from pyCCDA import CCDA

# Parse a CCDA document
with open('path/to/ccda.xml', 'r') as f:
    ccda_file = f.read()
    
parser = CCDA(ccda_file)

# Access the parsed data
demographics = parser.data.demographics
print(f"Patient: {demographics.name.given[0]} {demographics.name.family}")

# Access other sections
allergies = parser.data.allergies
medications = parser.data.medications
problems = parser.data.problems
procedures = parser.data.procedures
vitals = parser.data.vitals
```

### Available Data Sections

The parser provides access to the following clinical data sections:

- Demographics
- Allergies
- Care Plan
- Chief Complaint
- Encounters
- Functional Statuses
- Immunizations
- Instructions
- Results
- Medications
- Problems
- Procedures
- Smoking Status
- Vitals

## Library Structure

```
pyCCDA/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── _core.py
│   ├── codes.py
│   ├── wrappers.py
│   └── xml.py
├── documents/
│   ├── __init__.py
│   └── ccda.py
└── parsers/
    ├── __init__.py
    ├── ccda.py
    └── _ccda/
        ├── __init__.py
        ├── allergies.py
        ├── care_plan.py
        ├── demographics.py
        ├── document.py
        ├── encounters.py
        ├── free_text.py
        ├── functional_statuses.py
        ├── immunizations.py
        ├── instructions.py
        ├── medications.py
        ├── problems.py
        ├── procedures.py
        ├── results.py
        ├── smoking_status.py
        └── vitals.py
```

## Python Version Compatibility

- Python 3.6 or higher recommended
- No longer compatible with Python 2.x

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
