# Information Gathering Tool

**Author**: Harsh Sanjay Padishalwar  
**Date**: 1-11-24  

## Project Overview

The Information Gathering Tool is a Python-based command-line application developed to retrieve and display IP address and location data for a specified website URL. Designed for cybersecurity and ethical hacking domains, this tool leverages essential Python libraries and an external API to gather detailed IP information, including city, country, organization, and geographical coordinates.

## Features

- **IP Address Retrieval**: Fetches the IP address of a given website URL.
- **Location Information**: Provides city, region, country, and coordinates (latitude and longitude).
- **Organization Details**: Displays the organization associated with the IP address.
- **Error Handling**: Manages incorrect URLs and network issues, guiding the user to provide valid input.

## Technology Stack

- **Python**: Core programming language.
- **Libraries**:
  - `sys`: For command-line argument handling.
  - `requests`: For HTTP requests to the ipinfo.io API.
  - `json`: For parsing JSON data.
  - `socket`: For retrieving the IP address of a specified URL.

## Prerequisites

Ensure you have the following installed:
- Python (version X.X or higher)
- Required libraries, which can be installed via pip:
  ```bash
  pip install requests
  ```

## Usage

1. **Run the Script**: Open a command prompt or terminal in the directory containing `infotool.py`.
2. **Execute the Command**:
   ```bash
   python infotool.py <websiteurl>
   ```
   Example:
   ```bash
   python infotool.py google.com
   ```
3. **Output**: The tool will display:
   - IP Address
   - City
   - Region
   - Country
   - Coordinates (latitude and longitude)
   - Organization

## Example Output

For instance, running the tool on `yahoo.com` might yield:
- **IP Address**: 98.137.11.163
- **City**: Sunnyvale
- **Region**: California
- **Country**: United States
- **Coordinates**: 37.406, -122.071
- **Organization**: Yahoo Inc.

## Challenges & Future Improvements

- **Challenges**: Handling network errors and maintaining clear data formatting.
- **Future Enhancements**: Adding features like historical IP data and ISP details for more comprehensive information gathering.

## Conclusion

This project showcases the use of APIs, JSON data handling, and error management, building a foundational tool for cybersecurity and ethical hacking applications.
