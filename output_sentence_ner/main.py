import json

def merge_jsonl_files(file1, file2, merged_file):
    """
    Merges two JSONL (JSON Lines) files into a single file.
    Each line in the input files is expected to be a JSON object.
    """
    with open(merged_file, 'a', encoding='utf-8') as outfile:
        for file in [file1, file2]:
            with open(file, 'r', encoding='utf-8') as infile:
                for line in infile:
                    outfile.write(line)  # Write each JSON line to the merged file

merge_jsonl_files(
    './out_en.json', 
    './out_en_4.json', 
    "./out_en_5.json"
)
