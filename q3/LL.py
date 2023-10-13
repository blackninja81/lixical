# Define the production rules
# Replace this with your specific CFG rules
productions = {
    'S': [['E']],
    'E': [['E', '+', 'T'], ['T']],
    'T': [['T', '*', 'F'], ['F']],
    'F': [['(', 'E', ')'], ['id']]
}

# Define the terminals and non-terminals
terminals = {'+', '*', '(', ')', 'id'}
non_terminals = {'S', 'E', 'T', 'F'}

# Function to calculate the First set for a given symbol
def calculate_first(symbol, processed=None):
    if processed is None:
        processed = set()
    first_set = set()
    if symbol in terminals:
        first_set.add(symbol)
    elif symbol in non_terminals and symbol not in processed:
        processed.add(symbol)
        for production in productions[symbol]:
            if production[0] in terminals:
                first_set.add(production[0])
            else:
                for s in production:
                    if s in terminals:
                        first_set.add(s)
                        break
                    else:
                        first_set = first_set.union(calculate_first(s, processed))
                        if 'ε' not in calculate_first(s, processed):
                            break
    return first_set


# Function to calculate the Follow set for a given non-terminal
def calculate_follow(non_terminal):
    follow_set = set()
    if non_terminal == list(non_terminals)[0]:
        follow_set.add('$')
    for key in productions.keys():
        for production in productions[key]:
            if non_terminal in production:
                pos = production.index(non_terminal)
                if pos == (len(production)-1):
                    if key != non_terminal:
                        follow_set = follow_set.union(calculate_follow(key))
                else:
                    follow_of_next_symbol = calculate_first(production[pos+1])
                    if 'ε' in follow_of_next_symbol:
                        follow_of_next_symbol.remove('ε')
                        if key != non_terminal:
                            follow_set = follow_set.union(calculate_follow(key))
                    follow_set = follow_set.union(follow_of_next_symbol)
    return follow_set

# Initialize the LL(1) parsing table as an empty dictionary
ll1_table = {}

# Construct the LL(1) parsing table
for non_terminal in non_terminals:
    for production in productions[non_terminal]:
        first_of_production = calculate_first(production[0])
        for terminal in first_of_production:
            if terminal != 'ε':
                ll1_table[(non_terminal, terminal)] = production

        if 'ε' in first_of_production:
            follow_of_key = calculate_follow(non_terminal)
            for terminal in follow_of_key:
                ll1_table[(non_terminal, terminal)] = ['ε']

# Print the LL(1) parsing table
for key, production in ll1_table.items():
    print(f'M[{key}] = {production}')
