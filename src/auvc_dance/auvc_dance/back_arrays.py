import time
import numpy as np

class Back:
    def go_back(secs, strength):
        neutral = 750.0
        return [secs, neutral-strength, neutral, neutral, neutral]
    
    
