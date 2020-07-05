from influxdb import InfluxDBClient
import requests
import time
import schedule
import publisher as Producer

client = InfluxDBClient(host='localhost', port=8086, username='root', password='root', database='telegraf')
def extract():
    try:
        print(time.time())
        
        result = select_prev_metrics()
        if result is not None:
            post_to_service(result)

    except Exception as exc:
        print(exc)

def select_prev_metrics():
    query = 'select MEAN(average_response_ms) FROM ping WHERE time > now() - 1h GROUP BY url;'
    result_items = list(client.query(query).items())
    # nested tuples are used here, so: list of metrics -> tuple of (ping, 'url' : url)
    result_dict = { result_items[i][0][1]['url'] : list(result_items[i][1]) for i in range(0, len(result_items))}
    return result_dict

def post_to_service(metrics):
    for url,stats in metrics.items():
        data = {'storageGroupName':'ping', 'name':url + '-avg-resp-ms', 'data':stats[0]}

        Producer.publish(data)

if __name__ == '__main__':
    print('starting')
    schedule.every(1).hours.do(extract)
    while True:
        schedule.run_pending()
        time.sleep(300) # wait five minutes
