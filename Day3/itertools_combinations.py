from itertools import combinations, permutations, product, chain

students = ["Amit", "Rahul", "Priya", "Neha", "Karan"]

pairs = list(combinations(students, 2))

print("\n--- Student Combinations ---")

for pair in pairs:
    print(pair)
print("Total pairs:", len(pairs))


ordered_pairs = list(permutations(students, 2))

print("\n--- Student Permutations ---")

for pair in ordered_pairs:
    print(pair)

print("Total ordered pairs:", len(ordered_pairs))

# Permutations consider order, so ('Amit', 'Rahul')
# and ('Rahul', 'Amit') are counted separately.


colours = ["Red", "Blue", "Black"]
sizes = ["M", "L"]

shirt_combinations = list(product(colours, sizes))

print("\n--- Shirt Combinations ---")

for shirt in shirt_combinations:
    print(shirt)

print("Total combinations:", len(shirt_combinations))



features = ["Age", "Salary", "Experience", "Education"]

all_subsets = list(
    chain.from_iterable(
        combinations(features, r)
        for r in range(len(features) + 1)
    )
)

print("\n--- Feature Subsets ---")

for subset in all_subsets:
    print(subset)

print("Total subsets:", len(all_subsets))

