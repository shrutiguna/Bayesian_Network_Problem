# **Bayesian Network: Learning and Inference**

## **Overview**
This project implements a Bayesian Network (BN) for modeling and performing inference on relationships between variables. The network uses a training dataset to compute conditional probability tables (CPTs) for the variables and supports inference using **Inference by Enumeration**. The project can answer probabilistic queries with or without evidence.

The Bayesian Network contains four variables:
- **B**: Binary variable indicating whether there is a baseball game on TV.
- **G**: Binary variable indicating whether George watches TV.
- **C**: Binary variable indicating whether George is out of cat food.
- **F**: Binary variable indicating whether George feeds the cat.

- ![image](https://github.com/user-attachments/assets/3797f69c-0506-4e9b-8a53-6debd2554397)


---

## **File Descriptions**
- **`bnet.py`**: Main Python script implementing the Bayesian Network model and inference logic.
- **`training_data.txt`**: Training data file containing observations used to calculate CPTs.

- This project is written in Python version: 3.10.11
This project implements a simple Bayesian Network (BN) model using training data to estimate conditional probabilities. The model computes the joint probability distribution based on the observed frequencies in the training data and performs inference based on user queries. The Bayesian Network is structured around four variables:

- B: Binary variable (can be either 0 or 1)
- G: Binary variable (can be either 0 or 1)
- C: Binary variable (can be either 0 or 1)
- F: Binary variable (can be either 0 or 1)

The primary functionality includes processing training data, calculating joint probabilities, and performing inference queries with given evidence.

## Requirements
- Python 3.x
- The `collections` module (built-in in Python)

## File Structure
The main file of the project is `bnet.py`. It implements the Bayesian Network class and includes methods for training the network, computing joint probabilities, and handling inference queries.

## Installation
No installation is required. Simply ensure you have Python 3.x installed.


----Functions and Methods-----
1) process_training_data(file_path)
	Description: This method reads the training data from a file, processes the data to count the frequencies of different variable states, and stores these counts in a frequency map.
	Arguments: file_path - Path to the training data file.
2) compute_joint_probability(b, g, c, f)
	Description: This method computes the joint probability of all four variables B, G, C, and F using the probability table derived from the training data.
3) calculate_inference(query_vars, given_vars)
	Description: This method performs inference by summing the joint probabilities for all possible combinations of variables, based on the given query and evidence.
	Arguments:
		query_vars - Dictionary representing the query variables and their values.
		given_vars - Dictionary representing the given evidence variables and their values.
3) handle_query(user_input)
	Description: This method processes the user's query input, splits it into the query and evidence parts, and then calls calculate_inference to compute the result.
	Arguments: user_input - A string representing the user's query, possibly with evidence (e.g., B=t G=f given C=t).
4) start_program()
	Description: This is the main function that handles the overall flow of the program, including reading the training data, processing queries, and printing the results.

---Input File Format----
The training data must be a text file where each line contains four binary values (either 0 or 1):
Ensure the input data file is correctly formatted (four binary values per line). Incorrectly formatted files may result in errors during execution.

B: 0 (no baseball game) or 1 (baseball game is on TV)
G: 0 (George does not watch TV) or 1 (George watches TV)
C: 0 (George is not out of cat food) or 1 (George is out of cat food)
F: 0 (George does not feed the cat) or 1 (George feeds the cat)

## How to run the file:

1) No compilation is required
To run the program, use the following command:  python bnet.py <input_file_name.txt>
2) Then you will be prompted with "Query", where you can give in inputs such as B,C,G or F along with its bool value t or f.
3) Below is the example:

$ Query Variable Format
Bt: B is true (B=1), Bf: B is false (B=0)
Gt: G is true (G=1), Gf: G is false (G=0)
Ct: C is true (C=1), Cf: C is false (C=0)
Ft: F is true (F=1), Ff: F is false (F=0)

$ Example Queries

    Without Evidence:
        Input: Ct Ff
        Computes: P(C=true,F=false)

    With Evidence:
        Input: Bt Ff given Cf
        Computes: P(B=true,F=false∣C=false)

    Exit:
        Input: None



$ Example Execution of the program
	
	CMD: python bnet.py training_data.txt
	Query: Bt
	Probability: 0.304110
	Query: Bt given Ct
	Probability: 0.051657
	Query: None
