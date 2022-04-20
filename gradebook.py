last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [subjects, grades]
print(gradebook)
subjects.append("computer science")
grades.append(100)
print(gradebook)
subjects.append("visual arts")
grades.append(93)
print(gradebook)
subjects[-1]
grades[-1]

subjects.remove("poetry")
grades.remove(85)
print(gradebook)
gradebook.append("Pass")
print(gradebook)
full_gradebook = gradebook +last_semester_gradebook
print(full_gradebook)