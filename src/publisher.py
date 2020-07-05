from google.cloud import pubsub_v1
import json
import sys
# TODO(developer)
# project_id = "your-project-id"
# topic_id = "your-topic-id"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path('centralperk', 'metrics')

def publish(msg: dict):
    print(sys.getsizeof(dict))
    data = json.dumps(msg).encode("utf-8")
    print(data)
    future = publisher.publish(topic_path, data=data)
    print(future.result())
