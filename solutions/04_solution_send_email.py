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
Simulate emailing from an information systems dashboard.
1. Define send_email(recipient, subject="No Subject") that prints:
    Sending email to bob@example.com with subject: 'No Subject'
2. Call it once with only the recipient.
3. Call it again with recipient and a custom subject.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

def send_email(recipient, subject="No Subject"):
    print(f"Sending email to {recipient} with subject: '{subject}'")

send_email("bob@example.com")
send_email("alice@example.com", "Meeting Reminder")
