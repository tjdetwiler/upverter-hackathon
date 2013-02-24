from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
import json


from sensors import get_sensor_server

def test(request):
    # server = get_sensor_server()
    # packets = []
    # for c in server.clients:
    #     packets.append(c.get_last_packet())

    return render_to_response(
            'sensors/summary.html',
            context_instance=RequestContext(request))

def update(request):
    server = get_sensor_server()
    packets = []
    for c in server.clients:
        packets.append(c.get_last_packets())
    
    return HttpResponse(json.dumps(packets), mimetype="application/json")

