from openai import OpenAI
from pprint import pprint

from src.prompts.react_prompt import SYSTEM_PROMPT
from src.tools.tavily_search import tavily_search
from src.agents.react.parser import parse_response

client = OpenAI()

class ReAct_Agent:

    def __init__(self):
        self.messages = [
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            }
        ]

    def run(self, query:str):
        self.messages.append(
            {
                "role":"user",
                "content":query
            }
        )

        # pprint(self.messages)

        while True:

            response = client.chat.completions.create(
                model="gpt-4.1",
                messages=self.messages
            )

            output = response.choices[0].message.content

            print("\nLLM OUTPUT:")
            print(output)

            parsed = parse_response(output)

            if parsed["type"] == "final":
                return parsed["answer"]
            

            if parsed["type"] == "action":

                observation = tavily_search(
                    parsed["input"]
                )

                self.messages.append(
                    {
                        "role": "assistant",
                        "content": output
                    }
                )

                self.messages.append(
                    {
                        "role": "user",
                        "content":
                        f"Observation: {observation}"
                    }
                )

            