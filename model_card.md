# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

# VibeFinder 1.0

VibeFinder is a simple music recommendation system that suggests songs based on a user's preferred genre, mood, and energy level.

It was developed as a beginner Python project to demonstrate how content-based recommendation systems work.
---

## 2. Intended Use  

VibeFinder is designed to recommend songs that match a user's musical preferences.

The system is intended for educational purposes and classroom exploration rather than real-world commercial music recommendations.

It assumes that users can describe their musical preferences through three main characteristics:

    Favorite genre.
    Preferred mood.
    Target energy level.

The recommender compares these preferences against the characteristics of songs in its dataset and returns the five highest-scoring recommendations.
---

## 3. How the Model Works  

VibeFinder uses content-based filtering. This means it compares the characteristics of songs against the user's preferences instead of relying on other users' listening behavior.

Each song contains information such as genre, mood, energy, tempo, valence, danceability, and acousticness.

The user profile currently provides three preferences:

    Genre.
    Mood.
    Energy.

The scoring system uses the following rules:

    A matching genre earns 2 points.
    A matching mood earns 1 point.
    Energy similarity earns between 0 and 1 point.

Energy similarity is calculated by subtracting the difference between the song's energy and the user's target energy from 1.

The final score is calculated by adding the genre points, mood points, and energy similarity points.

After scoring all songs, the system sorts them from highest to lowest score and returns the top five recommendations.

Compared with the original starter logic, I implemented CSV loading, numerical value conversion, individual song scoring, recommendation ranking, and explanations showing why songs were recommended.
---

## 4. Data  

The recommender uses a CSV dataset containing 18 songs.

The original dataset contained 10 songs, and I added 8 additional songs to increase the variety of genres and moods.

The dataset includes genres such as:

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

The moods represented include happy, chill, intense, relaxed, focused, moody, peaceful, romantic, energetic, and melancholic.

Each song also includes numerical characteristics such as energy, tempo, valence, danceability, and acousticness.

Although these additional characteristics are stored in the dataset, the current scoring algorithm only uses genre, mood, and energy.

Some aspects of musical taste are missing, including lyrics, instruments, vocal style, cultural context, and personal listening history.
---

## 5. Strengths  

VibeFinder works well when users have clear preferences for genre, mood, and energy.

The Chill Lofi profile produced reasonable results because Midnight Coding, Library Rain, and Focus Flow closely matched the user's preferences.

The High-Energy Pop profile also produced sensible recommendations, with Sunrise City ranking first because it matched the preferred genre and mood.

The Deep Intense Rock profile successfully recommended Storm Runner first because it matched all three preferences.

Another strength is that the system provides explanations for its recommendations. Users can see whether a song received points for genre, mood, or energy similarity.

This makes the recommendation process easier to understand.
---

## 6. Limitations and Bias 

One limitation is that genre matching receives 2 points while mood matching receives only 1 point. This means the system may prioritize a user's favorite genre even when another song better matches their emotional preferences.

The system also ignores tempo, valence, danceability, and acousticness when calculating scores, even though these characteristics are available in the dataset.

The small dataset of 18 songs limits the variety of recommendations. Some genres and moods have only one song, which makes it difficult to recommend different options.

Another limitation appeared during the conflicting preferences experiment. A user who wanted rock music, a melancholic mood, and high energy received recommendations that matched only some of those preferences. This shows that the system cannot always find a song that satisfies every requirement.

The system also does not learn from listening history, likes, dislikes, or skipped songs. It depends entirely on the preferences entered by the user.
---

## 7. Evaluation  

I evaluated VibeFinder using four different user profiles to see how well the recommendation system handled different musical preferences.
Profile 1: High-Energy Pop

Preferences:

    Genre: Pop
    Mood: Happy
    Energy: 0.90

Top recommendations:

    Sunrise City - 3.92
    Gym Hero - 2.97
    Rooftop Lights - 1.86
    Island Breeze - 1.72
    Storm Runner - 0.99

Sunrise City ranked first because it matched both the preferred genre and mood while having similar energy.

Gym Hero also ranked highly because it matched the pop genre and had high energy.
Profile 2: Chill Lofi

Preferences:

    Genre: Lofi
    Mood: Chill
    Energy: 0.40

Top recommendations:

    Midnight Coding - 3.98
    Library Rain - 3.95
    Focus Flow - 3.00
    Spacewalk Thoughts - 1.88
    Coffee Shop Stories - 0.97

Midnight Coding ranked first because it matched the preferred genre and mood and had energy very close to the user's target.

Library Rain also performed well because it had similar characteristics.
Profile 3: Deep Intense Rock

Preferences:

    Genre: Rock
    Mood: Intense
    Energy: 0.95

Top recommendations:

    Storm Runner - 3.96
    Iron Heart - 1.99
    Gym Hero - 1.98
    Neon Dreams - 0.93
    Sunrise City - 0.87

Storm Runner ranked first because it matched the preferred genre and mood and had high energy.

Iron Heart ranked lower because it matched the intense mood and energy preference but not the rock genre.
Profile 4: Conflicting Preferences

Preferences:

    Genre: Rock
    Mood: Melancholic
    Energy: 0.90

Top recommendations:

    Storm Runner - 2.99
    Empty Streets - 1.55
    Autumn Letters - 1.41
    Neon Dreams - 0.98
    Gym Hero - 0.97

This profile was designed to test conflicting preferences because the dataset does not contain a song that matches both rock and melancholic.

Storm Runner ranked first because it matched the rock genre and had high energy.

Empty Streets and Autumn Letters received mood points because they matched the melancholic preference.

This demonstrated that the recommender can still produce results even when the user's preferences do not perfectly align with the available songs.
Comparison Between User Profiles

High-Energy Pop vs. Chill Lofi

The High-Energy Pop profile favored energetic pop songs, while the Chill Lofi profile favored relaxing lofi songs. This showed that changing the user's genre, mood, and energy preferences changes the recommendations.

Chill Lofi vs. Deep Intense Rock

Chill Lofi prioritized low-energy songs such as Midnight Coding. Deep Intense Rock prioritized high-energy songs such as Storm Runner. These results matched my expectations because the two users have very different musical preferences.

High-Energy Pop vs. Deep Intense Rock

Both profiles preferred energetic music, but their genre and mood preferences caused different songs to rank highly. This demonstrated why the system needs multiple features to understand musical taste.
Scoring Experiment: Removing Mood Points

I temporarily removed the mood-matching points from the scoring function to see how the recommendations would change.

For the Chill Lofi profile, the original ranking was:

    Midnight Coding - 3.98
    Library Rain - 3.95
    Focus Flow - 3.00

After removing mood scoring, the ranking became:

    Focus Flow - 1.00
    Midnight Coding - 0.98
    Library Rain - 0.95

Focus Flow moved into first place because its energy matched the user's target exactly.

This experiment showed that mood matching has an important influence on the final recommendations.

I concluded that removing mood scoring made the system less effective at understanding the emotional side of musical preferences.

Overall, the results were mostly consistent with my expectations, although some songs appeared in multiple recommendation lists because of overlapping characteristics.
---

## 8. Future Work  

There are several ways I could improve VibeFinder in the future:

    Add tempo, valence, danceability, and acousticness to the scoring algorithm.
    Allow users to select multiple favorite genres and moods.
    Adjust the scoring weights to make recommendations more balanced.
    Improve recommendation diversity so the same songs do not appear repeatedly.
    Include user feedback such as likes, dislikes, and skipped songs.
    Introduce collaborative filtering to compare listening behavior between users.
    Expand the dataset with more songs and a wider variety of genres.

These improvements could make the system more accurate and flexible.
---

## 9. Personal Reflection  

Building VibeFinder helped me understand how recommendation systems use user preferences and song characteristics to generate suggestions.

I learned how to use Python to load CSV data, calculate similarity scores, rank songs, and explain recommendations. I also learned that changing the scoring rules can have a noticeable effect on the results.

One interesting discovery was that a song can rank highly even when it does not match every user preference. For example, Gym Hero appeared in multiple recommendation lists because its genre, mood, and energy characteristics matched different users in different ways.

Testing conflicting preferences also showed me that recommendation systems have limitations when the available dataset does not contain songs that match everything a user wants.

Overall, this project gave me a better understanding of how recommendation algorithms work and why testing, evaluation, and fairness are important when designing AI systems.
---