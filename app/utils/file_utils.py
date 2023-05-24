def read_txt_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read().strip()
        return content
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        return None


def overwrite_txt_file(file_name, new_content):
    try:
        with open(file_name, "w") as file:
            file.write(new_content)
            return True
    except Exception as e:
        print(f"An error occurred while writing to the file: {str(e)}")
        return None
