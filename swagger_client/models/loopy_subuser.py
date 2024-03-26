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


class LoopySubuser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, parent=None, label=None, location=None, username=None, password=None, status=None, create_time=None, update_time=None):
        """
        LoopySubuser - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'parent': 'str',
            'label': 'str',
            'location': 'LoopyLocation',
            'username': 'str',
            'password': 'str',
            'status': 'LoopyStatus',
            'create_time': 'str',
            'update_time': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'parent': 'parent',
            'label': 'label',
            'location': 'location',
            'username': 'username',
            'password': 'password',
            'status': 'status',
            'create_time': 'createTime',
            'update_time': 'updateTime'
        }

        self._id = id
        self._parent = parent
        self._label = label
        self._location = location
        self._username = username
        self._password = password
        self._status = status
        self._create_time = create_time
        self._update_time = update_time

    @property
    def id(self):
        """
        Gets the id of this LoopySubuser.
        Subuser ID: compressed 22 character UUID.

        :return: The id of this LoopySubuser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LoopySubuser.
        Subuser ID: compressed 22 character UUID.

        :param id: The id of this LoopySubuser.
        :type: str
        """

        self._id = id

    @property
    def parent(self):
        """
        Gets the parent of this LoopySubuser.
        Parent user ID: compressed 22 character UUID. Readonly field; set based of the logged in user.

        :return: The parent of this LoopySubuser.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this LoopySubuser.
        Parent user ID: compressed 22 character UUID. Readonly field; set based of the logged in user.

        :param parent: The parent of this LoopySubuser.
        :type: str
        """

        self._parent = parent

    @property
    def label(self):
        """
        Gets the label of this LoopySubuser.
        Label for the sub-user for easy recognition.

        :return: The label of this LoopySubuser.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this LoopySubuser.
        Label for the sub-user for easy recognition.

        :param label: The label of this LoopySubuser.
        :type: str
        """

        self._label = label

    @property
    def location(self):
        """
        Gets the location of this LoopySubuser.
        Subuser location.

        :return: The location of this LoopySubuser.
        :rtype: LoopyLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this LoopySubuser.
        Subuser location.

        :param location: The location of this LoopySubuser.
        :type: LoopyLocation
        """

        self._location = location

    @property
    def username(self):
        """
        Gets the username of this LoopySubuser.
        Subuser username.

        :return: The username of this LoopySubuser.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this LoopySubuser.
        Subuser username.

        :param username: The username of this LoopySubuser.
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """
        Gets the password of this LoopySubuser.
        Subuser password - only for setting.

        :return: The password of this LoopySubuser.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this LoopySubuser.
        Subuser password - only for setting.

        :param password: The password of this LoopySubuser.
        :type: str
        """

        self._password = password

    @property
    def status(self):
        """
        Gets the status of this LoopySubuser.
        Subuser status.

        :return: The status of this LoopySubuser.
        :rtype: LoopyStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this LoopySubuser.
        Subuser status.

        :param status: The status of this LoopySubuser.
        :type: LoopyStatus
        """

        self._status = status

    @property
    def create_time(self):
        """
        Gets the create_time of this LoopySubuser.
        ISO8601 formatted create date.

        :return: The create_time of this LoopySubuser.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this LoopySubuser.
        ISO8601 formatted create date.

        :param create_time: The create_time of this LoopySubuser.
        :type: str
        """

        self._create_time = create_time

    @property
    def update_time(self):
        """
        Gets the update_time of this LoopySubuser.
        ISO8601 formatted update date.

        :return: The update_time of this LoopySubuser.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """
        Sets the update_time of this LoopySubuser.
        ISO8601 formatted update date.

        :param update_time: The update_time of this LoopySubuser.
        :type: str
        """

        self._update_time = update_time

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
