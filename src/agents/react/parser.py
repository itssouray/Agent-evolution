import re

def parse_response(response: str):

    if "Final Answer:" in response:
        return {
            "type": "final",
            "answer": response.split(
                "Final Answer:"
            )[1].strip()
        }

    action_match = re.search(
        r"Action:\s*(.*)",
        response
    )

    input_match = re.search(
        r"Action Input:\s*(.*)",
        response
    )

    if action_match and input_match:
        return {
            "type": "action",
            "action": action_match.group(1).strip(),
            "input": input_match.group(1).strip()
        }

    raise ValueError("Invalid agent response")