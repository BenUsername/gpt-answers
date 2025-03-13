import os
import pandas as pd
import time
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def query_openai(prompt, model="gpt-4o-mini"):
    """
    Send a prompt to OpenAI API and return the response
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error querying OpenAI: {e}")
        # Wait a bit before retrying in case of rate limits
        time.sleep(5)
        return f"Error: {e}"

def process_csv(input_file, output_file):
    """
    Process a CSV file with questions, query OpenAI for each,
    and save results to a new CSV
    """
    # Read the CSV file
    print(f"Reading {input_file}...")
    df = pd.read_csv(input_file)
    
    # Add a column for the responses
    df['response'] = ''
    
    # Process each question
    total = len(df)
    for i, row in df.iterrows():
        question = row['prompt']
        
        print(f"Processing question {i+1}/{total}...")
        print(f"Question: {question}")
        
        # Query OpenAI
        response = query_openai(question)
        
        # Save the response
        df.at[i, 'response'] = response
        
        # Print a snippet of the response
        print(f"Response snippet: {response[:100]}...\n")
        
        # Add a small delay to avoid hitting rate limits
        time.sleep(1)
    
    # Save the results
    print(f"Saving results to {output_file}...")
    df.to_csv(output_file, index=False)
    print("Done!")

if __name__ == "__main__":
    # Process only the France questions
    process_csv("workwithisland_questions_france.csv", "workwithisland_questions_france_with_responses.csv") 