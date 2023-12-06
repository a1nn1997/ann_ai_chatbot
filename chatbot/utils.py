import random
from transformers import pipeline, set_seed
from nltk.chat.util import Chat, reflections


def generate_questions_and_responses(prompt, model="gpt2", max_length=100, num_return_sequences=10):
    generator = pipeline('text-generation', model=model)
    set_seed(42)
    responses = generator(prompt, max_length=max_length, num_return_sequences=num_return_sequences)
    return [response['generated_text'] for response in responses]

def generate_chat_pairs(n=5, random_questions=[]):
    chat_pairs = []
    for _ in range(n):
        question = random.choice(random_questions)
        responses = generate_questions_and_responses(question)
        responses_list = [response.split('.') for response in responses]
        flat_responses = [item.strip() for sublist in responses_list for item in sublist if item]
        chat_pairs.append((question, flat_responses))

    return chat_pairs
