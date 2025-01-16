import re
import os

def clean_markdown_table(table_text):
    # Split the table into lines
    lines = table_text.strip().split('\n')

    # Remove completely empty lines
    lines = [line for line in lines if line.strip()]

    # Function to split row, respecting potential markdown formatting
    def split_table_row(line):
        # Remove leading/trailing pipes and split
        cells = [cell.strip() for cell in line.strip('|').split('|')]
        return cells

    # Parse lines
    parsed_lines = [split_table_row(line) for line in lines]

    # Identify non-empty columns
    non_empty_columns = []
    for col_index in range(len(parsed_lines[0])):
        # Check if any row in this column has non-empty content
        if any(row[col_index].strip() and row[col_index].strip() != '-----' for row in parsed_lines):
            non_empty_columns.append(col_index)

    # Filter rows to keep only non-empty columns
    filtered_lines = []
    for row in parsed_lines:
        filtered_row = [row[i] for i in non_empty_columns]
        filtered_lines.append(filtered_row)

    # Create output lines
    output_lines = []

    # First line is the header
    header = filtered_lines[0]
    output_lines.append('| ' + ' | '.join(header) + ' |')

    # Alignment line with proper alignment
    alignment = [':---'] * len(header)
    output_lines.append('| ' + ' | '.join(alignment) + ' |')

    # Rest of the rows
    for row in filtered_lines[1:]:
        output_lines.append('| ' + ' | '.join(row) + ' |')

    return '\n'.join(output_lines)

def process_markdown_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # More robust table detection regex
    table_pattern = r'(\|[^\n]+\n\|[-:| ]+\n(?:\|[^\n]+\n)+)'

    # Replace each found table with its cleaned version
    def replace_table(match):
        return clean_markdown_table(match.group(1))

    cleaned_content = re.sub(table_pattern, replace_table, content, flags=re.MULTILINE)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

def process_directory(input_dir, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Process each .md file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.md'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            process_markdown_file(input_path, output_path)

# Example usage
if __name__ == "__main__":
    # process_markdown_file('./docs/bees.md', 'cleaned/bees.md')
    process_directory('./docs', './cleaned')
