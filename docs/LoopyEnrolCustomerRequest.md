# LoopyEnrolCustomerRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **str** | The ID of the campaign. The Loopy Loyalty campaign ID can be found in the URL bar when looking at the campaign overview (https://app.loopyloyalty.com/overview/{campaignId}). | [optional] 
**customer_data** | **dict(str, str)** | A dictionary of customer data. The dictionary keys are the fields names set in the description column in the &#39;[Edit design data](http://docs.loopyloyalty.com/en/articles/932782-data-collection-and-customer-information)&#39; section of the portal. | [optional] 
**data_consent_opt_in** | **bool** | If the campaign has &#x60;consentEnabled &#x3D; true&#x60;, then we respect the dataConsentOptIn boolean for new members. If this field is not set on the campaign, then all new members will default to opted in. | [optional] 
**time_zone_offset** | **str** | Applicable to campaigns that have expiry settings. Will apply the timezone offset to the expiry date. Defaults to UTC if omitted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


