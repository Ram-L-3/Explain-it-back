import json
from datetime import datetime

with open("questions.json", encoding="utf-8") as f:
    snippets = json.load(f)

score = 0 
results = []

for s in snippets:
    print("\nCODE: \n" + s["code"])
    print("\nQUESTION:", s["question"])
    input("Type your answer, then press Enter: ")
    print("\nMODEL Answer:", s["answer"])
    got_it = input("Did you get it? (y/n): ").lower()
    if got_it == "y":
        score += 1

    results.append({
        "question": s["question"],
        "correct": got_it == "y",
        "time": datetime.now().isoformat(timespec="seconds"),
    })
        

print(f"\nScore: {score}/{len(snippets)}")
try:
    with open("history.json", encoding="utf-8") as f:
        history = json.load(f)
except FileNotFoundError:
    history = []
history.extend(results)

with open("history.json", "w", encoding="utf-8") as f:
    json.dump(history, f, indent=2)