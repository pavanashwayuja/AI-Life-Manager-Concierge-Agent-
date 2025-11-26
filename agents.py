import re
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

# ----------------------------- Memory Agent -----------------------------
class MemoryAgent:
    def __init__(self):
        self.memory = {}

    def handle(self, text):
        if "home" in text.lower():
            self.memory["home"] = self.extract_value(text)
            logging.info(f"[MEMORY] Stored: home → {self.memory['home']}")
        elif "favourite" in text.lower() or "favorite" in text.lower():
            self.memory["fav_destination"] = self.extract_value(text)
            logging.info(f"[MEMORY] Stored: fav_destination → {self.memory['fav_destination']}")

    def extract_value(self, text):
        return text.split("is")[-1].strip()

# ----------------------------- Task Agent -----------------------------
class TaskAgent:
    def __init__(self):
        self.tasks = []

    def handle(self, text):
        task = text.replace("Add task:", "").strip()
        self.tasks.append(task)
        logging.info(f"[Task Agent] Added task → {task}")

# ----------------------------- Reminder Agent -----------------------------
class ReminderAgent:
    def __init__(self):
        self.reminders = []

    def handle(self, text):
        self.reminders.append(text)
        logging.info(f"[Reminder Agent] Reminder set → {text}")

# ----------------------------- Travel Agent -----------------------------
class TravelAgent:
    def handle(self, text):
        logging.info("[Travel Agent] Best option from Bangalore to Varkala: Taxi")

# ----------------------------- Expense Agent -----------------------------
class ExpenseAgent:
    def __init__(self):
        self.expenses = []

    def handle(self, text):
        amount_match = re.findall(r'\d+', text)
        amount = amount_match[0] if amount_match else "Unknown"
        self.expenses.append(amount)
        logging.info(f"[Budget Agent] Expense added: {amount} under General")

# ----------------------------- Coordinator Agent -----------------------------
class CoordinatorAgent:
    def __init__(self, task, reminder, travel, expense, memory):
        self.task_agent = task
        self.reminder_agent = reminder
        self.travel_agent = travel
        self.expense_agent = expense
        self.memory_agent = memory

    def run(self, text):
        text_lower = text.lower()

        if "task" in text_lower:
            return self.task_agent.handle(text)

        elif "remind" in text_lower:
            return self.reminder_agent.handle(text)

        elif "travel" in text_lower or "trip" in text_lower:
            return self.travel_agent.handle(text)

        elif "spent" in text_lower or "expense" in text_lower:
            return self.expense_agent.handle(text)

        else:
            return self.memory_agent.handle(text)
