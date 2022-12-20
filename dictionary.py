from collections import Counter
import matplotlib.pyplot as plt
fruits = ["apples",
 "peaches", "peaches"
  "kiwis", "kiwis", "kiwis"
   "bananas", "bananas", "bananas", "bananas"
   "cherrires", "cherrires", "cherrires", "cherrires", "cherrires"
   ]
fruit_counter = Counter(fruits)

print(fruit_counter.keys())
print(fruit_counter.values())

plt.bar(fruit_counter.keys()), (fruit_counter.values())

plt.show()