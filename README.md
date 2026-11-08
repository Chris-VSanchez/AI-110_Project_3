# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

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

Each UserProfile object will store the user's musical preferences:

preferred_genres: List of favorite genres.
preferred_moods: List of preferred moods.
preferred_energy: Desired energy level (0–1).
preferred_tempo: Preferred tempo in BPM.
preferred_valence: Preferred positivity level (0–1).
Recommendation Scoring

The Recommender will calculate a score for every song by comparing its features with the user's preferences.

The scoring system will use these weights:

Genre match: 30%
Mood match: 25%
Energy similarity: 20%
Tempo similarity: 15%
Valence similarity: 10%

For numerical features, the system will reward songs that are closer to the user's preferred values rather than simply rewarding higher or lower values.

# Ranking and Recommendations

After calculating the score for each song, the recommender will sort all songs from highest to lowest score. It will then return the top 5 songs with the highest matching scores.

The goal is to create a simple recommendation system that understands a user's musical vibe and suggests songs that match their preferences.

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
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
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



