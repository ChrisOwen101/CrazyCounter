# Function to check if a number is prime
def is_prime(num):
    """Check if a number is a prime number."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate a list of prime numbers up to a given limit


def generate_primes(limit):
    """Generate a list of prime numbers up to a given limit."""
    primes = []
    for n in range(2, limit + 1):
        if is_prime(n):
            primes.append(n)
    print(primes)
    return primes


# Main code execution
if __name__ == "__main__":
    print("Jakub Was Here")
    limit = 100
    primes = generate_primes(limit)
    print(f"Prime numbers up to {limit}:")
    print(primes)
