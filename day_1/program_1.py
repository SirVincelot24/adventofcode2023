full_text = open("input", "rt")
numbers = []
for line in full_text:
    x = []
    for i in line:
        if (i.isdigit()):
            x.append(i)
    numbers.append(int(str(x[0])+str(x[-1])))
print(sum(numbers))