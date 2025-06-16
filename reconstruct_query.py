import re

def reconstruct_query(input_text):
    # Extract all query_text parts using regex
    pattern = r'query_text(?:_(\d+))?="([^"]*)"'
    matches = re.findall(pattern, input_text)
    
    # Sort by index
    query_parts = []
    for idx_str, text in matches:
        idx = int(idx_str) if idx_str else 0
        query_parts.append((idx, text))
    
    query_parts.sort()
    
    # Concatenate all parts
    full_query = ''.join(text for _, text in query_parts)
    
    return full_query

if __name__ == "__main__":
    print("Paste your Prometheus query below and press Enter twice when done:")
    
    # Collect input lines until empty line is entered
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    
    input_text = '\n'.join(lines)
    
    reconstructed_query = reconstruct_query(input_text)
    print("\nReconstructed Query:")
    print("-" * 80)
    print(reconstructed_query)
    print("-" * 80)
