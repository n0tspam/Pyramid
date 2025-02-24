#!/usr/bin/env python3
import sys
import base64
import os

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <path_to_dotnet_exe_or_dll>")
        sys.exit(1)

    assembly_path = sys.argv[1]
    
    if not os.path.isfile(assembly_path):
        print(f"Error: File not found - {assembly_path}")
        sys.exit(1)

    # Read all bytes of the .NET assembly
    with open(assembly_path, "rb") as f:
        data = f.read()

    # Convert to Base64
    b64_data = base64.b64encode(data).decode('ascii')

    # Print the Python line
    # ex: assembly_bytes = b'TVqQAAMAAAAEAAAA...'
    print(f"assembly_bytes = b'{b64_data}'")

if __name__ == "__main__":
    main()

