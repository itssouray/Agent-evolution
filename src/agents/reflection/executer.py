from src.agents.reflection.reflector import Reflector
from src.agents.react.react_agent import ReAct_Agent



class Executor:

    def __init__(self):
        self.agent = ReAct_Agent()
        self.reflector = Reflector()

    def execute(self, state):

        for task in state.tasks:

            print(f"\nExecuting: {task}")

            result = self.agent.run(task)

            state.results.append(
                {
                    "task": task,
                    "result": result
                }
            )

            reflection = self.reflector.reflect(
                task,
                result
            )

            state.reflections.append(
                {
                    "task": task,
                    **reflection
                }
            )

        return state