import argparse

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def manchester_encoding(binary_seq):
    return ''.join(['10' if bit == '0' else '01' for bit in binary_seq])

def manchester_decoding(encoded_seq):
    return ''.join(['0' if encoded_seq[i:i+2] == '10' else '1' for i in range(0, len(encoded_seq), 2)])


def encode_message(message):
    binary_seq = text_to_binary(message)
    manchester_encoded = manchester_encoding(binary_seq)
    return manchester_encoded

def decode_message(encoded_message):
    binary_seq = manchester_decoding(encoded_message)
    return binary_seq

def main():
    parser = argparse.ArgumentParser(description="Encode and decode messages using Manchester encoding.")
    subparsers = parser.add_subparsers(dest="command", help="Encode or decode commands")
    
    encode_parser = subparsers.add_parser('encode', help="Encode a message")
    encode_parser.add_argument('message', type=str, help="Message to encode")

    decode_parser = subparsers.add_parser('decode', help="Decode a message")
    decode_parser.add_argument('encoded_message', type=str, help="Encoded message to decode")
    
    args = parser.parse_args()
    
    if args.command == 'encode':
        encoded_message = encode_message(args.message)
        print(f"Encoded message: {encoded_message}")
    elif args.command == 'decode':
        decoded_message = decode_message(args.encoded_message)
        print(f"Decoded message: {decoded_message}")

if __name__ == "__main__":
    main()
