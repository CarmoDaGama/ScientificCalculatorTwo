operators = '^*/+-'


def get_list_expression(expression):
    global operators
    expression_list = []
    member = ''
    for index, character in enumerate(expression):

        if character == '(':
            expression_list.append(character)
        elif character == ')':
            if member != '':
                expression_list.append(member)
            expression_list.append(character)
            member = ''
        elif character in operators:
            if member.isnumeric() or member == '':
                if expression[index - 1] != ')' and member != '':
                    expression_list.append(member)
                expression_list.append(character)
            member = ''
        else:
            if character.isnumeric():
                print(character, end='...')
                member += character

    if member.isnumeric():
        expression_list.append(member)

    return expression_list


def calc(number1, number2, operator):
    if operator == '^':
        return number1**number2
    elif operator == '*':
        return number1*number2
    elif operator == '/':
        return number1 / number2
    elif operator == '-':
        return number1 - number2
    elif operator == '+':
        return number1 + number2
def contains_operator(expressions):
    for operator in operators:
        if operator in expressions:
            return True
    return False


def replace_operation(expressions, index_operator, result):
    tmp_expression = []

    for index, value in enumerate(expressions):
        if index == index_operator - 1 or index == index_operator + 1:
            continue
        elif index == index_operator:
            tmp_expression.append(result)
        else:
            tmp_expression.append(value)
    expressions.clear()
    return tmp_expression.copy()


def calculate_expression(l_expression):
    l_expression = get_list_expression(l_expression)
    idea_optional(l_expression)
    for operator in operators:
        while operator in l_expression:
            index_operator = l_expression.index(operator)
            result = calc(float(l_expression[index_operator - 1]), float(l_expression[index_operator + 1]), operator)
            l_expression = replace_operation(l_expression.copy(), index_operator, result)
    if contains_operator(l_expression):
        calculate_expression(l_expression)
    else:
        return float(l_expression[0])


def ValidParentsExpression(expression):
    stack = []
    for symbol in expression:
        if symbol == '(':
            stack.append('(')
        elif symbol == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        return True
    else:
        return False



def print_expressions(l_expression):
    print('\n\nValues: ', end='')
    for index, value in enumerate(l_expression):
        print(value, end='|')

    print('\n')
    print('Indexs: ', end='')
    for index, value in enumerate(l_expression):
        print(f'{index}', end='|')


def idea_optional(expressions):
    for index, value in enumerate(expressions):
        if value == '-' and not('-' in str(expressions[index + 1])):
            expressions[index + 1] = float(expressions[index + 1])*-1
            expressions[index] = '+'




# 5^(2+4)-(5-77)+55*79/93


expression = str(input('Type it Expression: '))


# expression = calculate_expression(expression)
print(f'\n\nFinal Result: {get_list_expression(expression)}')