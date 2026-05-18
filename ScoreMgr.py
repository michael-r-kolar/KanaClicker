import json
import os
from Constants import *

class ScoreMgr:
    def __init__(self):
        self.path = SCORE_FILE

    def read_score(self, mode):
        score = 0
        if os.path.exists(self.path):
            with open(self.path, "r") as file:
                data = json.load(file)
                score = data.get(mode)
        else:
            print("ERROR: could not open file {self.path}")
        return score

    def write_score(self, mode, score):
        if os.path.exists(self.path):
            with open(self.path, "r") as file:
                data = json.load(file)
            data[mode]=score
            with open(self.path, "w") as file:
                json.dump(data, file, indent=4)
        else:
            print("ERROR: could not open file {self.path}")

    def update_score(self, mode, new_score):
        past_score = self.read_score(mode)
        if past_score == -1:
            self.write_score(mode, new_score)
        elif new_score < past_score:
                self.write_score(mode, new_score)
        # else score should not be updated

    def format_timestamp(self, milliseconds):
        seconds, milliseconds_left = divmod(milliseconds, 1000)
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes}:{seconds}:{milliseconds_left}"

    def display_score(self, mode):
        score = self.read_score(mode)
        if score == -1:
            return NO_SCORE
        else:
            return self.format_timestamp(score)


