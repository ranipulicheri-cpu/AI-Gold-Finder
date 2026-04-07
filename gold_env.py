import random

class GoldDetectionEnv:

    def __init__(self):
        self.state = "start"

    def reset(self):
        self.state = "scan_area"
        return {"state": self.state}

    def step(self, action):

        gold_probability = random.random()

        if gold_probability > 0.7:
            reward = 1.0
            done = True
            result = "Gold detected"
        else:
            reward = 0.3
            done = False
            result = "No gold detected"

        return {
            "state": result,
            "reward": reward,
            "done": done
        }

    def state(self):
        return {"state": self.state}
