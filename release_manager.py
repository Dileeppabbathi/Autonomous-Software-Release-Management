import random
import json
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class ReleaseManager:
    def __init__(self):
        self.data = {
            "code_stability": [],
            "user_feedback": [],
            "testing_results": []
        }
        self.release_threshold = 70  # Minimum score to release software

    def analyze_code_stability(self, score):
        self.data["code_stability"].append(score)
        print(f"Code Stability Score: {score}")

    def analyze_user_feedback(self, score):
        self.data["user_feedback"].append(score)
        print(f"User Feedback Score: {score}")

    def analyze_testing_results(self, score):
        self.data["testing_results"].append(score)
        print(f"Testing Results Score: {score}")

    def calculate_release_decision(self):
        total_scores = (
            len(self.data["code_stability"]) + 
            len(self.data["user_feedback"]) + 
            len(self.data["testing_results"])
        )

        if total_scores == 0:
            print("No data available for analysis.")
            return

        average_score = (
            sum(self.data["code_stability"]) +
            sum(self.data["user_feedback"]) +
            sum(self.data["testing_results"])
        ) / total_scores
        
        print(f"Average Score: {average_score}")

        if average_score >= self.release_threshold:
            self.schedule_release()
        else:
            print("Release postponed. Scores are below the threshold.")

    def schedule_release(self):
        # Schedule the release (for simplicity, just print the date)
        release_date = datetime.now() + timedelta(days=1)  # Schedule for the next day
        print(f"Release scheduled for: {release_date.strftime('%Y-%m-%d %H:%M:%S')}")

    def save_data(self, filename="release_data.json"):
        with open(filename, "w") as file:
            json.dump(self.data, file)
        print(f"Data saved to {filename}")

    def plot_data(self):
        plt.figure(figsize=(10, 5))

        # Plotting code stability
        plt.subplot(1, 3, 1)
        plt.plot(self.data["code_stability"], marker='o', label='Code Stability')
        plt.axhline(y=self.release_threshold, color='r', linestyle='--', label='Release Threshold')
        plt.title('Code Stability Scores')
        plt.xlabel('Analysis Count')
        plt.ylabel('Score')
        plt.legend()

        # Plotting user feedback
        plt.subplot(1, 3, 2)
        plt.plot(self.data["user_feedback"], marker='o', label='User Feedback')
        plt.axhline(y=self.release_threshold, color='r', linestyle='--', label='Release Threshold')
        plt.title('User Feedback Scores')
        plt.xlabel('Analysis Count')
        plt.ylabel('Score')
        plt.legend()

        # Plotting testing results
        plt.subplot(1, 3, 3)
        plt.plot(self.data["testing_results"], marker='o', label='Testing Results')
        plt.axhline(y=self.release_threshold, color='r', linestyle='--', label='Release Threshold')
        plt.title('Testing Results Scores')
        plt.xlabel('Analysis Count')
        plt.ylabel('Score')
        plt.legend()

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    release_manager = ReleaseManager()
    
    # User input for scores
    for i in range(3):  # Simulating three analyses
        code_stability_score = int(input("Enter Code Stability Score (0-100): "))
        user_feedback_score = int(input("Enter User Feedback Score (0-100): "))
        testing_results_score = int(input("Enter Testing Results Score (0-100): "))
        
        release_manager.analyze_code_stability(code_stability_score)
        release_manager.analyze_user_feedback(user_feedback_score)
        release_manager.analyze_testing_results(testing_results_score)
    
    # Make a release decision
    release_manager.calculate_release_decision()
    
    # Save the data
    release_manager.save_data()
    
    # Plot the data
    release_manager.plot_data()

