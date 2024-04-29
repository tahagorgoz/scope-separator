import argparse
import requests

def extract_and_notify_params(target_url, keywords):
    try:
        response = requests.get(target_url)
        if response.status_code == 200:
            page_source = response.text
            found_params = set()
            for keyword in keywords:
                if keyword in page_source.lower():
                    found_params.add(keyword)
            return found_params
        else:
            print("HTTP request failed. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)
    return set()

# Handle arguments
parser = argparse.ArgumentParser(description='Process target URL file')
parser.add_argument('-f', '--file', metavar='url_file_path', type=str, help='Path to the target URL file', required=True)
parser.add_argument('-o', '--output', metavar='keywords_file_path', type=str, help='Path to the keywords file', required=True)
parser.add_argument('--dev', action='store_true', help='Run in development mode')
args = parser.parse_args()

# Print usage information for -h, --h, and --help
if args.file is None and args.output is None:
    print("Use: python scope-seperator.py -f url_file_path.txt -o keywords_file_path.txt")
    exit()

# Read keywords from file
with open(args.output, 'r') as file:
    keywords = [keyword.strip() for keyword in file.readlines()]

# Development mode
if args.dev:
    print("@blgsvnomer")
    print("@tahagorgoz")
else:
    # Path to the file containing target URLs
    url_file_path = args.file

    # Path to the result file
    result_file_path = "result.txt"

    # Process each URL and write the result to a file
    with open(url_file_path, 'r') as input_file, open(result_file_path, 'w') as output_file:
        for target_url in input_file:
            target_url = target_url.strip()  # Strip newline characters
            output_file.write(f"Target URL: {target_url}\n")
            found_params = extract_and_notify_params(target_url, keywords)
            if found_params:
                output_file.write("Found parameters:\n")
                for param in found_params:
                    output_file.write(f"{param}\n")
            else:
                output_file.write("No parameters containing specified keywords were found.\n")
            output_file.write("-" * 50 + "\n")

    print("Results have been saved to 'result.txt' file.")
