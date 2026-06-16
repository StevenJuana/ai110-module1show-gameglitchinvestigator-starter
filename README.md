# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game's purpose:** A number guessing game built with Streamlit where the player picks a difficulty, gets a limited number of attempts, and tries to guess a secret number using Higher/Lower hints. Score is tracked across guesses and awarded on a win.

- [x] **Bugs found:**
  - `get_range_for_difficulty` returned `(1, 50)` for Hard — a narrower range than Normal's `(1, 100)`, making Hard easier than Normal.
  - `attempt_limit_map` gave Easy only 6 attempts versus Normal's 8 — the ordering was backwards (easier difficulty should allow more attempts).
  - All four logic functions (`get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`) were defined directly in `app.py` instead of `logic_utils.py`, making them untestable in isolation.
  - Pre-existing tests in `test_game_logic.py` compared `check_guess`'s return value against a bare string, but the function returns a tuple `(outcome, message)`, so all three tests were silently broken.

- [x] **Fixes applied:**
  - Moved all four logic functions into `logic_utils.py` and updated `app.py` to import from there.
  - Corrected the Hard difficulty range to `(1, 200)` so difficulty scales consistently across Easy → Normal → Hard.
  - Updated Easy's attempt limit from `6` to `10` so attempts decrease as difficulty increases.
  - Fixed existing tests to unpack the tuple: `outcome, _ = check_guess(...)`.
  - Added pytest cases that directly target both difficulty bugs and a `conftest.py` inside `tests/` to fix module resolution when running pytest from any directory.

## 📸 Demo Walkthrough

Sample game on **Normal** difficulty (range 1–100, 8 attempts, secret = 63):

1. User selects **Normal** difficulty in the sidebar. The game displays range 1–100 and 8 attempts allowed.
2. User enters **40** and clicks Submit → game returns **"Too Low"**. Attempt count increases to 1, score decreases by 5.
3. User enters **70** → **"Too High"**. Score adjusts again; the narrowed range is now clear (41–69).
4. User enters **55** → **"Too Low"**. Range narrows further to 56–69.
5. User enters **65** → **"Too High"**. Range narrows to 56–64.
6. User enters **63** → **"Correct!"** Balloons appear, final score is displayed, and the game locks until New Game is clicked.

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
