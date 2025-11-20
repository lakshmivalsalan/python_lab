with open("example.txt", "w") as f:
    f.write("She sells seashells on the seashore\n")
    f.write("Some people smile\n")
    f.write("The snake is here\n")
    f.write("We love coding\n")

# Function to find lines with words starting with 's' and ending with 'e'
def find_matching_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.lower().startswith('s') and word.lower().endswith('e'):
                    print(line.strip())
                    break  # Only print line once


find_matching_lines("example.txt")
