import json
import datetime

class ReputationSystem:
    def __init__(self):
        self.users_reputation = {}

    def load_user_reputation_data(self):
        try:
            with open('user_reputation_data.json', 'r') as file:
                self.users_reputation = json.load(file)
        except FileNotFoundError:
            self.users_reputation = {}

    def save_user_reputation_data(self):
        with open('user_reputation_data.json', 'w') as file:
            json.dump(self.users_reputation, file)

    def get_user_reputation(self, user_id):
        return self.users_reputation.get(user_id, 0)

    def add_reputation(self, user_id, amount):
        if user_id in self.users_reputation:
            self.users_reputation[user_id] += amount
        else:
            self.users_reputation[user_id] = amount

    def remove_reputation(self, user_id, amount):
        if user_id in self.users_reputation:
            self.users_reputation[user_id] = max(0, self.users_reputation[user_id] - amount)

    def reset_user_reputation(self, user_id):
        if user_id in self.users_reputation:
            self.users_reputation[user_id] = 0

    def get_top_users(self, num_users):
        sorted_users = sorted(self.users_reputation.items(), key=lambda x: x[1], reverse=True)
        return sorted_users[:num_users]

    def update_reputation(self, user_id, action, amount):
        if action == "add":
            self.add_reputation(user_id, amount)
        elif action == "remove":
            self.remove_reputation(user_id, amount)
        self.save_user_reputation_data()

    def handle_user_activity(self, user_id, activity_type):
        if activity_type == "message":
            self.add_reputation(user_id, 1)
        elif activity_type == "voice_chat":
            self.add_reputation(user_id, 2)
        elif activity_type == "helpful":
            self.add_reputation(user_id, 3)
        self.save_user_reputation_data()

    def check_user_activity_threshold(self, user_id, threshold):
        return self.get_user_reputation(user_id) >= threshold

    def update_reputation_based_on_activity(self, user_id, threshold):
        if self.check_user_activity_threshold(user_id, threshold):
            self.add_reputation(user_id, 5)
        self.save_user_reputation_data()

reputation_system = ReputationSystem()
reputation_system.load_user_reputation_data()