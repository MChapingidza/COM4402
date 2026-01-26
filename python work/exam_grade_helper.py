def classify_mark(mark: int () ):
    if mark <= 100 and mark >= 0:
        if mark >= 70:
            return("Distinction")
        elif mark >= 40:
            return("Pass")
        else:
            return("Fail")
    else:
        return("ValueError")


classify_mark(200)




