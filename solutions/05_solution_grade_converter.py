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
Convert numeric grades to letters for a course gradebook.
1. Write convert_to_letter(grade) returning the correct letter using these
   rules:
       90+ → A
       80–89 → B
       70–79 → C
       60–69 → D
       below 60 → F
2. Call the function with at least three different numeric grades and print
   the results.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

def convert_to_letter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

print(convert_to_letter(92))
print(convert_to_letter(75))
print(convert_to_letter(58))
