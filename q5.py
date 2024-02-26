def find_cjeb_occurrences(text):
    # Split the text into words
    words = text.split()
    # Initialize a counter for matches
    count = 0
    # Loop through each word in the text
    for word in words:
        # Check if the word starts with 'C' and ends with 'jeb'
        if word.startswith('C') and word.endswith('jeb'):
            # If it does, increment the counter
            count += 1
    # Return the total count of matches
    return count

# Example usage
text = "Cjeb starts with C and ends with jeb. So does Coooljeb, but not Cjebb or Ceeb."
number_of_matches = find_cjeb_occurrences(text)
print("Number of matches:", number_of_matches)
