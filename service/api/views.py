# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from decimal import *
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from datetime import timedelta
from django.conf import settings
import json
REDIS_CONNECTION = settings.REDIS_CONNECTION

# Create your views here.

@api_view(['GET', 'POST', 'PUT'])
def user_rates_view(request, *args, **kwargs):
    key_name = kwargs.get("user")
    if request.method == 'GET':
        if key_name:
            key_value = REDIS_CONNECTION.get(key_name)
            if key_value != None:
                msg = "Key '%s' was found !" % key_name
                response = {
                    'msg': "Key '%s' was found !" % key_name,
                    'value': float(key_value)
                }
                status = 200
            else:
                response = {
                    'msg': "Key '%s' was NOT found !" % key_name,
                }
                status = 404
        else:
            values={}
            for key in REDIS_CONNECTION.keys("*"):
                values[key.decode("utf-8")] = float(REDIS_CONNECTION.get(key))

            if values:
                msg = "Found %s items" % len(values)
            else:
                msg = "No values found"
            response = {
                'msg': msg,
                'values': values
            }
            status = 200
        return Response(response, status=status)

    elif request.method == 'POST':
        if request.body:
            items = json.loads(request.body)
            i = 0
            for k in items.keys():
                value = items.get(k)
                REDIS_CONNECTION.set(k, value)
                i += 1
            response = {
                'msg': "Value successfully stored"
            }
            return Response(response, 201)
        else:
            response = {
                'msg': "No data are given"
            }
            return Response(response, 404)

    elif request.method == 'PUT':
        request_data = json.loads(request.body)
        i = 0
        for key_ in request_data:
            new_value = request_data[key_]
            old_value = REDIS_CONNECTION.get(key_)
            if old_value:
                REDIS_CONNECTION.set(key_, new_value)
                i += 1
        if i > 0:
            msg = "Successfully updated %s values" % i
            response = {
                'msg': msg
            }
            return Response(response, status=200)

        else:
            response = {
                'msg': 'Keys does not exist!'
            }
            return Response(response, status=404)

@api_view(['GET'])
def agv_rating_view(request, *args, **kwargs):
    items_count = 0
    summ = 0
    for key in REDIS_CONNECTION.scan_iter("*"):
        summ = summ + float(REDIS_CONNECTION.get(key))
        items_count = items_count + 1

    result = 0
    if items_count > 0 :
        result = summ/items_count

    response = {
        'msg': "Average rating has been calculated",
        'rating': result,
        'users_count': items_count
    }
    return Response(response, status=200)
