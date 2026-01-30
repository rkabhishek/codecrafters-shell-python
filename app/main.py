import os

CMD_ECHO = "echo"
CMD_EXIT = "exit"
CMD_TYPE = "type"
BUILTINS = [CMD_ECHO, CMD_EXIT, CMD_TYPE]


def search_path(file):
    paths = os.environ.get("PATH", "").split(os.pathsep)
    for path in paths:
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path

    return None


def handle_type(args):
    if args in BUILTINS:
        print(f"{args} is a shell builtin")
        return

    full_path = search_path(args)
    if full_path:
        print(f"{args} is {full_path}")
    else:
        print(f"{args}: not found")


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
                handle_type(args)
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
