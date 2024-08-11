import sys
import os
import subprocess

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
        if c[0] == "cd":
            if len(c) < 2 or c[1] == "~" or c[1] == "":
                os.chdir(os.path.expanduser("~"))
            elif c[1] == "/":
                os.chdir("/")
            else:
                try:
                    os.chdir(c[1])
                except FileNotFoundError:
                    print(f"sqish (said by cd): no such file or directory: {c[1]}")

        if c[0] == "pwd":
            os.getcwd()

        if c[0] == "type":
            for e in c[1:]:
                if e == "echo":
                    print("echo is builtin WOW")
                elif e == "exit":
                    print("exit is builtin WOW")
                elif e == "type":
                    print("type is builtin WOW")
                elif e == "cd":
                    print("cd is builtin WOW")
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

        else:
            found = False
            for path in os.getenv("PATH").split(os.pathsep):
                if os.path.isdir(path):
                    for f in os.listdir(path):
                        if f == c[0]:
                            result = subprocess.run(c, capture_output=True, text=True)
                            print(result.stdout, end="")
                            found = True
                            break
                    if found:
                        break
            if not found:
                print(f"sqish: '{command}' error")

if __name__ == "__main__":
    main()
