def menu():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")


def encode(password):
    string = str(password)
    list = []
    final_string = str()
    for i in string:
        list.append(i)
    for i in range(0, len(list)):
        number = int(list[i]) + 3
        final_string += str(number)
    return final_string


def decode(password):
    return "(Decode is work in progress!)"


def main():
    menu()
    choice = int(input("Please enter an option:"))
    while choice != 3:
        password = input("Please enter your password to encode:")
        if choice == 1:
            print("Your password has been encoded and stored!\n")
            menu()
            choice = int(input("Please enter an option:"))
        if choice == 2:
            print(f"The encoded password is {encode(password)}, and the original password is {decode(password)}.\n")
            menu()
            choice = int(input("Please enter an option:"))
        if choice == 3:
            break


if __name__ == "__main__":
    main()
