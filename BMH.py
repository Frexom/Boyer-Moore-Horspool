def BMH (arg, chaine):
    step = len(arg)-1
    while step <= len(chaine):
        if chaine[step] != arg[-1]:
            if chaine[step] not in arg:
                step += len(arg)-1
            else:
                for i in range(len(arg)-1, -1, -1):
                    if arg[i] == chaine[step]:
                        step += len(arg) - i -1
        else:
            if chaine[(step - len(arg)+1):step+1] == arg:
                print(chaine[step - len(arg)+1])
                return (step - len(arg)+1)
            else:
                step += len(arg)
