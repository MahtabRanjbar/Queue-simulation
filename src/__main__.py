from simulation import run_simulation
from stats import display_stats

NUMBER_OF_CUSTOMERS = int(input("Customers Count: "))
NUMBER_OF_RESOURCES = int(input("Employees Count: "))
PRIORITY_CHANCE = float(input("Priority Chance (0-1): "))
LOGGING = bool(input("Log each action? (y/n): ") == "y")

customers, server_stats, total_time, waiting_count, busy_servers_count = run_simulation(
    NUMBER_OF_RESOURCES, NUMBER_OF_CUSTOMERS, PRIORITY_CHANCE, LOGGING
)

display_stats(customers, server_stats, total_time, waiting_count, busy_servers_count)
