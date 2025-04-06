from utils.communication import message_queue

class CoordinatorAgent:
    def __init__(self, store_agents, warehouse_agent, supplier_agent, customer_agent):
        self.store_agents = store_agents
        self.warehouse_agent = warehouse_agent
        self.supplier_agent = supplier_agent
        self.customer_agent = customer_agent

    def step(self, inventory_data, demand_data, pricing_data):
        # Step through all store agents
        for store_id in self.store_agents:
            self.store_agents[store_id](int(store_id.split("_")[1]), inventory_data, demand_data, pricing_data)

        # Process messages
        while not message_queue.empty():
            message = message_queue.get()

            if message.receiver == "warehouse":
                self.warehouse_agent.process_resupply_request(message)

            elif message.receiver.startswith("store_"):
                print(f"[Coordinator] Message sent to {message.receiver}: {message.message_type}")

        # Future: add logic for triggering supplier orders, customer modeling
