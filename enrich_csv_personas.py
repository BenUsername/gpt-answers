import pandas as pd

# Read the CSV file
print("Reading CSV file...")
df = pd.read_csv('workwithisland_questions_personas_with_responses.csv')

# Add new columns
print("Adding new columns...")

# Check if brand is mentioned in the answer
df['brand_mentioned'] = df['response'].str.lower().str.contains('workwithisland', na=False)

# Check if client is in the list (I assume this means checking if workwithisland is mentioned)
df['visibule'] = df['response'].str.lower().str.contains('workwithisland', na=False)

# Check if the name of the client is in the question
df['branded'] = df['prompt'].str.lower().str.contains('workwithisland', na=False)

# Save the enriched CSV
print("Saving enriched CSV...")
df.to_csv('workwithisland_questions_personas_enriched.csv', index=False)

print("Done! CSV has been enriched with the requested columns.") 