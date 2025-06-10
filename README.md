# Logfile-Analysis

A collection of Python scripts for analyzing web server log files.

## Scripts

### 1. Rapid Requests Analysis (`1_rapid_requests.py`)
Identifies how many requests came from each IP address within 10 seconds of their first request.

```bash
python3 1_rapid_requests.py
```

### 2. User Agent Analysis (`2_user_agents.py`)
Counts and categorizes all user agents in the log file.

```bash
python3 2_user_agents.py
```

### 3. Endpoint Access Analysis (`3_endpoint_counter.py`)
Counts how many times each endpoint was accessed.

```bash
python3 3_endpoint_counter.py
```

## Usage

All scripts default to analyzing `nodelog.log` in the current directory. You can specify a different log file as a command-line argument:

```bash
python3 script_name.py /path/to/other/logfile.log
```

## Log Format

These scripts are designed to work with standard web server access logs that include:
- Timestamps (ISO format)
- IP addresses
- HTTP methods and paths
- Status codes
- User agent information