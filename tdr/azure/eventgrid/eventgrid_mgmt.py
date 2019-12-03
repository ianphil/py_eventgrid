#!/usr/bin/env python
from . import eventgrid_mgmt_client
from .. import poll_for_complete
import requests


def create_eventgrid_topic(resource_group, topic_name, location):
    result = eventgrid_mgmt_client.topics.create_or_update(
        resource_group, topic_name, {"location": location}
    )
    poll_for_complete(result)


def subscribe_http_eventgrid_topic(
    subscription_id, resource_group, topic_name, eventgrid_subscription_name, endpoint
):
    scope = f"/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.EventGrid/topics/{topic_name}"
    info = {"destination": {"endpoint_url": endpoint, "endpoint_type": "WebHook"}}
    result = eventgrid_mgmt_client.event_subscriptions.create_or_update(
        scope, eventgrid_subscription_name, info
    )
    poll_for_complete(result)


def send_eventgrid_event(
    subscription_id, resource_group, topic_name, eventgrid_subscription_name, data
):
    scope = f"/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.EventGrid/topics/{topic_name}"
    eventgrid_subscription_endpoint_url = eventgrid_mgmt_client.event_subscriptions.get_full_url(
        scope, eventgrid_subscription_name
    ).endpoint_url
    eventgrid_topic_key = eventgrid_mgmt_client.topics.list_shared_access_keys(
        resource_group, topic_name
    ).key1
    headers = {"aeg-sas-key": eventgrid_topic_key}
    response = requests.post(
        eventgrid_subscription_endpoint_url, data=data, headers=headers
    )
    assert response.status_code == 200
