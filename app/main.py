import os
import subprocess

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
    for arg in args:
        if arg in BUILTINS:
            print(f"{arg} is a shell builtin")
            return

        full_path = search_path(arg)
        if full_path:
            print(f"{arg} is {full_path}")
        else:
            print(f"{arg}: not found")

def handle_external(cmd, args):
    full_path = search_path(cmd)

    if full_path:
        subprocess.run([cmd, *args])

    else:
        print(f"{cmd}: command not found")


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        try:
            print("$ ", end="", flush=True)
            line = input().strip()
            cmd, *args = line.split()
            if cmd == CMD_EXIT:
                break
            elif cmd == CMD_ECHO:
                print(*args)
            elif cmd == CMD_TYPE:
                handle_type(args)
            else:
                handle_external(cmd, args)


        except KeyboardInterrupt:
            print()
            continue
        except EOFError:
            print()
            break


if __name__ == "__main__":
    main()
