from csv import reader
avg_rating = sum(rating_sum) / len(rating_sum)
print(avg_rating)

rating = []
for row in apps_data[1:]:
    rating = float(row[7])
    ratings.append(rating)


opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

rating_sum = 0
for row in apps_data[1:]:
    rating = float(row[7])
    rating_sum = rating_sum + rating

avg_rating = rating_sum / 7197

avg_rating_free = free_apps_ratings / len(free_apps_ratings)
