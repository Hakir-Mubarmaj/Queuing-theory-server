from math import factorial

def mms_queue_metrics_3(lambda_rate, mu_rate, s):
    # Calculate traffic intensity (rho)
    rho = lambda_rate / (s * mu_rate)

    # Ensure the system is stable
    if rho >= 1:
        return "The system is unstable because utilization (rho) is greater than or equal to 1."

    # Calculate P0 (probability that there are no customers in the system)
    sum_term = sum((lambda_rate / mu_rate) ** n / factorial(n) for n in range(s))
    P0 = 1 / (sum_term + ((lambda_rate / mu_rate) ** s / (factorial(s) * (1 - rho))))

    # Calculate Lq (average number of customers in the queue)
    Lq = (P0 * (lambda_rate / mu_rate) ** s * rho) / (factorial(s) * (1 - rho) ** 2)

    # Calculate L (average number of customers in the system)
    L = Lq + lambda_rate / mu_rate

    # Calculate W (average time a customer spends in the system)
    W = L / lambda_rate

    # Calculate Wq (average time a customer spends in the queue)
    Wq = Lq / lambda_rate

    # Return the computed metrics
    return {
        'Utilization (ρ)': rho,
        'Probability system is empty (P0)': P0,
        'Average number of customers in the queue (Lq)': Lq,
        'Average number of customers in the system (L)': L,
        'Average time in the queue (Wq)': Wq,
        'Average time in the system (W)': W
    }

# Example usage
lambda_rate = 4.0  # Arrival rate (customers per time unit)
mu_rate = 3.0      # Service rate (customers per time unit per server)
s = 2              # Number of servers

metrics = mms_queue_metrics_3(lambda_rate, mu_rate, s)
for metric, value in metrics.items():
    print(f"{metric}: {value:.4f}")
