
import json
import base64


def decode_python_file_code(encoded_content):
    try:
        # Decode Base64 back to original content
        decoded_content = base64.b64decode(encoded_content).decode()
        return decoded_content

    except Exception as ex:
        raise ex


if __name__ == "__main__":
    encoded_str = "<encoded string>"
    decoded_content = decode_python_file_code(encoded_str)
    print(decoded_content)
