import csv

input_file = "D:/SDET/src/test/java/assignment_day3/input1.txt"  # Change to full path if needed
output_file = "D:/SDET/src/test/java/assignment_day3/output1.csv"

try:
    # Open input file for reading
    with open(input_file, "r", encoding="utf-8") as txt_file:
        lines = txt_file.readlines()  # Read all lines

    # Open output file for writing
    with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        if not lines:
            print("Warning: input.txt is empty!")

        for line in lines:
            writer.writerow([line.strip()])  # Strip and write

    print(f"✅ Data successfully written to {output_file}")

except FileNotFoundError:
    print(f"❌ Error: {input_file} not found!")

except Exception as e:
    print(f"❌ Unexpected error: {e}")