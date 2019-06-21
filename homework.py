who = None
action = None
assignment = None


import random
# create lists of excuses# your own code
who = ["my dog", "my cat", "my little brother", "my hamster", "Thanos"]
action = ["ate", "burned", "destroyed", "snapped", "erased", "went potty on"]
assignment = ["my homework", "my PowerPoint", "my essay", "my math problems"]
# Shuffle all three lists# your own code
random.shuffle(who)# your own code
random.shuffle(action)# your own code
random.shuffle(assignment)# your own code
# Print out excuse# your own code
print(who[0] + " " + action[0] + " " + assignment[0] + ".")
