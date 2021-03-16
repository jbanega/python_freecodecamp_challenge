def arithmetic_arranger(problems, displayResult=False):
    lineOne = str()
    lineTwo = str()
    lineThree = str()
    lineFour = str()
    arranged_problems = str()


    for operation in problems:

        if len(problems) > 5:
            return "Error: Too many problems."

        # Values
        numbers_and_operator = operation.split(" ")
        firstValue = numbers_and_operator[0]
        operator = numbers_and_operator[1]
        secondValue = numbers_and_operator[2]

        if firstValue.isnumeric() == False or secondValue.isnumeric() == False:
            return "Error: Numbers must only contain digits."
        
        if len(firstValue) > 4 or len(secondValue) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        if operator == "+":
            result = int(firstValue) + int(secondValue)
        elif operator == "-":
            result = int(firstValue) - int(secondValue)
        else:
            return "Error: Operator must be '+' or '-'."

        # Formatting lines
        firstLine = str(firstValue)
        secondLine = str(secondValue)
        lengthLine = len(max([firstLine, secondLine], key=len)) + 2
        line_separator = ("-" * lengthLine)
        white_space = (" " * 4)

        # Numbers right-aligned
        firstLine = firstLine.rjust(lengthLine)
        secondLine = operator + secondLine.rjust(lengthLine - 1)
        result = str(result).rjust(lengthLine)

        # Displaying
        if operation != problems[-1]:
            lineOne += firstLine + white_space
            lineTwo += secondLine + white_space
            lineThree += line_separator + white_space
            lineFour += result + white_space
        else:
            lineOne += firstLine
            lineTwo += secondLine
            lineThree += line_separator
            lineFour += result
        
        if displayResult == True:
            arranged_problems = lineOne + "\n" + lineTwo + "\n" + lineThree + "\n" + lineFour
        else:
            arranged_problems = lineOne + "\n" + lineTwo + "\n" + lineThree


    return arranged_problems


if __name__ == "__main__":
    problems = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
    result = arithmetic_arranger(problems, displayResult=True)
    print(result)