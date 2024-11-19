import argparse
from translator import translate

def main():
    parser = argparse.ArgumentParser(description="XML to Config Language Translator")
    parser.add_argument("--input", type=str, help="Path to input XML file", default=None)
    parser.add_argument("--output", type=str, required=True, help="Path to output file")
    args = parser.parse_args()

    # Read XML from stdin or file
    xml_data = input() if not args.input else open(args.input).read()

    # Translate and write output
    with open(args.output, 'w') as outfile:
        outfile.write(translate(xml_data))

if __name__ == "__main__":
    main()

