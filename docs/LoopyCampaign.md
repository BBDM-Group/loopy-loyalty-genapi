# LoopyCampaign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Campaign ID: compressed 22 character UUID. | [optional] 
**uid** | **str** | User ID of the user the campaign belongs to:  compressed 22 character UUID; auto generated. | [optional] 
**name** | **str** | Name of the campaign. | [optional] 
**short_code** | **str** | 6 character shortcode for the campaign; auto generated. | [optional] 
**description** | **str** | Description for the campaign. | [optional] 
**org_name** | **str** | The organization name; used on lockscreen messages for Apple. | [optional] 
**type** | [**LoopyCampaignType**](LoopyCampaignType.md) |  | [optional] 
**rewards** | [**list[LoopyReward]**](LoopyReward.md) | Array of the rewards and reward logic. | [optional] 
**links** | [**list[LoopyLink]**](LoopyLink.md) | Array of links used in the campaign. | [optional] 
**collect_value** | **str** | What customers need to do to collect a stamp. | [optional] 
**locations** | [**list[LoopyLocation]**](LoopyLocation.md) | Array of locations used in the campaign. | [optional] 
**beacons** | [**list[LoopyBeacon]**](LoopyBeacon.md) | Array of beacons used in the campaign. | [optional] 
**stamp_value** | **float** | The value that equals one stamp. | [optional] 
**currency** | **str** | The currency of the stamp value. | [optional] 
**expiry** | [**LoopyExpiry**](LoopyExpiry.md) |  | [optional] 
**fields_to_collect** | [**LoopyDataField**](LoopyDataField.md) |  | [optional] 
**design** | [**LoopyDesign**](LoopyDesign.md) |  | [optional] 
**base_strip_image** | [**LoopyStripImage**](LoopyStripImage.md) |  | [optional] 
**allow_push_to_passes** | **bool** | Indicates if pushes are allowed for passes in this campaign. | [optional] 
**terms** | **str** | Terms &amp; conditions for the campaign. | [optional] 
**disable_terms** | **bool** | Indicates if terms &amp; conditions are enabled. | [optional] 
**link_to_terms** | **str** | Optional link to the terms &amp; conditions. | [optional] 
**labels** | **list[str]** | Translated labels used in the campaign. [Base object to be used](https://github.com/PassKit/loopy-loyalty-rest-examples/blob/main/docs-references/labels.md). | [optional] 
**custom_front_fields** | [**list[LoopyCustomFrontField]**](LoopyCustomFrontField.md) |  | [optional] 
**business** | [**LoopyBusiness**](LoopyBusiness.md) |  | [optional] 
**unique_email_field_name** | **str** | Optional field that contains the name of the data field that is used for unique email enrolments. The field name needs to exists in &#x60;campaign.fieldsToCollect&#x60;. If left blank, email is not enforced as unique. | [optional] 
**unique_phone_field_name** | **str** | Optional field that contains the name of the data field that is used for unique phone number enrolments. The field name needs to exists in &#x60;campaign.fieldsToCollect&#x60;. If left blank, phone number is not enforced as unique. | [optional] 
**unique_text_field_name** | **str** | Optional field that contains the name of the data field that is used for unique text enrolments. The field name needs to exists in &#x60;campaign.fieldsToCollect&#x60;. If left blank, text is not enforced as unique. | [optional] 
**default_country_code** | **str** | Default country code to be used for telephone number formatting. | [optional] 
**consent_enabled** | **bool** | Indicates if data consent text is enabled. | [optional] 
**consent_text** | **str** | Data consent text for the campaign. | [optional] 
**consent_checkbox_enabled** | **bool** | Indicates if the data consent checkbox is enabled by default. | [optional] 
**status** | **str** | Campaign status enum. &#x60;1&#x60;: draft, &#x60;2&#x60;: published. | [optional] 
**create_time** | **str** | ISO8601 formatted create date. | [optional] 
**update_time** | **str** | ISO8601 formatted update date. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


