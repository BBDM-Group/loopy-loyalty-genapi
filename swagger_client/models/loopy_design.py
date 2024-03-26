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


class LoopyDesign(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, icon_image_id=None, logo_image_id=None, background_color=None, text_color=None):
        """
        LoopyDesign - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'icon_image_id': 'str',
            'logo_image_id': 'str',
            'background_color': 'str',
            'text_color': 'str'
        }

        self.attribute_map = {
            'icon_image_id': 'iconImageId',
            'logo_image_id': 'logoImageId',
            'background_color': 'backgroundColor',
            'text_color': 'textColor'
        }

        self._icon_image_id = icon_image_id
        self._logo_image_id = logo_image_id
        self._background_color = background_color
        self._text_color = text_color

    @property
    def icon_image_id(self):
        """
        Gets the icon_image_id of this LoopyDesign.
        Path for the icon image. Prefix with https://images.loopyloyalty.com/ to get the full image URL. The image ID is generated by the '[Create image asset](#operation/LoopyLoyalty_createImageAssets)' method.

        :return: The icon_image_id of this LoopyDesign.
        :rtype: str
        """
        return self._icon_image_id

    @icon_image_id.setter
    def icon_image_id(self, icon_image_id):
        """
        Sets the icon_image_id of this LoopyDesign.
        Path for the icon image. Prefix with https://images.loopyloyalty.com/ to get the full image URL. The image ID is generated by the '[Create image asset](#operation/LoopyLoyalty_createImageAssets)' method.

        :param icon_image_id: The icon_image_id of this LoopyDesign.
        :type: str
        """

        self._icon_image_id = icon_image_id

    @property
    def logo_image_id(self):
        """
        Gets the logo_image_id of this LoopyDesign.
        Path for the logo image. Prefix with https://images.loopyloyalty.com/ to get the full image URL. The image ID is generated by the '[Create image asset](#operation/LoopyLoyalty_createImageAssets)' method.

        :return: The logo_image_id of this LoopyDesign.
        :rtype: str
        """
        return self._logo_image_id

    @logo_image_id.setter
    def logo_image_id(self, logo_image_id):
        """
        Sets the logo_image_id of this LoopyDesign.
        Path for the logo image. Prefix with https://images.loopyloyalty.com/ to get the full image URL. The image ID is generated by the '[Create image asset](#operation/LoopyLoyalty_createImageAssets)' method.

        :param logo_image_id: The logo_image_id of this LoopyDesign.
        :type: str
        """

        self._logo_image_id = logo_image_id

    @property
    def background_color(self):
        """
        Gets the background_color of this LoopyDesign.
        Background color of the pass (in hex format: `#000000`).

        :return: The background_color of this LoopyDesign.
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """
        Sets the background_color of this LoopyDesign.
        Background color of the pass (in hex format: `#000000`).

        :param background_color: The background_color of this LoopyDesign.
        :type: str
        """

        self._background_color = background_color

    @property
    def text_color(self):
        """
        Gets the text_color of this LoopyDesign.
        Text color of the pass (in hex format: `#000000`).

        :return: The text_color of this LoopyDesign.
        :rtype: str
        """
        return self._text_color

    @text_color.setter
    def text_color(self, text_color):
        """
        Sets the text_color of this LoopyDesign.
        Text color of the pass (in hex format: `#000000`).

        :param text_color: The text_color of this LoopyDesign.
        :type: str
        """

        self._text_color = text_color

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
