import json
from collections import Counter

with open("history.json", encoding="utf-8") as f:
    history = json.load(f)

attempts = Counter()
misses = Counter()

for r in history:
    attempts[r["question"]] += 1
    if not r["correct"]:
        misses[r["question"]] += 1

print(f"Total answers recorded: {len(history)}")

if not misses:
    print("No misses yet. Nice!")
else:
    print("\nMost missed questions:")
    for question, count in misses.most_common(3):
        print(f"- {question} (misses {count} of {attempts[question]})")