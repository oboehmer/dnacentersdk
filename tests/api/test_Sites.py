# -*- coding: utf-8 -*-
"""DNACenterAPI sites API fixtures and tests.

Copyright (c) 2019 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import pytest
import dnacentersdk




# 17a8-2ac9-4cf9-9ab0
def is_valid_get_site_health(obj):
    some_keys = ['executionId', 'executionStatusUrl', 'message']
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_site_health(api):
    endpoint_result = api.sites.get_site_health( param_timestamp = '1562604696', payload = '' )
    return endpoint_result


def test_get_site_health(api):
    assert is_valid_get_site_health(get_site_health(api))


# 50b5-89fd-4c7a-930a
def is_valid_create_site(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def create_site(api):
    endpoint_result = api.sites.create_site( rq_site = None, rq_type = None, payload = '' )
    return endpoint_result


def test_create_site(api):
    assert is_valid_create_site(create_site(api))


# eeb1-68eb-4198-8e07
def is_valid_assign_device_to_site(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def assign_device_to_site(api):
    endpoint_result = api.sites.assign_device_to_site( path_param_site_id = '', rq_device = None, payload = '' )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_assign_device_to_site(api):
    assert is_valid_assign_device_to_site(assign_device_to_site(api))

