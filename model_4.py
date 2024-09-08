from math import factorial

def mmsn_queue_metrics_4(lambda_rate, mu_rate, s, n):
    # Calculate traffic intensity (rho)
    rho = lambda_rate / (s * mu_rate)

    # Ensure the system is stable
    if rho >= 1:
        return "The system is unstable because utilization (rho) is greater than or equal to 1."

    # Calculate P0 (probability that there are no customers in the system)
    sum_term_1 = sum((lambda_rate / mu_rate) ** k / factorial(k) for k in range(s))
    sum_term_2 = sum((lambda_rate / mu_rate) ** k / (factorial(s) * s ** (k - s)) for k in range(s, n + 1))
    P0 = 1 / (sum_term_1 + sum_term_2)

    # Calculate Pn (blocking probability)
    Pn = P0 * ((lambda_rate / mu_rate) ** n) / (factorial(s) * s ** (n - s))

    # Calculate average number of customers in the system (L)
    L = sum(k * P0 * ((lambda_rate / mu_rate) ** k) / factorial(k) if k < s else
            k * P0 * ((lambda_rate / mu_rate) ** k) / (factorial(s) * s ** (k - s)) for k in range(n + 1))

    # Calculate average number of customers in the queue (Lq)
    Lq = L - (lambda_rate / mu_rate) * (1 - Pn)

    # Calculate average time a customer spends in the system (W)
    W = L / (lambda_rate * (1 - Pn))

    # Calculate average time a customer spends in the queue (Wq)
    Wq = Lq / (lambda_rate * (1 - Pn))

    # Return the computed metrics
    return {
        'Utilization (ρ)': rho,
        'Probability system is empty (P0)': P0,
        'Blocking probability (Pn)': Pn,
        'Average customers in the system (L)': L,
        'Average customers in the queue (Lq)': Lq,
        'Average time in the system (W)': W,
        'Average time in the queue (Wq)': Wq
    }

# Example usage
lambda_rate = 4.0  # Arrival rate (customers per time unit)
mu_rate = 3.0      # Service rate (customers per time unit per server)
s = 2              # Number of servers
n = 5              # Maximum system capacity

metrics = mmsn_queue_metrics_4(lambda_rate, mu_rate, s, n)
for metric, value in metrics.items():
    print(f"{metric}: {value:.4f}")
