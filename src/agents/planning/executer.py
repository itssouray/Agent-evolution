from src.agents.react.react_agent import ReAct_Agent


class Executor:

    def __init__(self):
        self.agent = ReAct_Agent()

    def execute(self, tasks):

        results = []

        for task in tasks:

            print(f"\nExecuting: {task}")

            result = self.agent.run(task)

            results.append(
                {
                    "task": task,
                    "result": result
                }
            )

        return results