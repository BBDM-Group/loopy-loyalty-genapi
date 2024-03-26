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

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.campaigns_api import CampaignsApi


class TestCampaignsApi(unittest.TestCase):
    """ CampaignsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.campaigns_api.CampaignsApi()

    def tearDown(self):
        pass

    def test_loopy_loyalty_campaign_exists(self):
        """
        Test case for loopy_loyalty_campaign_exists

        Campaign exists (by name)
        """
        pass

    def test_loopy_loyalty_create_campaign(self):
        """
        Test case for loopy_loyalty_create_campaign

        Create campaign
        """
        pass

    def test_loopy_loyalty_delete_campaign(self):
        """
        Test case for loopy_loyalty_delete_campaign

        Delete campaign
        """
        pass

    def test_loopy_loyalty_get_campaign_by_id(self):
        """
        Test case for loopy_loyalty_get_campaign_by_id

        Get campaign (by id)
        """
        pass

    def test_loopy_loyalty_get_campaign_by_name(self):
        """
        Test case for loopy_loyalty_get_campaign_by_name

        Get campaign (by name)
        """
        pass

    def test_loopy_loyalty_list_campaigns(self):
        """
        Test case for loopy_loyalty_list_campaigns

        List campaigns
        """
        pass

    def test_loopy_loyalty_push_changes_to_cards(self):
        """
        Test case for loopy_loyalty_push_changes_to_cards

        Push latest campaign changes
        """
        pass

    def test_loopy_loyalty_update_campaign(self):
        """
        Test case for loopy_loyalty_update_campaign

        Update campaign
        """
        pass


if __name__ == '__main__':
    unittest.main()