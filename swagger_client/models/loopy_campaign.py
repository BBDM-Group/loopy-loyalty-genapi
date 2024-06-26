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


class LoopyCampaign(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, uid=None, name=None, short_code=None, description=None, org_name=None, type=None, rewards=None, links=None, collect_value=None, locations=None, beacons=None, stamp_value=None, currency=None, expiry=None, fields_to_collect=None, design=None, base_strip_image=None, allow_push_to_passes=None, terms=None, disable_terms=None, link_to_terms=None, labels=None, custom_front_fields=None, business=None, unique_email_field_name=None, unique_phone_field_name=None, unique_text_field_name=None, default_country_code=None, consent_enabled=None, consent_text=None, consent_checkbox_enabled=None, status=None, create_time=None, update_time=None):
        """
        LoopyCampaign - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'uid': 'str',
            'name': 'str',
            'short_code': 'str',
            'description': 'str',
            'org_name': 'str',
            'type': 'LoopyCampaignType',
            'rewards': 'list[LoopyReward]',
            'links': 'list[LoopyLink]',
            'collect_value': 'str',
            'locations': 'list[LoopyLocation]',
            'beacons': 'list[LoopyBeacon]',
            'stamp_value': 'float',
            'currency': 'str',
            'expiry': 'LoopyExpiry',
            'fields_to_collect': 'LoopyDataField',
            'design': 'LoopyDesign',
            'base_strip_image': 'LoopyStripImage',
            'allow_push_to_passes': 'bool',
            'terms': 'str',
            'disable_terms': 'bool',
            'link_to_terms': 'str',
            'labels': 'list[str]',
            'custom_front_fields': 'list[LoopyCustomFrontField]',
            'business': 'LoopyBusiness',
            'unique_email_field_name': 'str',
            'unique_phone_field_name': 'str',
            'unique_text_field_name': 'str',
            'default_country_code': 'str',
            'consent_enabled': 'bool',
            'consent_text': 'str',
            'consent_checkbox_enabled': 'bool',
            'status': 'str',
            'create_time': 'str',
            'update_time': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'uid': 'uid',
            'name': 'name',
            'short_code': 'shortCode',
            'description': 'description',
            'org_name': 'orgName',
            'type': 'type',
            'rewards': 'rewards',
            'links': 'links',
            'collect_value': 'collectValue',
            'locations': 'locations',
            'beacons': 'beacons',
            'stamp_value': 'stampValue',
            'currency': 'currency',
            'expiry': 'expiry',
            'fields_to_collect': 'fieldsToCollect',
            'design': 'design',
            'base_strip_image': 'baseStripImage',
            'allow_push_to_passes': 'allowPushToPasses',
            'terms': 'terms',
            'disable_terms': 'disableTerms',
            'link_to_terms': 'linkToTerms',
            'labels': 'labels',
            'custom_front_fields': 'customFrontFields',
            'business': 'business',
            'unique_email_field_name': 'uniqueEmailFieldName',
            'unique_phone_field_name': 'uniquePhoneFieldName',
            'unique_text_field_name': 'uniqueTextFieldName',
            'default_country_code': 'defaultCountryCode',
            'consent_enabled': 'consentEnabled',
            'consent_text': 'consentText',
            'consent_checkbox_enabled': 'consentCheckboxEnabled',
            'status': 'status',
            'create_time': 'createTime',
            'update_time': 'updateTime'
        }

        self._id = id
        self._uid = uid
        self._name = name
        self._short_code = short_code
        self._description = description
        self._org_name = org_name
        self._type = type
        self._rewards = rewards
        self._links = links
        self._collect_value = collect_value
        self._locations = locations
        self._beacons = beacons
        self._stamp_value = stamp_value
        self._currency = currency
        self._expiry = expiry
        self._fields_to_collect = fields_to_collect
        self._design = design
        self._base_strip_image = base_strip_image
        self._allow_push_to_passes = allow_push_to_passes
        self._terms = terms
        self._disable_terms = disable_terms
        self._link_to_terms = link_to_terms
        self._labels = labels
        self._custom_front_fields = custom_front_fields
        self._business = business
        self._unique_email_field_name = unique_email_field_name
        self._unique_phone_field_name = unique_phone_field_name
        self._unique_text_field_name = unique_text_field_name
        self._default_country_code = default_country_code
        self._consent_enabled = consent_enabled
        self._consent_text = consent_text
        self._consent_checkbox_enabled = consent_checkbox_enabled
        self._status = status
        self._create_time = create_time
        self._update_time = update_time

    @property
    def id(self):
        """
        Gets the id of this LoopyCampaign.
        Campaign ID: compressed 22 character UUID.

        :return: The id of this LoopyCampaign.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LoopyCampaign.
        Campaign ID: compressed 22 character UUID.

        :param id: The id of this LoopyCampaign.
        :type: str
        """

        self._id = id

    @property
    def uid(self):
        """
        Gets the uid of this LoopyCampaign.
        User ID of the user the campaign belongs to:  compressed 22 character UUID; auto generated.

        :return: The uid of this LoopyCampaign.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this LoopyCampaign.
        User ID of the user the campaign belongs to:  compressed 22 character UUID; auto generated.

        :param uid: The uid of this LoopyCampaign.
        :type: str
        """

        self._uid = uid

    @property
    def name(self):
        """
        Gets the name of this LoopyCampaign.
        Name of the campaign.

        :return: The name of this LoopyCampaign.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LoopyCampaign.
        Name of the campaign.

        :param name: The name of this LoopyCampaign.
        :type: str
        """

        self._name = name

    @property
    def short_code(self):
        """
        Gets the short_code of this LoopyCampaign.
        6 character shortcode for the campaign; auto generated.

        :return: The short_code of this LoopyCampaign.
        :rtype: str
        """
        return self._short_code

    @short_code.setter
    def short_code(self, short_code):
        """
        Sets the short_code of this LoopyCampaign.
        6 character shortcode for the campaign; auto generated.

        :param short_code: The short_code of this LoopyCampaign.
        :type: str
        """

        self._short_code = short_code

    @property
    def description(self):
        """
        Gets the description of this LoopyCampaign.
        Description for the campaign.

        :return: The description of this LoopyCampaign.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LoopyCampaign.
        Description for the campaign.

        :param description: The description of this LoopyCampaign.
        :type: str
        """

        self._description = description

    @property
    def org_name(self):
        """
        Gets the org_name of this LoopyCampaign.
        The organization name; used on lockscreen messages for Apple.

        :return: The org_name of this LoopyCampaign.
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """
        Sets the org_name of this LoopyCampaign.
        The organization name; used on lockscreen messages for Apple.

        :param org_name: The org_name of this LoopyCampaign.
        :type: str
        """

        self._org_name = org_name

    @property
    def type(self):
        """
        Gets the type of this LoopyCampaign.


        :return: The type of this LoopyCampaign.
        :rtype: LoopyCampaignType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this LoopyCampaign.


        :param type: The type of this LoopyCampaign.
        :type: LoopyCampaignType
        """

        self._type = type

    @property
    def rewards(self):
        """
        Gets the rewards of this LoopyCampaign.
        Array of the rewards and reward logic.

        :return: The rewards of this LoopyCampaign.
        :rtype: list[LoopyReward]
        """
        return self._rewards

    @rewards.setter
    def rewards(self, rewards):
        """
        Sets the rewards of this LoopyCampaign.
        Array of the rewards and reward logic.

        :param rewards: The rewards of this LoopyCampaign.
        :type: list[LoopyReward]
        """

        self._rewards = rewards

    @property
    def links(self):
        """
        Gets the links of this LoopyCampaign.
        Array of links used in the campaign.

        :return: The links of this LoopyCampaign.
        :rtype: list[LoopyLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this LoopyCampaign.
        Array of links used in the campaign.

        :param links: The links of this LoopyCampaign.
        :type: list[LoopyLink]
        """

        self._links = links

    @property
    def collect_value(self):
        """
        Gets the collect_value of this LoopyCampaign.
        What customers need to do to collect a stamp.

        :return: The collect_value of this LoopyCampaign.
        :rtype: str
        """
        return self._collect_value

    @collect_value.setter
    def collect_value(self, collect_value):
        """
        Sets the collect_value of this LoopyCampaign.
        What customers need to do to collect a stamp.

        :param collect_value: The collect_value of this LoopyCampaign.
        :type: str
        """

        self._collect_value = collect_value

    @property
    def locations(self):
        """
        Gets the locations of this LoopyCampaign.
        Array of locations used in the campaign.

        :return: The locations of this LoopyCampaign.
        :rtype: list[LoopyLocation]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """
        Sets the locations of this LoopyCampaign.
        Array of locations used in the campaign.

        :param locations: The locations of this LoopyCampaign.
        :type: list[LoopyLocation]
        """

        self._locations = locations

    @property
    def beacons(self):
        """
        Gets the beacons of this LoopyCampaign.
        Array of beacons used in the campaign.

        :return: The beacons of this LoopyCampaign.
        :rtype: list[LoopyBeacon]
        """
        return self._beacons

    @beacons.setter
    def beacons(self, beacons):
        """
        Sets the beacons of this LoopyCampaign.
        Array of beacons used in the campaign.

        :param beacons: The beacons of this LoopyCampaign.
        :type: list[LoopyBeacon]
        """

        self._beacons = beacons

    @property
    def stamp_value(self):
        """
        Gets the stamp_value of this LoopyCampaign.
        The value that equals one stamp.

        :return: The stamp_value of this LoopyCampaign.
        :rtype: float
        """
        return self._stamp_value

    @stamp_value.setter
    def stamp_value(self, stamp_value):
        """
        Sets the stamp_value of this LoopyCampaign.
        The value that equals one stamp.

        :param stamp_value: The stamp_value of this LoopyCampaign.
        :type: float
        """

        self._stamp_value = stamp_value

    @property
    def currency(self):
        """
        Gets the currency of this LoopyCampaign.
        The currency of the stamp value.

        :return: The currency of this LoopyCampaign.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this LoopyCampaign.
        The currency of the stamp value.

        :param currency: The currency of this LoopyCampaign.
        :type: str
        """

        self._currency = currency

    @property
    def expiry(self):
        """
        Gets the expiry of this LoopyCampaign.


        :return: The expiry of this LoopyCampaign.
        :rtype: LoopyExpiry
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """
        Sets the expiry of this LoopyCampaign.


        :param expiry: The expiry of this LoopyCampaign.
        :type: LoopyExpiry
        """

        self._expiry = expiry

    @property
    def fields_to_collect(self):
        """
        Gets the fields_to_collect of this LoopyCampaign.


        :return: The fields_to_collect of this LoopyCampaign.
        :rtype: LoopyDataField
        """
        return self._fields_to_collect

    @fields_to_collect.setter
    def fields_to_collect(self, fields_to_collect):
        """
        Sets the fields_to_collect of this LoopyCampaign.


        :param fields_to_collect: The fields_to_collect of this LoopyCampaign.
        :type: LoopyDataField
        """

        self._fields_to_collect = fields_to_collect

    @property
    def design(self):
        """
        Gets the design of this LoopyCampaign.


        :return: The design of this LoopyCampaign.
        :rtype: LoopyDesign
        """
        return self._design

    @design.setter
    def design(self, design):
        """
        Sets the design of this LoopyCampaign.


        :param design: The design of this LoopyCampaign.
        :type: LoopyDesign
        """

        self._design = design

    @property
    def base_strip_image(self):
        """
        Gets the base_strip_image of this LoopyCampaign.


        :return: The base_strip_image of this LoopyCampaign.
        :rtype: LoopyStripImage
        """
        return self._base_strip_image

    @base_strip_image.setter
    def base_strip_image(self, base_strip_image):
        """
        Sets the base_strip_image of this LoopyCampaign.


        :param base_strip_image: The base_strip_image of this LoopyCampaign.
        :type: LoopyStripImage
        """

        self._base_strip_image = base_strip_image

    @property
    def allow_push_to_passes(self):
        """
        Gets the allow_push_to_passes of this LoopyCampaign.
        Indicates if pushes are allowed for passes in this campaign.

        :return: The allow_push_to_passes of this LoopyCampaign.
        :rtype: bool
        """
        return self._allow_push_to_passes

    @allow_push_to_passes.setter
    def allow_push_to_passes(self, allow_push_to_passes):
        """
        Sets the allow_push_to_passes of this LoopyCampaign.
        Indicates if pushes are allowed for passes in this campaign.

        :param allow_push_to_passes: The allow_push_to_passes of this LoopyCampaign.
        :type: bool
        """

        self._allow_push_to_passes = allow_push_to_passes

    @property
    def terms(self):
        """
        Gets the terms of this LoopyCampaign.
        Terms & conditions for the campaign.

        :return: The terms of this LoopyCampaign.
        :rtype: str
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """
        Sets the terms of this LoopyCampaign.
        Terms & conditions for the campaign.

        :param terms: The terms of this LoopyCampaign.
        :type: str
        """

        self._terms = terms

    @property
    def disable_terms(self):
        """
        Gets the disable_terms of this LoopyCampaign.
        Indicates if terms & conditions are enabled.

        :return: The disable_terms of this LoopyCampaign.
        :rtype: bool
        """
        return self._disable_terms

    @disable_terms.setter
    def disable_terms(self, disable_terms):
        """
        Sets the disable_terms of this LoopyCampaign.
        Indicates if terms & conditions are enabled.

        :param disable_terms: The disable_terms of this LoopyCampaign.
        :type: bool
        """

        self._disable_terms = disable_terms

    @property
    def link_to_terms(self):
        """
        Gets the link_to_terms of this LoopyCampaign.
        Optional link to the terms & conditions.

        :return: The link_to_terms of this LoopyCampaign.
        :rtype: str
        """
        return self._link_to_terms

    @link_to_terms.setter
    def link_to_terms(self, link_to_terms):
        """
        Sets the link_to_terms of this LoopyCampaign.
        Optional link to the terms & conditions.

        :param link_to_terms: The link_to_terms of this LoopyCampaign.
        :type: str
        """

        self._link_to_terms = link_to_terms

    @property
    def labels(self):
        """
        Gets the labels of this LoopyCampaign.
        Translated labels used in the campaign. [Base object to be used](https://github.com/PassKit/loopy-loyalty-rest-examples/blob/main/docs-references/labels.md).

        :return: The labels of this LoopyCampaign.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this LoopyCampaign.
        Translated labels used in the campaign. [Base object to be used](https://github.com/PassKit/loopy-loyalty-rest-examples/blob/main/docs-references/labels.md).

        :param labels: The labels of this LoopyCampaign.
        :type: list[str]
        """

        self._labels = labels

    @property
    def custom_front_fields(self):
        """
        Gets the custom_front_fields of this LoopyCampaign.


        :return: The custom_front_fields of this LoopyCampaign.
        :rtype: list[LoopyCustomFrontField]
        """
        return self._custom_front_fields

    @custom_front_fields.setter
    def custom_front_fields(self, custom_front_fields):
        """
        Sets the custom_front_fields of this LoopyCampaign.


        :param custom_front_fields: The custom_front_fields of this LoopyCampaign.
        :type: list[LoopyCustomFrontField]
        """

        self._custom_front_fields = custom_front_fields

    @property
    def business(self):
        """
        Gets the business of this LoopyCampaign.


        :return: The business of this LoopyCampaign.
        :rtype: LoopyBusiness
        """
        return self._business

    @business.setter
    def business(self, business):
        """
        Sets the business of this LoopyCampaign.


        :param business: The business of this LoopyCampaign.
        :type: LoopyBusiness
        """

        self._business = business

    @property
    def unique_email_field_name(self):
        """
        Gets the unique_email_field_name of this LoopyCampaign.
        Optional field that contains the name of the data field that is used for unique email enrolments. The field name needs to exists in `campaign.fieldsToCollect`. If left blank, email is not enforced as unique.

        :return: The unique_email_field_name of this LoopyCampaign.
        :rtype: str
        """
        return self._unique_email_field_name

    @unique_email_field_name.setter
    def unique_email_field_name(self, unique_email_field_name):
        """
        Sets the unique_email_field_name of this LoopyCampaign.
        Optional field that contains the name of the data field that is used for unique email enrolments. The field name needs to exists in `campaign.fieldsToCollect`. If left blank, email is not enforced as unique.

        :param unique_email_field_name: The unique_email_field_name of this LoopyCampaign.
        :type: str
        """

        self._unique_email_field_name = unique_email_field_name

    @property
    def unique_phone_field_name(self):
        """
        Gets the unique_phone_field_name of this LoopyCampaign.
        Optional field that contains the name of the data field that is used for unique phone number enrolments. The field name needs to exists in `campaign.fieldsToCollect`. If left blank, phone number is not enforced as unique.

        :return: The unique_phone_field_name of this LoopyCampaign.
        :rtype: str
        """
        return self._unique_phone_field_name

    @unique_phone_field_name.setter
    def unique_phone_field_name(self, unique_phone_field_name):
        """
        Sets the unique_phone_field_name of this LoopyCampaign.
        Optional field that contains the name of the data field that is used for unique phone number enrolments. The field name needs to exists in `campaign.fieldsToCollect`. If left blank, phone number is not enforced as unique.

        :param unique_phone_field_name: The unique_phone_field_name of this LoopyCampaign.
        :type: str
        """

        self._unique_phone_field_name = unique_phone_field_name

    @property
    def unique_text_field_name(self):
        """
        Gets the unique_text_field_name of this LoopyCampaign.
        Optional field that contains the name of the data field that is used for unique text enrolments. The field name needs to exists in `campaign.fieldsToCollect`. If left blank, text is not enforced as unique.

        :return: The unique_text_field_name of this LoopyCampaign.
        :rtype: str
        """
        return self._unique_text_field_name

    @unique_text_field_name.setter
    def unique_text_field_name(self, unique_text_field_name):
        """
        Sets the unique_text_field_name of this LoopyCampaign.
        Optional field that contains the name of the data field that is used for unique text enrolments. The field name needs to exists in `campaign.fieldsToCollect`. If left blank, text is not enforced as unique.

        :param unique_text_field_name: The unique_text_field_name of this LoopyCampaign.
        :type: str
        """

        self._unique_text_field_name = unique_text_field_name

    @property
    def default_country_code(self):
        """
        Gets the default_country_code of this LoopyCampaign.
        Default country code to be used for telephone number formatting.

        :return: The default_country_code of this LoopyCampaign.
        :rtype: str
        """
        return self._default_country_code

    @default_country_code.setter
    def default_country_code(self, default_country_code):
        """
        Sets the default_country_code of this LoopyCampaign.
        Default country code to be used for telephone number formatting.

        :param default_country_code: The default_country_code of this LoopyCampaign.
        :type: str
        """

        self._default_country_code = default_country_code

    @property
    def consent_enabled(self):
        """
        Gets the consent_enabled of this LoopyCampaign.
        Indicates if data consent text is enabled.

        :return: The consent_enabled of this LoopyCampaign.
        :rtype: bool
        """
        return self._consent_enabled

    @consent_enabled.setter
    def consent_enabled(self, consent_enabled):
        """
        Sets the consent_enabled of this LoopyCampaign.
        Indicates if data consent text is enabled.

        :param consent_enabled: The consent_enabled of this LoopyCampaign.
        :type: bool
        """

        self._consent_enabled = consent_enabled

    @property
    def consent_text(self):
        """
        Gets the consent_text of this LoopyCampaign.
        Data consent text for the campaign.

        :return: The consent_text of this LoopyCampaign.
        :rtype: str
        """
        return self._consent_text

    @consent_text.setter
    def consent_text(self, consent_text):
        """
        Sets the consent_text of this LoopyCampaign.
        Data consent text for the campaign.

        :param consent_text: The consent_text of this LoopyCampaign.
        :type: str
        """

        self._consent_text = consent_text

    @property
    def consent_checkbox_enabled(self):
        """
        Gets the consent_checkbox_enabled of this LoopyCampaign.
        Indicates if the data consent checkbox is enabled by default.

        :return: The consent_checkbox_enabled of this LoopyCampaign.
        :rtype: bool
        """
        return self._consent_checkbox_enabled

    @consent_checkbox_enabled.setter
    def consent_checkbox_enabled(self, consent_checkbox_enabled):
        """
        Sets the consent_checkbox_enabled of this LoopyCampaign.
        Indicates if the data consent checkbox is enabled by default.

        :param consent_checkbox_enabled: The consent_checkbox_enabled of this LoopyCampaign.
        :type: bool
        """

        self._consent_checkbox_enabled = consent_checkbox_enabled

    @property
    def status(self):
        """
        Gets the status of this LoopyCampaign.
        Campaign status enum. `1`: draft, `2`: published.

        :return: The status of this LoopyCampaign.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this LoopyCampaign.
        Campaign status enum. `1`: draft, `2`: published.

        :param status: The status of this LoopyCampaign.
        :type: str
        """

        self._status = status

    @property
    def create_time(self):
        """
        Gets the create_time of this LoopyCampaign.
        ISO8601 formatted create date.

        :return: The create_time of this LoopyCampaign.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this LoopyCampaign.
        ISO8601 formatted create date.

        :param create_time: The create_time of this LoopyCampaign.
        :type: str
        """

        self._create_time = create_time

    @property
    def update_time(self):
        """
        Gets the update_time of this LoopyCampaign.
        ISO8601 formatted update date.

        :return: The update_time of this LoopyCampaign.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """
        Sets the update_time of this LoopyCampaign.
        ISO8601 formatted update date.

        :param update_time: The update_time of this LoopyCampaign.
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
