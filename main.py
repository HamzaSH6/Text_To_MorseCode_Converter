print("\n_____Text to Morse Code Converter_____")

morse_code = {"a": "•—", "b": "—•••", "c": "—•—•", "d": "—••", "e": "•", "f": "••—•", "g": "— —•", "h": "••••",
              "i": "••", "j": "•— — —", "k": "—•—", "l": "•—••", "m": "— —", "n": "—•", "o": "— — —", "p": "•— —•",
              "q": "— —•—", "r": "•—•", "s": "•••", "t": "—", "u": "••—", "v": "•••—", "w": "•— —", "x": "—••—",
              "y": "—•— —", "z": "— —••", "1": "•— — — —", "2": "••— — —", "3": "•• — —", "4": "••••—", "5": "•••••",
              "6": "—••••", "7": "— —•••", "8": "— — —••", "9": "— — — —•", "0": "— — — — —"}
alphabets = {'•—': 'a', '—•••': 'b', '—•—•': 'c', '—••': 'd', '•': 'e', '••—•': 'f', '——•': 'g', '••••': 'h', '••': 'i',
             '•———': 'j', '—•—': 'k', '•—••': 'l', '——': 'm', '—•': 'n', '———': 'o', '•——•': 'p', '——•—': 'q',
             '•—•': 'r', '•••': 's', '—': 't', '••—': 'u', '•••—': 'v', '•——': 'w', '—••—': 'x', '—•——': 'y',
             '——••': 'z', '•————': '1', '••———': '2', '••——': '3', '••••—': '4', '•••••': '5', '—••••': '6',
             '——•••': '7', '———••': '8', '————•': '9', '—————': '0'}


def s_alpha(word):
    return [letter for letter in word]


def s_code(code):
    return [morse for morse in code]


while True:
    try:
        option = int(input("\n1) Text to Morse Code Converter\n"
                           "2) Morse Code To Text Converter\n"
                           "3) Exit\n"
                           "Choose Converter Mode (Type Number of the Option): "))

        # Text to Morse Code Converter
        if option == 1:
            string = input("Text: ").lower().replace(" ", "")
            a_string = s_alpha(string)

            for s in a_string:
                print(morse_code[s], end=" / ")
            print(" ")

        # Morse Code To Text Converter
        elif option == 2:
            try:
                morse = input("Morse Code (separate by space): ")
                a_morse = s_code(morse.split(" "))

                for m in a_morse:
                    print(alphabets[m], end="")
            except KeyError:
                print("Invalid Morse Code, Again")

        # Exit the Program
        elif option == 3:
            print("Program Closed/Stopped Successfully!")
            exit()
        # elif type(option) is str():
        #     print("Invalid Choice Insert a Number, Choose Again")
        else:
            print("Invalid Number Choice, Choose Again")
    except ValueError:
        print("Invalid Choice Insert a Number, Choose Again")
