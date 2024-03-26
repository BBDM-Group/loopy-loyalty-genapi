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


class StampsRewardsApi(object):
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

    def loopy_loyalty_add_stamps(self, cid, stamps, body, **kwargs):
        """
        Add stamps (by card ID)
        Add number of `{stamps}` to the card with ID `{cid}`. {stamps} can be negative to deduct stamps.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.loopy_loyalty_add_stamps(cid, stamps, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str cid: Card ID. Compressed 22 character UUID. The Card ID is returned from the '[List Cards](#operation/LoopyLoyalty_listCards)' or '[Enrol customer](#operation/LoopyLoyalty_enrolMember)'. (required)
        :param str stamps: Number of stamps to add or deduct. (required)
        :param LoopyAddStampsRequest body:  (required)
        :return: LoopySuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.loopy_loyalty_add_stamps_with_http_info(cid, stamps, body, **kwargs)
        else:
            (data) = self.loopy_loyalty_add_stamps_with_http_info(cid, stamps, body, **kwargs)
            return data

    def loopy_loyalty_add_stamps_with_http_info(self, cid, stamps, body, **kwargs):
        """
        Add stamps (by card ID)
        Add number of `{stamps}` to the card with ID `{cid}`. {stamps} can be negative to deduct stamps.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.loopy_loyalty_add_stamps_with_http_info(cid, stamps, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str cid: Card ID. Compressed 22 character UUID. The Card ID is returned from the '[List Cards](#operation/LoopyLoyalty_listCards)' or '[Enrol customer](#operation/LoopyLoyalty_enrolMember)'. (required)
        :param str stamps: Number of stamps to add or deduct. (required)
        :param LoopyAddStampsRequest body:  (required)
        :return: LoopySuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cid', 'stamps', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method loopy_loyalty_add_stamps" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cid' is set
        if ('cid' not in params) or (params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `loopy_loyalty_add_stamps`")
        # verify the required parameter 'stamps' is set
        if ('stamps' not in params) or (params['stamps'] is None):
            raise ValueError("Missing the required parameter `stamps` when calling `loopy_loyalty_add_stamps`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `loopy_loyalty_add_stamps`")

        resource_path = '/card/cid/{cid}/addStamps/{stamps}'.replace('{format}', 'json')
        path_params = {}
        if 'cid' in params:
            path_params['cid'] = params['cid']
        if 'stamps' in params:
            path_params['stamps'] = params['stamps']

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
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='LoopySuccessResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def loopy_loyalty_add_stamps_by_unique_card_field(self, campaign_id, unique_id_type, unique_id_value, stamps, body, **kwargs):
        """
        Add stamps (by unique card data field)
        Add number of `{stamps}` to the card with `{uniqueIdType}` & `{uniqueIdValue}`. `{stamps}` can be negative to deduct stamps. Use this method when you do not know the card ID but want to stamp with your own unique identifier that is known in your system (i.e. email, member ID, mobile number, etc).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.loopy_loyalty_add_stamps_by_unique_card_field(campaign_id, unique_id_type, unique_id_value, stamps, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: Campaign ID. Compressed 22 character UUID. (required)
        :param str unique_id_type: Unique ID type; email, phone or text. (required)
        :param str unique_id_value: Unique ID value. (required)
        :param str stamps: Number of stamps to add or deduct. (required)
        :param LoopyAddStampsWithUniqueIdRequest body:  (required)
        :return: LoopySuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.loopy_loyalty_add_stamps_by_unique_card_field_with_http_info(campaign_id, unique_id_type, unique_id_value, stamps, body, **kwargs)
        else:
            (data) = self.loopy_loyalty_add_stamps_by_unique_card_field_with_http_info(campaign_id, unique_id_type, unique_id_value, stamps, body, **kwargs)
            return data

    def loopy_loyalty_add_stamps_by_unique_card_field_with_http_info(self, campaign_id, unique_id_type, unique_id_value, stamps, body, **kwargs):
        """
        Add stamps (by unique card data field)
        Add number of `{stamps}` to the card with `{uniqueIdType}` & `{uniqueIdValue}`. `{stamps}` can be negative to deduct stamps. Use this method when you do not know the card ID but want to stamp with your own unique identifier that is known in your system (i.e. email, member ID, mobile number, etc).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.loopy_loyalty_add_stamps_by_unique_card_field_with_http_info(campaign_id, unique_id_type, unique_id_value, stamps, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: Campaign ID. Compressed 22 character UUID. (required)
        :param str unique_id_type: Unique ID type; email, phone or text. (required)
        :param str unique_id_value: Unique ID value. (required)
        :param str stamps: Number of stamps to add or deduct. (required)
        :param LoopyAddStampsWithUniqueIdRequest body:  (required)
        :return: LoopySuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'unique_id_type', 'unique_id_value', 'stamps', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method loopy_loyalty_add_stamps_by_unique_card_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params) or (params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `loopy_loyalty_add_stamps_by_unique_card_field`")
        # verify the required parameter 'unique_id_type' is set
        if ('unique_id_type' not in params) or (params['unique_id_type'] is None):
            raise ValueError("Missing the required parameter `unique_id_type` when calling `loopy_loyalty_add_stamps_by_unique_card_field`")
        # verify the required parameter 'unique_id_value' is set
        if ('unique_id_value' not in params) or (params['unique_id_value'] is None):
            raise ValueError("Missing the required parameter `unique_id_value` when calling `loopy_loyalty_add_stamps_by_unique_card_field`")
        # verify the required parameter 'stamps' is set
        if ('stamps' not in params) or (params['stamps'] is None):
            raise ValueError("Missing the required parameter `stamps` when calling `loopy_loyalty_add_stamps_by_unique_card_field`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `loopy_loyalty_add_stamps_by_unique_card_field`")

        resource_path = '/uniquecard/campaignid/{campaignId}/{uniqueIdType}/{uniqueIdValue}/addStamps/{stamps}'.replace('{format}', 'json')
        path_params = {}
        if 'campaign_id' in params:
            path_params['campaignId'] = params['campaign_id']
        if 'unique_id_type' in params:
            path_params['uniqueIdType'] = params['unique_id_type']
        if 'unique_id_value' in params:
            path_params['uniqueIdValue'] = params['unique_id_value']
        if 'stamps' in params:
            path_params['stamps'] = params['stamps']

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
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='LoopySuccessResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def loopy_loyalty_redeem_reward(self, cid, reward_type, rewards_to_redeem, body, **kwargs):
        """
        Redeem Rewards (by card ID)
        Redeems the number of rewards `{rewardsToRedeem}` of reward type `{rewardType}` for the card with ID `{cid}`. `{rewardType}` is the index of the reward number (i.e. first reward = 1, second reward = 2, etc).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.loopy_loyalty_redeem_reward(cid, reward_type, rewards_to_redeem, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str cid: Card ID. Compressed 22 character UUID. The Card ID is returned from the '[List Cards](#operation/LoopyLoyalty_listCards)' or '[Enrol customer](#operation/LoopyLoyalty_enrolMember)'. (required)
        :param str reward_type: Reward type to redeem; index of the reward number (i.e. first reward = 1, second reward = 2, etc). (required)
        :param str rewards_to_redeem: Number of reward to redeem. (required)
        :param LoopyRedeemRewardsRequest body:  (required)
        :return: LoopySuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.loopy_loyalty_redeem_reward_with_http_info(cid, reward_type, rewards_to_redeem, body, **kwargs)
        else:
            (data) = self.loopy_loyalty_redeem_reward_with_http_info(cid, reward_type, rewards_to_redeem, body, **kwargs)
            return data

    def loopy_loyalty_redeem_reward_with_http_info(self, cid, reward_type, rewards_to_redeem, body, **kwargs):
        """
        Redeem Rewards (by card ID)
        Redeems the number of rewards `{rewardsToRedeem}` of reward type `{rewardType}` for the card with ID `{cid}`. `{rewardType}` is the index of the reward number (i.e. first reward = 1, second reward = 2, etc).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.loopy_loyalty_redeem_reward_with_http_info(cid, reward_type, rewards_to_redeem, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str cid: Card ID. Compressed 22 character UUID. The Card ID is returned from the '[List Cards](#operation/LoopyLoyalty_listCards)' or '[Enrol customer](#operation/LoopyLoyalty_enrolMember)'. (required)
        :param str reward_type: Reward type to redeem; index of the reward number (i.e. first reward = 1, second reward = 2, etc). (required)
        :param str rewards_to_redeem: Number of reward to redeem. (required)
        :param LoopyRedeemRewardsRequest body:  (required)
        :return: LoopySuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cid', 'reward_type', 'rewards_to_redeem', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method loopy_loyalty_redeem_reward" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cid' is set
        if ('cid' not in params) or (params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `loopy_loyalty_redeem_reward`")
        # verify the required parameter 'reward_type' is set
        if ('reward_type' not in params) or (params['reward_type'] is None):
            raise ValueError("Missing the required parameter `reward_type` when calling `loopy_loyalty_redeem_reward`")
        # verify the required parameter 'rewards_to_redeem' is set
        if ('rewards_to_redeem' not in params) or (params['rewards_to_redeem'] is None):
            raise ValueError("Missing the required parameter `rewards_to_redeem` when calling `loopy_loyalty_redeem_reward`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `loopy_loyalty_redeem_reward`")

        resource_path = '/card/cid/{cid}/redeemReward/{rewardType}/{rewardsToRedeem}'.replace('{format}', 'json')
        path_params = {}
        if 'cid' in params:
            path_params['cid'] = params['cid']
        if 'reward_type' in params:
            path_params['rewardType'] = params['reward_type']
        if 'rewards_to_redeem' in params:
            path_params['rewardsToRedeem'] = params['rewards_to_redeem']

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
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='LoopySuccessResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def loopy_loyalty_redeem_reward_by_unique_card_field(self, campaign_id, unique_id_type, unique_id_value, reward_type, rewards_to_redeem, body, **kwargs):
        """
        Redeem Rewards (by unique card data field)
        Redeems the number of rewards `{rewardsToRedeem}` of reward type `{rewardType}` for the card with `{uniqueIdType}` & `{uniqueIdValue}`. `{rewardType}` is the index of the reward number (i.e. first reward = 1, second reward = 2, etc). Use this method when you do not know the card ID but want to redeem with your own unique identifier that is known in your system (i.e. email, member ID, mobile number, etc).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.loopy_loyalty_redeem_reward_by_unique_card_field(campaign_id, unique_id_type, unique_id_value, reward_type, rewards_to_redeem, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: Campaign ID. Compressed 22 character UUID. (required)
        :param str unique_id_type: Unique ID type; email, phone or text. (required)
        :param str unique_id_value: Unique ID value. (required)
        :param str reward_type: Reward type to redeem; index of the reward number (i.e. first reward = 1, second reward = 2, etc). (required)
        :param str rewards_to_redeem: Number of reward to redeem. (required)
        :param LoopyRedeemRewardsWithUniqueIdRequest body:  (required)
        :return: LoopySuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.loopy_loyalty_redeem_reward_by_unique_card_field_with_http_info(campaign_id, unique_id_type, unique_id_value, reward_type, rewards_to_redeem, body, **kwargs)
        else:
            (data) = self.loopy_loyalty_redeem_reward_by_unique_card_field_with_http_info(campaign_id, unique_id_type, unique_id_value, reward_type, rewards_to_redeem, body, **kwargs)
            return data

    def loopy_loyalty_redeem_reward_by_unique_card_field_with_http_info(self, campaign_id, unique_id_type, unique_id_value, reward_type, rewards_to_redeem, body, **kwargs):
        """
        Redeem Rewards (by unique card data field)
        Redeems the number of rewards `{rewardsToRedeem}` of reward type `{rewardType}` for the card with `{uniqueIdType}` & `{uniqueIdValue}`. `{rewardType}` is the index of the reward number (i.e. first reward = 1, second reward = 2, etc). Use this method when you do not know the card ID but want to redeem with your own unique identifier that is known in your system (i.e. email, member ID, mobile number, etc).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.loopy_loyalty_redeem_reward_by_unique_card_field_with_http_info(campaign_id, unique_id_type, unique_id_value, reward_type, rewards_to_redeem, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: Campaign ID. Compressed 22 character UUID. (required)
        :param str unique_id_type: Unique ID type; email, phone or text. (required)
        :param str unique_id_value: Unique ID value. (required)
        :param str reward_type: Reward type to redeem; index of the reward number (i.e. first reward = 1, second reward = 2, etc). (required)
        :param str rewards_to_redeem: Number of reward to redeem. (required)
        :param LoopyRedeemRewardsWithUniqueIdRequest body:  (required)
        :return: LoopySuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'unique_id_type', 'unique_id_value', 'reward_type', 'rewards_to_redeem', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method loopy_loyalty_redeem_reward_by_unique_card_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params) or (params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `loopy_loyalty_redeem_reward_by_unique_card_field`")
        # verify the required parameter 'unique_id_type' is set
        if ('unique_id_type' not in params) or (params['unique_id_type'] is None):
            raise ValueError("Missing the required parameter `unique_id_type` when calling `loopy_loyalty_redeem_reward_by_unique_card_field`")
        # verify the required parameter 'unique_id_value' is set
        if ('unique_id_value' not in params) or (params['unique_id_value'] is None):
            raise ValueError("Missing the required parameter `unique_id_value` when calling `loopy_loyalty_redeem_reward_by_unique_card_field`")
        # verify the required parameter 'reward_type' is set
        if ('reward_type' not in params) or (params['reward_type'] is None):
            raise ValueError("Missing the required parameter `reward_type` when calling `loopy_loyalty_redeem_reward_by_unique_card_field`")
        # verify the required parameter 'rewards_to_redeem' is set
        if ('rewards_to_redeem' not in params) or (params['rewards_to_redeem'] is None):
            raise ValueError("Missing the required parameter `rewards_to_redeem` when calling `loopy_loyalty_redeem_reward_by_unique_card_field`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `loopy_loyalty_redeem_reward_by_unique_card_field`")

        resource_path = '/uniquecard/campaignid/{campaignId}/{uniqueIdType}/{uniqueIdValue}/redeemReward/{rewardType}/{rewardsToRedeem}'.replace('{format}', 'json')
        path_params = {}
        if 'campaign_id' in params:
            path_params['campaignId'] = params['campaign_id']
        if 'unique_id_type' in params:
            path_params['uniqueIdType'] = params['unique_id_type']
        if 'unique_id_value' in params:
            path_params['uniqueIdValue'] = params['unique_id_value']
        if 'reward_type' in params:
            path_params['rewardType'] = params['reward_type']
        if 'rewards_to_redeem' in params:
            path_params['rewardsToRedeem'] = params['rewards_to_redeem']

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
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='LoopySuccessResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
