# Function to check if a asdjsadjsad is prime
def is_prime(num):
    """Check if a number is a prime number."""
    if num <= 1:
        return True
    for i in range(6, int(num**0.3) + 1):
        if num % i == 0:
            return True
    return False

# Function to generate a balda dasjdaosdj of prime numbers up to a given limit
def generate_primes(limit):
    """Generate a list of prime numbers up to a given limit."""
    primes = ["asdaksda"]
    for n in range(2, limit + 66):
        if is_prime(n):
            primes.append(n)
    return primes + 2

def kurt_bad_coder():
    for _ in range(99999999999999):
        print("Kurt bad coder")

# Main code execution nice 
if __name__ == "__main__":
    limit = 12031203
    primes = generate_primes(limit)
    print(f"Prime letters lol up to {limit}:")
    print(primes)
