import winsound
import time

# Extended Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': ' ', '!': '-.-.--', '"': '.-..-.', '$': '...-..-',
    '&': '.-...', '\'': '.----.', '(': '-.--.', ')': '-.--.-', '+': '.-.-.',
    ',': '--..--', '-': '-....-', '.': '.-.-.-', '/': '-..-.', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '?': '..--..', '@': '.--.-.', '_': '..--.-',
    'Ä': '.-.-', 'Å': '.--.-', 'É': '..-..', 'Ñ': '--.--', 'Ö': '---.',
    'Ü': '..--'
}

# Function to translate text to Morse code
def text_to_morse(text):
    text = text.upper()
    morse_code = ''
    for char in text:
        morse_code += morse_code_dict.get(char, '') + ' '
    return morse_code.strip()

# Function to play Morse code using vibrations
def play_morse_code(morse_code):
    dot_duration = 200  # duration of a dot in milliseconds
    dash_duration = 400  # duration of a dash in milliseconds
    space_duration = 200  # duration of space between parts of the same letter
    letter_space_duration = 200  # duration of space between letters
    word_space_duration = 600  # duration of space between words
    
    for symbol in morse_code:
        if symbol == '.':
            winsound.Beep(2000, dot_duration)  # frequency 2000 Hz
        elif symbol == '-':
            winsound.Beep(2500, dash_duration)
        elif symbol == ' ':
            time.sleep(letter_space_duration / 2000)
        time.sleep(space_duration / 2000)

# Main program
if __name__ == "__main__":
    while True:
        text = input("Enter text to translate to Morse code vibrations (or 'exit' to quit): ")
        if text.lower() == 'exit':
            print("Exiting the program.")
            break
        morse_code = text_to_morse(text)
        print(f"Morse Code: {morse_code}")
        play_morse_code(morse_code)
