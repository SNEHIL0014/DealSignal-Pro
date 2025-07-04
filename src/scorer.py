def seniority_score(title):
    title = title.lower()
    if any(k in title for k in ["ceo", "founder", "president"]):
        return 100
    elif "cto" in title:
        return 80
    elif "manager" in title:
        return 60
    else:
        return 40

def industry_score(industry):
    return 100 if industry.lower() in ["saas", "ai", "fintech"] else 50

def size_score(size):
    try:
        size = int(size)
        return 40 if size < 50 else 70 if size < 500 else 100
    except:
        return 50

def score_lead(row):
    s = seniority_score(row['Title'])
    i = industry_score(row['Industry'])
    c = size_score(row['CompanySize'])
    return round((0.4 * s + 0.3 * i + 0.3 * c), 2)

def estimate_roi(row):
    win_probability = row['LeadScore'] / 100
    try:
        revenue = int(row['CompanySize']) * 10000  # $10k per employee
    except:
        revenue = 1_000_000
    potential_fee = revenue * 0.03  # 3% PE deal value
    return round(win_probability * potential_fee, 2)

def is_nurture_candidate(score):
    return "Yes" if score < 50 else "No"

def caprae_lens(industry):
    return "✓" if industry.lower() in ["saas", "ai"] else ""

def is_regulated_country(location):
    return "Yes" if location.lower() in ["india", "germany", "france", "uk", "europe"] else "No"

def run_scoring(input_path, output_path):
    import pandas as pd
    df = pd.read_csv(input_path)

    df['LeadScore'] = df.apply(score_lead, axis=1)
    df['EstimatedValue'] = df.apply(estimate_roi, axis=1)
    df['NurtureCandidate'] = df['LeadScore'].apply(is_nurture_candidate)
    df['CapraeLens'] = df['Industry'].apply(caprae_lens)
    df['GDPR_Applicable'] = df['Location'].apply(is_regulated_country)

    df.to_csv(output_path, index=False)
    return df
