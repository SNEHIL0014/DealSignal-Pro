def generate_message(row):
    name = row['Name']
    company = row['Company']
    title = row['Title']
    industry = row['Industry']
    score = row['LeadScore']

    tone = "direct" if score > 80 else "nurturing"

    return f"Hi {name}, as {title} at {company}, I’d love to connect about opportunities in {industry}. This message is {tone}."

def add_messages(df):
    df['Message'] = df.apply(generate_message, axis=1)
    return df
