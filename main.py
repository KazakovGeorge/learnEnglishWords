import random
import config
from wordFunctions import getWord

for i in range(10):
    print(getWord(random.randint(0, config.numberOfWords)))