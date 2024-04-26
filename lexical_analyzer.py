import re

def tokenize(input_string):
    tokens = []
    keywords = ['int', 'float', 'if', 'else', 'while', 'for', 'return']
    operators = ['+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>=']
    separators = [';', ',', '(', ')', '{', '}']
    
    # Regular expressions for token patterns
    pattern_identifier = r'[a-zA-Z_][a-zA-Z0-9_]*'
    pattern_integer = r'\d+'
    pattern_operator = '|'.join(re.escape(op) for op in operators)
    pattern_separator = '|'.join(re.escape(sep) for sep in separators)
    
    # Combined regular expression pattern
    pattern = f'{pattern_identifier}|{pattern_integer}|{pattern_operator}|{pattern_separator}'
    
    # Tokenize the input string
    for match in re.finditer(pattern, input_string):
        value = match.group()
        token_type = ''
        
        if value in keywords:
            token_type = 'Keyword'
        elif re.match(pattern_identifier, value):
            token_type = 'Identifier'
        elif re.match(pattern_integer, value):
            token_type = 'Integer'
        elif re.match(pattern_operator, value):
            token_type = 'Operator'
        elif re.match(pattern_separator, value):
            token_type = 'Separator'
        else:
            token_type = 'Unidentified'
        
        tokens.append({'Token': token_type, 'Value': value})
    
    return tokens

# Test cases
input1 = "int a = b + c"
input2 = "int x=ab+bc+30+y+z"

output1 = tokenize(input1)
output2 = tokenize(input2)

print("For Expression \"int a = b + c\":")
for token in output1:
    print(f"Token: {token['Token']}, Value: {token['Value']}")

print("\nFor Expression \"int x=ab+bc+30+y+z\":")
for token in output2:
    print(f"Token: {token['Token']}, Value: {token['Value']}")
