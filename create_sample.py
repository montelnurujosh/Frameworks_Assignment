import pandas as pd

# Small dataset similar to the real metadata.csv
data = {
    "title": [
        "COVID-19 Vaccine Development",
        "Impact of Lockdowns on Public Health",
        "AI in Pandemic Response",
        "Mental Health Challenges During COVID-19",
        "Genomic Analysis of SARS-CoV-2",
        "Long-term Effects of COVID-19",
        "Global Vaccination Strategies",
        "COVID-19 and Education Disruption",
        "Pandemic Preparedness with AI",
        "Economic Impact of COVID-19"
    ],
    "abstract": [
        "This study explores progress in vaccine development.",
        "We analyze the effects of lockdowns on healthcare systems.",
        "AI applications have been used in diagnostics and predictions.",
        "The pandemic has caused significant stress worldwide.",
        "We report on genomic sequencing of SARS-CoV-2.",
        "Research into long-term complications of COVID-19.",
        "Strategies for mass vaccination programs globally.",
        "Analysis of school closures and online learning.",
        "AI tools for better pandemic forecasting.",
        "COVID-19 has disrupted economies worldwide."
    ],
    "publish_time": [
        "2020-05-01", "2020-08-15", "2021-01-10", "2021-06-20", "2019-12-25",
        "2021-09-30", "2021-12-05", "2020-11-11", "2022-03-01", "2020-04-05"
    ],
    "authors": [
        "Smith J; Brown K",
        "Lopez M; Singh R",
        "Chen L; Wang H",
        "Johnson P; Ahmed Y",
        "Davis R; Miller S",
        "Garcia F; Kim H",
        "Patel A; O'Neill P",
        "Martinez L; Rossi G",
        "Zhang X; Lee D",
        "White K; Black T"
    ],
    "journal": [
        "Nature", "The Lancet", "Journal of AI Research", "BMJ", "Science",
        "Nature Medicine", "Vaccine", "Educational Review", "AI Journal", "Economic Studies"
    ],
    "source_x": [
        "Elsevier", "Springer", "arXiv", "WHO", "MedRxiv",
        "Elsevier", "Springer", "UNESCO", "arXiv", "OECD"
    ]
}

# Create dataframe
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("metadata_sample.csv", index=False)

print("✅ metadata_sample.csv created successfully!")
