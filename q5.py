import re
def find_pattern_occurrences(text):
    pattern = r'C\w*jeb'

    # Find all occurrences of the pattern
    matches = (re.findall(pattern, text))

    # Return the number of matches
    return len(matches)


# Example usage:
sample_text = "Caaaaajeb has many different things than Cbbbbbjeb or Cjeb."
number_of_matches = find_pattern_occurrences(sample_text)
