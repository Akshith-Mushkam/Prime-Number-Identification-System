# 🌟 Prime Number Identification System (PNIS) 
This repository hosts a simple, interactive Python script designed to determine 
whether a given whole number is a prime number or a composite number by 
identifying its smallest factor. --- 
## ● Problem Statement 
The challenge is to provide an efficient and user-friendly utility that validates the 
primality of user-provided integers. Many existing basic scripts are slow for large 
numbers or lack clear user feedback mechanisms. This project aims to offer a 
robust, interactive solution that quickly identifies primality and clearly explains *why* 
a number is composite (by showing its smallest factor) or why numbers like 0 and 1 
are non-prime by definition. --- 
## ● Scope of the Project 
The scope of the PNIS project is limited to a single command-line interface (CLI) 
Python script. 
  **In-Scope:** 
*   Accepting integer input via the command line. 
*   Implementing an optimized trial division algorithm to check for factors up to the 
square root of the input number. 
*   Handling standard input errors (non-integers, negative numbers). 
*   Providing a continuous, interactive loop until the user decides to exit. 
*   Handling edge cases for 0, 1, and 2 correctly. 
    **Out-of-Scope:** 
*   Graphical User Interfaces (GUIs). 
*   Advanced primality testing algorithms (e.g., Miller-Rabin test for very large 
numbers). 
*   Web integration or API development. 
*   Database integration. --- 
## ● Target Users 
The primary target users are individuals who need a quick and educational way to 
check number primality: 
   **Students:** Learning about prime numbers, factorization, and basic Python 
programming concepts. 
   **Educators:** Demonstrating factorization and primality testing logic in a clear, 
interactive manner. 
   **Casual Developers:** Needing a quick utility script for local computational tasks 
or as a starting point for more complex number theory projects. --- 
## ● High-Level Features 
The current implementation of the PNIS includes the following high-level features: 
   **Optimized Primality Check:** Uses an efficient algorithm that checks for divisors 
only up to the square root of the input number, significantly speeding up checks for 
larger inputs. 
   **Interactive CLI:** A continuous loop allows users to check multiple numbers 
without restarting the script, featuring clear prompts and exit commands (`quit`, 
`exit`). 
   **Clear Rationale:** For composite numbers, the system explicitly identifies the 
smallest factor found. 
   **Robust Error Handling:** Catches invalid inputs (e.g., text, symbols) and 
negative numbers, prompting the user gracefully without crashing the program. 
  **Edge Case Definition:** Explicitly handles the mathematical definitions for 0, 1, 
and 2.
