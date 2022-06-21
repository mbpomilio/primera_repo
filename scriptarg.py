import sys

print(sys.argv)

if len(sys.argv) != 3:
    print("error, necesito 2 argumentos")
else:
    for i in range(int(sys.argv[2])):
        print(sys.argv[1])
