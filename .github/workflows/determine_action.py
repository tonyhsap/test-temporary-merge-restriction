from datetime import datetime
import pytz

def determine_action():
    # Define the target timezone
    tz = pytz.timezone('Europe/Berlin')

    # Get the current time in the target timezone
    local_time = datetime.now(tz)

    # Desired times for action
    if local_time.hour == 11 and local_time.minute == 30:
        print('ACTION=add')
    elif local_time.hour == 13 and local_time.minute == 15:
        print('ACTION=remove')
    else:
        print('ACTION=none')

if __name__ == "__main__":
    determine_action()
