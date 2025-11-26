from agents import (
    TaskAgent,
    ReminderAgent,
    TravelAgent,
    ExpenseAgent,
    MemoryAgent,
    CoordinatorAgent
)

def demo():
    # Initialize agents
    task_agent = TaskAgent()
    reminder_agent = ReminderAgent()
    travel_agent = TravelAgent()
    expense_agent = ExpenseAgent()
    memory_agent = MemoryAgent()

    # Coordinator
    system = CoordinatorAgent(
        task_agent,
        reminder_agent,
        travel_agent,
        expense_agent,
        memory_agent
    )

    print("\n=== AI PERSONAL LIFE MANAGER – DEMO ===\n")

    # Sample 1 – Store user preferences
    system.run("My home is Bangalore")
    system.run("My favourite destination is Varkala")

    # Sample 2 – Add a task
    system.run("Add task: Buy groceries today")

    # Sample 3 – Plan travel
    system.run("Plan travel from Bangalore to Varkala tonight")

    # Sample 4 – Add an expense
    system.run("I spent 500 rupees on food")

    # Sample 5 – Create a reminder
    system.run("Remind me to call mom at 9:00 AM")

    print("\n=== END OF DEMO ===\n")


if __name__ == "__main__":
    demo()
