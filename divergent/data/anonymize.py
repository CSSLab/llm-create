import pandas as pd
import hashlib

# Function to hash values using SHA256 for anonymization
def anonymize_value(value):
    return hashlib.sha256(value.encode()).hexdigest()

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('responses.csv')

# Apply the anonymization function to the relevant columns
df['assignment_id'] = df['assignment_id'].apply(anonymize_value)
df['hit_id'] = df['hit_id'].apply(anonymize_value)
df['worker_id'] = df['worker_id'].apply(anonymize_value)

# Save the anonymized DataFrame back to a new CSV file
df.to_csv('anonymized_responses.csv', index=False)

print("Anonymization completed and saved to 'anonymized_file.csv'.")