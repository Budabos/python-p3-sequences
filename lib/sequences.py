def print_fibonacci(length):
    sequence = [0] if length >= 1 else []

    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2] if len(sequence) > 1 else 1)

    print(sequence)