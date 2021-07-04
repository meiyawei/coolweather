import time
import datetime
import random

messages = [
    "of all the trees we could've hit, we had to get one that hits .",
    "If he doesn't stop trying to save your life he's going to kill "
]

print("Typing speed test. Type the following message. I will time you")
time.sleep(2)
print("\nReady")
time.sleep(1)
print("\nSet...")
time.sleep(1)
print("\nGo")
message = random.choice(messages)
print("\n" + message)
start_time = datetime.datetime.now()
typing = raw_input('>')
end_time = datetime.datetime.now()
