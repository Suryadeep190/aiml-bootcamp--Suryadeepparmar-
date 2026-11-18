with open("big_data.txt","w") as file:
    for i in range(1, 500001):
        file.write(f"this is line {i}.Python is useful for data processingg\n")
        
print("file generated successfully")

total_lines = 0
total_words = 0

search_word ="Python"

with open("big_data.txt","r") as file:
    for line in file:
        total_lines += 1
        
        if search_word in line:
            total_words += 1
        
print(f"rsults")
print(f"total line:{total_lines}")
print(f"total words:{total_words}")
    