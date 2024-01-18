# Activity watch tinyscripts

Those are a few scripts I wrote for [ActivityWatch](https://activitywatch.net/).

## Installation

1. Clone this repository
2. Install Activity-Watch with pip: `pip install aw-client`
3. Edit the scripts to your liking
4. Run the scripts with `python3 <scriptname>.py`

## Scripts

### remove-sensitive.py

Removes all events that contain a given string from the database.

You'll need to know in which bucket you want to remove the events. You can find out by running the `number-of-events.py` script.

### insert-json.py

Inserts a JSON file into the ActivityWatch database.

### number-of-events.py

Prints the number of events in each bucket.
