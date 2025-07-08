# DealSignal Pro 🚀  
AI-Driven Lead Intelligence Engine for Private Equity Targeting

> "We don't just find leads — we rank opportunities."  

DealSignal Pro is a Python-based AI tool built in 5 hours for Caprae Capital’s internship challenge. It prioritizes acquisition-ready targets using lead scoring, value estimation, and event-triggered messaging — aligning with Caprae's #BleedandBuild and operator-first M&A mindset.

---

## 🔍 What It Does

| Module              | Function                                        | Business Value                                  |
|---------------------|-------------------------------------------------|--------------------------------------------------|
| Lead Scoring        | Prioritizes leads by job title, size, industry  | Focuses sales on high-conversion targets         |
| ROI Estimation      | Calculates deal potential per lead              | Quantifies pipeline value for Caprae operators   |
| Nurture Detection   | Flags “long-term build” leads                   | Powers Caprae’s #BleedandBuild strategy          |
| Message Generator   | Creates personalized messages                   | Scales intelligent outreach                      |
| CapraeLens™         | Flags SaaS/AI/Fintech targets                   | Filters for firm’s preferred sectors             |
| GDPR Safeguard      | Detects regulated countries                     | Adds compliance awareness                        |

---

## 💼 Sample Output (CSV)

| Name         | Title             | Industry | Score | Est. Value | Nurture? | CapraeLens | Message Preview                        |
|--------------|-------------------|----------|-------|------------|----------|------------|----------------------------------------|
| John Smith   | Founder & CEO     | SaaS     | 82    | $4,920     | No       | ✓          | “Hi John, I noticed your growth in…”   |
| Emma Watson  | Marketing Manager | Health   | 60    | $54,000    | No       |            | “Hi Emma, I’d love to connect…”        |

---

## 📁 Folder Structure

DealSignal-Pro/
│

├── data/ # Raw leads.csv input

├── output/ # Scored leads output

├── src/

│ ├── scorer.py # Scoring, ROI, CapraeLens logic

│ └── messenger.py # Message generation

├── Caprae_Challenge_Report_SnehilSrivastava.md  # 1-page summary

├── main.py # Run the full pipeline

├── requirements.txt # Python dependencies

├── README.md # 

└── DealSignal_Pro.ipynb.ipynb     # Jupyter Notebook walkthrough
---

📓 Demo (Jupyter Notebook)
View the full scoring and enrichment logic in:
👉 demo/DealSignal_Pro.ipynb

The notebook shows:

Data preprocessing

Scoring and tagging logic

Visualization of lead scores

Final output export

▶️ How to Run
Install dependencies:
pip install -r requirements.txt

Run the main pipeline:
python main.py

Output will be saved to:
/output/scored_with_messages.csv



| Name        | Title   | Score | Category | GDPR | Industry | Message                   |
| ----------- | ------- | ----- | -------- | ---- | -------- | ------------------------- |
| John Smith  | CEO     | 90    | Hot      | No   | SaaS     | "Hi John, congrats..."    |
| Priya Mehta | Manager | 55    | Warm     | Yes  | EdTech   | "Hi Priya, thanks for..." |



---

##🧠 Business Alignment

🎯 Caprae’s operator-first approach:

“LeadScore” ranks operators, not just companies

“NurtureCandidate” supports long-term plays

“EstimatedValue” quantifies pipeline value

---

## 📊 Output Metrics:


Estimated Pipeline Value: $405,420

Nurture Candidates: 0

GDPR-Applicable: 1

CapraeLens Matches: 1

---
© 2025 Snehil Srivastava — Built for Caprae Capital AI Internship Challenge
