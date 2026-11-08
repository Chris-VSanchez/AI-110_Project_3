import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class Song:
    """Represents a song and its musical attributes."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """Stores a user's musical preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """Recommends songs using content-based filtering."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs matching the user's preferences."""
        scored_songs = []

        for song in self.songs:
            score = 0.0

            if song.genre == user.favorite_genre:
                score += 2.0

            if song.mood == user.favorite_mood:
                score += 1.0

            energy_score = 1 - abs(song.energy - user.target_energy)
            score += energy_score

            scored_songs.append((song, score))

        scored_songs.sort(key=lambda item: item[1], reverse=True)

        return [item[0] for item in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a song matches the user's preferences."""
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append("Genre match")

        if song.mood == user.favorite_mood:
            reasons.append("Mood match")

        energy_score = 1 - abs(song.energy - user.target_energy)
        reasons.append(f"Energy similarity ({energy_score:.2f})")

        return ", ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""
    songs = []

    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])

            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate a song's matching score and explain the result."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["genre"]:
        score += 2.0
        reasons.append("Genre match (+2.0)")

    if song["mood"] == user_prefs["mood"]:
        score += 1.0
        reasons.append("Mood match (+1.0)")

    energy_score = 1 - abs(
        song["energy"] - user_prefs["energy"]
    )

    score += energy_score
    reasons.append(f"Energy similarity (+{energy_score:.2f})")

    return score, reasons

def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """Rank songs and return the top k recommendations with explanations."""
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)

        explanation = ", ".join(reasons)

        scored_songs.append((song, score, explanation))

    ranked_songs = sorted(
        scored_songs,
        key=lambda item: item[1],
        reverse=True
    )

    return ranked_songs[:k]