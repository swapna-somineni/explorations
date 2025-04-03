
import base64
import requests


def encode_local_python_file(filename):
    try:
        # Read the Python file
        with open(filename, "r") as file:
            file_contents = file.read()

        # Encode the content in Base64
        encoded_content = base64.b64encode(file_contents.encode()).decode()

        return encoded_content

    except Exception as ex:
        raise ex


def encode_remote_python_file(file_url):
    try:
       # Download file from GitHub
        response = requests.get(file_url)
        response.raise_for_status()  # Raise an error for failed requests

        # Read file content
        file_content = response.text

        # Encode the content in Base64
        encoded_content = base64.b64encode(file_content.encode()).decode()

        return encoded_content

    except Exception as ex:
        raise ex


if __name__ == "__main__":
    #file_path = "/Users/swapna/git/explorations/ai_tools/wikipedia_tool.py"
    #encoded_string = encode_local_python_file(file_path)

    file_path = "https://raw.github.ibm.com/swapna-somineni/explorations/main/ai_tools/googlesearch_tool.py"
    encoded_string = encode_remote_python_file(file_path)

    print(encoded_string)
