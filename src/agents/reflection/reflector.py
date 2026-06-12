import json

from src.llm.openai_client import llm
from src.agents.reflection.prompts import REFLECTION_PROMPT


class Reflector:

    def reflect(self, task: str, result: str):

        response = llm.invoke(
            [
                ("system", REFLECTION_PROMPT),
                (
                    "user",
                    f"""
                        Task:
                        {task}

                        Result:
                        {result}
                    """  
                )
            ]
        )

        # print(response.content)

        reflection = json.loads(
            response.content
        )

        return reflection