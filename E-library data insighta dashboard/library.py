import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

class LibraryDashboard:
    def __init__(self):
        self.df = None

    def load_data(self, filename='library_transactions.csv'):
        try:
            self.df = pd.read_csv(filename)
            print("csv file successfully!")
            self.df.dropna(inplace=True)
            return True
        except:
            ("file not found")
        return False


    def calculate_statistics(self):
        most_book = self.df['Book Title'].mode()[0]
        print("most borrowd book:")
        avg_days = np.mean(self.df['borrowing duration days'])
        print(f"average borrowing days: {avg_days}")

    def filter_transactions(self, genre):
        if self.df is None:
                print("No data loaded!")
    
        if len > 0:
            pass
            # if(genre in df['genre'])
        else:
            print("no records found")    
    
            return 
    
    def generate_visualization(self):
        if self.df is None:
                print("No data available.")
                return
        
        print("genreating visualizations")
        plt.figure(figsize=(12, 10))
                
        #bar chart
        plt.subplot(2, 2, 1)
        self.df['Book Title'].value_counts().plot(kind='bar', color="blue")
        plt.title('top Borrowed Books')
        plt.xlabel('Books')
        plt.ylabel('Count')
        
        #pie chart
        plt.subplot(2, 2, 2)
        self.df['Book Title'].value_counts().plot(kind='pie',autopct='1.0f%%')
        plt.title("Books by Genre")
        plt.ylabel(' ')

        #histogram
        plt.subplot(2, 2, 3)
        plt.hist(self.df)
        plt.title()

        #heatmap
        plt.subplot(2,2,4)
        sns.heatmap()
        plt.title()

        plt.tight_layout()
        plt.show()

def main():
    dashboard = LibraryDashboard()
    file_name = "library_transactions.csv"

    if dashboard.load_data("library_transactions.csv"):
        while True:
            print("1. View Statistics")
            print("2. Filter by Genre")
            print("3. Generate Visualizations Graphs")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                dashboard.calculate_statistics()
            elif choice == '2':
                dashboard.filter_transactions()
            elif choice == '3':
                dashboard.generate_visualizations()
            elif choice == '4':
                print("Exit!")
                break
            else:
                print("Invalid choice! Please select between 1 and 4.")
main()

