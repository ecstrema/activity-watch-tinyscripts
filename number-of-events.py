import aw_client

def main():
    aw = aw_client.ActivityWatchClient()
    buckets = aw.get_buckets()
    # print the number of events in each bucket
    for bucket in buckets:
        events = aw.get_events(bucket)
        print(f"{bucket}: {len(events)}")


if __name__ == "__main__":
    main()
