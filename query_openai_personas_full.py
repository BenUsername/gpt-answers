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

def process_csv(input_file, output_file, max_questions=None, countries=None):
    """
    Process a CSV file with questions, query OpenAI for each,
    and save results to a new CSV
    
    Parameters:
    - input_file: path to the input CSV
    - output_file: path to save the output CSV
    - max_questions: maximum number of questions to process per persona/country
    - countries: list of countries to filter for, or None for all countries
    """
    # Read the CSV file
    print(f"Reading {input_file}...")
    df = pd.read_csv(input_file)
    
    # Extract persona from prompt
    df['persona'] = df['prompt'].str.extract(r'As an? (.*?)\s+\w+\s+')
    
    # Clean up personas by removing trailing "I need to know" etc.
    df['persona'] = df['persona'].str.replace(r'\s+I need to know.*', '', regex=True)
    df['persona'] = df['persona'].str.replace(r'\s+I.*', '', regex=True)
    df['persona'] = df['persona'].str.replace(r'\s+looking.*', '', regex=True)
    df['persona'] = df['persona'].str.replace(r'\s+concerned.*', '', regex=True)
    df['persona'] = df['persona'].str.replace(r'\s+with.*', '', regex=True)
    df['persona'] = df['persona'].str.replace(r'\s+focused.*', '', regex=True)
    df['persona'] = df['persona'].str.strip()
    
    # Filter by country if specified
    if countries:
        df = df[df['country'].isin(countries)]
    
    # Group by persona and country, limit questions per group if specified
    if max_questions:
        groups = []
        for (persona, country), group in df.groupby(['persona', 'country']):
            groups.append(group.head(max_questions))
        df = pd.concat(groups)
    
    # Add a column for the responses
    df['response'] = ''
    
    # Process each question
    total = len(df)
    for i, row in df.iterrows():
        question = row['prompt']
        country = row['country']
        persona = row['persona']
        
        print(f"Processing question {i+1}/{total} for {persona} in {country}...")
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
    # Process persona questions for multiple countries
    process_csv(
        "workwithisland_questions_personas.csv", 
        "workwithisland_questions_personas_with_responses.csv",
        max_questions=10,  # Process up to 10 questions per persona/country
        countries=["France", "United Kingdom", "Spain", "Switzerland", "Benelux"]  # Process all available countries
    ) 