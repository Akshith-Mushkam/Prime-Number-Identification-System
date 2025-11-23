import math
import sys

def get_smallest_factor(n: int) -> int:
    """
    Checks if n is prime by finding its smallest factor.
    
    Args:
        n: The integer to check (must be non-negative).

    Returns:
        The smallest factor of n if it's composite (factor > 1).
        Returns 1 if n is 0 or 1 (non-prime by definition).
        Returns 0 if n is prime.
    """
    if n <= 1:
        return 1  # 0 or 1 is non-prime
    
    # 2 is the only even prime number
    if n == 2:
        return 0  # 0 indicates prime
        
    # All other even numbers are not prime, smallest factor is 2
    if n % 2 == 0:
        return 2
        
    # Check for divisibility up to the square root of n (Trial Division Optimization)
    limit = int(math.sqrt(n))
    
    # Only check odd numbers for divisors
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return i # Found the smallest odd factor
            
    # If no divisors were found, the number is prime
    return 0 # 0 indicates prime

def prime_identification_system():
    """
    The main interactive loop for the Prime Number Identification System.
    """
    print("==============================================")
    print("✨ Prime Number Identification System (PNIS) ✨")
    print("==============================================")
    print("Enter 'quit' or 'exit' at any time to close.")
    
    while True:
        try:
            user_input = input("\nEnter a whole number to check: ")
            
            if user_input.lower() in ('quit', 'exit'):
                print("\nSystem shutting down. Thank you for using PNIS!")
                sys.exit(0)
                
            n = int(user_input)
            
            # Ensure the number is non-negative
            if n < 0:
                print(f"⚠️ {n} is negative. Primality is generally defined for natural numbers (>0).")
                continue
            
            # Perform the single, efficient check
            smallest_factor = get_smallest_factor(n)
            
            if smallest_factor == 0:
                # Case 1: Prime (function returned 0)
                print(f"✅ Result: The number {n} IS a prime number.")
            else:
                # Case 2: Composite (function returned a factor > 0)
                if smallest_factor == 1:
                    # Handles n=0 and n=1, where factor returned is 1
                    print(f"❌ Result: The number {n} IS NOT a prime number. (Non-prime by definition)")
                else:
                    # Handles all other composite numbers (smallest_factor > 1)
                    print(f"❌ Result: The number {n} IS NOT a prime number. (It is divisible by {smallest_factor})")


        except ValueError:
            print("🛑 Error: Invalid input. Please enter a valid whole number.")
        except KeyboardInterrupt:
            print("\n\nSystem shutting down. Thank you for using PNIS!")
            sys.exit(0)

# Execute the main system function when the script is run
if __name__ == "__main__":
    prime_identification_system()