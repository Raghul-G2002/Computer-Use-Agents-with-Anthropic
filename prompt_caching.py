from anthropic import Anthropic
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
# Load API Key from environment variable
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
print("Anthropic API Key Loaded:", ANTHROPIC_API_KEY)

# with open ('files/demo.txt','r') as file:
#     content = file.read()

# Client = Anthropic(
#     api_key = ANTHROPIC_API_KEY
# )
# MODEL_NAME = 'claude-3-5-sonnet-20241022'


# # Uncached Request
# import time
# def make_non_cached_api_call():
#     messages = [
#         {
#             "role":"user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": "<book>" + content + "</book>"
#                 },
#                 {
#                     "type": "text",
#                     "text": "Summarize the above text in a concise manner."
#                 }
#             ]
#         }
#     ]
#     start_time = time.time()
#     response = Client.messages.create(
#         model = MODEL_NAME,
#         max_tokens = 500,
#         messages = messages
#     )
#     end_time = time.time() - start_time
#     return response, end_time

# non_cached_response, non_cached_time = make_non_cached_api_call()
# print("Non-Cached Response Time:", non_cached_time)
# print("Non-Cached Response:", non_cached_response)

# def make_cached_api_call():
#     messages = [
#         {
#             "role":"user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": "<book>" + content + "</book>",
#                     "cache_control": {"type":"ephermal"}
#                 },
#                 {
#                     "type": "text",
#                     "text": "Summarize the above text in a concise manner."
#                 }
#             ]
#         }
#     ]
#     start_time = time.time()
#     response = Client.messages.create(
#         model = MODEL_NAME,
#         max_tokens = 500,
#         messages = messages
#     )
#     end_time = time.time() - start_time
#     return response, end_time

# response1, duration1 = make_cached_api_call()
# print("Cached Call 1 Time:", duration1)
# print("Cached Call 1 Response:", response1)
# response2, duration2 = make_cached_api_call()
# print("Cached Call 2 Time:", duration2)
# print("Cached Call 2 Response:", response2)
