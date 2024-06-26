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


class LoopyListEventsRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, dt=None, cid=None, count=None):
        """
        LoopyListEventsRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'dt': 'LoopyListEventsDataTableInput',
            'cid': 'str',
            'count': 'bool'
        }

        self.attribute_map = {
            'dt': 'dt',
            'cid': 'cid',
            'count': 'count'
        }

        self._dt = dt
        self._cid = cid
        self._count = count

    @property
    def dt(self):
        """
        Gets the dt of this LoopyListEventsRequest.
        Search, paging and order criteria for the query.

        :return: The dt of this LoopyListEventsRequest.
        :rtype: LoopyListEventsDataTableInput
        """
        return self._dt

    @dt.setter
    def dt(self, dt):
        """
        Sets the dt of this LoopyListEventsRequest.
        Search, paging and order criteria for the query.

        :param dt: The dt of this LoopyListEventsRequest.
        :type: LoopyListEventsDataTableInput
        """

        self._dt = dt

    @property
    def cid(self):
        """
        Gets the cid of this LoopyListEventsRequest.
        Campaign ID: compressed 22 character UUID.

        :return: The cid of this LoopyListEventsRequest.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """
        Sets the cid of this LoopyListEventsRequest.
        Campaign ID: compressed 22 character UUID.

        :param cid: The cid of this LoopyListEventsRequest.
        :type: str
        """

        self._cid = cid

    @property
    def count(self):
        """
        Gets the count of this LoopyListEventsRequest.
        Indicates if a count is returned or a list of records.

        :return: The count of this LoopyListEventsRequest.
        :rtype: bool
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this LoopyListEventsRequest.
        Indicates if a count is returned or a list of records.

        :param count: The count of this LoopyListEventsRequest.
        :type: bool
        """

        self._count = count

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
