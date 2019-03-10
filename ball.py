import random

def is_burning(question):
    """Takes a question in the form of a string and returns True if the question is burning and False if it is not burning."""

    burning_words = [
        'ever',
        'really',
        'need',
        'never'
    ]

    burning = False

    for word in burning_words:
        if word in question:
            burning = True

    return burning


def answer_question(question):
    """Takes a question and returns an answer formatted in HTML. Incorporates our "burning questions" logic and our HTML formatter."""
    burning_answers = [
        'Absolutely!',
        'HELL no',
    ]

    cold_answers = [
        "Maybe.",
        "Meh",
        "Sure...",
        "Sigh.....",
    ]

    if is_burning(question):
        answer = random.choice(burning_answers)
    else:
        answer = random.choice(cold_answers)

    formatted_answer = format_answer(answer)

    return formatted_answer



def format_answer(answer):
    """Take an answer as a string and add HTML formatting to it"""

    html_begin = "<html><body><p>"
    html_end = "</p></body></html>"

    formatted_answer = html_begin + answer + html_end

    return formatted_answer


if __name__ == '__main__':
    print('I am the Magic 9 Ball, oracle and auspex.')
    print()

    while True:
        question = input("Pose your question. ")
        
        answer = answer_question(question)

        print(answer)
