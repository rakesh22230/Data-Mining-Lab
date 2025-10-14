class Student:
    def __init__(self, marks):
        self.marks = marks  # Store the list of marks
        self.result = {}    # Dictionary to store the results
    
    def process_marks(self):
        # Separate marks into pass and fail lists
        pass_list = [mark for mark in self.marks if mark >= 50]
        fail_list = [mark for mark in self.marks if mark < 50]
        
        # Function to calculate highest, lowest, and average score for a list
        def calculate_stats(marks_list):
            if len(marks_list) == 0:
                # Handle empty list case to avoid errors
                return {"Highest": None, "Lowest": None, "Average": None}
            highest = max(marks_list)
            lowest = min(marks_list)
            average = sum(marks_list) / len(marks_list)
            return {"Highest": highest, "Lowest": lowest, "Average": round(average, 2)}
        
        # Calculate stats for pass and fail lists
        self.result["Pass"] = calculate_stats(pass_list)
        self.result["Fail"] = calculate_stats(fail_list)
    
    def display_result(self):
        # Display the results neatly
        for key, stats in self.result.items():
            print(f"\n{key} Students:")
            print(f"Highest Score: {stats['Highest']}")
            print(f"Lowest Score: {stats['Lowest']}")
            print(f"Average Score: {stats['Average']}")

# Example usage:
marks = [56, 72, 89, 45, 90, 67, 38]
student = Student(marks)
student.process_marks()
student.display_result()
