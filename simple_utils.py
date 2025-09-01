# simple_utils.py - A tiny utility library

def reverse_string(text):
    """Reverses the characters in a string."""
    return text[::-1]

def count_words(sentence):
    """
    Return the number of words in the given sentence.
    
    Words are determined by splitting on any whitespace (uses Python's `str.split()`), so consecutive whitespace is treated as a single separator and an empty string yields 0.
    
    Parameters:
        sentence (str): Input text to count words in.
    
    Returns:
        int: Number of words in `sentence`.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.
    
    Parameters:
        celsius (int | float): Temperature in degrees Celsius.
    
    Returns:
        float: Temperature in degrees Fahrenheit calculated as (celsius * 9/5) + 32.
    """
    return (celsius * 9/5) + 32
