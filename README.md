# BioAMLA Datasets

## Datasets
- [audio/scp-frogs](audio/scp-frogs/): A very small audio set built for environmental sound analyis at Steele Creek Park in Bristol TN. Currently consisting of 11 species of frogs. Dataset has been initially developed to support The Frogs of Steele Creek Park. This is a work in progress. 

## Externally Hosted Datasets
- [Steele Creek Park Wetlands, Bristol, TN 2023](external/steele-creek-park-2023-raw/README.md) : 
This raw audio dataset contains 2822 wav/mp3 files collected from five locations in Steele Creek Park from Feb. through Sept. 2023. 
- [Braulio Carillo National Park/ La Selva Research Station, Costa Rica 2024](external/costa-rica-2024-raw/README) :
This raw audio dataset contains 601 wav/mp3 files (600 hours) collected from five locations at Braulio Carillo National Park, Costa Rica from July 9th - 24th, 2024.

# Licenses
All metadata files in this repository contain licensing and attribution. The included license_generator.py file generates a LICENSE.
- Parses CSV files with required fields: `file_name`, `attr_id`, `attr_lic`, `attr_url`, `attr_note`
- Data validation and error handling
- Whitespace cleaning and empty row handling
- Creates neatly formatted attributions for each file
- Optional template file prepending
- UTF-8 encoding support

## Usage Examples:

**Basic usage:**
```bash
python license_generator.py attributions.csv -o LICENSE.txt
```

**With template file:**
```bash
python license_generator.py attributions.csv -o LICENSE.txt -t license_template.txt
```

**Preview CSV structure:**
```bash
python license_generator.py attributions.csv -o LICENSE.txt --preview
```

**Validate CSV only:**
```bash
python license_generator.py attributions.csv -o LICENSE.txt --validate-only
```

## CSV Format:

Your CSV file should have these columns:
```csv
file_name,attr_id,attr_lic,attr_url,attr_note
background_music.wav,"John Smith","CC BY 4.0","https://example.com/music","Background music for intro"
sound_effect.wav,"Jane Doe","MIT License","https://sounds.com/effect","Button click sound"
```

## Sample Output:

The generated license file will look like:
```
LICENSE AND ATTRIBUTION FILE
================================================================================
Generated on: 2025-06-20 14:30:15
Total files: 2
================================================================================

1. File: background_music.wav
--------------------------
Attribution ID: John Smith
License: CC BY 4.0
Source URL: https://example.com/music
Notes: Background music for intro

2. File: sound_effect.wav
-----------------------
Attribution ID: Jane Doe
License: MIT License
Source URL: https://sounds.com/effect
Notes: Button click sound

================================================================================
END OF ATTRIBUTIONS
================================================================================
```

## Template File Support:

If you specify a template file with `-t`, its content will be prepended to the license file. For example, if your template contains:
```
MY PROJECT LICENSE
==================

This project uses various third-party assets.
Please see the attributions below for details.

All original code is licensed under MIT License.
```

This will appear at the top of your license file, followed by the individual attributions.
