import ast
from src.llm.openai_client import llm
from src.agents.planning.prompts import PLANNER_PROMPT


class Planner:

    def create_plan(self, goal: str):

        response = llm.invoke(
            [
                ("system", PLANNER_PROMPT),
                ("user", goal)
            ]
        )

        plan = ast.literal_eval(
            response.content
        )

        return plan