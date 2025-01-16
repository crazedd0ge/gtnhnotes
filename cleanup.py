import os

def fix_title(filename):
    """Fix common title formatting issues"""
    fixes = {
        'Ic2': 'IC2',
        'Tc (': 'TC (',
        'Gt)': 'GT)',
        'Tic)': 'TiC)',
        'Ebfs': 'EBFs'
    }

    content = []
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.readlines()

    # Fix the title line
    for i, line in enumerate(content):
        if line.startswith('title:'):
            title = line.replace('title:', '').strip()
            # Apply fixes
            for old, new in fixes.items():
                title = title.replace(old, new)
            content[i] = f'title: {title}\n'
            break

    # Write back
    with open(filename, 'r+', encoding='utf-8') as file:
        file.seek(0)
        file.writelines(content)
        file.truncate()

def process_files():
    guides_dir = '_guides'
    for filename in os.listdir(guides_dir):
        if filename.endswith('.md'):
            fix_title(os.path.join(guides_dir, filename))
            print(f'Fixed title in {filename}')

if __name__ == '__main__':
    process_files()
