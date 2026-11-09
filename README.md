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

My music recommendation system uses content-based filtering to recommend songs that match a user's musical preferences.

Real-world platforms like Spotify combine collaborative filtering, which uses listening behavior from similar users, with content-based filtering, which analyzes song characteristics. My simulation focuses on content-based filtering to keep the recommendation process simple and understandable.
Song Features

Each Song object contains the following attributes:

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

The UserProfile stores the user's musical preferences.

For the initial simulation, the user profile contains:

    genre: Preferred musical genre.
    mood: Preferred musical mood.
    energy: Target energy level (0–1).

For example:
python

user_prefs = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.8
}

Dataset

The original dataset contained 10 songs. I expanded it to 18 songs by adding more genres and moods.

The dataset includes:

    Pop
    Lofi
    Rock
    Ambient
    Jazz
    Synthwave
    Indie pop
    Country
    Classical
    R&B
    Metal
    Reggae
    Folk
    Electronic
    Blues

This provides more variety when testing different musical preferences.
Algorithm Recipe

The Recommender calculates a score for every song by comparing its features with the user's preferences.

The scoring rules are:

    Matching genre: +2.0 points.
    Matching mood: +1.0 point.
    Energy similarity: 0–1.0 points.

The energy similarity formula is:

EnergyScore = 1 - abs(song.energy - target_energy)

This rewards songs whose energy is closer to the user's preferred energy level.

The total scoring formula is:

Total Score = Genre Points + Mood Points + Energy Similarity

The maximum possible score is 4 points.
Ranking and Recommendations

After calculating the score for every song, the recommender:

    Loads songs from the CSV dataset.
    Compares each song against the user's preferences.
    Calculates a matching score.
    Generates explanations describing why the song matched.
    Sorts songs from highest to lowest score.
    Returns the top 5 recommendations.

The system also provides explanations such as genre matches, mood matches, and energy similarity.
Data Flow
mermaid

flowchart TD
    A[Load User Preferences] --> B[Load songs.csv]
    B --> C[Loop Through Every Song]
    C --> D[Compare Genre and Mood]
    D --> E[Calculate Energy Similarity]
    E --> F[Calculate Total Score]
    F --> G{More Songs?}
    G -->|Yes| C
    G -->|No| H[Sort by Highest Score]
    H --> I[Return Top 5 Recommendations]
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

==================================================
USER PROFILE: High-Energy Pop
==================================================
1. Sunrise City - Score: 3.92
   Artist: Neon Echo
   Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.92)

2. Gym Hero - Score: 2.97
   Artist: Max Pulse
   Because: Genre match (+2.0), Energy similarity (+0.97)

3. Rooftop Lights - Score: 1.86
   Artist: Indigo Parade
   Because: Mood match (+1.0), Energy similarity (+0.86)

4. Island Breeze - Score: 1.72
   Artist: Coastal Roots
   Because: Mood match (+1.0), Energy similarity (+0.72)

5. Storm Runner - Score: 0.99
   Artist: Voltline
   Because: Energy similarity (+0.99)


==================================================
USER PROFILE: Chill Lofi
==================================================
1. Midnight Coding - Score: 3.98
   Artist: LoRoom
   Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.98)

2. Library Rain - Score: 3.95
   Artist: Paper Lanterns
   Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.95)

3. Focus Flow - Score: 3.00
   Artist: LoRoom
   Because: Genre match (+2.0), Energy similarity (+1.00)

4. Spacewalk Thoughts - Score: 1.88
   Artist: Orbit Bloom
   Because: Mood match (+1.0), Energy similarity (+0.88)

5. Coffee Shop Stories - Score: 0.97
   Artist: Slow Stereo
   Because: Energy similarity (+0.97)


==================================================
USER PROFILE: Deep Intense Rock
==================================================
1. Storm Runner - Score: 3.96
   Artist: Voltline
   Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.96)

2. Iron Heart - Score: 1.99
   Artist: Black Voltage
   Because: Mood match (+1.0), Energy similarity (+0.99)

3. Gym Hero - Score: 1.98
   Artist: Max Pulse
   Because: Mood match (+1.0), Energy similarity (+0.98)

4. Neon Dreams - Score: 0.93
   Artist: Pixel Motion
   Because: Energy similarity (+0.93)

5. Sunrise City - Score: 0.87
   Artist: Neon Echo
   Because: Energy similarity (+0.87)


==================================================
USER PROFILE: Conflicting Preferences
==================================================
1. Storm Runner - Score: 2.99
   Artist: Voltline
   Because: Genre match (+2.0), Energy similarity (+0.99)

2. Empty Streets - Score: 1.55
   Artist: Silver Lines
   Because: Mood match (+1.0), Energy similarity (+0.55)

3. Autumn Letters - Score: 1.41
   Artist: Willow Creek
   Because: Mood match (+1.0), Energy similarity (+0.41)

4. Neon Dreams - Score: 0.98
   Artist: Pixel Motion
   Because: Energy similarity (+0.98)

5. Gym Hero - Score: 0.97
   Artist: Max Pulse
   Because: Energy similarity (+0.97)

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->
---

## Experiments You Tried

The experiments showed that changing user preferences significantly changes the recommendation results.

    High-Energy Pop favored energetic pop songs.
    Chill Lofi favored relaxing lofi songs.
    Deep Intense Rock favored intense rock songs.
    Conflicting Preferences demonstrated how the algorithm handles preferences that do not perfectly match the available songs.

One interesting result was that Gym Hero appeared in both the High-Energy Pop and Deep Intense Rock recommendation lists. This happened because it matches the pop genre in one profile and the intense mood in the other, while also having high energy.

Another interesting result was that Storm Runner appeared in the High-Energy Pop recommendations even though it is a rock song. Its high energy gave it a relatively strong similarity score.
Scoring Experiment: Removing Mood Points

I also experimented with temporarily removing the mood-matching points from the scoring function.

For the Chill Lofi profile, the original ranking was:
text

1. Midnight Coding - Score: 3.98
2. Library Rain - Score: 3.95
3. Focus Flow - Score: 3.00

Without mood scoring, the ranking became:
text

1. Focus Flow - Score: 1.00
2. Midnight Coding - Score: 0.98
3. Library Rain - Score: 0.95

This demonstrated that mood matching has an important effect on recommendations. Removing it caused the system to rely more heavily on genre and energy.

I concluded that combining multiple features produces more meaningful recommendations than relying on only one or two characteristics.
---

## Limitations and Risks

My recommendation system has several limitations:

    It only uses genre, mood, and energy when calculating scores.
    It does not consider tempo, valence, danceability, or acousticness.
    Genre matching is worth more points than mood matching, which can create a bias toward a preferred genre.
    The dataset contains only 18 songs, so recommendation variety is limited.
    It does not learn from user behavior, such as likes, skips, or listening history.
    It may recommend songs that match numerical preferences without fully matching the user's emotional expectations.

These limitations mean that the recommendations are useful for demonstrating the basic idea of content-based filtering but are not as sophisticated as real streaming platform recommendations.
---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

  Building this music recommender helped me understand how recommendation systems use data and mathematical scoring rules to predict what 
users might enjoy. I learned that small changes to scoring weights can significantly affect recommendation results. I also discovered that 
a song does not need to match every user preference to receive a high score because the algorithm combines multiple features.

  Testing different user profiles helped me understand how recommendation systems can produce different results depending on the information 
they receive. I also learned that recommendation systems can have biases when certain features are given more importance than others.
Overall, this project helped me understand the basic ideas behind music recommendation platforms and how their algorithms can be improved 
through testing and evaluation.