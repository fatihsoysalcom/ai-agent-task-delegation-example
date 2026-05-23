import time

class Agent:
    """Base class for all agents."""
    def __init__(self, name):
        self.name = name

    def handle_task(self, task):
        raise NotImplementedError("Subclasses must implement handle_task method.")

class AnalysisAgent(Agent):
    """A specialized agent for complex data analysis tasks."""
    def handle_task(self, task):
        if "analysis" in task.lower():
            print(f"[{self.name}] Analyzing task: '{task}'...")
            time.sleep(1) # Simulate work
            return f"[{self.name}] Analysis complete for '{task}'. Result: Detailed report generated."
        else:
            return f"[{self.name}] Cannot handle '{task}'. This agent specializes in analysis."

class MainAgent(Agent):
    """A main agent that can handle simple tasks or delegate complex ones."""
    def __init__(self, name, delegate_agent=None):
        super().__init__(name)
        self.delegate_agent = delegate_agent # An agent to delegate tasks to

    def handle_task(self, task):
        print(f"\n[{self.name}] Received task: '{task}'")
        
        # Decision logic: can this agent handle the task directly?
        if "simple query" in task.lower() or "operating hours" in task.lower():
            print(f"[{self.name}] Handling simple query directly...")
            time.sleep(0.5) # Simulate work
            return f"[{self.name}] Answered: '{task}' is a common question. We operate 9 AM - 5 PM."
        
        # --- ARTICLE'S CORE CONCEPT: DELEGATION --- 
        # If the task is complex and a suitable delegate agent exists
        elif ("complex analysis" in task.lower() or "sales data" in task.lower()) and self.delegate_agent:
            print(f"[{self.name}] Task '{task}' is complex. Delegating to {self.delegate_agent.name}...")
            delegated_result = self.delegate_agent.handle_task(task) # Delegate the task
            print(f"[{self.name}] Received delegated result from {self.delegate_agent.name}.")
            return delegated_result
        
        # If the task cannot be handled by this agent or delegated
        else:
            return f"[{self.name}] Cannot handle '{task}' or no suitable delegate available for this task."

# --- Simulation --- 
if __name__ == "__main__":
    # 1. Create specialized agents
    data_analyst_bot = AnalysisAgent("DataAnalystBot")

    # 2. Create a main agent, capable of delegating to the data analyst
    customer_service_bot = MainAgent("CustomerServiceBot", delegate_agent=data_analyst_bot)

    print("--- Scenario 1: Simple Query Handled Directly ---")
    result1 = customer_service_bot.handle_task("What are your operating hours? (simple query)")
    print(result1)
    print("-" * 50)

    print("--- Scenario 2: Complex Analysis Requiring Delegation ---")
    result2 = customer_service_bot.handle_task("Please perform a complex analysis of Q3 sales data.")
    print(result2)
    print("-" * 50)

    print("--- Scenario 3: Task Not Handled by Main or Delegate ---")
    result3 = customer_service_bot.handle_task("Order a pizza for lunch.")
    print(result3)
    print("-" * 50)

    print("--- Scenario 4: Main Agent Without a Delegate for Complex Tasks ---")
    # A main agent that cannot delegate complex analysis (no delegate_agent assigned)
    simple_faq_bot = MainAgent("SimpleFAQBot")
    result4 = simple_faq_bot.handle_task("Please perform a complex analysis of Q3 sales data.")
    print(result4)
    print("-" * 50)
