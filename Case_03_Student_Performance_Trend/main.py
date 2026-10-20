# Case Study 3: Student Performance Trend Analysis
# PDF Topic No. 17

subjects = ["Mathematics", "English", "Python"]
assessments = ["Assessment 1", "Assessment 2", "Assessment 3"]
marks = []

print("Enter marks out of 100 for each subject.")
for assessment in assessments:
    print("\n" + assessment)
    assessment_marks = []

    for subject in subjects:
        while True:
            try:
                score = float(input(f"{subject}: "))
                if 0 <= score <= 100:
                    assessment_marks.append(score)
                    break
                else:
                    print("Marks must be between 0 and 100. Try again.")
            except ValueError:
                print("Please enter a valid number.")

    marks.append(assessment_marks)

print("\n--- Subject-wise Performance Analysis ---")
weak_subjects = []

for index, subject in enumerate(subjects):
    first_score = marks[0][index]
    last_score = marks[2][index]
    change = last_score - first_score

    print("\nSubject:", subject)
    print("Assessment 1:", first_score)
    print("Assessment 2:", marks[1][index])
    print("Assessment 3:", last_score)
    print("Change from Assessment 1 to 3:", round(change, 2))

    if change > 0:
        print("Trend: Improved")
    elif change < 0:
        print("Trend: Declined")
    else:
        print("Trend: No change")

    if all(marks[assessment_index][index] < 40 for assessment_index in range(3)):
        weak_subjects.append(subject)

averages = []
for assessment_marks in marks:
    average = sum(assessment_marks) / len(assessment_marks)
    averages.append(average)

print("\n--- Overall Assessment Averages ---")
for index, assessment in enumerate(assessments):
    print(assessment + " average:", round(averages[index], 2))

overall_change = averages[2] - averages[0]
print("Overall change:", round(overall_change, 2))

if overall_change > 0:
    print("Overall trend: Improved")
elif overall_change < 0:
    print("Overall trend: Declined")
else:
    print("Overall trend: No change")

if weak_subjects:
    print("Consistently weak subjects (below 40 in all assessments):")
    for subject in weak_subjects:
        print("-", subject)
else:
    print("No consistently weak subjects found.")
