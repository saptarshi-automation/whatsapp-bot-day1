# WhatsApp Bot (Day 1)

## Overview
A basic chatbot built using Python.  
It responds to user input using simple conditions.

## Features
- Greeting response
- Product pricing
- Store location
- Product availability
- Discount information

## How to Run
```bash
python app.py

## Learning
- Python basics (if/elif, loops)
- Input/output handling
- Case handling using `.lower()`
- Debugging errors

## Key Learnings (Day 1)

### Concepts I Understood
- How `while True` creates a continuous chat loop
- How `input()` takes user input and `print()` returns output
- How `if/elif/else` controls chatbot responses
- Why `.lower()` is important for handling user input (case-insensitive matching)

### Mistakes I Made
- Forgot `.lower()` → bot didn’t respond to uppercase inputs
- Syntax errors (missing `:` or brackets)
- Indentation issues (Python is space-sensitive)
- Tried running commands while Python script was still active

###  Thinking Improvements
- Always ask: “What input is this code expecting?”
- Test edge cases (PRICE vs price vs Price)
- Break problems into conditions (if this → then what?)

### Questions to Think About
- How can I remove hardcoded conditions and make this dynamic?
- What happens if user asks something unexpected?
- How can this connect to real businesses?

### Notes
- Code must be clean before uploading (not messy experiments)
- Always verify output before committing
- Terminal vs Python execution difference matters

## Status
Day 1 complete (rule-based bot, no AI yet)

## Next Step
- Convert this bot into an AI-powered chatbot using OpenAI API
