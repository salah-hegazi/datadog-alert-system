import json
import requests

from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .models import DatadogAlert, AuthenticationKey


@csrf_exempt
@require_POST
def datadog_alert(request):
	payload_string = str(request.body.decode('utf-8'))
	payload_json = json.loads(payload_string)
	DatadogAlert.objects.create(payload = payload_json)
	return HttpResponse('Ok')


def get_api_key():
	api_key = AuthenticationKey.objects.filter(
		key_type=AuthenticationKey.API_KEY).first()
	if api_key:
		api_key = api_key.key
	return api_key


def get_application_key():
	application_key = AuthenticationKey.objects.filter(
		key_type=AuthenticationKey.APPLICATION_KEY).first()
	if application_key:
		application_key = application_key.key
	return application_key


def validate_api_key(request):
	headers = {
		'Content-Type': 'application/json',
		'DD-API-KEY': get_api_key()
		}
	url = 'https://api.datadoghq.com/api/v1/validate'
	resp = requests.get(url, headers=headers)
	message = resp.text
	if resp.status_code != 200:
		return HttpResponse(message, status=403)
	return HttpResponse(message, status=200)


def mute_monitor(request, monitor_id):
	headers = {
		'Content-Type': 'application/json',
		'DD-API-KEY': get_api_key(),
		'DD-APPLICATION-KEY': get_application_key()
		}
	url = 'https://api.datadoghq.com/api/v1/monitor/'+ monitor_id +'/mute'
	resp = requests.post(url, headers=headers)
	message = resp.text
	if resp.status_code == 200:
		return HttpResponse(message, status=200)
	elif resp.status_code == 400:
	    return HttpResponse(message, status=400)
	elif resp.status_code == 401:
	    return HttpResponse(message, status=401)
	elif resp.status_code == 404:
	    return HttpResponse(message, status=404)



def resolve_monitor(request, monitor_id, group):
	headers = {
		'Content-Type': 'application/json',
		'DD-API-KEY': get_api_key(),
		'DD-APPLICATION-KEY': get_application_key()
		}
	url = 'https://api.datadoghq.com/monitor/bulk_resolve'
	payload = {"resolve": [{monitor_id: group}]}
	payload = json.dumps(payload)
	payload = json.loads(payload)
	resp = requests.post(url, headers=headers, json=payload)
	message = resp.text
	if resp.status_code == 200:
		return HttpResponse(message, status=200)
	else:
	    return HttpResponse(message, status=401)


def list_all_monitor(request):
	headers = {
		'Content-Type': 'application/json',
		'DD-API-KEY': get_api_key(),
		'DD-APPLICATION-KEY': get_application_key()
		}
	url = 'https://api.datadoghq.com/api/v1/monitor'
	resp = requests.get(url, headers=headers)
	message = resp.text
	if resp.status_code == 200:
		return HttpResponse(message, status=200)
	elif resp.status_code == 400:
	    return HttpResponse(message, status=400)
	elif resp.status_code == 403:
	    return HttpResponse(message, status=403)

