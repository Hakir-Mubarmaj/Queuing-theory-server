def mm1_n_queue_metrics_2(lambda_rate, mu_rate, n):
    # Ensure the input rates are positive and n is a non-negative integer
    if lambda_rate <= 0 or mu_rate <= 0 or n < 0:
        return "Invalid inputs: Arrival rate, service rate must be positive and capacity must be non-negative."

    # Utilization (ρ)
    rho = lambda_rate / mu_rate

    # Ensure the system is stable: rho should be less than 1
    if rho >= 1:
        return "The system is unstable because utilization (rho) is greater than or equal to 1."

    # Calculate P0 (probability the system is empty)
    P0 = (1 - rho) / (1 - rho**(n + 1))

    # Calculate Pn (probability of n customers in the system, i.e., blocking probability)
    Pn = P0 * (rho**n)

    # Calculate average number of customers in the system (L)
    L = sum(k * (P0 * (rho**k)) for k in range(n + 1))

    # Calculate average time a customer spends in the system (W)
    W = L / (lambda_rate * (1 - Pn))

    # Calculate average number of customers in the queue (Lq)
    Lq = L - (1 - Pn)

    # Calculate average time a customer spends in the queue (Wq)
    Wq = Lq / (lambda_rate * (1 - Pn))

    # Return the computed metrics
    return {
        'Utilization (ρ)': rho,
        'Probability system is empty (P0)': P0,
        'Blocking probability (Pn)': Pn,
        'Average number of customers in the system (L)': L,
        'Average time in the system (W)': W,
        'Average number of customers in the queue (Lq)': Lq,
        'Average time in the queue (Wq)': Wq
    }

# Example usage
lambda_rate = 3.0  # Arrival rate (customers per time unit)
mu_rate = 5.0      # Service rate (customers per time unit)
n = 4              # System capacity

metrics = mm1_n_queue_metrics_2(lambda_rate, mu_rate, n)
for metric, value in metrics.items():
    print(f"{metric}: {value:.4f}")
