newlist=list()    
fhand = open('romeo.txt')
for line in fhand:
    words=line.split()
    for words in words:
        if words in newlist:continue
        newlist.append(words)
        newlist.sort()
print(newlist)
        
