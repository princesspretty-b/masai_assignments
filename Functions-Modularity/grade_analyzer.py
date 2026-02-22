# Name: Bhuvaneshwari G
# Roll Number: IITP_AIMLTN_2602317
# Assignment: Python Function & Modularity - Subjective Question

def process_scores(students):
    """
    Calculate the average score (rounded to 2 decimals) for each student.
    Returns: { name: average_score }
    """
    averages = {}
    for name, scores in students.items():
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg
    return averages


def classify_grades(averages):
    """
    Assign letter grades based on average score.
    Returns: { name: (average, grade) }
    """
    # Define grading thresholds locally (not global)
    A_THRESHOLD = 90
    B_THRESHOLD = 75
    C_THRESHOLD = 60

    classified = {}
    for name, avg in averages.items():
        if avg >= A_THRESHOLD:
            grade = "A"
        elif avg >= B_THRESHOLD:
            grade = "B"
        elif avg >= C_THRESHOLD:
            grade = "C"
        else:
            grade = "F"

        classified[name] = (avg, grade)

    return classified


def generate_report(classified, passing_avg=70):
    """
    Print formatted report and return number of students who passed.
    """
    print("===== Student Grade Report =====")

    passed_count = 0

    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed_count += 1

        print(f"{name:<10} | Avg: {avg:<6} | Grade: {grade} | Status: {status}")

    total_students = len(classified)
    failed_count = total_students - passed_count

    print("================================")
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed_count}")
    print(f"Failed         : {failed_count}")

    return passed_count


# -------------------- Main Block --------------------

if __name__ == "__main__":
    students = {
        "Alice": [85, 90, 84, 86],
        "Bob": [60, 65, 58, 67],
        "Clara": [95, 98, 94, 98]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified,60)