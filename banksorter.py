# coded by: Joshua Turner
# Helper program used to sort initial data file into more manageable files

def main():
    banksort()
    accountsort()
    creditsort()
    financesort()
    servicesort()

def banksort():
    """
    This function reads the contents of a text file, scans for BankA,B,C,D,
    and writes the list item to the appropriate output
    file.
    """
    infileName = "DataSet.txt"
    infile = open(infileName, "rb")
    bankAoutfile = "bankA.txt"
    bankBoutfile = "bankB.txt"
    bankCoutfile = "bankC.txt"
    bankDoutfile = "bankD.txt"
    outfileA = open(bankAoutfile, "w")
    outfileB = open(bankBoutfile, "w")
    outfileC = open(bankCoutfile, "w")
    outfileD = open(bankDoutfile, "w")
    for line in infile:
        if b"BankA" in line:
            print(line, file=outfileA)
        elif b"BankB" in line:
            print(line, file=outfileB)
        elif b"BankC" in line:
            print(line, file=outfileC)
        elif b"BankD" in line:
            print(line, file=outfileD)

    infile.close()
    outfileA.close()
    outfileB.close()
    outfileC.close()
    outfileD.close()

def accountsort():
    """
    This function reads the contents of the sorted bank files (A,B,C,D), scans
    for the word 'account' and writes to the appropriate output file.
    """
    infileA = open("bankA.txt", "rb")
    infileB = open("bankB.txt", "rb")
    infileC = open("bankC.txt", "rb")
    infileD = open("bankD.txt", "rb")
    accountoutA = open("accountA.txt", "w")
    accountoutB = open("accountB.txt", "w")
    accountoutC = open("accountC.txt", "w")
    accountoutD = open("accountD.txt", "w")
    for line in infileA:
        if b"account" in line:
            print(line, file=accountoutA)
    for line in infileB:
        if b"account" in line:
            print(line, file=accountoutB)
    for line in infileC:
        if b"account" in line:
            print(line, file=accountoutC)
    for line in infileD:
        if b"account" in line:
            print(line, file=accountoutD)

    infileA.close()
    infileB.close()
    infileC.close()
    infileD.close()
    accountoutA.close()
    accountoutB.close()
    accountoutC.close()
    accountoutD.close()

def creditsort():
    """
    This function reads the contents of the sorted bank files (A,B,C,D), scans
    for the word 'credit' and writes to the appropriate output file.
    """
    infileA = open("bankA.txt", "rb")
    infileB = open("bankB.txt", "rb")
    infileC = open("bankC.txt", "rb")
    infileD = open("bankD.txt", "rb")
    creditoutA = open("creditA.txt", "w")
    creditoutB = open("creditB.txt", "w")
    creditoutC = open("creditC.txt", "w")
    creditoutD = open("creditD.txt", "w")
    for line in infileA:
        if b"credit" in line:
            print(line, file=creditoutA)
    for line in infileB:
        if b"credit" in line:
            print(line, file=creditoutB)
    for line in infileC:
        if b"credit" in line:
            print(line, file=creditoutC)
    for line in infileD:
        if b"credit" in line:
            print(line, file=creditoutD)

    infileA.close()
    infileB.close()
    infileC.close()
    infileD.close()
    creditoutA.close()
    creditoutB.close()
    creditoutC.close()
    creditoutD.close()

def financesort():
    """
    This function reads the contents of the sorted bank files (A,B,C,D), scans
    for the word 'finance' and writes to the appropriate output file.
    """
    infileA = open("bankA.txt", "rb")
    infileB = open("bankB.txt", "rb")
    infileC = open("bankC.txt", "rb")
    infileD = open("bankD.txt", "rb")
    financeoutA = open("financeA.txt", "w")
    financeoutB = open("financeB.txt", "w")
    financeoutC = open("financeC.txt", "w")
    financeoutD = open("financeD.txt", "w")
    for line in infileA:
        if b"finance" in line:
            print(line, file=financeoutA)
    for line in infileB:
        if b"finance" in line:
            print(line, file=financeoutB)
    for line in infileC:
        if b"finance" in line:
            print(line, file=financeoutC)
    for line in infileD:
        if b"finance" in line:
            print(line, file=financeoutD)

    infileA.close()
    infileB.close()
    infileC.close()
    infileD.close()
    financeoutA.close()
    financeoutB.close()
    financeoutC.close()
    financeoutD.close()

def servicesort():
    """
    This function reads the contents of the sorted bank files (A,B,C,D), scans
    for the word 'service' and writes to the appropriate output file.
    """
    infileA = open("bankA.txt", "rb")
    infileB = open("bankB.txt", "rb")
    infileC = open("bankC.txt", "rb")
    infileD = open("bankD.txt", "rb")
    serviceoutA = open("serviceA.txt", "w")
    serviceoutB = open("serviceB.txt", "w")
    serviceoutC = open("serviceC.txt", "w")
    serviceoutD = open("serviceD.txt", "w")
    for line in infileA:
        if b"service" in line:
            print(line, file=serviceoutA)
    for line in infileB:
        if b"service" in line:
            print(line, file=serviceoutB)
    for line in infileC:
        if b"service" in line:
            print(line, file=serviceoutC)
    for line in infileD:
        if b"service" in line:
            print(line, file=serviceoutD)

    infileA.close()
    infileB.close()
    infileC.close()
    infileD.close()
    serviceoutA.close()
    serviceoutB.close()
    serviceoutC.close()
    serviceoutD.close()

main()
