# Prime-Number-Identification-System
This Python code implements an Optimized Prime Number Identification System (PNIS). It efficiently checks if an integer is prime by using a single O(sqrt of n)  trial division function that returns the smallest factor (or 0 if prime). It includes an interactive command-line interface.

● Overview of the project :

 The Prime Number Identification System (PNIS) is a command-line utility built in Python designed to efficiently determine if a positive integer is a prime number. If the number is composite (not prime), the system identifies and reports its **smallest factor**, providing immediate feedback to the user.

The core design principle is **efficiency**. The system avoids redundant calculations by performing the costly trial division operation only once per input, making it fast and reliable even for checking large numbers.


● Features : 

*Optimized Primality Test :- Uses a single, $O(\sqrt{n})$ trial division check to determine primality.
*Smallest Factor Reporting:- For composite numbers, it immediately provides the smallest factor (e.g., 7 for 49).
*High Efficiency:- The logic is structured to prevent repeating the trial division, which is common in less optimized systems.
*Zero External Dependencies:- No external libraries are needed, keeping the code lightweight.
*Graceful Exit:- Supports multiple exit commands (`quit`, `exit`, or Ctrl+C/KeyboardInterrupt).
*Input Validation:- Handles non-integer input and negative numbers gracefully.


● Technologies/tools used : 

*Primary Language:- Python 3.x
*Built-in Modules:- `sys` (for exit handling)
*Algorithm:- Optimized Trial Division (using $i*i \le n$ instead of $\texttt{math.sqrt()}$)


● Steps to install & run the project : 

### Prerequisites

You must have **Python 3.x** installed on your operating system (Windows, macOS, or Linux).

### Installation and Setup

1.Clone the Repository:-
    ```bash
    git clone [YOUR_REPO_URL]
    cd [YOUR_REPO_NAME]
    ```

2.Save the Code:- Ensure your provided Python code is saved in a file named `prime_identification_system.py` inside the cloned directory.

### Running the System

Execute the script directly from your terminal:

```bash
python3 prime_identification_system.py


● Instructions for testing :

The system is interactive and designed for immediate testing.

Test Cases
To verify correct functionality, enter the following numbers one by one:

Input (n)	  Expected Outcome	         Reason/Factor
0            IS NOT a prime number.     Non-prime by defination.
2            IS a prime number.         Only even prime number.
55           IS NOT a prime number.     Divisible by 5.
97           IS a prime number.         No factors other than 1 and itself.
143          IS NOT a prime number.     Divisible by 11.
Hello        Error: Invalid input.      Tests the **ValueError** handling.
