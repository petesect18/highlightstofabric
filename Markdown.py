import os
import subprocess

def extract_wisdom_from_markdown(input_folder, output_folder):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Get list of Markdown files in the input folder
    markdown_files = [f for f in os.listdir(input_folder) if f.endswith(".md")]
    total_files = len(markdown_files)

    # Iterate through all Markdown files
    for index, file_name in enumerate(markdown_files):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, f"processed_{file_name}")

        # Run fabric command on each Markdown file using cat and pipe
        try:
            command = f"cat {input_path} | fabric -p extract_wisdom"
            result = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)
            
            # Save the result to an individual Markdown file
            with open(output_path, "w", encoding="utf-8") as output_file:
                output_file.write(result.stdout)
            
            # Print progress
            percentage = ((index + 1) / total_files) * 100
            print(f"Processed file '{file_name}' ({index + 1}/{total_files}) - {percentage:.2f}% completed")
        except subprocess.CalledProcessError as e:
            print(f"Error processing file '{file_name}': {e}")

if __name__ == "__main__":
    # Set paths
    input_folder = "/notes"  # Folder containing Markdown files
    output_folder = "/processed_notes/output"  # Folder to save processed notes

    # Run the extraction process
    extract_wisdom_from_markdown(input_folder, output_folder)
    print(f"Wisdom extraction completed. Individual Markdown files are saved in {output_folder}")
