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


class LoopyCustomFrontField(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, label=None, field_to_display=None):
        """
        LoopyCustomFrontField - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'label': 'str',
            'field_to_display': 'str'
        }

        self.attribute_map = {
            'label': 'label',
            'field_to_display': 'fieldToDisplay'
        }

        self._label = label
        self._field_to_display = field_to_display

    @property
    def label(self):
        """
        Gets the label of this LoopyCustomFrontField.
        Label to be used for the custom front field.

        :return: The label of this LoopyCustomFrontField.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this LoopyCustomFrontField.
        Label to be used for the custom front field.

        :param label: The label of this LoopyCustomFrontField.
        :type: str
        """

        self._label = label

    @property
    def field_to_display(self):
        """
        Gets the field_to_display of this LoopyCustomFrontField.
        Stamp field to display on the front of the card. `stampsRequiredForNextReward`, `lifetimeStamps`, or any data field name from the `campaign.fieldsToCollect` array.

        :return: The field_to_display of this LoopyCustomFrontField.
        :rtype: str
        """
        return self._field_to_display

    @field_to_display.setter
    def field_to_display(self, field_to_display):
        """
        Sets the field_to_display of this LoopyCustomFrontField.
        Stamp field to display on the front of the card. `stampsRequiredForNextReward`, `lifetimeStamps`, or any data field name from the `campaign.fieldsToCollect` array.

        :param field_to_display: The field_to_display of this LoopyCustomFrontField.
        :type: str
        """

        self._field_to_display = field_to_display

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
