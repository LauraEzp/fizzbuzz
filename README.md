# FizzBuzz Kata

**Author:** Laura Ezpeleta

A Python implementation of the FizzBuzz Coding Dojo kata, including all the requirements from Stage 2.

## Description

The program prints the numbers from 1 to 100, following these rules:

- Print `Fizz` if the number is divisible by 3.
- Print `Fizz` if the number contains the digit 3.
- Print `Buzz` if the number is divisible by 5.
- Print `Buzz` if the number contains the digit 5.
- If multiple conditions are met, concatenate their corresponding words in the order in which the rules are evaluated.
- If no condition is met, print the original number.

## Requirements

- Python 3.10 or later
- pytest (for running automated tests)

## Installation

Clone the repository and navigate to the project directory.

Install the required dependency:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the program from the project root directory:

```bash
python fizzbuzz.py
```

The program will print the FizzBuzz sequence from 1 to 100.

## Running tests

To execute the automated tests, run:

```bash
python -m pytest -v
```

The tests cover the original FizzBuzz rules and the additional requirements introduced in Stage 2.

## Technical decisions

- **Python:** Chosen for its simplicity, readability and familiarity.
- **Functions:** The FizzBuzz logic is separated from the main execution flow.
- **Independent conditions:** Each rule is evaluated separately, allowing multiple conditions to be met simultaneously.
- **String concatenation:** Used to build the output dynamically, without introducing unnecessary data structures.
- **pytest:** Used to automate the verification of different input scenarios.