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


class LoopyEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, username=None, campaign_id=None, card_id=None, timestamp=None, event_type=None, quantity=None, meta_data=None, request_meta_data=None):
        """
        LoopyEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'username': 'str',
            'campaign_id': 'str',
            'card_id': 'str',
            'timestamp': 'str',
            'event_type': 'int',
            'quantity': 'int',
            'meta_data': 'dict(str, str)',
            'request_meta_data': 'LoopyRequestMetaData'
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username',
            'campaign_id': 'campaignId',
            'card_id': 'cardId',
            'timestamp': 'timestamp',
            'event_type': 'eventType',
            'quantity': 'quantity',
            'meta_data': 'metaData',
            'request_meta_data': 'requestMetaData'
        }

        self._id = id
        self._username = username
        self._campaign_id = campaign_id
        self._card_id = card_id
        self._timestamp = timestamp
        self._event_type = event_type
        self._quantity = quantity
        self._meta_data = meta_data
        self._request_meta_data = request_meta_data

    @property
    def id(self):
        """
        Gets the id of this LoopyEvent.
        Event ID: compressed 22 character UUID.

        :return: The id of this LoopyEvent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LoopyEvent.
        Event ID: compressed 22 character UUID.

        :param id: The id of this LoopyEvent.
        :type: str
        """

        self._id = id

    @property
    def username(self):
        """
        Gets the username of this LoopyEvent.
        Username of the user the event belongs to.

        :return: The username of this LoopyEvent.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this LoopyEvent.
        Username of the user the event belongs to.

        :param username: The username of this LoopyEvent.
        :type: str
        """

        self._username = username

    @property
    def campaign_id(self):
        """
        Gets the campaign_id of this LoopyEvent.
        Campaign ID the card belongs to: compressed 22 character UUID.

        :return: The campaign_id of this LoopyEvent.
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """
        Sets the campaign_id of this LoopyEvent.
        Campaign ID the card belongs to: compressed 22 character UUID.

        :param campaign_id: The campaign_id of this LoopyEvent.
        :type: str
        """

        self._campaign_id = campaign_id

    @property
    def card_id(self):
        """
        Gets the card_id of this LoopyEvent.
        Card ID of the card the event belongs to: compressed 22 character UUID.

        :return: The card_id of this LoopyEvent.
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        """
        Sets the card_id of this LoopyEvent.
        Card ID of the card the event belongs to: compressed 22 character UUID.

        :param card_id: The card_id of this LoopyEvent.
        :type: str
        """

        self._card_id = card_id

    @property
    def timestamp(self):
        """
        Gets the timestamp of this LoopyEvent.
        ISO8601 formatted date of when the event was created.

        :return: The timestamp of this LoopyEvent.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this LoopyEvent.
        ISO8601 formatted date of when the event was created.

        :param timestamp: The timestamp of this LoopyEvent.
        :type: str
        """

        self._timestamp = timestamp

    @property
    def event_type(self):
        """
        Gets the event_type of this LoopyEvent.
        Event type (`0`:\"Enrol\",`1`:\"Stamp\",`2`:\"ReceiveReward\",`3`:\"RedeemReward\",`4`:\"TapLink\",`5`:\"WalletRegister\",`6`\"WalletDeregister\",`7`:\"AndroidPayRegister\",`8`:\"DeleteCard\",`9`:\"ForfeitReward\".

        :return: The event_type of this LoopyEvent.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this LoopyEvent.
        Event type (`0`:\"Enrol\",`1`:\"Stamp\",`2`:\"ReceiveReward\",`3`:\"RedeemReward\",`4`:\"TapLink\",`5`:\"WalletRegister\",`6`\"WalletDeregister\",`7`:\"AndroidPayRegister\",`8`:\"DeleteCard\",`9`:\"ForfeitReward\".

        :param event_type: The event_type of this LoopyEvent.
        :type: int
        """

        self._event_type = event_type

    @property
    def quantity(self):
        """
        Gets the quantity of this LoopyEvent.
        Quantity of the event.

        :return: The quantity of this LoopyEvent.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this LoopyEvent.
        Quantity of the event.

        :param quantity: The quantity of this LoopyEvent.
        :type: int
        """

        self._quantity = quantity

    @property
    def meta_data(self):
        """
        Gets the meta_data of this LoopyEvent.
        If the eventType is `2` (ReceiveReward) or `3` (RedeemReward), then this will contain the reward meta data.

        :return: The meta_data of this LoopyEvent.
        :rtype: dict(str, str)
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """
        Sets the meta_data of this LoopyEvent.
        If the eventType is `2` (ReceiveReward) or `3` (RedeemReward), then this will contain the reward meta data.

        :param meta_data: The meta_data of this LoopyEvent.
        :type: dict(str, str)
        """

        self._meta_data = meta_data

    @property
    def request_meta_data(self):
        """
        Gets the request_meta_data of this LoopyEvent.
        Request meta data.

        :return: The request_meta_data of this LoopyEvent.
        :rtype: LoopyRequestMetaData
        """
        return self._request_meta_data

    @request_meta_data.setter
    def request_meta_data(self, request_meta_data):
        """
        Sets the request_meta_data of this LoopyEvent.
        Request meta data.

        :param request_meta_data: The request_meta_data of this LoopyEvent.
        :type: LoopyRequestMetaData
        """

        self._request_meta_data = request_meta_data

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
