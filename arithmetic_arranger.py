def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return('Error: Too many problems.')

    first_line = []
    second_line = []
    dashes_line = []
    answer_line = []

    for problem in problems:
        operand1, operator, operand2 = problem.split()
        if operator != '+' and operator !='-':
            return("Error: Operator must be '+' or '-'.")
        if not operand1.isdigit() or not operand2.isdigit():
            return('Error: Numbers must only contain digits.')
        if len(operand1) > 4 or len(operand2) > 4:
            return('Error: Numbers cannot be more than four digits.')

        num1 = int(operand1)
        num2 = int(operand2)

        width = max(len(operand1), len(operand2)) + 2
        formatted_op1 = operand1.rjust(width)
        first_line.append(formatted_op1)

        formatted_op2 = operator + ' ' + operand2.rjust(width - len(operator) - 1)
        second_line.append(formatted_op2)

        dashes = ('-' * width)
        dashes_line.append(dashes)

        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2

        formatted_answer = str(answer)
        answer_align = formatted_answer.rjust(width)
        answer_line.append(answer_align)

    one_line= ('    ').join(first_line)
    two_line = ('    ').join(second_line)
    three_line = ('    ').join(dashes_line)
    arranged_problems = one_line + '\n' + two_line + '\n' + three_line

    if show_answers:
        answer_string = ('    ').join(answer_line)
        arranged_problems += '\n' + answer_string

    return arranged_problems