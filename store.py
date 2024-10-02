import os

# Function to store all files and their contents in a single output file
def store_all_files_to_single_file(root_directory, additional_extensions):
    output_file_path = os.path.join(root_directory, "stored_files.txt")
    
    # Walk through the directory structure and show the structure
    print("Directory structure and files:")
    for dirpath, dirnames, filenames in os.walk(root_directory):
        print(f"{dirpath}/")
        for dirname in dirnames:
            print(f"  [DIR] {dirname}/")
        for filename in filenames:
            print(f"  [FILE] {filename}")
    print("\nStarting to store file contents...\n")
    
    # Open output file with utf-8 encoding to handle special characters
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for dirpath, _, filenames in os.walk(root_directory):
            # Ignore __pycache__, .git, and image files
            if '__pycache__' in dirpath or '.git' in dirpath:
                continue
            
            for filename in filenames:
                # Ignore image files and .pyc files
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.pyc')):
                    continue
                
                # Only store specified file types
                if filename.lower().endswith(additional_extensions):
                    file_path = os.path.join(dirpath, filename)
                    # Get the relative path from the root directory
                    relative_path = os.path.relpath(file_path, root_directory)
                    
                    # Write the file's relative path to the output file
                    output_file.write(f"File: {relative_path}\n")
                    
                    # Write the file content directly to the output file
                    try:
                        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                            for line in file:
                                # Write only non-empty lines (removes empty lines while storing)
                                if line.strip():
                                    output_file.write(line)
                    except Exception as e:
                        print(f"Error reading file {filename}: {e}")
                    
                    # Add a separator between file contents
                    output_file.write("\n" + "="*80 + "\n\n")
                    
                    print(f"Stored content of {filename} to {output_file_path} with relative path: {relative_path}")

# Function to remove empty lines and lines starting with '#' from a file
def remove_empty_and_comment_lines_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Filter out empty lines and lines starting with '#'
    filtered_lines = [line for line in lines if line.strip() and not line.strip().startswith('#') and not line.strip().startswith('=')]
    
    # Write the filtered lines back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(filtered_lines)
    
    print(f"Empty lines and comment lines removed from {file_path}")

# Example usage
if __name__ == "__main__":
    root_directory = "./"  # Replace with your root directory path
    additional_extensions = ('.py', '.txt', '.json', '.drawio', '.md', '.env', '.editorconfig', '.gitignore', '.sql')  # Add other file types you want to store

    # Step 1: Store all file contents
    store_all_files_to_single_file(root_directory, additional_extensions)
    
    # Step 2: Remove empty lines and comment lines from the stored file
    stored_file_path = os.path.join(root_directory, "stored_files.txt")
    remove_empty_and_comment_lines_from_file(stored_file_path)
