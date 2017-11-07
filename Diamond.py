numRow = int(input("How many rows? (ODD NUMBERS ONLY) "))


cur = 0
for i in range(0, numRow + 1):
    if (i % 2 != 0 or i == numRow + 1):
        cur += 1
        for a in range(0, int((numRow + 1) / 2) - cur):
            print("", end = " ")
        for j in range(0, i):
            print("*", end = "")
        print("")

cur = int((numRow + 1) / 2)
for k in range(numRow, 0, -1):
    if (k % 2 != 0 and k != numRow):
        cur -= 1
        for a in range(0, int((numRow + 1) / 2) - cur):
            print("", end = " ")
        for l in range(0, k):
            print("*", end = "")
        print("")

input("PRESS ENTER TO EXIT")
