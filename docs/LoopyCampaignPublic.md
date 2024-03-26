# LoopyCampaignPublic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Campaign ID (unique). Compressed 22 character UUID. | [optional] 
**description** | **str** | Campaign description. | [optional] 
**fields_to_collect** | [**list[LoopyDataField]**](LoopyDataField.md) | Data fields that this campaign collects on enrolment. | [optional] 
**design** | [**LoopyDesign**](LoopyDesign.md) |  | [optional] 
**rewards** | [**list[LoopyReward]**](LoopyReward.md) | Array of the rewards and reward logic. | [optional] 
**terms** | **str** | Terms &amp; conditions for the campaign. | [optional] 
**disable_terms** | **bool** | Indicates if terms &amp; conditions are enabled. | [optional] 
**unique_email_field_name** | **str** | Optional field that contains the name of the data field that is used for unique email enrolments. The field name needs to exists in &#x60;campaign.fieldsToCollect&#x60;. If left blank, email is not enforced as unique. | [optional] 
**unique_phone_field_name** | **str** | Optional field that contains the name of the data field that is used for unique phone number enrolments. The field name needs to exists in &#x60;campaign.fieldsToCollect&#x60;. If left blank, phone number is not enforced as unique. | [optional] 
**unique_text_field_name** | **str** | Optional field that contains the name of the data field that is used for unique text enrolments. The field name needs to exists in &#x60;campaign.fieldsToCollect&#x60;. If left blank, text is not enforced as unique. | [optional] 
**default_country_code** | **str** | Optional default country code to be used for telephone number formatting. Country code needs to be a valid &#39;[ISO3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)&#39; code. | [optional] 
**consent_enabled** | **bool** | Indicates if data consent text is enabled. | [optional] 
**consent_text** | **str** | Data consent text for the campaign. | [optional] 
**consent_checkbox_enabled** | **bool** | Indicates if the data consent checkbox is enabled by default. | [optional] 
**labels** | **list[str]** | Translated labels used in the campaign. [Base object to be used](https://github.com/PassKit/loopy-loyalty-rest-examples/blob/main/docs-references/labels.md). | [optional] 
**business** | [**LoopyBusiness**](LoopyBusiness.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


