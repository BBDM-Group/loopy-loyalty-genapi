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


class LoopyAddStampsRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cid=None, stamps=None, scan_latitude=None, scan_longitude=None):
        """
        LoopyAddStampsRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cid': 'str',
            'stamps': 'str',
            'scan_latitude': 'float',
            'scan_longitude': 'float'
        }

        self.attribute_map = {
            'cid': 'cid',
            'stamps': 'stamps',
            'scan_latitude': 'scanLatitude',
            'scan_longitude': 'scanLongitude'
        }

        self._cid = cid
        self._stamps = stamps
        self._scan_latitude = scan_latitude
        self._scan_longitude = scan_longitude

    @property
    def cid(self):
        """
        Gets the cid of this LoopyAddStampsRequest.
        Card ID. Compressed 22 character UUID. The Card ID is returned from the '[List Cards](#operation/LoopyLoyalty_listCards)' or '[Enrol customer](#operation/LoopyLoyalty_enrolMember)'.

        :return: The cid of this LoopyAddStampsRequest.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """
        Sets the cid of this LoopyAddStampsRequest.
        Card ID. Compressed 22 character UUID. The Card ID is returned from the '[List Cards](#operation/LoopyLoyalty_listCards)' or '[Enrol customer](#operation/LoopyLoyalty_enrolMember)'.

        :param cid: The cid of this LoopyAddStampsRequest.
        :type: str
        """

        self._cid = cid

    @property
    def stamps(self):
        """
        Gets the stamps of this LoopyAddStampsRequest.
        Number of stamps to add or deduct.

        :return: The stamps of this LoopyAddStampsRequest.
        :rtype: str
        """
        return self._stamps

    @stamps.setter
    def stamps(self, stamps):
        """
        Sets the stamps of this LoopyAddStampsRequest.
        Number of stamps to add or deduct.

        :param stamps: The stamps of this LoopyAddStampsRequest.
        :type: str
        """

        self._stamps = stamps

    @property
    def scan_latitude(self):
        """
        Gets the scan_latitude of this LoopyAddStampsRequest.
        Latitude were the scan took place.

        :return: The scan_latitude of this LoopyAddStampsRequest.
        :rtype: float
        """
        return self._scan_latitude

    @scan_latitude.setter
    def scan_latitude(self, scan_latitude):
        """
        Sets the scan_latitude of this LoopyAddStampsRequest.
        Latitude were the scan took place.

        :param scan_latitude: The scan_latitude of this LoopyAddStampsRequest.
        :type: float
        """

        self._scan_latitude = scan_latitude

    @property
    def scan_longitude(self):
        """
        Gets the scan_longitude of this LoopyAddStampsRequest.
        Longitude were the scan took place.

        :return: The scan_longitude of this LoopyAddStampsRequest.
        :rtype: float
        """
        return self._scan_longitude

    @scan_longitude.setter
    def scan_longitude(self, scan_longitude):
        """
        Sets the scan_longitude of this LoopyAddStampsRequest.
        Longitude were the scan took place.

        :param scan_longitude: The scan_longitude of this LoopyAddStampsRequest.
        :type: float
        """

        self._scan_longitude = scan_longitude

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