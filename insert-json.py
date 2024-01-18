import aw_client
from aw_core import Event
import json
import datetime

def main():
    aw = aw_client.ActivityWatchClient()
    dest_id = "aw-watcher-window_ecstrema-pc"

    src_events = aw.get_events(dest_id)
    print(f"✓ src events: {len(src_events)}")
    print(f"✓ src events: {src_events[-1]}")

    # open aw-backup.json, read it into a variable: events,
    # then call aw.insert_events(dest_id, events)
    with open('./aw-backup.json', 'r', encoding="utf8") as f:
        data = json.load(f)
        events = data["rows"]
        # events are in this format:
        #  [8667, 2, 1705334846292000000, 1705334846292000000, '{"app":"SearchApp.exe","title":"Search"}']
        # dest events are in this format:
        # {'id': 152493, 'timestamp': datetime.datetime(2024, 1, 17, 22, 1, 48, 486000, tzinfo=datetime.timezone.utc), 'duration': datetime.timedelta(seconds=38, microseconds=573000), 'data': {'app': 'Code.exe', 'title': '● test.py - aw-bucket-move - VS Code'}}
        # Convert events to dest events
        print(events[0])
        events_converted = []
        for event in events:
            if (event[3] - event[2]) <= 0:
                continue
            events_converted.append(Event(
                id=event[0],
                timestamp=datetime.datetime.fromtimestamp(event[2] / 1000000000, tz=datetime.timezone.utc),
                duration=datetime.timedelta(seconds=(event[3] - event[2]) / 1000000000),
                data=json.loads(event[4])
            ))
        print(f"✓ dest events: {len(events_converted)}")
        print("✓ dest events:", events_converted[0])
        aw.insert_events(dest_id, events_converted)

    print("Operation complete")


if __name__ == "__main__":
    main()
