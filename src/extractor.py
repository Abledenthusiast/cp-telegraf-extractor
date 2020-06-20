from influxdb import InfluxDBClient
import requests
import time
import schedule

client = InfluxDBClient(host='localhost', port=8086, username='root', password='root', database='telegraf')
def main():
    result = select_prev_metrics()
    if result is not None:
        post_to_service(result)

def select_prev_metrics():
    query = 'select "average_response_ms" FROM ping WHERE time > now() - 24h GROUP BY url;'
    return client.query(query)


def post_to_service(metrics):
    data = {'storageGroupName':'ping', 'name':'avg-resp-ms-' + time.strftime()}
    res = requests.post('https://centralperk-dot-centralperk.appspot.com/api/save', data=data)
    print(res)

if __name__ == '__Main__':
    print('starting')
    main()
    print('completed')