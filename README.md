# Manchester Encoding Script

This Python script allows you to encode and decode messages using Manchester encoding.

## Requirements

- Python 3

## Usage

1. **Encode a Message:**

   ```sh
   python main.py encode "YOUR_MESSAGE"
2. **Decode a Message:**
    ```
    python line_encoder.py decode "ENCODED_MESSAGE"

## Example
    ```
    python3 .\main.py encode "this is a secret message. only manchester fans can see it!!"
    Encoded message: 10010101100110101001011001101010100101100110100110010101101001011010011010101010100101100110100110010101101001011010011010101010100101101010100110100110101010101001010110100101100101101001100110010110101001011001010110100110100101101001100110010101100110101010011010101010100101100101100110010110100110011001010110100101100101011010010110010110101010011001011010010101100101101001100110100110010101101010011010101010100101100101010110010110010101101001011001011010100101010110100110100110101010101001011001011001100101101010100110010110010101101001011010100101100101100110101010010110100110011001010110100101100101011001101010010110100110011001010110100110101001101010101010010110100101101001011010101001100101100101011010010101101001011010011010101010100101101010010110010110101010011001011001010110101001101010101010010101101001011001011010011001100101101001100110100110101010101001011001101001100101011001101010100110101010011010011010101001
    python3 .\main.py decode 10010101100110101001011001101010100101100110100110010101101001011010011010101010100101100110100110010101101001011010011010101010100101101010100110100110101010101001010110100101100101101001100110010110101001011001010110100110100101101001100110010101100110101010011010101010100101100101100110010110100110011001010110100101100101011010010110010110101010011001011010010101100101101001100110100110010101101010011010101010100101100101010110010110010101101001011001011010100101010110100110100110101010101001011001011001100101101010100110010110010101101001011010100101100101100110101010010110100110011001010110100101100101011001101010010110100110011001010110100110101001101010101010010110100101101001011010101001100101100101011010010101101001011010011010101010100101101010010110010110101010011001011001010110101001101010101010010101101001011001011010011001100101101001100110100110101010101001011001101001100101011001101010100110101010011010011010101001
    Decoded message: this is a secret message. only manchester fans can see it!!
