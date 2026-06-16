# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. New Game button doesn't work
  2. Some hints would say "go higher" when the number right after it said "go lower"

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 20 | "Go HIGHER!" hint | "Go LOWER!" hint | Out of attempts! The secret was 29. Score: -5 |
| pressing "New Game" after previous game | New Game Started | Crashes Game, can't play more | none |
| incorrect guess with two attempts left | one more guess attempt | out of attempts message appears | Out of attempts! The secret was 6. Score: -35 |
| correct guess on first attempt with 7 attempts | maximum score awarded (probably should be 100) | Final score is 70, debug shows score as 0 | You won! The secret was 47. Final score: 70 |
| no guesses or attempts used | debug attempts is 0 | debug attempts is 1 | none |
| incorrect guess on first attempt | all debug metrics update correctly | all debug metrics stay the same until next input applied | none |
| changing difficulty to "Hard" | hard number range should be larger than easy and medium number range | hard number range is smaller than medium number range | none |
| changing difficulty to "Hard" | hard attempt count should be less than easy and medium attempt count | hard attempt count is greater than easy and medium attempt count | Guess a number between 1 and 100. Attempts left: 4 |
| guess of 201 | invalid input message, don't use an attempt | guess uses an attempt and says "Go HIGHER!" | Go HIGHER! |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
