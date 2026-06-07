import re


def extract_score(text):


    match = re.search(
        r"(\d+)\s*/\s*10",
        text
    )


    if match:

        return match.group(1) + "/10"


    return "N/A"