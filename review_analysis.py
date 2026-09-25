from review_words import pos, neg
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

    return rs, pw, nw, ar
