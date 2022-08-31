import math

def calculate_halstead(n1, N1, n2, N2):

    n = n1 + n2
    N = N1 + N2

    estimated_length = n1 * math.log2(n1) + n2 * math.log2(n2)
    purity_ratio = estimated_length / N
    volume = estimated_length * math.log2(n)

    difficulty = (n1 / 2) * (N2 / n2)
    effort = difficulty * volume
    time = effort / 18
    bugs = volume / 3000

    return {
        "Program vocabulary": n,
        "Program length": N,
        "Estimated length": estimated_length,
        "Purity ratio": purity_ratio,
        "Volume": volume,
        "Difficulty": difficulty,
        "Program effort": effort,
        "Time required to program": time,
        "Number of delivered bugs": bugs,
    }