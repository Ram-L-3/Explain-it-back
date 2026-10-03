import json

with open("questions.json", encoding="utf-8") as f:
    snippets = json.load(f)

score = 0 

for s in snippets:
    print("\nCODE: \n" + s["code"])
    print("\nQUESTION:", s["question"])
    input("Type your answer, then press Enter: ")
    print("\nMODEL Answer:", s["answer"])
    got_it = input("Did you get it? (y/n): ").lower()
    if got_it == "y":
        score += 1

print(f"\nScore: {score}/{len(snippets)}")