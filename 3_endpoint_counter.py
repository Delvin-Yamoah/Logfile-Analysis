#!/usr/bin/env python3
import re
from collections import Counter

def count_endpoints(log_file="nodelog.log"):
    """
    Count the number of times each endpoint was accessed.
    """
    # Pattern to extract HTTP method and path
    pattern = r'"([A-Z]+) ([^ ]+) HTTP/\d\.\d"'
    endpoints = []
    
    try:
        with open(log_file, 'r') as f:
            for line in f:
                match = re.search(pattern, line)
                if match:
                    method, path = match.groups()
                    endpoints.append(f"{method} {path}")
        
        # Count endpoints
        endpoint_counter = Counter(endpoints)
        
        # Print results
        print("Endpoint Access Analysis")
        print("=" * 70)
        for endpoint, count in endpoint_counter.most_common():
            print(f"Count: {count} - Endpoint: {endpoint}")
        
        print(f"\nTotal unique endpoints: {len(endpoint_counter)}")
            
    except Exception as e:
        print(f"Error analyzing log file: {e}")

if __name__ == "__main__":
    count_endpoints()