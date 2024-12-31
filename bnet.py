#NAME: Shruti Gunasekaran
#ID: 1002162170

import sys
from collections import defaultdict


# ModelNetwork class to define the structure of the probabilistic model
class ModelNetwork:
    def __init__(self):
        # Initialize the probability table for B, G, C, F with default float values
        self.probability_table = {
            'B': defaultdict(float),
            'G': defaultdict(float),
            'C': defaultdict(float),
            'F': defaultdict(float)
        }
        self.frequency_map = defaultdict(int)
        self.total_entries = 0

    # Method to process the training data and update the probability table
    def process_training_data(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                b, g, c, f = map(int, line.strip().split())
                self.frequency_map[('B', b)] += 1
                self.frequency_map[('G', g, 'B', b)] += 1
                self.frequency_map[('C', c)] += 1
                self.frequency_map[('F', f, 'G', g, 'C', c)] += 1
                self.total_entries += 1

        # Update probability table for B and C based on the frequencies
        for var in ['B', 'C']:
            for val in [0, 1]:
                # Calculate the probability of each variable (B, C) being 0 or 1
                self.probability_table[var][val] = self.frequency_map[('B', val)] / self.total_entries if var == 'B' else self.frequency_map[('C', val)] / self.total_entries

        # Update probability table for G given B (P(G | B))
        for g in [0, 1]:
            for b in [0, 1]:
                total = sum(self.frequency_map[('G', g, 'B', b)] for g in [0, 1])
                self.probability_table['G'][(g, b)] = self.frequency_map[('G', g, 'B', b)] / total if total else 0.5

        # Update probability table for F given G and C (P(F | G, C))
        for f in [0, 1]:
            for g in [0, 1]:
                for c in [0, 1]:
                    total = sum(self.frequency_map[('F', f, 'G', g, 'C', c)] for f in [0, 1])
                    self.probability_table['F'][(f, g, c)] = self.frequency_map[('F', f, 'G', g, 'C', c)] / total if total else 0.5


    # Method to compute the joint probability for the variables B, G, C, F
    def compute_joint_probability(self, b, g, c, f):
        return (self.probability_table['B'][b] * self.probability_table['G'][(g, b)] *
                self.probability_table['C'][c] * self.probability_table['F'][(f, g, c)])

    # Method to calculate the probability of query variables given evidence
    def calculate_inference(self, query_vars, given_vars):
        variable_map = {'B': 0, 'G': 1, 'C': 2, 'F': 3}
        query_list = [v for v in 'BGCF' if v in query_vars]
        evidence_list = [v for v in 'BGCF' if v in given_vars]
        hidden_vars = [v for v in 'BGCF' if v not in query_list and v not in evidence_list]

        numerator = 0
        denominator = 0
        # Loop through all possible combinations of (B, G, C, F)
        for values in [(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 0, 1, 1),
                    (0, 1, 0, 0), (0, 1, 0, 1), (0, 1, 1, 0), (0, 1, 1, 1),
                    (1, 0, 0, 0), (1, 0, 0, 1), (1, 0, 1, 0), (1, 0, 1, 1),
                    (1, 1, 0, 0), (1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)]:
            if all(values[variable_map[v]] == given_vars[v] for v in evidence_list):
                prob = self.compute_joint_probability(*values)
                denominator += prob
                if all(values[variable_map[v]] == query_vars[v] for v in query_list):
                    numerator += prob

        return numerator / denominator if denominator != 0 else 0

    # Method to process the user input for queries
    def handle_query(self, user_input):
        if user_input.lower() == 'none':
            return None
        parts = user_input.split('given')
        query = {}
        evidence = {}
        for item in parts[0].split():
            var, val = item[0], item[1]
            query[var] = 1 if val == 't' else 0
        if len(parts) > 1:
            for item in parts[1].split():
                var, val = item[0], item[1]
                evidence[var] = 1 if val == 't' else 0
        return self.calculate_inference(query, evidence)


# Function to start the program
def start_program():
    # Ensure that the correct number of command-line arguments are passed
    if len(sys.argv) != 2:
        print("How to use: python bnet.py <training_data.txt>")
        sys.exit(1)
    model = ModelNetwork()
    model.process_training_data(sys.argv[1])
    # Enter a loop to continuously accept user queries
    while True:
        user_input = input("Query: ")
        # Exit condition for the program
        if user_input.lower() == 'none':
            break
        result = model.handle_query(user_input)
        
        if result is not None:
            print(f"Probability: {result:.6f}")


if __name__ == "__main__":
    start_program()
