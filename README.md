# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

---

## How The System Works

My music recommendation system uses content-based filtering to recommend songs that match a user's musical preferences. Real-world platforms like Spotify combine collaborative filtering, which uses listening behavior from similar users, with content-based filtering, which analyzes song characteristics. My simulation will focus on content-based filtering to keep the recommendation process simple and understandable.

# Song Features

Each Song object will contain:

id: Unique song identifier.
title: Name of the song.
artist: Artist name.
genre: Musical genre.
mood: Emotional feeling of the song.
energy: How energetic the song is (0–1).
tempo_bpm: Speed of the song in beats per minute.
valence: How positive or happy the music sounds (0–1).
danceability: How suitable the song is for dancing (0–1).
acousticness: How acoustic the song sounds (0–1).
UserProfile Features

The UserProfile will store the user's musical preferences in a dictionary:

python
user_profile = {
    "preferred_genres": ["lofi", "ambient"],
    "preferred_moods": ["chill", "focused"],
    "target_energy": 0.40
}


This profile represents someone who enjoys relaxing, low-energy music while studying or working.

# Dataset

The initial dataset contains 10 songs. I plan to expand it to 18 songs by adding more genres and moods, including country, classical, R&B, metal, reggae, folk, electronic, and blues.

This will give the recommender more variety when comparing songs.

# Algorithm Recipe

The Recommender will calculate a score for every song by comparing its features with the user's preferences.

The scoring rules are:

Matching preferred genre: +2.0 points.
Matching preferred mood: +1.0 point.
Energy similarity: 0–1.0 points.

The energy similarity formula is:

EnergyScore = 1 - abs(song.energy - target_energy)

This rewards songs whose energy is closer to the user's preferred energy level.

The maximum possible score is 4 points.

# Ranking and Recommendations

After calculating the score for each song, the recommender will:

Loop through all songs in the dataset.
Calculate each song's matching score.
Store each song with its score.
Sort the songs from highest to lowest score.
Return the top 5 recommendations.
Data Flow
mermaid
flowchart TD
    A[Load User Preferences] --> B[Load songs.csv]
    B --> C[Loop Through Songs]
    C --> D[Compare Genre and Mood]
    D --> E[Calculate Energy Similarity]
    E --> F[Calculate Total Score]
    F --> G{More Songs?}
    G -->|Yes| C
    G -->|No| H[Sort Scores]
    H --> I[Return Top 5 Recommendations]

# Potential Biases and Limitations

My recommendation system might over-prioritize genre because genre matching is worth more points than mood matching. This could cause it to overlook songs from different genres that match the user's mood and energy preferences.

Another limitation is that the system only considers the preferences stored in the user profile. It does not learn from actual listening behavior, skips, or likes.

In the future, I could improve the system by adjusting feature weights, adding more musical attributes, or incorporating collaborative filtering.

# Project Goal

The goal is to create a simple recommendation system that understands a user's musical vibe, compares it against song attributes, and suggests the five songs that best match their preferences.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
User profile: genre=pop, mood=happy, energy=0.8

Top recommendations:

Sunrise City - Score: 3.98
Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.98)

Gym Hero - Score: 2.87
Because: Genre match (+2.0), Energy similarity (+0.87)

Rooftop Lights - Score: 1.96
Because: Mood match (+1.0), Energy similarity (+0.96)

Island Breeze - Score: 1.82
Because: Mood match (+1.0), Energy similarity (+0.82)

Night Drive Loop - Score: 0.95
Because: Energy similarity (+0.95)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



