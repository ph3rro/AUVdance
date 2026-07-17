class Right:
    def go_right(secs, strength):
        neutral = 500
        movement_arr = [secs, neutral, neutral + strength, neutral, neutral]
        return movement_arr    