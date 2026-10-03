snippets = [
    {
        "code": "for i in range(3):\n  print(i)",
        "question": "What does this print, and why does it stop at 2?",
        "answer": "It prints 0, 1, 2. range(3) starts at 0 and stops before 3",
    },
]

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