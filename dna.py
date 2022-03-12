# identifies a person based on their DNA

import csv
import sys


def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Read sequence
    dna = open(str(sys.argv[2])).read()

    # nucleotides and counts of them
    nucleotides = {}

    # Read people into memory from file
    with open(str(sys.argv[1]), "r") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames

        for header in range(1, len(headers)):
            str_count = []
            STR = headers[header]
            for i in range(len(dna)):
                repeat = 0
                if dna[i:i + len(headers[header])] == STR:
                    for j in range(i, len(dna), len(headers[header])):
                        if dna[j:j + len(headers[header])] == STR:
                            repeat += 1
                            continue
                        else:
                            str_count.append(repeat)
                            break
            if len(str_count) != 0:
                nucleotides[headers[header]] = max(str_count)
            else:
                nucleotides[headers[header]] = 0

        # Compare the nucleotides with the persons DNA
        for person in reader:
            count = 0
            for head in headers[1:]:
                if person[head] == str(nucleotides[head]):
                    count += 1
            if count == len(headers) - 1:
                print(person["name"])
                sys.exit()

    print("No match")


if __name__ == "__main__":
    main()
