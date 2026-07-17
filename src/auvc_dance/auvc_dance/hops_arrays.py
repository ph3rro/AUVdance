import time
import numpy as np

class Hops:
    def hop(secs, strength):
        neutral = 500.0
        return [secs, neutral, neutral, neutral + strength, neutral]
    
    
