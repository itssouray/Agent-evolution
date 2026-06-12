from src.agents.reflection.reflector import Reflector
from src.agents.react.react_agent import ReAct_Agent



class Executor:

    def __init__(self):
        self.agent = ReAct_Agent()
        self.reflector = Reflector()

    def execute(self, state):

        MAX_RETRIES = 2

        for task in state.tasks:

            feedback = None

            for attempt in range(MAX_RETRIES + 1):

                result = self.agent.run(
                    task,
                    feedback
                )

                reflection = self.reflector.reflect(
                    task,
                    result
                )

                if reflection["success"]:
                    break

                feedback = reflection["feedback"]

        return state