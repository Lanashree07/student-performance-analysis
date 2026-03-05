import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students.csv")

data["Average"] = (data["Math"] + data["Science"] + data["English"]) / 3

data["Result"] = data["Average"].apply(lambda x: "Pass" if x >= 50 else "Fail")

def assign_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    else:
        return "C"

data["Grade"] = data["Average"].apply(assign_grade)

top_student = data.loc[data["Average"].idxmax()]
subject_average = data[["Math", "Science", "English"]].mean()

data.to_csv("students_analysis_output.csv", index=False)

print("Final Dataset with Analysis:")
print(data)

print("\nTop Performer:")
print(top_student["Name"], "-", top_student["Average"])

subject_average.plot(kind="bar")
plt.title("Subject-wise Average Marks")
plt.ylabel("Average Marks")
plt.savefig("output_graph.png")
plt.show()
