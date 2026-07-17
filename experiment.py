import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file.")

# Create Groq client
client = Groq(api_key=api_key)


def generate_response(prompt, temperature):
    """
    Generate a single response for a given prompt and temperature.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_tokens=300
    )

    return response.choices[0].message.content


def run_experiment(prompt):
    """
    Runs the same prompt 5 times for each temperature.
    Returns a dictionary of results.
    """

    temperatures = [0.2, 0.7, 1.4]
    results = {}

    for temp in temperatures:
        outputs = []

        for _ in range(5):
            response = generate_response(prompt, temp)
            outputs.append(response)

        results[temp] = outputs

    return results


# Test the backend independently
if __name__ == "__main__":

    prompt = "Write a short funny story about a dragon."

    results = run_experiment(prompt)

    for temperature, responses in results.items():

        print("\n" + "=" * 60)
        print(f"Temperature: {temperature}")
        print("=" * 60)

        for i, response in enumerate(responses, start=1):
            print(f"\nResponse {i}")
            print("-" * 40)
            print(response)