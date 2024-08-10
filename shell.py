import sys
import os

def main():
    while True:
        sys.stdout.write("(~>) ")
        sys.stdout.flush()
        command = input("🫧 ")
        c = command.split(" ")
        if c[0] == "exit":
            if len(c) > 1 and c[1].isdigit():
                sys.exit(int(c[1]))
            else:
                sys.exit()

        if c[0] == "echo":
            sys.stdout.write(" ".join(c[1:]) + "\n")
            continue

        if c[0] == "type":
            for e in c[1:]:
                if e == "echo":
                    print("echo is a shell builtin")
                elif e == "exit":
                    print("exit is a shell builtin")
                elif e == "type":
                    print("type is a shell builtin")
                else:
                    found = False
                    for path in os.getenv("PATH").split(":"):
                        if os.path.isdir(path):
                            for f in os.listdir(path):
                                if f == e:
                                    print(f"{e} is {path}/{e}")
                                    found = True
                                    break
                            if found:
                                break
                    if not found:
                        print(f"{e}: not found")
            continue

        # Catch-all for unsupported commands
        print(f"oyster: '{command}' error")

if __name__ == "__main__":
    main()
