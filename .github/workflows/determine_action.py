import os
from datetime import datetime, time
import pytz


def determine_action():
    # Define CET timezone
    cet = pytz.timezone("Europe/Berlin")

    # Get current time in CET
    current_time = datetime.now(cet).time()

    # Define time range
    start_time = time(11, 30)  # 11:30
    end_time = time(13, 15)    # 13:15

    # Determine the action based on the current time
    action = "none"
    if start_time <= current_time <= end_time:
        action = "add"
    else:
        action = "remove"

    # Write the action to $GITHUB_ENV for subsequent steps
    github_env = os.getenv("GITHUB_ENV")
    if github_env:
        with open(github_env, "a") as env_file:
            env_file.write(f"ACTION={action}\n")
    else:
        print("GITHUB_ENV is not set. Cannot persist environment variable.")

if __name__ == "__main__":
    determine_action()
