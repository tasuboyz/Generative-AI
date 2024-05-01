from datetime import datetime, timedelta

class RateLimiter:
    def __init__(self):
        self.actions = {}

    def is_limited(self, user_id, post_id, max_actions, period):
        now = datetime.now()
        action_key = (user_id, post_id)

        if action_key not in self.actions:
            self.actions[action_key] = [now]
            return False

        self.actions[action_key] = [time for time in self.actions[action_key] if now - time <= timedelta(seconds=period)]
        self.actions[action_key].append(now)

        return len(self.actions[action_key]) > max_actions
