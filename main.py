#!/usr/bin/env python
from tdr.azure import subscription_id
from tdr.azure.eventgrid import (
    create_eventgrid_topic,
    subscribe_http_eventgrid_topic,
    send_eventgrid_event,
)

resource_group = "ipeventgridtest"
topic_name = "iptopic"
location = "eastus"
eventgrid_subscription_name = "ipeventgridsubscription"
endpoint_url = (
    "https://endpn9dc3hzbj.x.pipedream.net"  # "https://requestbin.com/r/endpn9dc3hzbj"
)
data = '{Name": "Hello EventGrid"}'

create_eventgrid_topic(resource_group, topic_name, location)
subscribe_http_eventgrid_topic(
    subscription_id,
    resource_group,
    topic_name,
    eventgrid_subscription_name,
    endpoint_url,
)
send_eventgrid_event(
    subscription_id, resource_group, topic_name, eventgrid_subscription_name, data
)
