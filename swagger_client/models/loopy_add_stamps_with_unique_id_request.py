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

from pprint import pformat
from six import iteritems
import re


class LoopyAddStampsWithUniqueIdRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, stamps=None, scan_latitude=None, scan_longitude=None, campaign_id=None, unique_id_type=None, unique_id_value=None):
        """
        LoopyAddStampsWithUniqueIdRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'stamps': 'str',
            'scan_latitude': 'float',
            'scan_longitude': 'float',
            'campaign_id': 'str',
            'unique_id_type': 'str',
            'unique_id_value': 'str'
        }

        self.attribute_map = {
            'stamps': 'stamps',
            'scan_latitude': 'scanLatitude',
            'scan_longitude': 'scanLongitude',
            'campaign_id': 'campaignId',
            'unique_id_type': 'uniqueIdType',
            'unique_id_value': 'uniqueIdValue'
        }

        self._stamps = stamps
        self._scan_latitude = scan_latitude
        self._scan_longitude = scan_longitude
        self._campaign_id = campaign_id
        self._unique_id_type = unique_id_type
        self._unique_id_value = unique_id_value

    @property
    def stamps(self):
        """
        Gets the stamps of this LoopyAddStampsWithUniqueIdRequest.
        Number of stamps to add or deduct.

        :return: The stamps of this LoopyAddStampsWithUniqueIdRequest.
        :rtype: str
        """
        return self._stamps

    @stamps.setter
    def stamps(self, stamps):
        """
        Sets the stamps of this LoopyAddStampsWithUniqueIdRequest.
        Number of stamps to add or deduct.

        :param stamps: The stamps of this LoopyAddStampsWithUniqueIdRequest.
        :type: str
        """

        self._stamps = stamps

    @property
    def scan_latitude(self):
        """
        Gets the scan_latitude of this LoopyAddStampsWithUniqueIdRequest.
        Latitude were the scan took place.

        :return: The scan_latitude of this LoopyAddStampsWithUniqueIdRequest.
        :rtype: float
        """
        return self._scan_latitude

    @scan_latitude.setter
    def scan_latitude(self, scan_latitude):
        """
        Sets the scan_latitude of this LoopyAddStampsWithUniqueIdRequest.
        Latitude were the scan took place.

        :param scan_latitude: The scan_latitude of this LoopyAddStampsWithUniqueIdRequest.
        :type: float
        """

        self._scan_latitude = scan_latitude

    @property
    def scan_longitude(self):
        """
        Gets the scan_longitude of this LoopyAddStampsWithUniqueIdRequest.
        Longitude were the scan took place.

        :return: The scan_longitude of this LoopyAddStampsWithUniqueIdRequest.
        :rtype: float
        """
        return self._scan_longitude

    @scan_longitude.setter
    def scan_longitude(self, scan_longitude):
        """
        Sets the scan_longitude of this LoopyAddStampsWithUniqueIdRequest.
        Longitude were the scan took place.

        :param scan_longitude: The scan_longitude of this LoopyAddStampsWithUniqueIdRequest.
        :type: float
        """

        self._scan_longitude = scan_longitude

    @property
    def campaign_id(self):
        """
        Gets the campaign_id of this LoopyAddStampsWithUniqueIdRequest.
        Campaign ID. Compressed 22 character UUID.

        :return: The campaign_id of this LoopyAddStampsWithUniqueIdRequest.
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """
        Sets the campaign_id of this LoopyAddStampsWithUniqueIdRequest.
        Campaign ID. Compressed 22 character UUID.

        :param campaign_id: The campaign_id of this LoopyAddStampsWithUniqueIdRequest.
        :type: str
        """

        self._campaign_id = campaign_id

    @property
    def unique_id_type(self):
        """
        Gets the unique_id_type of this LoopyAddStampsWithUniqueIdRequest.
        Unique ID type; email, phone or text.

        :return: The unique_id_type of this LoopyAddStampsWithUniqueIdRequest.
        :rtype: str
        """
        return self._unique_id_type

    @unique_id_type.setter
    def unique_id_type(self, unique_id_type):
        """
        Sets the unique_id_type of this LoopyAddStampsWithUniqueIdRequest.
        Unique ID type; email, phone or text.

        :param unique_id_type: The unique_id_type of this LoopyAddStampsWithUniqueIdRequest.
        :type: str
        """

        self._unique_id_type = unique_id_type

    @property
    def unique_id_value(self):
        """
        Gets the unique_id_value of this LoopyAddStampsWithUniqueIdRequest.
        Unique ID value.

        :return: The unique_id_value of this LoopyAddStampsWithUniqueIdRequest.
        :rtype: str
        """
        return self._unique_id_value

    @unique_id_value.setter
    def unique_id_value(self, unique_id_value):
        """
        Sets the unique_id_value of this LoopyAddStampsWithUniqueIdRequest.
        Unique ID value.

        :param unique_id_value: The unique_id_value of this LoopyAddStampsWithUniqueIdRequest.
        :type: str
        """

        self._unique_id_value = unique_id_value

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other