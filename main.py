# Name: August McDaniel

def encode(encoded_pw):
    initial_list = list(encoded_pw)
    encoded_list = []
    for i in initial_list:
        encoded = str((int(i) - 3) % 10)
        encoded_list.append(encoded)
    new_password = encoded_list.join
    return new_password

# Name: Noah Lunberry
def decode(encoded_pw):
    # Name: Noah Lunberry
    templist = list(encoded_pw)
    newlist = []
    for i in templist:
        encoded_char = str((int(i) - 3) % 10)
        newlist.append(encoded_char)
    return ''.join(newlist)


def main():
    encoded_pw = None
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        user_input = int(input('Please enter an option: '))
        if user_input == 1:
            password = input('Please enter your password to decode: ')
            encoded_pw = encode(password)
            print('Your password has been encoded and stored!')
            print()
        elif user_input == 2:
            decoded_pw = decode(str(encoded_pw))
            print('The encoded password is ' + encoded_pw + ', and the original password is ' + decoded_pw + '.')
        elif user_input == 3:
            break

if __name__ == '__main__':
    main()
