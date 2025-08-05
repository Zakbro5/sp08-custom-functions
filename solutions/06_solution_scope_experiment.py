'''
OPTIONAL AI GUIDANCE PROMPT:
----------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions to
a practice problem that my professor gave me to try before class. Please be my
kind tutor and walk me through how to solve the problem step by step.

Don't just give me the full solution all at once (unless I later ask for it).
Instead, help me work through it gradually, with clear explanations and small,
easy-to-understand examples. Please use everyday language and explain things
in a simple, friendly way.


INSTRUCTIONS:
-------------
You're troubleshooting a budgeting tool.
1. Create a global variable budget = 1000 at the top of the file.
2. Write spend_money() that defines a local budget = 200 and prints:
    Inside function, budget is: 200
3. Outside the function, print:
    Outside function, budget is: 1000
This exercise shows the difference between local and global variables with
the same name.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

budget = 1000

def spend_money():
    budget = 200
    print(f"Inside function, budget is: {budget}")

spend_money()
print(f"Outside function, budget is: {budget}")
