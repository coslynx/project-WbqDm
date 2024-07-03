import datetime
import json

def log_action(action_type, user_id, moderator_id, reason=None):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = {
        "timestamp": timestamp,
        "action_type": action_type,
        "user_id": user_id,
        "moderator_id": moderator_id,
        "reason": reason
    }
    
    with open('log.json', 'a') as log_file:
        json.dump(log_entry, log_file)
        log_file.write('\n')