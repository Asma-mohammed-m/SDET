import csv

# Input text file
input_file = "D:/SDET/src/test/java/assignment_day3/input.txt"

# Output CSV file
output_file = "D:/SDET/src/test/java/assignment_day3/output.csv"

# Open the text file for reading
with open(input_file, "r") as txt_file:
    lines = txt_file.readlines()  # Read all lines
    for data in lines:
            print(data)

# Open the CSV file for writing
with open(output_file, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)

    # Write each line as a new row in the CSV
    for line in lines:
        writer.writerow([line.strip()])  # Strip removes newline characters

print(f"Data written to {output_file}")