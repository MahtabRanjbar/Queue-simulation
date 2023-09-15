from customer import Customer
from distributions import service_time


class System:
    def __init__(self, resource_count: int):
        # create an array of resources with the value indicating the availability of the resource
        self.servers = [False] * resource_count
        self.init_stats()

    def init_stats(self):
        self.server_stats = {}
        for s in range(len(self.servers)):
            self.server_stats[s] = {"customers": 0, "service_time": 0}

    def can_serve(self):
        return not all(self.servers)

    def serve(self):
        first_available_server = self.servers.index(False)

        serve_time = service_time()

        self.servers[first_available_server] = True
        self.server_stats[first_available_server]["customers"] += 1
        self.server_stats[first_available_server]["service_time"] += serve_time

        return (first_available_server, serve_time)

    def free_server(self, server):
        self.servers[server] = False

    def available_servers(self):
        return len(list(filter(lambda server: server == False, self.servers)))

    def busy_servers(self):
        return len(list(filter(lambda server: server == True, self.servers)))
