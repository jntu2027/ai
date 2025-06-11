def TOH(n,a,b,c):
    if (n > 0):
        TOH(n-1,a,c,b)
        print(f"Move disk {n} from {a} -> {c}")
        TOH(n-1,b,a,c)

TOH(int(input("Enter number of disks:\t")),"A","B","C")