import os
import re

def update_frontmatter(file_path):
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Get the filename without extension to use as title
    title = os.path.splitext(os.path.basename(file_path))[0]
    # Capitalize title and replace hyphens with spaces
    title = title.replace('-', ' ').title()

    # Create new frontmatter
    new_frontmatter = f"""---
layout: default
title: {title}
---

"""

    # Remove existing frontmatter if it exists
    content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)

    # Combine new frontmatter with content
    new_content = new_frontmatter + content.lstrip()

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md') and filename != 'index.md':
            file_path = os.path.join(directory, filename)
            print(f"Updating {filename}...")
            update_frontmatter(file_path)

# Usage
guides_dir = '_guides'  # Change this if your directory is different
process_directory(guides_dir)
print("All files updated!")
