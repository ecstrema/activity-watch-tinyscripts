import aw_client
import json

def main():
    aw = aw_client.ActivityWatchClient()
    dest_id = "aw-watcher-window_ecstrema-pc"
    target_window_title = "ANY WINDOW TITLE THAT CONTAINS THIS STRING WILL BE DELETED"

    deleted_events = []

    if (input("Are you sure you want to delete all events with the title '" + target_window_title + "'? (y/n): ") != "y"):
        print("Aborting")
        return

    src_events = aw.get_events(dest_id)
    print(f"✓ src events: {len(src_events)}")
    for (i, event) in enumerate(src_events):
        if (event.data["app"] == "msedge.exe" and target_window_title in event.data["title"]):
          aw.delete_event(dest_id, event.id)
          print(f"{event} -- DELETED")
          deleted_events.append(event)

    print(f"✓ deleted events: {len(deleted_events)}")
    # Write the deleted events to a JSON file in the current directory
    with open(f'aw-deleted-events_{target_window_title}_{dest_id}.json', 'w', encoding="utf8") as f:
        f.write(json.dumps([event.to_dict() for event in deleted_events], indent=4))

    print(f'aw-deleted-events_{target_window_title}_{dest_id}.json')


if __name__ == "__main__":
    main()
