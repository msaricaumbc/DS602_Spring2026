# Option1

## Student Success Prediction

### Business Context

**Campus Success Analytics** is helping an introductory course team identify students who may need support before the end of the semester. The goal is to use course activity, assessment progress, and workload indicators to discover meaningful student groups, create tentative labels, and then build a supervised model that predicts likely course success.

This is a **semi-supervised classification** task. You should begin with the unlabeled data, use feature engineering and clustering to create your own student success labels, and only use the provided labels file at the end for evaluation.

### Dataset Overview

- **Total Records**: 5,000
- **Features**: 17 modeling features
- **Target Variable**: NOT INCLUDED in the unlabeled file
- **Missing Values**: 0
- **Success Rate**: 56.82%
- **Class Distribution**: {0: 2159, 1: 2841}

### Feature Categories

#### 1. Attendance Features
- `classes_attended`: Number of class meetings the student attended
- `classes_total`: Total number of class meetings available

#### 2. Study and Engagement Features
- `study_hours_per_week`: Estimated weekly study time
- `discussion_posts`: Number of course discussion posts
- `office_hours_visits`: Number of office hours visits
- `lms_logins_last_30_days`: Learning management system logins in the last 30 days

#### 3. Assignment Features
- `assignments_submitted`: Number of assignments submitted
- `assignments_total`: Total number of assignments available
- `late_submissions`: Number of late assignments

#### 4. Assessment Features
- `quiz_points_earned`: Quiz points earned so far
- `quiz_points_possible`: Quiz points possible so far
- `practice_exam_points`: Practice exam points earned
- `practice_exam_possible`: Practice exam points possible
- `prior_gpa`: Student's prior GPA

#### 5. Life and Workload Features
- `sleep_hours`: Average nightly sleep hours
- `work_hours_per_week`: Weekly outside work hours
- `commute_minutes`: Typical commute time in minutes

#### 6. Target
- `likely_success`: 1 if the student is likely to pass or succeed, 0 if the student may be at risk

### Using the Subject Matter Expert (SME)

The SME class allows you to query label for a specific `student_id`. It should be treated like a limited expert resource rather than as a dataset to inspect directly.

#### Example Usage:

```python
from student_success_sme import SME

# Initialize SME
sme = SME()

# Query the hidden label for one student_id
likely_success = sme.ask("S00001")

print(f"Likely success: {likely_success}")
```

#### Important Notes:
- You can ask up to 500 times
- Pass one `student_id` string to `sme.ask()`
- `sme.ask(student_id)` returns `0` for an at-risk student and `1` for a student likely to succeed
- The `student_id` must exist in the student dataset
- Do not use `student_success_labels.csv` during the initial clustering and label creation process
- Scale numeric features before using distance-based clustering methods
- Inspect cluster centers and summary statistics before assigning labels
- Ambiguous clusters are expected and should be discussed in the analysis
- Compare student-created labels against `likely_success` only at the end, after the semi-supervised workflow is complete

