def decode(encoded_password):
    templist = list(encoded_password)
    newlist = []
    for i in templist:
        encoded_char = str(int(i) -3)
        newlist.append(encoded_char)
    return ''.join(newlist)
