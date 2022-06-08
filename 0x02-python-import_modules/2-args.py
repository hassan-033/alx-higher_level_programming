#!/usr/bin/python3
if __name__ == "__main__":
    import sys
narg = len(sys.argv)
if narg == 1:
    print("0 arguments.")
elif narg == 2:
    print("1 argument:")
    print(f"{narg - 1}: {sys.argv[narg - 1]}")
else:
    print(f"{narg - 1} arguments:")
    for arg in range(1, narg):
        print(f"{arg}: {sys.argv[arg]}")
