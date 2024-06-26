# coding: utf-8

"""
    Loopy Loyalty API

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    Contact: support@loopyloyalty.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class EnrolmentApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def loopy_loyalty_enrol_member(self, campaign_id, body, **kwargs):
        """
        Enrol customer (public)
        Enrols a new customer into the loyalty program with ID `{campaignId}`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.loopy_loyalty_enrol_member(campaign_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: The ID of the campaign. The Loopy Loyalty campaign ID can be found in the URL bar when looking at the campaign overview (https://app.loopyloyalty.com/overview/{campaignId}). (required)
        :param LoopyEnrolCustomerRequest body:  (required)
        :return: LoopyEnrolCustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.loopy_loyalty_enrol_member_with_http_info(campaign_id, body, **kwargs)
        else:
            (data) = self.loopy_loyalty_enrol_member_with_http_info(campaign_id, body, **kwargs)
            return data

    def loopy_loyalty_enrol_member_with_http_info(self, campaign_id, body, **kwargs):
        """
        Enrol customer (public)
        Enrols a new customer into the loyalty program with ID `{campaignId}`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.loopy_loyalty_enrol_member_with_http_info(campaign_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: The ID of the campaign. The Loopy Loyalty campaign ID can be found in the URL bar when looking at the campaign overview (https://app.loopyloyalty.com/overview/{campaignId}). (required)
        :param LoopyEnrolCustomerRequest body:  (required)
        :return: LoopyEnrolCustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method loopy_loyalty_enrol_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params) or (params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `loopy_loyalty_enrol_member`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `loopy_loyalty_enrol_member`")

        resource_path = '/enrol/{campaignId}'.replace('{format}', 'json')
        path_params = {}
        if 'campaign_id' in params:
            path_params['campaignId'] = params['campaign_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='LoopyEnrolCustomerResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def loopy_loyalty_get_campaign_public(self, id, **kwargs):
        """
        Get campaign (public)
        Gets the campaign details for campaign with `{id}`. Can be used to render a custom enrolment page.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.loopy_loyalty_get_campaign_public(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The unique identifier to an object or record. (required)
        :return: LoopyCampaignPublic
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.loopy_loyalty_get_campaign_public_with_http_info(id, **kwargs)
        else:
            (data) = self.loopy_loyalty_get_campaign_public_with_http_info(id, **kwargs)
            return data

    def loopy_loyalty_get_campaign_public_with_http_info(self, id, **kwargs):
        """
        Get campaign (public)
        Gets the campaign details for campaign with `{id}`. Can be used to render a custom enrolment page.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.loopy_loyalty_get_campaign_public_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The unique identifier to an object or record. (required)
        :return: LoopyCampaignPublic
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method loopy_loyalty_get_campaign_public" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `loopy_loyalty_get_campaign_public`")

        resource_path = '/campaign/public/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='LoopyCampaignPublic',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
