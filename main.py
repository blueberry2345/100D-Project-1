# Dictionary that matches a character with the morse code translation
morse_code_translation = {
    'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.','F': '..-.',
    'G': '--.','H': '....','I': '..','J': '.---','K': '-.-','L': '.-..',
    'M': '--','N': '-.','O': '---','P': '.--.','Q': '--.-','R': '.-.',
    'S': '...','T': '-','U': '..-','V': '...-','W': '.--','X': '-..-',
    'Y': '-.--','Z': '--..','0': '-----','1': '.----','2': '..---',
    '3': '...--','4': '....-','5': '.....','6': '-....','7': '--...',
    '8': '---..','9': '----.','.': '.-.-.-',',': '--..--','?': '..--..',
    '!': '-.-.--',':': '---...',"'": '.----.','-': '-....-','/': '-..-.',
    '(': '-.--.',')': '-.--.-','"': '.-..-.','@': '.--.-.','&': '.-...',
    '=': '-...-','+': '.-.-.','$': '...-..-','%': '.-..-.'}


# Loop that keeps program going until user types exit
while True:
    # get user input
    program_input = input("Type in your input or type 'exit' to exit the program: ")
    if program_input == "exit":
        break
    # If user input is empty, send a message
    elif program_input == "":
        print("User input was empty.")

    else:
        # Program fills the output string by looping through each character in the user's input and adding it to the output
        program_output = ""
        for letter in program_input.upper():
            try:
                # As space doesnt have a translation, it needs to be added separately
                if letter == " ":
                    program_output += " "
                else:
                    program_output += morse_code_translation[letter]
                program_output += " "
            # If key isnt a space character or in the dictionary, an error message will be sent notifying the user of the unrecognised character
            except KeyError:
                print(f"Character '{letter}' not recognised.")
                break
        # Print translation
        print("output: " + program_output)
