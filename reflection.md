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
ChatGPT, Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI noticed that the three pre-existing tests in test_game_logic.py were asserting result == "Win" (a string), but check_guess actually returns a tuple. The AI flagged this unprompted before being asked to fix it. Verification was straightforward — running pytest -v showed the exact failure. The fix made all three tests pass immediately.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When I hit a ModuleNotFoundError: No module named 'logic_utils' error when running pytest, the AI's first fix was adding a conftest.py at the project root. It claimed this would resolve the import error. It didn't — running pytest from inside the tests/ subdirectory still failed because pytest set rootdir to tests/ and never loaded the root-level conftest.py. The AI had to course-correct and add a second conftest.py inside tests/ itself (using Path(__file__).parent.parent to locate the project root), which actually worked. The first suggestion was half-right in reasoning but wrong in practice for the specific invocation context.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I ran pytest -v after each change and checked that the relevant test passed with the correct logic — not just that it didn't crash. For the Hard difficulty range, I confirmed the test test_hard_range_wider_than_normal actually compared the values, not just that the function ran.
- Describe at least one test you ran (manual or using pytest)  
Running pytest -v after fixing the Hard difficulty range showed test_difficulty_ranges_increase_in_order passing — it checks that Easy's upper bound < Normal's < Hard's. Before the fix, Hard returned (1, 50) which is narrower than Normal's (1, 100), so that ordering assertion would have failed. Seeing it pass confirmed the range was actually wider now, not just that the number changed.
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
Yes — for the Hard difficulty range bug, the AI suggested writing test_difficulty_ranges_increase_in_order which compares all three difficulty upper bounds in sequence rather than just checking one hardcoded value. That was more useful than something like assert hard_high == 200, because it tests the intent (Hard should be hardest) instead of just the specific number chosen.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Every time you interact with anything on the page — clicking a button, typing in a box — Streamlit reruns the entire script from top to bottom. That means regular variables reset every time. st.session_state is basically a dictionary that survives those reruns, so things like your score, attempt count, and secret number don't get wiped on each interaction.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Writing tests that check intent rather than hardcoded values — like asserting that Hard's range is wider than Normal's instead of asserting it equals exactly 200. That kind of test survives future changes better.
- What is one thing you would do differently next time you work with AI on a coding task?
Ask the AI to explain why a fix works before accepting it, not just whether the tests pass. The conftest fix worked but I didn't fully understand it until the first attempt failed.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI-generated code looks correct at a glance but can have subtle logic errors that only show up when you actually run it against real inputs — like difficulty ranges that are backwards. You still have to read it critically, not just trust it.
