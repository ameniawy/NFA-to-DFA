
from collections import defaultdict
import argparse


class NFA:
    def __init__(self, alphabet, initial_state, final_state, transitions, states):
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_state = final_state
        self.transitions = transitions
        self.states = states


class DFA:
    def __init__(self, alphabet, initial_state, final_states, transitions, states):
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        self.states = states

    def __str__(self):
        res = ''
        res = res + ', '.join([str(state) for state in self.states]) + '\n'
        res = res + ', '.join([str(char) for char in self.alphabet]) + '\n'
        res = res + str(self.initial_state) + '\n'
        res = res + ', '.join([str(state)
                               for state in self.final_states]) + '\n'
        res = res + ', '.join(['('+str(transition['arc_from'])+', '+str(transition['arc_condition']) +
                               ', '+str(transition['arc_to'])+')' for transition in self.transitions])
        return res


def dfs(state, transitions):

    valid_transitions = [transition['arc_to']
                         for transition in transitions if transition['arc_from'] == state and transition['arc_condition'] == ' ']

    if not valid_transitions:
        return valid_transitions

    res = []

    for valid_transition in valid_transitions:
        res += dfs(valid_transition, transitions)

    return valid_transitions + res


def epsilon_closure(NFA):
    eps_dict = defaultdict(list)

    for state in NFA.states:
        eps_dict[state] = list(set([state] + dfs(state, NFA.transitions)))

    return eps_dict


def create_table(NFA, eps_dict):
    dict_index = 0
    table = defaultdict(dict)
    table[dict_index] = {
        'nfa_state': eps_dict[NFA.initial_state]
    }
    dict_index += 1

    pointer = 0

    while pointer < len(table.keys()):

        current_nfa_state = table[pointer]
        for char in NFA.alphabet:
            found_states = find_states_from_condition(
                current_nfa_state['nfa_state'], char, NFA.transitions, eps_dict)
            search_result = [key for key in table.keys() if 'nfa_state' in table[key].keys(
            ) and set(table[key]['nfa_state']) == set(found_states)]
            if search_result:
                table[pointer][char] = search_result[0]
            else:
                if found_states:
                    table[dict_index]['nfa_state'] = found_states
                    table[pointer][char] = dict_index
                    dict_index += 1
                else:
                    table[pointer][char] = 'DEAD'

        pointer += 1

    return table


def find_states_from_condition(from_states, condition, transitions, eps_dict):
    res = set()
    for transition in transitions:
        if transition['arc_from'] in from_states and transition['arc_condition'] == condition:
            res.add(transition['arc_to'])

    res_temp = []

    for state in list(res):
        res_temp += eps_dict[state]

    return list(set(res_temp).union(res))


def nfa_to_dfa(nfa):

    closure = epsilon_closure(nfa)
    table = create_table(nfa, closure)

    initial_state = 0
    final_states = [key for key in table.keys(
    ) if nfa.final_state in table[key]['nfa_state']]

    alphabet = nfa.alphabet
    transitions = list()

    found_dead = False

    for state in table.keys():
        for char in nfa.alphabet:
            if table[state][char] == 'DEAD':
                found_dead = True
            transitions.append({
                'arc_from': state,
                'arc_condition': char,
                'arc_to': table[state][char]
            })

    if found_dead:
        for char in alphabet:
            if char != ' ':
                transitions.append({
                    'arc_from': 'DEAD',
                    'arc_condition': char,
                    'arc_to': 'DEAD'
                })

    dfa = DFA(alphabet, initial_state, final_states, transitions, [
              i for i in range(len(table.keys()))] + (['DEAD'] if found_dead else []))

    return dfa


def read_nfa_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        states = lines[0].split(',')
        states = [state.strip() for state in states]
        alphabet = lines[1].split(',')
        if ' ' in alphabet:
            alphabet.remove(' ')
        alphabet = [char.strip() for char in alphabet]
        initial_state = lines[2].strip()
        final_state = lines[3].strip()
        transitions = list()
        for transition_tuple in lines[4].replace(" ", "").replace("),(", "|").replace("(", "").replace(")", "").split("|"):
            splitted_tuple = [element.strip(
            ) if element != '' else ' ' for element in transition_tuple.split(",")]
            transition = {
                'arc_from': splitted_tuple[0],
                'arc_condition': splitted_tuple[1],
                'arc_to': splitted_tuple[2]
            }
            transitions.append(transition)

        return NFA(alphabet, initial_state, final_state, transitions, states)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()

    print(args.file)

    loaded_nfa = read_nfa_from_file(args.file)

    dfa = nfa_to_dfa(loaded_nfa)
    print(dfa)

    output_file = open('task_2_2_result.txt', 'w+')
    output_file.write(str(dfa))
