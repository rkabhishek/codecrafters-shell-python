import sys

def main():
    # TODO: Uncomment the code below to pass the first stage
    print("$ ", end="", flush=True)
    cmd = input()
    sys.stdout.write(f"{cmd}: command not found\n")


if __name__ == "__main__":
    main()
