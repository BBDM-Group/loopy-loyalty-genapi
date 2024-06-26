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


class LoopyFilterCondition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, field=None, operator=None, value=None):
        """
        LoopyFilterCondition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'field': 'str',
            'operator': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'field': 'field',
            'operator': 'operator',
            'value': 'value'
        }

        self._field = field
        self._operator = operator
        self._value = value

    @property
    def field(self):
        """
        Gets the field of this LoopyFilterCondition.
        One of the valid fields to filter on. Valid values are: `currentStamps`, `totalStampsEarned`, `totalRewardsEarned`, `totalRewardsRedeemed`.

        :return: The field of this LoopyFilterCondition.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this LoopyFilterCondition.
        One of the valid fields to filter on. Valid values are: `currentStamps`, `totalStampsEarned`, `totalRewardsEarned`, `totalRewardsRedeemed`.

        :param field: The field of this LoopyFilterCondition.
        :type: str
        """

        self._field = field

    @property
    def operator(self):
        """
        Gets the operator of this LoopyFilterCondition.
        The operator to apply to the filter condition. Valid values are: `>`, `<`, `=`, `>=`, `<=`.

        :return: The operator of this LoopyFilterCondition.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this LoopyFilterCondition.
        The operator to apply to the filter condition. Valid values are: `>`, `<`, `=`, `>=`, `<=`.

        :param operator: The operator of this LoopyFilterCondition.
        :type: str
        """

        self._operator = operator

    @property
    def value(self):
        """
        Gets the value of this LoopyFilterCondition.
        The value to filter on.

        :return: The value of this LoopyFilterCondition.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this LoopyFilterCondition.
        The value to filter on.

        :param value: The value of this LoopyFilterCondition.
        :type: str
        """

        self._value = value

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
