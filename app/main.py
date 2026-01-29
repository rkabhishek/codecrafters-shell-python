import sys

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        try:
            print("$ ", end="", flush=True)
            line = input().strip()
            if line == "exit":
                break
            elif line.startswith("echo"):
                cmd, args = line.split(maxsplit=1) if " " in line else (line, "")
                print(args)
            else:
                print(f"{line}: command not found")
        except KeyboardInterrupt:
            print()
            continue
        except EOFError:
            print()
            break



if __name__ == "__main__":
    main()
