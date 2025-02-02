import os
from openai import OpenAI
from fireworks.client import Fireworks
from dotenv import load_dotenv
load_dotenv()

FIREWORKS_API_KEY = os.getenv("FIREWORKS_API_KEY")

# Point to the local server
# client1 = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")  # html to json
# model = r"lmstudio-ai/gemma-2b-it-GGUF"

def get_completion(prompt):
    client = Fireworks(api_key=FIREWORKS_API_KEY)


    response = client.chat.completions.create(
    # model="accounts/fireworks/models/mixtral-8x22b-instruct",
    model = "accounts/fireworks/models/llama-v3p1-8b-instruct",
    messages=[{"role": "user", "content": prompt}],
    stream=True,
    temperature=0.2
    )

    new_message = {"role": "assistant", "content": ""}

    for chunk in response:
        if chunk.choices[0].delta.content:
            # print(chunk.choices[0].delta.content, end="", flush=True)
            val = chunk.choices[0].delta.content
            new_message["content"] += val

    # bot_response = response.choices[0].message.content


    # return bot_response
    return new_message["content"]

# def get_completion(prompt, client=client1, model=model):
#     """
#     given the prompt, obtain the response from LLM hosted by LM Studio as a server
#     :param prompt: prompt to be sent to LLM server
#     :return: response from the LLM
#     """
#     prompt = [
#         {"role": "user", "content": prompt}
#     ]
#     completion = client.chat.completions.create(
#         model=model,
#         messages=prompt,
#         temperature=0.0,
#         stream=True,
#     )

#     new_message = {"role": "assistant", "content": ""}

#     for chunk in completion:
#         if chunk.choices[0].delta.content:
#             # print(chunk.choices[0].delta.content, end="", flush=True)
#             val = chunk.choices[0].delta.content
#             new_message["content"] += val

#     # print(type()
#     val = new_message["content"]  # .split("<end_of_turn>")[0]

#     return val


if __name__ == '__main__':
    prompt = """
    You are a political leader and your party is trying to win the general elections in India. 
    You are given an LLM that can provide you the analytics using the past historical data given to it.
    In particular the LLM has been provided data on which party won each constituency out of 545 and which assembly segment within the main constituency is more favorable.
    It also has details of votes polled by every candidate.
    Tell me 10 questions that you want to ask the LLM.
    """
    results = get_completion(prompt)
    print(results)

# OUTPUT :

# 1. Which party won the most seats in the recent general elections?


# 2. Which assembly segment has been consistently more favorable for a particular party?


# 3. What are the key factors that contributed to the party's success or failure in different constituencies?


# 4. How did the party's performance vary across different states and regions?


# 5. Which candidate won the most votes in each constituency?


# 6. What were the demographics of the voters who voted for each party?


# 7. How did the party's vote share change over time?


# 8. Which issues were most important to voters when they made their decisions?


# 9. What were the major challenges faced by the party in winning the elections?


# 10. What are the party's plans for improving its performance in the future?
