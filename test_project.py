from review_analysis import analyze_review

r1 = analyze_review("good fast helpful service")
assert r1[0] == "Positive"

r2 = analyze_review("bad slow service")
assert r2[0] == "Negative"

r3 = analyze_review("good but slow delivery")
assert r3[0] == "Mixed"

r4 = analyze_review("hello welcome")
assert r4[0] == "Neutral"

print("All tests passed successfully.")
