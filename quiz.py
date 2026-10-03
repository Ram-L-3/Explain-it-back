snippets = [
    {
        "code": "for i in range(3):\n  print(i)",
        "question": "What does this print, and why does it stop at 2?",
        "answer": "It prints 0, 1, 2. range(3) starts at 0 and stops before 3",
    },
    {
        "code": "i = 5\n while(i>0):\n print(i)\n i -= 1",
        "question": "What does this print, and why does it stop at 1?",
        "answer": "It prints 5, 4, 3, 2, 1. The loop continues while i is greater than 0, and i is decremented by 1 in each iteration."
    },
    {
        "code": "def add(a, b):\n return a + b\n\nresult = add(3, 4)\nprint(result)",
        "question": "What does this print, and what is the purpose of the add function?",
        "answer": "It prints 7. The add function takes two arguments and returns their sum."
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