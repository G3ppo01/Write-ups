import sys
import re
from collections import Counter
import matplotlib.pyplot as plt

def open_file(file_path):
    """
    Opens the log file in common log format.

    :param file_path: Path to the log file (.txt)
    """
    try:
        # Attempt to open the file at the given path in read mode
        with open(file_path, 'r') as file:
            # Read all lines from the file into a list
            content = file.readlines()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def is_clf(logs):
    """
    Checks if the log file is in Common Log Format (CLF).

    :param logs: file content
    :return: True if the file is in CLF format, kills the script otherwise
    """
    # Define the regular expression pattern for Common Log Format (CLF)
    clf_pattern = r'(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] ([\"])(\S+) (\S+)\s*(\S*)([\"]) (\d{3}) (\d+)([\n])'

    # Iterate over each line in the logs, with line numbers starting from 1
    for i, line in enumerate(logs, start=1):
        if re.match(clf_pattern, line) == "None":
            print(f"Error: Line {i} is not in Common Log Format (CLF).")
            return False
            sys.exit(1)
    # If all lines match the pattern, print a success message    
    print("The file is in Common Log Format (CLF). Proceeding...")
    return True

def count_status_codes(logs):
    """
    Reads the log file and counts the occurrence of each status code.

    :param logs: file content as a list of lines
    :return: Ordered dictionary of status codes and their occurrences
    """
    try:
        # Define the regular expression pattern to extract status codes from CLF logs
        status_code_pattern = r'^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] \"(\S+) (\S+)\s*(\S*)\" (\d{3}) (\d+|-)$'
        
        # Initialize a Counter to keep track of status codes
        status_counter = Counter()
        
        # Iterate over each line to extract and count status codes
        for line in logs:
            match = re.match(status_code_pattern, line)
            if match:
                # Extract the status code (8th group in the pattern)
                status_code = match.group(8)
                status_counter[status_code] += 1
            else:
                # Handle the case where a line does not match the expected pattern
                print(f"Warning: A line did not match the expected format and was skipped.")
        
        # Return the ordered dictionary of status codes and their occurrences
        for code, count in sorted(status_counter.items()):
            return status_counter
    except Exception as e:
        # Handle any other exception that may occur during processing
        print(f"An error occurred while counting status codes: {e}")
        sys.exit(1)

def write_to_yaml(data, output_file="results.yml"):
    """
    Writes the key-value pairs to a YAML file, representing every pair on a new line.

    :param data: Dictionary of status codes and their occurrences
    :param output_file: Path to the output YAML file
    """
    try:
        # Write the status codes and their occurrences to a YAML file
        with open(output_file, 'w') as file:
            # Start the YAML file with '---'
            file.write("---\n")
            # Using collections to write the data in YAML format
            for key, value in sorted(data.items()):
                file.write(f"{key}: {value}\n")
        print(f"Results have been written to {output_file}")
    except Exception as e:
        # Handle any other exception that may occur during file writing
        print(f"An error occurred while writing to the YAML file: {e}")
        sys.exit(1)

def generate_pie_chart(data, output_file="statuscode.png"):
    """
    Generates a pie chart of the status code occurrences and saves it as an image file.

    :param data: Dictionary of status codes and their occurrences
    :param output_file: Path to save the pie chart image
    """
    try:
        # Extract labels and sizes for the pie chart
        labels = list(data.keys())
        sizes = list(data.values())
        
        # Generate the pie chart
        plt.figure(figsize=(10, 6))
        plt.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.title("Status Code Distribution")
        
        # Save the pie chart as an image file
        plt.savefig(output_file)
        print(f"Pie chart has been saved to {output_file}")
    except Exception as e:
        # Handle any other exception that may occur during pie chart generation
        print(f"An error occurred while generating the pie chart: {e}")
        sys.exit(1)

def main():

    # Check if the argument for the file path is provided
    if len(sys.argv) < 2:
        print("Error: No file path provided. Please provide the path to a CLF file as an argument.")
        sys.exit(1)

    # Extract file path from arguments
    file_path = sys.argv[1]
    
    # Open the log file
    logs = open_file(file_path)
    
    #Check if the file is in CLF
    is_clf(logs)

    # Count and print the occurrence of each status code
    status_counts = count_status_codes(logs)

    # Write the results to a YAML file
    write_to_yaml(status_counts)

    # Generate a pie chart of the status code occurrences
    generate_pie_chart(status_counts)

if __name__ == "__main__":
    main()
