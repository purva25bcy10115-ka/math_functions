''' question-33: Write a function zeta_approx(s, terms) that approximates the Riemann zeta function'''

def zeta_approx(s, terms):
    # Approximates the Riemann zeta function ζ(s) using 'terms' of the series:
    # ζ(s) = Σ (1 / n^s) for n = 1 to ∞
    # Valid only for s > 1 (for convergence)
    
    if s <= 1:
        raise ValueError("s must be > 1 for convergence.")
    
    result = 0.0
    for n in range(1, terms + 1):
        result += 1 / (n ** s)
    return result


# Example usage:
print(zeta_approx(2, 1000))
print(zeta_approx(3, 1000))
print(zeta_approx(4, 1000))