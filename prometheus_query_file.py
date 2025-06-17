import os
import re

def reconstruct_query(input_text):
    """Extract and reconstruct a query from Prometheus query_text fragments."""
    # Extract all query_text parts using regex
    pattern = r'query_text(?:_(\d+))?=\"([^\"]*)"'
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
    except Exception as e:
        print(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    main()