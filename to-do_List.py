class Activities:
    activities_List = []
    
    title = ""
    date = ""
    time = ""
    is_completed = False
    
    def add_activities(self):
        self.title = input('Enter activity: ')
        self.date = input('Enter date: ')
        self.time = input('Enter time: ')
        self.is_completed = False
        
        self.activities_List.append({
            'title': self.title,
            'date': self.date,
            'time': self.time,
            'Is completed': self.is_completed
        })
        print("Activities added successful")
        
    def read_activities(self):
        for activity in self.activities_List:
            print(activity)
                
                
while True:
    print("\n To-Do List")
    print('1. To add for a movie: ')
    print('2. To view movies: ')
    print('3. To exit: ')
    
    choice = input("Choose from the option: ")
    
    if choice == 1:
        activity = Activities()
        activity.add_activities()
        
    elif choice == 2:
        activity = Activities()
        activity.read_activities()
        
    elif choice == 3:
        print("Existing activities ")
        break