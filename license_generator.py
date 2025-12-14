#!/usr/bin/env python3
"""
Attribution License File Generator
Parses a CSV file with attribution data and generates a formatted license file
with proper attributions for each file.
"""

import csv
import argparse
import sys
from pathlib import Path
from datetime import datetime

def read_template_file(template_path):
    """
    Read the content of a template file.
    
    Args:
        template_path (Path): Path to the template file
        
    Returns:
        str: Content of the template file, or empty string if error
    """
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Warning: Could not read template file '{template_path}': {str(e)}")
        return ""

def parse_csv_file(csv_path):
    """
    Parse the CSV file and extract attribution data.
    
    Args:
        csv_path (Path): Path to the CSV file
        
    Returns:
        list: List of dictionaries containing attribution data
    """
    required_fields = ['file_name', 'attr_id', 'attr_lic', 'attr_url', 'attr_note']
    attributions = []
    
    try:
        with open(csv_path, 'r', encoding='utf-8', newline='') as csvfile:
            # Try to detect delimiter
            sample = csvfile.readline()
            csvfile.seek(0)
            sniffer = csv.Sniffer()
            delimiter = sniffer.sniff(sample).delimiter
            
            reader = csv.DictReader(csvfile, delimiter=delimiter)
            
            # Check if required fields are present
            if not reader.fieldnames:
                raise ValueError("CSV file appears to be empty or invalid")
            
            missing_fields = [field for field in required_fields if field not in reader.fieldnames]
            if missing_fields:
                raise ValueError(f"Missing required fields in CSV: {', '.join(missing_fields)}")
            
            # Read all rows
            for row_num, row in enumerate(reader, start=2):  # Start at 2 because header is row 1
                # Clean whitespace from all fields
                cleaned_row = {key: str(value).strip() if value else '' for key, value in row.items()}
                
                # Skip rows with empty file_name
                if not cleaned_row.get('file_name'):
                    print(f"Warning: Skipping row {row_num} - empty file_name")
                    continue
                
                # Extract only the required fields
                attribution = {field: cleaned_row.get(field, '') for field in required_fields}
                attribution['row_number'] = row_num
                attributions.append(attribution)
                
        return attributions
        
    except FileNotFoundError:
        print(f"Error: CSV file not found: {csv_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        sys.exit(1)

def format_attribution(attribution):
    """
    Format a single attribution entry.
    
    Args:
        attribution (dict): Attribution data dictionary
        
    Returns:
        str: Formatted attribution text
    """
    file_name = attribution['file_name']
    attr_id = attribution['attr_id']
    attr_lic = attribution['attr_lic']
    attr_url = attribution['attr_url']
    attr_note = attribution['attr_note']
    
    # Start with the file name as a header
    formatted = f"File: {file_name}\n"
    formatted += "-" * (len(file_name) + 6) + "\n"
    
    # Add attribution ID if present
    if attr_id:
        formatted += f"Attribution ID: {attr_id}\n"
    
    # Add license information if present
    if attr_lic:
        formatted += f"License: {attr_lic}\n"
    
    # Add URL if present
    if attr_url:
        formatted += f"Source URL: {attr_url}\n"
    
    # Add notes if present
    if attr_note:
        formatted += f"Notes: {attr_note}\n"
    
    return formatted

def generate_license_file(attributions, output_path, template_content=""):
    """
    Generate the license file with all attributions.
    
    Args:
        attributions (list): List of attribution dictionaries
        output_path (Path): Path for the output license file
        template_content (str): Content from template file to prepend
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            # Write template content if provided
            if template_content:
                f.write(template_content)
                # Add separator between template and attributions
                if not template_content.endswith('\n'):
                    f.write('\n')
                f.write('\n' + '='*80 + '\n')
                f.write('FILE ATTRIBUTIONS\n')
                f.write('='*80 + '\n\n')
            else:
                # Write a default header
                f.write('LICENSE AND ATTRIBUTION FILE\n')
                f.write('='*80 + '\n')
                f.write(f'Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
                f.write(f'Total files: {len(attributions)}\n')
                f.write('='*80 + '\n\n')
            
            # Write each attribution
            for i, attribution in enumerate(attributions, 1):
                f.write(f"{i}. ")
                f.write(format_attribution(attribution))
                f.write('\n')  # Extra line between entries
            
            # Write footer
            f.write('='*80 + '\n')
            f.write('END OF ATTRIBUTIONS\n')
            f.write('='*80 + '\n')
        
        return True
        
    except Exception as e:
        print(f"Error writing license file: {str(e)}")
        return False

def validate_csv_structure(csv_path, show_preview=False):
    """
    Validate CSV structure and optionally show a preview.
    
    Args:
        csv_path (Path): Path to the CSV file
        show_preview (bool): Whether to show a preview of the data
        
    Returns:
        tuple: (is_valid, field_names, row_count)
    """
    try:
        with open(csv_path, 'r', encoding='utf-8', newline='') as csvfile:
            sample = csvfile.readline()
            csvfile.seek(0)
            sniffer = csv.Sniffer()
            delimiter = sniffer.sniff(sample).delimiter
            
            reader = csv.DictReader(csvfile, delimiter=delimiter)
            field_names = reader.fieldnames or []
            
            rows = list(reader)
            row_count = len(rows)
            
            if show_preview and rows:
                print(f"\nCSV Preview (first 3 rows):")
                print("-" * 60)
                for i, row in enumerate(rows[:3], 1):
                    print(f"Row {i}:")
                    for field in ['file_name', 'attr_id', 'attr_lic', 'attr_url', 'attr_note']:
                        if field in row:
                            value = str(row[field]).strip()
                            display_value = value[:50] + "..." if len(value) > 50 else value
                            print(f"  {field}: {display_value}")
                    print()
            
            return True, field_names, row_count
            
    except Exception as e:
        print(f"Error validating CSV: {str(e)}")
        return False, [], 0

def find_datasets(audio_dir):
    """
    Find all datasets in the audio directory.
    A dataset is identified by a directory containing a metadata.csv file.

    Args:
        audio_dir (Path): Path to the audio directory

    Returns:
        list: List of tuples (dataset_name, dataset_path, csv_path)
    """
    datasets = []

    if not audio_dir.exists():
        print(f"Error: Audio directory not found: {audio_dir}")
        return datasets

    for item in sorted(audio_dir.iterdir()):
        if item.is_dir():
            csv_path = item / "metadata.csv"
            if csv_path.exists():
                datasets.append((item.name, item, csv_path))

    return datasets


def process_single_dataset(csv_path, output_path, template_content="", preview=False, validate_only=False):
    """
    Process a single dataset and generate its license file.

    Args:
        csv_path (Path): Path to the CSV file
        output_path (Path): Path for the output license file
        template_content (str): Content from template file to prepend
        preview (bool): Whether to show a preview of the data
        validate_only (bool): Only validate without generating output

    Returns:
        bool: True if successful, False otherwise
    """
    # Validate CSV structure and show preview if requested
    print(f"  Validating CSV file: {csv_path}")
    is_valid, field_names, row_count = validate_csv_structure(csv_path, preview)

    if not is_valid:
        print("  CSV validation failed.")
        return False

    required_fields = ['file_name', 'attr_id', 'attr_lic', 'attr_url', 'attr_note']
    missing_fields = [field for field in required_fields if field not in field_names]

    print(f"  ✅ CSV structure valid")
    print(f"     Fields found: {', '.join(field_names)}")
    print(f"     Data rows: {row_count}")

    if missing_fields:
        print(f"  ❌ Missing required fields: {', '.join(missing_fields)}")
        return False

    if validate_only:
        return True

    # Parse CSV file
    print(f"  Parsing CSV file...")
    attributions = parse_csv_file(csv_path)

    if not attributions:
        print("  No valid attributions found in CSV file.")
        return False

    valid_attributions = [attr for attr in attributions if attr['file_name']]
    print(f"  ✅ Found {len(valid_attributions)} valid attributions")

    # Generate license file
    print(f"  Generating license file: {output_path}")

    success = generate_license_file(valid_attributions, output_path, template_content)

    if success:
        file_size = output_path.stat().st_size
        print(f"  ✅ License file generated successfully!")
        print(f"     Output file: {output_path}")
        print(f"     File size: {file_size:,} bytes")
        print(f"     Attributions included: {len(valid_attributions)}")
    else:
        print("  ❌ Failed to generate license file")

    return success


def main():
    parser = argparse.ArgumentParser(
        description="Generate license files with attributions from CSV data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
CSV Format:
  Required columns: file_name, attr_id, attr_lic, attr_url, attr_note

  - file_name: Name of the file requiring attribution
  - attr_id: Attribution identifier (author, creator, etc.)
  - attr_lic: License information
  - attr_url: Source URL or reference
  - attr_note: Additional notes or requirements

Examples:
  # Process a single CSV file
  python license_generator.py data.csv -o LICENSE.txt
  python license_generator.py data.csv -o LICENSE.txt -t template.txt

  # Process all datasets in audio directory
  python license_generator.py --audio-dir audio/
  python license_generator.py --audio-dir audio/ -t templates/license_template
        """
    )

    parser.add_argument(
        "csv_file",
        nargs='?',
        help="Input CSV file containing attribution data (optional if --audio-dir is used)"
    )

    parser.add_argument(
        "-o", "--output",
        help="Output filename for the license file (required if csv_file is specified)"
    )

    parser.add_argument(
        "--audio-dir",
        help="Audio directory to scan for datasets. Each subdirectory with a metadata.csv will be processed."
    )

    parser.add_argument(
        "-t", "--template",
        help="Template file to prepend to the license file"
    )

    parser.add_argument(
        "--preview",
        action="store_true",
        help="Preview CSV structure and first few rows before processing"
    )

    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Only validate the CSV structure without generating output"
    )

    args = parser.parse_args()

    # Read template file if specified
    template_content = ""
    if args.template:
        template_path = Path(args.template)
        if template_path.exists():
            template_content = read_template_file(template_path)
            print(f"✅ Template file loaded: {template_path}")
        else:
            print(f"Warning: Template file not found: {args.template}")

    # Mode 1: Process all datasets in audio directory
    if args.audio_dir:
        audio_dir = Path(args.audio_dir)
        print(f"\nScanning audio directory: {audio_dir}")

        datasets = find_datasets(audio_dir)

        if not datasets:
            print("No datasets found (no directories with metadata.csv)")
            sys.exit(1)

        print(f"Found {len(datasets)} dataset(s):\n")

        success_count = 0
        fail_count = 0

        for dataset_name, dataset_path, csv_path in datasets:
            print(f"\n{'='*60}")
            print(f"Processing dataset: {dataset_name}")
            print(f"{'='*60}")

            output_path = dataset_path / "LICENSE"

            if process_single_dataset(csv_path, output_path, template_content,
                                       args.preview, args.validate_only):
                success_count += 1
            else:
                fail_count += 1

        print(f"\n{'='*60}")
        print(f"Summary")
        print(f"{'='*60}")
        print(f"  Datasets processed: {len(datasets)}")
        print(f"  Successful: {success_count}")
        print(f"  Failed: {fail_count}")

        if fail_count > 0:
            sys.exit(1)
        return

    # Mode 2: Process single CSV file (original behavior)
    if not args.csv_file:
        parser.error("Either csv_file or --audio-dir must be specified")

    if not args.output:
        parser.error("-o/--output is required when processing a single CSV file")

    # Validate input CSV file
    csv_path = Path(args.csv_file)
    if not csv_path.exists():
        print(f"Error: CSV file not found: {args.csv_file}")
        sys.exit(1)

    if not csv_path.is_file():
        print(f"Error: Path is not a file: {args.csv_file}")
        sys.exit(1)

    # Validate CSV structure and show preview if requested
    print(f"Validating CSV file: {csv_path}")
    is_valid, field_names, row_count = validate_csv_structure(csv_path, args.preview)

    if not is_valid:
        print("CSV validation failed.")
        sys.exit(1)

    required_fields = ['file_name', 'attr_id', 'attr_lic', 'attr_url', 'attr_note']
    missing_fields = [field for field in required_fields if field not in field_names]

    print(f"✅ CSV structure valid")
    print(f"   Fields found: {', '.join(field_names)}")
    print(f"   Data rows: {row_count}")

    if missing_fields:
        print(f"❌ Missing required fields: {', '.join(missing_fields)}")
        sys.exit(1)

    if args.validate_only:
        print("Validation complete. Exiting (--validate-only specified).")
        return

    # Parse CSV file
    print(f"\nParsing CSV file...")
    attributions = parse_csv_file(csv_path)

    if not attributions:
        print("No valid attributions found in CSV file.")
        sys.exit(1)

    valid_attributions = [attr for attr in attributions if attr['file_name']]
    print(f"✅ Found {len(valid_attributions)} valid attributions")

    # Generate license file
    output_path = Path(args.output)
    print(f"\nGenerating license file: {output_path}")

    success = generate_license_file(valid_attributions, output_path, template_content)

    if success:
        file_size = output_path.stat().st_size
        print(f"✅ License file generated successfully!")
        print(f"   Output file: {output_path}")
        print(f"   File size: {file_size:,} bytes")
        print(f"   Attributions included: {len(valid_attributions)}")
    else:
        print("❌ Failed to generate license file")
        sys.exit(1)

if __name__ == "__main__":
    main()