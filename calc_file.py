with open('step_2.txt') as f:
    for line in f:
        line = f.readline()
        sections = line.split()
        sign = sections[1]
        num1 = int(sections[2])
        num2 = int(sections[3])
        
        print(line)

        def add(num1, num2):
            return num1 + num2

        def subtract(num1, num2):
            return num1 - num2

        def multiply(num1, num2):
            return num1 * num2

        def divide(num1, num2):
           return num1 / num2

        if sign == '+':
            print(add(num1, num2))
        if sign == '-':
            print(subtract(num1, num2))
        if sign == '/':
            print(divide(num1, num2))
        if sign == '*':
            print(multiply(num1, num2))

output = open('C:\\Users\\mcadec\\Desktop\\DevOps\\Scripts\\step_2_exp.txt')
output.write

