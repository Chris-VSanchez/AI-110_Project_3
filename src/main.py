"""
Command line runner for evaluating the Music Recommender.
"""

from src.recommender import load_songs, recommend_songs

def main() -> None:
    songs = load_songs("data/songs.csv")

    # Three different user profiles
    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.90
        },

        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.40
        },

        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.95
        },

        "Conflicting Preferences": {
            "genre": "rock",
            "mood": "melancholic",
            "energy": 0.90
        }
    }

    # Run recommendations for each profile
    for profile_name, user_prefs in profiles.items():

        print("\n" + "=" * 50)
        print(f"USER PROFILE: {profile_name}")
        print("=" * 50)

        recommendations = recommend_songs(
            user_prefs, songs, k=5
        )

        for index, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec

            print(f"{index}. {song['title']} - Score: {score:.2f}")
            print(f"   Artist: {song['artist']}")
            print(f"   Because: {explanation}")
            print()


if __name__ == "__main__":
    main()