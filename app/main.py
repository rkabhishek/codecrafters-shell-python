
CMD_ECHO = "echo"
CMD_EXIT = "exit"
CMD_TYPE = "type"
BUILTINS = [CMD_ECHO, CMD_EXIT, CMD_TYPE]

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        try:
            print("$ ", end="", flush=True)
            line = input().strip()
            cmd, *rest = line.split(maxsplit=1)
            args = rest[0] if rest else ""
            if line == CMD_EXIT:
                break
            elif line.startswith(CMD_ECHO):
                print(args)
            elif line.startswith(CMD_TYPE):
                if args in BUILTINS:
                    print(f"{args} is a shell builtin")
                else:
                    print(f"{args}: not found")
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
