import sys

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        try:
            print("$ ", end="", flush=True)
            cmd = input()
            print(f"{cmd}: command not found")
        except KeyboardInterrupt:
            print()
            continue
        except EOFError:
            print()
            break



if __name__ == "__main__":
    main()
