"""There should be a doc string here"""

# Function to check if a number is prime
def is_prime(num: int):
    """Check if a number is a prime number."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate a list of prime numbers up to a given limit
def generate_primes(limit: int):
    """Generate a list of prime numbers up to a given limit."""
    primes = [n for n in range(2, limit + 1) if is_prime(n)]
    return primes

# Main code execution
if __name__ == "__main__":
    limit = 500
    primes = generate_primes(limit)
    print(f"Prime numbers up to {limit}:")
    print(primes)
