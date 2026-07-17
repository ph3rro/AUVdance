import time
import numpy as np

class Back:
    def go_back(secs, strength):
        neutral = 500.0
        return [secs, neutral, neutral+strength, neutral, neutral]
    
    
