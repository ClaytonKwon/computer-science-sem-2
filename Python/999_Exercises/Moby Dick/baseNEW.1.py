c = 0
with open('moby.txt') as f:
    for line in f:
        sentence = line.strip()
        for x in range(0,len(sentence)):
            if sentence[x:x+5].lower() == "whale":
                c = c+1
print(c)
f.close()