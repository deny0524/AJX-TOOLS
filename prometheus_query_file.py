import os
import re

def reconstruct_query(input_text):
    """Extract and reconstruct a query from Prometheus query_part fragments."""
    # Extract query_part_1, query_part_2, etc.
    pattern = r'query_part_(\d+)=\"([^\"]*)"'
    matches = re.findall(pattern, input_text)
    
    if not matches:
        return "No query_part fragments found"
    
    # Sort by index and concatenate
    query_parts = [(int(idx), text) for idx, text in matches]
    query_parts.sort()
    
    return ''.join(text for _, text in query_parts)

def main():
    """Read query.txt and display the reconstructed query."""
    try:
        # Look for query.txt in the same directory as this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "query.txt")
        
        with open(file_path, 'r') as file:
            input_text = file.read()
        
        reconstructed_query = reconstruct_query(input_text)
        
        print("\nReconstructed Query:")
        print("-" * 80)
        print(reconstructed_query)
        print("-" * 80)
    except FileNotFoundError:
        print(f"Error: File 'query.txt' not found in {os.path.dirname(os.path.abspath(__file__))}")
        print("\nUsage: Copy Prometheus query output to query.txt in the same directory")
        print("Format: query_part_1=\"...\", query_part_2=\"...\", etc.")
    except Exception as e:
        print(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    main()