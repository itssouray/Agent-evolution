import ast

from src.llm.openai_client import llm
from src.agents.planning.prompts import PLANNER_PROMPT


class Planner:

    def create_plan(self, state):

        response = llm.invoke(
            [
                ("system", PLANNER_PROMPT),
                ("user", state.goal)
            ]
        )

        plan = ast.literal_eval(
            response.content
        )

        state.original_plan = plan.copy()

        state.pending_tasks = plan.copy()

        return state