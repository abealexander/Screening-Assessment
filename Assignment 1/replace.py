# Function to read and replace text file
def replace_data(file_name_with_ext, find, replace):
    with open(file_name_with_ext, "r") as f:
        content = f.read()
        updated_content = content.replace(find, replace)
    with open(file_name_with_ext, "w") as f:
        f.write(updated_content)

try:
    replace_data("example.txt", "placement", "screening")
except Exception as e:
    print(e)