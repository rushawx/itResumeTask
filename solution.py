import random

class Bucket:
    def __init__(self, keys, values):
        self.keys = keys
        self.values = values
        
        self.probs = []
        value = 0.0
        for x in self.values:
            self.probs.append((value, value + x))
            value += x

    def get(self):
        p = random.randint(0, 100) / 100
        for i in range(len(self.probs)):
            if self.probs[i][0] <= p and p < self.probs[i][1]:
                return self.keys[i]
        return self.keys[-1]
