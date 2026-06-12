class AgentState:

    def __init__(self, goal: str):
        self.goal = goal
        self.tasks = []
        self.results = []
        self.reflections = []