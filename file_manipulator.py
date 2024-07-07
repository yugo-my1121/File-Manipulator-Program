import sys

def main():
    args = sys.argv

    if len(args) > 1 :

        if args[1] == 'reverse' :
            with open(args[2]) as f :
                contents = f.read()

            with open(args[3],'w') as f:
                f.write(contents[::-1])

        elif args[1] == 'copy':
                with open(args[2]) as f :
                    contents = f.read()

                with open(args[3],'w') as f:
                    f.write(contents)

        elif args[1] == 'duplicate-contents':
            with open(args[2]) as f :
                    contents = f.read()

            for i in range(int(args[3])):
                with open(args[2],'a') as f:
                    f.write(contents)

        elif args[1] == 'replace-string':
                with open(args[2]) as f :
                    contents = f.read()

                replaced_contents = contents.replace(args[3], args[4])
                with open(args[2],'w') as f:
                    f.write(replaced_contents)

if __name__ == "__main__":
    main()
