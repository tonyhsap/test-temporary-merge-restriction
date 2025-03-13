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

    # Write the action to $GITHUB_ENV so it can be used in subsequent steps
    with open('/github/env', 'a') as env_file:
        env_file.write(f"ACTION={action}\n")

if __name__ == "__main__":
    determine_action()
