file1 = open("input.txt","w") 

n = int(input("").strip())
file1.write(str(n) + "\n")
pa = ""
for i in range(n):
    pa += str(i+1) + " "
file1.write(pa)
file1.close() 