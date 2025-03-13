import os
from datetime import datetime
import pytz


def determine_action():
    # Define the target timezone
    tz = pytz.timezone("Europe/Berlin")

    # Get the current time in the target timezone
    local_time = datetime.now(tz)

    # Determine the action based on the current time
    if local_time.hour == 11 and local_time.minute == 30:
        action = "add"
    elif local_time.hour == 13 and local_time.minute == 15:
        action = "remove"
    else:
        action = "none"

    # Write the action to $GITHUB_ENV for subsequent steps
    github_env = os.getenv("GITHUB_ENV")
    if github_env:
        with open(github_env, "a") as env_file:
            env_file.write(f"ACTION={action}\n")
    else:
        print("GITHUB_ENV is not set. Cannot persist environment variable.")

if __name__ == "__main__":
    determine_action()
