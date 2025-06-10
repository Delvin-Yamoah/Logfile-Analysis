#!/usr/bin/env python3
import re
from collections import Counter

def analyze_user_agents(log_file="nodelog.log"):
    """
    Count and categorize user agents in the log file.
    """
    # Pattern to extract user agent
    pattern = r'"([^"]+)"$'
    user_agents = []
    
    try:
        with open(log_file, 'r') as f:
            for line in f:
                match = re.search(pattern, line.strip())
                if match:
                    user_agent = match.group(1)
                    user_agents.append(user_agent)
        
        # Count user agents
        agent_counter = Counter(user_agents)
        
        # Print results
        print("User Agent Analysis")
        print("=" * 70)
        for agent, count in agent_counter.most_common():
            print(f"Count: {count} - Agent: {agent}")
        
        print(f"\nTotal unique user agents: {len(agent_counter)}")
            
    except Exception as e:
        print(f"Error analyzing log file: {e}")

if __name__ == "__main__":
    analyze_user_agents()