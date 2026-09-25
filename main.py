from review_analysis import analyze_review
from review_data import save_review, show_reviews
from review_display import show_result
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

            rs, pw, nw, ar = analyze_review(rv)
            show_result(rs, pw, nw, ar)
            save_review(nm, rv, rs)

            print("\nReview saved successfully.")

    elif ch == "2":
        show_reviews()

    elif ch == "3":
        print("\nThank you for using the system!")
        break

    else:
        print("\nInvalid choice. Please enter 1, 2 or 3.")
       
