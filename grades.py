def average_score(scores:list[int])->float:
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def pass_fail(score:int)->str:
    return "pass" if score >= 60 else "fail"

def analyze_scores(scores:list[int])->None:
    for i in scores:
        print(f"Score {i} -> {pass_fail(i)}")
        

if __name__ == "__main__":
    scores = [95, 82, 67, 54, 100, 73]

    print("All scores:", scores)
    print("Class average:", average_score(scores))
    print()

    analyze_scores(scores)