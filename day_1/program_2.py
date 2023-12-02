full_text = open("input.txt", "rt")
repl_numbers = {"one":"o1e",
                "two":"t2o",
                "three":"t3e",
                "four":"f4r",
                "five":"f5e",
                "six":"s6x",
                "seven":"s7n",
                "eight":"e8t",
                "nine": "n9e"}
numbers = []
for line in full_text:
    for j in repl_numbers.keys():
        line = line.replace(j, repl_numbers[j])
    x = []
    for i in line:
        if i.isdigit():
            x.append(i)
    numbers.append(int(str(x[0])+str(x[-1])))
print(sum(numbers))