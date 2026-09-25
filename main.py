pos = ["good", "great", "excellent", "amazing", "helpful", "friendly", "fast", "quick", "affordable", "easy", "smooth", "useful", "polite", "reliable", "happy"]

neg = ["bad", "poor", "worst", "terrible", "slow", "late", "delayed", "expensive", "costly", "rude", "unhelpful", "difficult", "error", "broken", "damaged", "defective", "ignored", "problem"]

sug = {"service": "Improve customer support and response time.", "product": "Improve product quality and check products before delivery.", "delivery": "Improve delivery speed and give better delivery updates.", "price": "Review the pricing and provide better value.", "app": "Fix technical errors and improve app performance.", "staff": "Give staff proper training and improve communication."}

def analyze_review(rv):
    wd = rv.lower().split()
    pw = []
    nw = []

    for w in wd:
        w = w.strip(".,!?;:")

        if w in pos and w not in pw:
            pw.append(w)

        if w in neg and w not in nw:
            nw.append(w)

    ar = []

    for w in wd:
        w = w.strip(".,!?;:")

        if w in ["service", "support", "response", "complaint"]:
            if "service" not in ar:
                ar.append("service")

        elif w in ["product", "quality", "damaged", "broken", "defective"]:
            if "product" not in ar:
                ar.append("product")

        elif w in ["delivery", "late", "delayed", "shipping"]:
            if "delivery" not in ar:
                ar.append("delivery")

        elif w in ["price", "expensive", "costly", "affordable"]:
            if "price" not in ar:
                ar.append("price")

        elif w in ["app", "application", "website", "error"]:
            if "app" not in ar:
                ar.append("app")

        elif w in ["staff", "employee", "employees", "worker"]:
            if "staff" not in ar:
                ar.append("staff")

    ps = len(pw)
    ns = len(nw)

    if ps > ns:
        rs = "Positive"
    elif ns > ps:
        rs = "Negative"
    elif ps > 0 and ns > 0:
        rs = "Mixed"
    else:
        rs = "Neutral"

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

    return rs


def save_review(nm, rv, rs):
    fl = open("reviews.txt", "a")
    fl.write("Company: " + nm + "\n")
    fl.write("Review: " + rv + "\n")
    fl.write("Result: " + rs + "\n")
    fl.write("-" * 50 + "\n")
    fl.close()


def show_reviews():
    try:
        fl = open("reviews.txt", "r")
        dt = fl.read()
        fl.close()

        print("\n" + "=" * 50)
        print("              SAVED REVIEWS")
        print("=" * 50)

        if dt == "":
            print("No reviews saved yet.")
        else:
            print(dt)

    except FileNotFoundError:
        print("\nNo reviews saved yet.")


while True:
    print("\n")
    print("=" * 50)
    print("     COMPANY REVIEW & COMPLAINT SYSTEM")
    print("=" * 50)

    print("\n1. Analyze Review")
    print("2. View Saved Reviews")
    print("3. Exit")

    ch = input("\nEnter your choice: ")

    if ch == "1":
        nm = input("\nEnter company name: ")
        rv = input("Enter company review or complaint: ")

        if nm == "" or rv == "":
            print("\nPlease enter both company name and review.")
        else:
            print("\nCompany:", nm)
            print("Review:", rv)

            rs = analyze_review(rv)
            save_review(nm, rv, rs)

            print("\nReview saved successfully.")

    elif ch == "2":
        show_reviews()

    elif ch == "3":
        print("\nThank you for using the system!")
        break

    else:
        print("\nInvalid choice. Please enter 1, 2 or 3.")
