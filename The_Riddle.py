from random import randint

def generate_unique_random_list(size, start=0, end=99):
    """Generate a list of unique random integers within a range."""
    unique_list = set()
    while len(unique_list) < size:
        unique_list.add(randint(start, end))
    return list(unique_list)

def find_cycles_and_success(sequence, max_iterations=50):
    """Find cycles in the sequence and count successful matches."""
    success_count = 0
    visited = set()

    for start in range(len(sequence)):
        if start in visited:
            continue
        
        current = start
        cycle = set()
        steps = 0
        
        while steps < max_iterations:
            if current in cycle:
                # Found a cycle without success
                break
            cycle.add(current)
            visited.add(current)
            
            # Check if the sequence points back to the start
            if sequence[current] == start:
                success_count += 1
                break
            
            current = sequence[current]
            steps += 1

    return success_count

def main():
    size = 100
    random_sequence = generate_unique_random_list(size)
    
    # Identify missing numbers
    missing_numbers = set(range(size)) - set(random_sequence)
    if missing_numbers:
        print(f"Missing numbers in the sequence: {sorted(missing_numbers)}")
    
    # Find cycles and successful matches
    success_count = find_cycles_and_success(random_sequence)
    print(f"Number of successful cycles: {success_count}")

if __name__ == "__main__":
    main()
