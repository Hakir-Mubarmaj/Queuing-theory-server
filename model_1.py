def mm1_queue_metrics_1(lambda_rate, mu_rate):
    # Ensure lambda < mu for the system to be stable
    if lambda_rate >= mu_rate:
        return "The system is unstable because the arrival rate is greater than or equal to the service rate."

    # Calculate Utilization (ρ)
    rho = lambda_rate / mu_rate

    # Calculate average number of customers in the system (L)
    L = rho / (1 - rho)

    # Calculate average time a customer spends in the system (W)
    W = 1 / (mu_rate - lambda_rate)

    # Calculate average number of customers in the queue (Lq)
    Lq = (rho ** 2) / (1 - rho)

    # Calculate average time a customer spends in the queue (Wq)
    Wq = rho / (mu_rate - lambda_rate)

    # Return results as a dictionary
    return {
        'Utilization (ρ)': rho,
        'Average number of customers in the system (L)': L,
        'Average time in the system (W)': W,
        'Average number of customers in the queue (Lq)': Lq,
        'Average time in the queue (Wq)': Wq
    }

# Example usage
lambda_rate = 3.0  # Arrival rate (customers per time unit)
mu_rate = 5.0      # Service rate (customers per time unit)

metrics = mm1_queue_metrics_1(lambda_rate, mu_rate)
for metric, value in metrics.items():
    print(f"{metric}: {value:.2f}")
