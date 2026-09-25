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
