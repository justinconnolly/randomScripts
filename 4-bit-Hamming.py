def getHamming(bits: list):
    bits.append("-")
    bits.append(bits[1] ^ bits[2] ^ bits[3])
    bits.append(bits[0] ^ bits[2] ^ bits[3])
    bits.append(bits[0] ^ bits[1] ^ bits[3])
    print(''.join([str(x) for x in bits]))

if __name__ == '__main__':
    choice = ""
    bin = ["0","1"]
    while True:
        choice = input("(M)anual entry, (A)utomatic, or (Q)uit:\n")
        if choice.lower() == "m":
            while True:
                userIn = input("Enter 4 bit binary code, (Q)uit, or return to the (M)enu:\n")
                if userIn.lower() == "q":
                    quit()
                elif userIn.lower() == "m":
                    break
                charCheck = [character in bin for character in userIn]
                if len(userIn) != 4 or not all(charCheck):
                    print("Invalid input.")
                    continue
                bitList = [int(x) for x in list(userIn)]
                getHamming(bitList)
                # print(''.join([str(x) for x in bitList]))
                # print(bitList)
        elif choice.lower() == "a":
            from itertools import product

            productList = []
            products = list(product(bin,repeat=4))
            for tuple in products:
                productList.append([int(item) for item in tuple])
                getHamming(productList[len(productList) - 1])
                # print(''.join([str(x) for x in productList[len(productList) - 1]]))
        elif choice.lower() == "q":
            quit()
