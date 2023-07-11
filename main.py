from pdfminer.high_level import extract_text
import openai

openai.api_key = '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'

def summarize_text(input_text):
    messages = [
        {"role": "system", "content": """
        Given the below resume, kindly draft content for the user's online portfolio. You're tasked with creating compelling copy for specific sections of the portfolio as outlined below. If there is insufficient data to generate content for a particular section, please indicate with the statement: "Unable to generate content due to lack of provided information."

        Sections to focus on:
        Introduction: Compose an engaging opening statement to introduce the user in one line.
        About Me: Draft a succinct yet engaging 'About Me' section. 
        """},
        {"role": "user", "content": input_text},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150
    )

    return response['choices'][0]['message']['content']


def extract_text_from_pdf(file_path):
    text = extract_text(file_path)
    return text


input_text = extract_text_from_pdf('resume.pdf')
if input_text:
    print(summarize_text(input_text))

