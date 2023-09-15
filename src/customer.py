class Customer:
    def __init__(self, arrival_time, priority=False):
        self.start_time = arrival_time
        self.service_start = -1
        self.service_end = -1
        self.priority = priority
        self.server = -1

    def start_service(self, time, server):
        self.service_start = time
        self.server = server

    def end_service(self, time):
        self.service_end = time
