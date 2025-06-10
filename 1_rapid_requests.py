#!/usr/bin/env python3
import re
from datetime import datetime
from collections import defaultdict

def analyze_rapid_requests(log_file="nodelog.log"):
    """
    Analyze how many requests came from each IP address within 10 seconds of their first request.
    """
    # Pattern to extract timestamp and IP
    pattern = r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z) (\d+\.\d+\.\d+\.\d+)'
    
    # Store first request time for each IP
    first_requests = {}
    # Count requests within 10 seconds for each IP
    rapid_requests = defaultdict(int)
    
    try:
        with open(log_file, 'r') as f:
            for line in f:
                match = re.search(pattern, line)
                if match:
                    timestamp_str, ip = match.groups()
                    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                    
                    if ip not in first_requests:
                        # First request from this IP
                        first_requests[ip] = timestamp
                    else:
                        # Calculate time difference in seconds
                        time_diff = (timestamp - first_requests[ip]).total_seconds()
                        if time_diff <= 10:
                            rapid_requests[ip] += 1
        
        # Print results
        print("Rapid Requests Analysis (requests within 10 seconds of first request)")
        print("=" * 70)
        for ip, count in sorted(rapid_requests.items(), key=lambda x: x[1], reverse=True):
            print(f"IP: {ip} - Rapid requests: {count}")
            
    except Exception as e:
        print(f"Error analyzing log file: {e}")

if __name__ == "__main__":
    analyze_rapid_requests()