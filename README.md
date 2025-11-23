# math_functions
# 📘 Number Theory & Mathematical Functions – Python Implementations

This repository contains Python programs for 34 number-theoretic and mathematical functions.  
All programs are arranged according to weekly assignments (Week 2 – Week 5).  
Each function is implemented in its own `.py` file.

---


Each folder contains `.py` files corresponding to the functions listed below.

---

# 📝 **List of Programs (All Weeks)**

---

## 🔵 **Assignment – Week 2**

### 1. `factorial(n)`  
Computes the factorial of a non-negative integer `n`.

### 2. `is_palindrome(n)`  
Checks whether a number reads the same forward and backward.

### 3. `mean_of_digits(n)`  
Returns the average (mean) of all digits in a number.

### 4. `digital_root(n)`  
Repeatedly sums digits until a single digit remains.

### 5. `is_abundant(n)`  
Returns `True` if the sum of proper divisors of `n` is greater than `n`.

### 6. `is_deficient(n)`  
Returns `True` if the sum of proper divisors of `n` is less than `n`.

### 7. `is_harshad(n)`  
Checks whether the number is divisible by the sum of its digits.

### 8. `is_automorphic(n)`  
Checks if `n²` ends with the digits of `n`.

### 9. `is_pronic(n)`  
Checks whether a number is the product of two consecutive integers.

### 10. `prime_factors(n)`  
Returns a list of prime factors of a number.

---

## 🔵 **Assignment – Week 3**

### 11. `count_distinct_prime_factors(n)`  
Returns how many *unique* prime factors a number has.

### 12. `is_prime_power(n)`  
Checks if a number can be expressed as `pᵏ` where `p` is prime and `k ≥ 1`.

### 13. `is_mersenne_prime(p)`  
Checks if `2ᵖ − 1` is prime, given that `p` is prime.

### 14. `twin_primes(limit)`  
Generates all pairs of twin primes up to a given limit.

### 15. `count_divisors(n)`  
Returns the number of positive divisors of `n`.

### 16. `aliquot_sum(n)`  
Returns the sum of proper divisors of a number.

### 17. `are_amicable(a, b)`  
Checks if two numbers are amicable (each is the other's aliquot sum).

### 18. `multiplicative_persistence(n)`  
Counts how many steps until the digits multiply to a single digit.

### 19. `is_highly_composite(n)`  
Checks if a number has more divisors than any smaller number.

---

## 🔵 **Assignment – Week 4**

### 20. `mod_exp(base, exponent, modulus)`  
Efficiently computes `(base^exponent) % modulus`.

### 21. `mod_inverse(a, m)`  
Finds `x` such that `(a * x) ≡ 1 (mod m)`.

### 22. `crt(remainders, moduli)`  
Solves a system of congruences using the Chinese Remainder Theorem.

### 23. `is_quadratic_residue(a, p)`  
Checks if the congruence `x² ≡ a (mod p)` has a solution.

### 24. `order_mod(a, n)`  
Finds the smallest positive integer `k` such that `aᵏ ≡ 1 (mod n)`.

### 25. `is_fibonacci_prime(n)`  
Checks whether a number is *both* Fibonacci and prime.

### 26. `lucas_sequence(n)`  
Generates the first `n` Lucas numbers (sequence starting with 2, 1).

### 27. `is_perfect_power(n)`  
Checks if `n = aᵇ` for integers `a > 0` and `b > 1`.

### 28. `collatz_length(n)`  
Returns the number of steps for the Collatz sequence to reach 1.

### 29. `polygonal_number(s, n)`  
Returns the `n`-th `s`-gonal number.

### 30. `is_carmichael(n)`  
Checks if a composite number `n` satisfies:  
`a^(n−1) ≡ 1 (mod n)` for all `a` coprime to `n`.

---

## 🔵 **Assignment – Week 5**

### 31. `is_prime_miller_rabin(n, k)`  
Implements the probabilistic **Miller–Rabin primality test** with `k` rounds.

### 32. `pollard_rho(n)`  
Factorizes integers using **Pollard’s Rho algorithm**.

### 33. `zeta_approx(s, terms)`  
Approximates the Riemann Zeta function using the first `terms` of the series.

### 34. `partition_function(n)`  
Computes the number of ways to represent `n` as a sum of positive integers.

---

## 🛠️ Requirements

- **Python 3.8+**
- **Standard Python libraries only** (no external modules required)

# ▶️ Running the Programs

Use Python to run any file:

```bash
python filename.py
