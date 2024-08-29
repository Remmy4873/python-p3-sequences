def print_fibonacci(length):
    if length <= 0:
        print([])  # Print an empty list when length is 0 or negative
        return
    
    # Initialize the list to store the Fibonacci sequence
    fib_sequence = []
    
    # Start with the first two numbers in the Fibonacci sequence
    a, b = 0, 1
    for _ in range(length):
        fib_sequence.append(a)
        a, b = b, a + b
    
    print(fib_sequence)
