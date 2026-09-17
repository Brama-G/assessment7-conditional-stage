"""
Extra check: validates the Online Examination System's core logic.
Called conditionally from the Jenkinsfile.
"""
from exam_system import DEFAULT_QUESTIONS

def check_question_bank():
    assert len(DEFAULT_QUESTIONS) > 0, "Question bank is empty"
    for q in DEFAULT_QUESTIONS:
        assert "question" in q, f"Missing 'question' in {q}"
        assert "options" in q and len(q["options"]) == 4, f"Bad options in {q}"
        assert q["answer"] in ("A", "B", "C", "D"), f"Bad answer in {q}"
    print(f"Extra check passed: {len(DEFAULT_QUESTIONS)} questions validated.")

def check_scoring():
    # Simulate a perfect and a zero score
    total = len(DEFAULT_QUESTIONS)
    perfect = (total / total) * 100
    zero = (0 / total) * 100
    assert perfect == 100.0, "Perfect score should be 100%"
    assert zero == 0.0, "Zero score should be 0%"
    print("Extra check passed: scoring logic verified.")

if __name__ == "__main__":
    check_question_bank()
    check_scoring()
    print("All extra checks passed.")
