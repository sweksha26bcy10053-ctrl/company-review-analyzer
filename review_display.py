from review_words import sug

def show_result(rs, pw, nw, ar):
    print("\n" + "=" * 50)
    print("             REVIEW ANALYSIS")
    print("=" * 50)
    print("\nOverall Result:", rs)

    print("\nGOOD POINTS")
    print("-" * 50)

    if len(pw) > 0:
        for w in pw:
            print("+", w)
    else:
        print("No major positive points found.")

    print("\nPROBLEMS")
    print("-" * 50)

    if len(nw) > 0:
        for w in nw:
            print("-", w)
    else:
        print("No major problems found.")

    print("\nAREAS IDENTIFIED")
    print("-" * 50)

    if len(ar) > 0:
        for a in ar:
            print("*", a)
    else:
        print("No specific area identified.")

    print("\nSUGGESTIONS")
    print("-" * 50)

    if len(ar) > 0:
        for a in ar:
            print("*", sug[a])
    elif rs == "Positive":
        print("Continue the things that customers like.")
    elif rs == "Negative":
        print("Check the complaints and take corrective action.")
    else:
        print("Collect more customer feedback.")

    print("=" * 50)
