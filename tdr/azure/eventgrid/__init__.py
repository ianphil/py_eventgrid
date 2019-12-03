#!/usr/bin/env python
from tdr.azure import credentials, subscription_id
from azure.mgmt.eventgrid import EventGridManagementClient

eventgrid_mgmt_client = EventGridManagementClient(credentials, subscription_id)

from .eventgrid_mgmt import (
    create_eventgrid_topic,
    subscribe_http_eventgrid_topic,
    send_eventgrid_event,
)
