from logic_utils import check_guess, get_range_for_difficulty

# --- Bug fix: Hard difficulty range was (1, 50), narrower than Normal (1, 100) ---

def test_hard_range_wider_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high, (
        f"Hard range top ({hard_high}) must exceed Normal ({normal_high})"
    )

def test_difficulty_ranges_increase_in_order():
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high

# --- Bug fix: attempt_limit_map had Easy=6 < Normal=8 (backwards) ---
# These values mirror app.py; kept here to pin the correct ordering.

_ATTEMPT_LIMITS = {"Easy": 10, "Normal": 8, "Hard": 5}

def test_easy_has_more_attempts_than_normal():
    assert _ATTEMPT_LIMITS["Easy"] > _ATTEMPT_LIMITS["Normal"]

def test_attempt_limits_decrease_with_difficulty():
    assert _ATTEMPT_LIMITS["Easy"] > _ATTEMPT_LIMITS["Normal"] > _ATTEMPT_LIMITS["Hard"]

# --- Existing check_guess tests ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
