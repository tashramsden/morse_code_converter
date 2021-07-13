"""A class which converts between text and morse code"""

from morse_dict import MORSE_DICT
import winsound
import time


class TextConverter:

    def __init__(self):
        self.text = ""
        self.morse = ""

    def new_text(self):
        self.text = input("Please enter the text you would like to be converted into morse code:\n"
                          "  (Special characters and punctuation other than full stops will be ignored.)\n")

    def convert_to_morse(self):
        self.morse = ""
        for char in self.text:
            if char == ".":
                self.morse += "   "
                for letter in "STOP":
                    morse_char = MORSE_DICT[letter.upper()]
                    self.morse += morse_char + " "
            else:
                try:
                    morse_char = MORSE_DICT[char.upper()]
                    self.morse += morse_char + " "
                except AttributeError:
                    morse_char = MORSE_DICT[char]
                    self.morse += morse_char + " "
                except KeyError:
                    pass
        print(f"\nHere is the morse code version of your message':\n"
              f"  (Turn up the volume to hear the pips)\n\n"
              f"{self.morse}\n")

    def play_morse_sound(self):
        """Takes the morse code and converts to short sound beeps. The duration of a dash is three times the
        duration of a dot. Each dot or dash in morse is followed by a period of signal absence, called a space,
        equal to the dot duration. The letters of a word are separated by a space of duration equal to three dots,
        and words are separated by a space equal to seven dots."""
        for word in self.morse.split("   "):
            for char in word:
                if char == ".":
                    winsound.Beep(frequency=700, duration=150)  # milliseconds
                    time.sleep(0.15)  # seconds
                elif char == "-":
                    winsound.Beep(frequency=700, duration=450)
                    time.sleep(0.15)
                elif char == " ":
                    time.sleep(0.45)
            time.sleep(1.05)

    def new_morse(self):
        self.morse = input("Please enter the morse code that you would like to convert to text.\n"
                           "  Please enter your code using '.' and '-',\n"
                           "  leave no spaces between dots and dashes of the same letter,\n"
                           "  leave one space between letters in a word,\n"
                           "  and leave 3 spaces between words.\n")

    def convert_to_text(self):
        self.text = ""
        morse_words = self.morse.split("   ")
        for word in morse_words:
            morse_letters = word.split(" ")
            for morse_letter in morse_letters:
                for letter, morse in MORSE_DICT.items():
                    if morse == morse_letter:
                        self.text += letter
            self.text += " "
        print(f"\nHere is the text version of your morse input:\n\n"
              f"{self.text}\n")
