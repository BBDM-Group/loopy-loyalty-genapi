# LoopyCampaignForList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Campaign ID: compressed 22 character UUID. | [optional] 
**name** | **str** | Name of the campaign. | [optional] 
**labels** | **list[str]** | Translated labels used in the campaign. [Base object to be used](https://github.com/PassKit/loopy-loyalty-rest-examples/blob/main/docs-references/labels.md). | [optional] 
**design** | [**LoopyDesign**](LoopyDesign.md) |  | [optional] 
**unique_email_field_name** | **str** | Optional field that contains the name of the data field that is used for unique email enrolments. The field name needs to exists in &#x60;campaign.fieldsToCollect&#x60;. If left blank, email is not enforced as unique. | [optional] 
**unique_phone_field_name** | **str** | Optional field that contains the name of the data field that is used for unique phone number enrolments. The field name needs to exists in &#x60;campaign.fieldsToCollect&#x60;. If left blank, phone number is not enforced as unique. | [optional] 
**unique_text_field_name** | **str** | Optional field that contains the name of the data field that is used for unique text enrolments. The field name needs to exists in &#x60;campaign.fieldsToCollect&#x60;. If left blank, text is not enforced as unique. | [optional] 
**status** | **str** | Campaign status enum. &#x60;1&#x60;: draft, &#x60;2&#x60;: published. | [optional] 
**create_time** | **str** | ISO8601 formatted create date. | [optional] 
**update_time** | **str** | ISO8601 formatted update date. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


