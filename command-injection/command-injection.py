import subprocess

filename = input("Please provide a file name to search and display:\n")

# Validate the filename to allow alphanumeric, underscores, and periods
if not all(c.isalnum() or c in {'_', '.'} for c in filename):
    print("Invalid filename.")
else:
    command = ["cat", filename]

    try:
        # Use subprocess.run instead of os.system
        result = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Display the result
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
