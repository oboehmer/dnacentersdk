# -*- coding: utf-8 -*-
"""CatalystCenterAPI eox API fixtures and tests.

Copyright (c) 2025 Cisco Systems.

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
from fastjsonschema.exceptions import JsonSchemaException
from dnacentersdk.exceptions import MalformedRequest
from tests.environment import DNA_CENTER_VERSION

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '3.1.3.0', reason='version does not match')


def is_valid_get_eox_status_for_all_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_64d5d27a53ac53258fa2183b7e93a7d5_v3_1_3_0').validate(obj)
    return True


def get_eox_status_for_all_devices_v1(api):
    endpoint_result = api.eox.get_eox_status_for_all_devices_v1(
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.eox
def test_get_eox_status_for_all_devices_v1(api, validator):
    try:
        assert is_valid_get_eox_status_for_all_devices_v1(
            validator,
            get_eox_status_for_all_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_eox_status_for_all_devices_v1_default_val(api):
    endpoint_result = api.eox.get_eox_status_for_all_devices_v1(
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.eox
def test_get_eox_status_for_all_devices_v1_default_val(api, validator):
    try:
        assert is_valid_get_eox_status_for_all_devices_v1(
            validator,
            get_eox_status_for_all_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_eox_details_per_device_v1(json_schema_validate, obj):
    json_schema_validate('jsd_816ec048832853f8a63f34415d0e6fce_v3_1_3_0').validate(obj)
    return True


def get_eox_details_per_device_v1(api):
    endpoint_result = api.eox.get_eox_details_per_device_v1(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.eox
def test_get_eox_details_per_device_v1(api, validator):
    try:
        assert is_valid_get_eox_details_per_device_v1(
            validator,
            get_eox_details_per_device_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_eox_details_per_device_v1_default_val(api):
    endpoint_result = api.eox.get_eox_details_per_device_v1(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.eox
def test_get_eox_details_per_device_v1_default_val(api, validator):
    try:
        assert is_valid_get_eox_details_per_device_v1(
            validator,
            get_eox_details_per_device_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_eox_summary_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f0a0dfdaca465bdc91fc290d87476b89_v3_1_3_0').validate(obj)
    return True


def get_eox_summary_v1(api):
    endpoint_result = api.eox.get_eox_summary_v1(

    )
    return endpoint_result


@pytest.mark.eox
def test_get_eox_summary_v1(api, validator):
    try:
        assert is_valid_get_eox_summary_v1(
            validator,
            get_eox_summary_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_eox_summary_v1_default_val(api):
    endpoint_result = api.eox.get_eox_summary_v1(

    )
    return endpoint_result


@pytest.mark.eox
def test_get_eox_summary_v1_default_val(api, validator):
    try:
        assert is_valid_get_eox_summary_v1(
            validator,
            get_eox_summary_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
