def alternate_chars(text, index=0):
    """
    Recursively prints alternate characters from the string 'text'
    starting from index 0.
    """
    if index >= len(text):
        return
    print(text[index], end='') 
    alternate_chars(text, index + 2)  


line = "Hello, World!"
print("Original line:", line)
print("Alternate characters:", end=' ')
alternate_chars(line)
