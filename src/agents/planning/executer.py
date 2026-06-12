from src.agents.react.react_agent import ReAct_Agent


class Executor:

    def __init__(self):
        self.agent = ReAct_Agent()

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

        return state