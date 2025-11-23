''' question-34: Write a function partition_function(n) that calculates
 the number of distinct ways to write n as a sum of positive integers.'''

def partition_function(n):
    # Dynamic programming approach to compute partition numbers
    if n < 0:
        return 0

    partitions = [0] * (n + 1)
    partitions[0] = 1  # Base case: one way to partition zero

    for k in range(1, n + 1):
        for i in range(k, n + 1):
            partitions[i] += partitions[i - k]

    return partitions[n]


# Example usage:
print(partition_function(4))   # 5
print(partition_function(5))   # 7
print(partition_function(10))  # 42
print(partition_function(0))   # 1