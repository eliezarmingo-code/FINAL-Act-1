print("Part 2: Manipulation Challenge")
    
fruits = ("apple", "banana", "orange", "grape", "Mango")
print(" My Five Favorite fruits are: ", fruits)
# fruits[0] = "kiwi"  # This will raise an error because tuples are immutable

# List of my daily tasks
tasks = ["wake up", "eat breakfast", "go to work", "exercise", "sleep"]
tasks.append("read a book")
tasks.remove("go to work")
tasks.sort()
print(" My Daily Tasks are: ", tasks)
    
# A set of unique numbers from this list: [1, 2, 2, 3, 4, 4, 5]
numbers = {1, 2, 2, 3, 4, 4, 5}
numbers.add(6)
numbers.remove(2)   
print(" My Unique Numbers are: ", numbers)
    
# My dictionary of personal information
me = {
        "name": "Eliezar Mingo",
        "age": 21,
        "course": "Information Technology"
}
me["grade"] = "A"
me.update({"age": 22})
print(" My Personal Information is: ", me)