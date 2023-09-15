import matplotlib.pyplot as plt
import pandas as pd


def display_stats(
    customers_data, server_stats, total_time, waiting_count, busy_servers_count
):
    # customer stats
    customers_data = sorted(customers_data, key=lambda q: q.start_time)
    customer_arrival = []
    customer_service_start = []
    customer_service_end = []
    customer_service_time = []
    customer_service_wait = []
    customer_total_time = []
    customer_server = []

    for customer in customers_data:
        customer_arrival.append(customer.start_time)
        customer_service_start.append(customer.service_start)
        customer_service_end.append(customer.service_end)
        customer_service_time.append(customer.service_end - customer.service_start)
        customer_service_wait.append(customer.service_start - customer.start_time)
        customer_total_time.append(customer.service_end - customer.start_time)
        customer_server.append(customer.server)

    customer_stats = pd.DataFrame(
        data=zip(
            customer_arrival,
            customer_service_start,
            customer_service_end,
            customer_service_time,
            customer_service_wait,
            customer_total_time,
            customer_server,
        ),
        columns=[
            "Arrival Time",
            "Service Start",
            "Service End",
            "Service Time",
            "Service Wait",
            "Total Time",
            "Server #",
        ],
    )
    print("Simulation states (first 10 rows):")
    print(customer_stats.head(10))

    print("Customer stats:")
    print(customer_stats.describe().drop(columns=["Server #"]))

    # server stats
    server_customers = []
    server_service_time = []
    server_idle_time = []

    for server_number in server_stats:
        stats = server_stats[server_number]

        server_customers.append(stats["customers"])
        server_service_time.append(stats["service_time"])
        server_idle_time.append(total_time - stats["service_time"])

    servers_df = pd.DataFrame(
        data=zip(server_customers, server_service_time, server_idle_time),
        columns=("Customers Count", "Service Time", "Idle Time"),
    )

    print("Servers:")
    print(servers_df)
    print("Servers stats:")
    print(servers_df.describe())

    # Plots
    plt.plot(waiting_count.keys(), waiting_count.values())
    plt.title("Number of waiting customers at a time (NC):")
    plt.savefig("nc.png")
    plt.show()

    plt.plot(busy_servers_count.keys(), busy_servers_count.values())
    plt.title("Number of busy servers at a time (NE):")
    plt.savefig("ne.png")
    plt.show()
