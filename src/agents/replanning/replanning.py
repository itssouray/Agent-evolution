import ast

from src.llm.openai_client import llm
from src.agents.replanning.prompts import REPLANNER_PROMPT


class Replanner:

    def replan(self, state):

        response = llm.invoke(
            [
                ("system", REPLANNER_PROMPT),
                (
                    "user",
                    f"""
                    Goal:
                    {state.goal}

                    Original Plan:
                    {state.original_plan}

                    Completed Tasks:
                    {state.completed_tasks}

                    Failed Tasks:
                    {state.failed_tasks}

                    Pending Tasks:
                    {state.pending_tasks}

                    Results:
                    {state.results}
                    """
                )
            ]
        )

        new_tasks = ast.literal_eval(
            response.content
        )

        state.pending_tasks.extend(new_tasks)
        state.failed_tasks.clear()

        state.replan_count += 1

        return state