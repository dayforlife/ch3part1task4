def myfunc():
    text = input().split(" ")
    for i in range(len(text)):
        text[i] = int(text[i])
    if max(text)<=0:
        print(1)
    else:
        for i in range(1, max(text)+ 3):
            if i > 0 and i not in text:
                print(i)
                break
            else:
                continue
myfunc()