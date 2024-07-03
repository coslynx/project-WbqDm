import json
import datetime

class Maintenance:
    def __init__(self):
        self.config_file = 'config.json'

    def load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Config file not found.")
            return {}

    def save_config(self, config):
        with open(self.config_file, 'w') as file:
            json.dump(config, file, indent=4)

    def perform_maintenance(self):
        config = self.load_config()
        if 'maintenance_tasks' in config:
            for task in config['maintenance_tasks']:
                if 'task_type' in task and 'task_details' in task:
                    if task['task_type'] == 'spam_check':
                        self.perform_spam_check(task['task_details'])
                    elif task['task_type'] == 'word_filter':
                        self.perform_word_filter(task['task_details'])
                    # Add more maintenance tasks as needed

    def perform_spam_check(self, details):
        # Logic to perform spam check
        pass

    def perform_word_filter(self, details):
        # Logic to perform word filter
        pass

    def schedule_task(self, task_type, task_details):
        config = self.load_config()
        if 'maintenance_tasks' not in config:
            config['maintenance_tasks'] = []
        config['maintenance_tasks'].append({'task_type': task_type, 'task_details': task_details})
        self.save_config(config)

if __name__ == "__main__":
    maintenance = Maintenance()
    maintenance.perform_maintenance()