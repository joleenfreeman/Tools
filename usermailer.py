import argparse

def ascii_art():
    print("""
    ____  ____  _     _        _____ _______ 
   / __ \|  _ \| |   (_)      / ____|__   __|
  | |  | | |_) | |__  _ ___  | |       | |   
  | |  | |  _ <| '_ \| / __| | |       | |   
  | |__| | |_) | | | | \__ \ | |____   | |   
   \____/|____/|_| |_|_|___/  \_____|  |_|   
                                            
    """)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate unique email addresses and usernames from names.")
    parser.add_argument("-i", "--input_file", type=str, required=True, help="Input file containing 'Firstname Lastname' per line.")
    parser.add_argument("-o", "--output_file", type=str, required=True, help="Output file to save generated email addresses and usernames.")
    parser.add_argument("-d", "--domain", type=str, required=True, help="The domain for the email addresses.")
    return parser.parse_args()

def get_user_options():
    print("Available formats:")
    print("1. first.last@domain.com")
    print("2. flast")
    print("3. lastf")
    print("4. firstl")
    formats = input("Enter the formats you want separated by commas (default is all): ")
    if formats.strip() == "":
        return ["1", "2", "3", "4"]
    return formats.split(",")

def capitalize_choice():
    choice = input("Capitalize all characters? (yes/no): ").strip().lower()
    return choice == "yes"

def generate_email(firstname, lastname, domain, formats, capitalize):
    email_formats = {
        "1": f"{firstname.lower()}.{lastname.lower()}@{domain}",
        "2": f"{firstname[0].lower()}{lastname.lower()}",
        "3": f"{lastname.lower()}{firstname[0].lower()}",
        "4": f"{firstname.lower()}{lastname[0].lower()}",
    }
    if capitalize:
        email_formats = {k: v.upper() for k, v in email_formats.items()}
    return [email_formats[f] for f in formats if f in email_formats]

def main():
    ascii_art()
    args = parse_arguments()
    formats = get_user_options()
    capitalize = capitalize_choice()

    results = set()  # Using a set to avoid duplicates

    with open(args.input_file, 'r') as infile:
        for line in infile:
            line = line.strip()
            if line:
                parts = line.split()
                if len(parts) >= 2:
                    firstname = parts[0]
                    lastname = ' '.join(parts[1:])  # Handle names with spaces
                    emails = generate_email(firstname, lastname, args.domain, formats, capitalize)
                    results.update(emails)
                else:
                    print(f"Skipping invalid line: {line}")

    with open(args.output_file, 'w') as outfile:
        for result in sorted(results):  # Optional: sort results for better readability
            outfile.write(result + '\n')

    print("Generated results:")
    print("\n".join(sorted(results)))  # Display sorted results to the terminal
    print(f"Email addresses and usernames have been generated and saved to {args.output_file}")

if __name__ == "__main__":
    main()
