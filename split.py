import re
import sys
from pathlib import Path
from urllib.parse import urlparse

def extract_extension(url):
    path = urlparse(url).path
    match = re.search(r'\.([a-zA-Z0-9]+)$', path)
    return match.group(1).lower() if match else None

def split_by_extension(input_file):
    input_path = Path(input_file)
    if not input_path.exists():
        print(f"Error: '{input_file}' not found.")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        print(f"'{input_file}' is empty. Nothing to do.")
        sys.exit(0)

    categorized = {}
    for line in lines:
        ext = extract_extension(line) or "no_extension"
        categorized.setdefault(ext, []).append(line)

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    print(f"Processing {len(lines)} entries from '{input_file}'...\n")
    for ext, urls in categorized.items():
        out_path = output_dir / f"{ext}.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(urls))
        print(f"{ext}.txt -> {len(urls)} URLs")

    print("\nDone. Files created inside 'output/' folder.")

if __name__ == "__main__":
    split_by_extension("output.txt")

