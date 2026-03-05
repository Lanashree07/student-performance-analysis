import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("students.csv")

# Calculate Average
data["Average"] = (data["Math"] + data["Science"] + data["English"]) / 3

# Add Pass/Fail column
data["Result"] = data["Average"].apply(lambda x: "Pass" if x >= 50 else "Fail")

# Add Grade column
def assign_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    else:
        return "C"

data["Grade"] = data["Average"].apply(assign_grade)

# Find Top Performer
top_student = data.loc[data["Average"].idxmax()]

# Subject-wise average
subject_average = data[["Math", "Science", "English"]].mean()

# Export to new CSV
data.to_csv("students_analysis_output.csv", index=False)

# Print results
print("Final Dataset with Analysis:")
print(data)

print("\nTop Performer:")
print(top_student["Name"], "-", top_student["Average"])

# Plot subject averages
subject_average.plot(kind="bar")
plt.title("Subject-wise Average Marks")
plt.ylabel("Average Marks")
plt.show()
