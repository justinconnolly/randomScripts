def getHamming(bits: list):
    bits.append(bits[1] ^ bits[2] ^ bits[3])
    bits.append(bits[0] ^ bits[2] ^ bits[3])
    bits.append(bits[0] ^ bits[1] ^ bits[3])

if __name__ == '__main__':
    while True:
        userIn = input("Enter 4 bit code: ")
        if userIn == "exit":
            break
        bitList = [int(x) for x in list(userIn)]
        getHamming(bitList)
        bitList.insert(4,'-')
        print(''.join([str(x) for x in bitList]))
