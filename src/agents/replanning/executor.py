from src.agents.replanning.reflector import Reflector
from src.agents.react.react_agent import ReAct_Agent


class Executor:

    def __init__(self):

        self.agent = ReAct_Agent()

        self.reflector = Reflector()

    def execute(self, state):

        MAX_RETRIES = 2

        tasks = state.pending_tasks.copy()

        state.pending_tasks.clear()

        for task in tasks:

            feedback = None

            success = False

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

                    state.completed_tasks.append(task)

                    state.results[task] = result

                    success = True

                    break

                feedback = reflection["feedback"]

            if not success:

                state.failed_tasks.append(
                    {
                        "task": task,
                        "error": feedback
                    }
                )

        return state