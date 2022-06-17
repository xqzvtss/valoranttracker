import os
import valorant

KEY = os.environ["VALPY-KEY"]
client = valorant.Client(KEY, region="eu")

leaderboard = client.get_leaderboard(size=15)

for p in leaderboard.players:
    print(f"#{p.leaderboardRank} - {p.gameName} ({p.numberOfWins} wins)")
