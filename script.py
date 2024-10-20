import os
import re
import socket
from collections import Counter

# Function to read and process a text file, returning a list of words
def extract_words_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()  # Convert text to lowercase
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []  # Return an empty list if the file is missing
    # Replace common apostrophes and handle contractions
    content = re.sub(r"’", "'", content)
    contraction_map = {
        "i'm": "i am", "can't": "cannot", "don't": "do not", "won't": "will not", 
        "you're": "you are", "it's": "it is", "let's": "let us", "i've": "i have",
        "isn't": "is not", "aren't": "are not", "couldn't": "could not"
    }
    for contraction, expanded in contraction_map.items():
        content = content.replace(contraction, expanded)
    # Extract words using regex
    words_list = re.findall(r'\b\w+\b', content)
    return words_list

# Function to get the N most frequent words in a word list
def get_most_frequent_words(words_list, top_n=3):
    word_frequencies = Counter(words_list)
    return word_frequencies.most_common(top_n)

# Function to retrieve the IP address of the current container/host
def fetch_ip_address():
    current_hostname = socket.gethostname()
    ip_address = socket.gethostbyname(current_hostname)
    return ip_address

# Define directory paths and file locations
root_dir = "/home/data"
input_file1 = os.path.join(root_dir, "IF.txt")
input_file2 = os.path.join(root_dir, "AlwaysRememberUsThisWay.txt")
result_output_file = os.path.join(root_dir, "output", "result.txt")

# Ensure the output directory exists
os.makedirs(os.path.dirname(result_output_file), exist_ok=True)

# Read and process words from both input files
word_list_file1 = extract_words_from_file(input_file1)
word_list_file2 = extract_words_from_file(input_file2)

# Count total words in each file
total_words_file1 = len(word_list_file1)
total_words_file2 = len(word_list_file2)

# Calculate the total word count across both files
combined_word_count = total_words_file1 + total_words_file2

# Identify the top 3 frequent words in IF.txt
top_words_file1 = get_most_frequent_words(word_list_file1)

# Identify the top 3 frequent words in AlwaysRememberUsThisWay.txt
top_words_file2 = get_most_frequent_words(word_list_file2)

# Get the container or system's IP address
current_ip_address = fetch_ip_address()

# Write the results to the output file and print them to the console
with open(result_output_file, 'w') as result_file:
    result_file.write(f"Total words in IF.txt: {total_words_file1}\n")
    result_file.write(f"Total words in AlwaysRememberUsThisWay.txt: {total_words_file2}\n")
    result_file.write(f"Combined word count from both files: {combined_word_count}\n")
    result_file.write(f"Top 3 words in IF.txt: {top_words_file1}\n")
    result_file.write(f"Top 3 words in AlwaysRememberUsThisWay.txt: {top_words_file2}\n")
    result_file.write(f"Host/Container IP Address: {current_ip_address}\n")

# Display the results on the console
with open(result_output_file, 'r') as result_file:
    print(result_file.read())


