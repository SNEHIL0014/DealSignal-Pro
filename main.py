from src.scorer import run_scoring
from src.messenger import add_messages

input_path = 'data/leads.csv'
output_path = 'output/scored_with_messages.csv'

# Run scoring + enhancements
df = run_scoring(input_path, output_path)

# Add AI-generated messages
df = add_messages(df)

# Save final file
df.to_csv(output_path, index=False)

# Print summary
print(" Done! Output saved to output/scored_with_messages.csv")
print(f" Total Pipeline Value: ${df['EstimatedValue'].sum():,.2f}")
print(f" Nurture Candidates: {df['NurtureCandidate'].value_counts().get('Yes', 0)}")
print(f" CapraeLens Matches (SaaS/AI): {df['CapraeLens'].value_counts().get('✓', 0)}")
print(f" Leads in GDPR-regulated regions: {df['GDPR_Applicable'].value_counts().get('Yes', 0)}")
