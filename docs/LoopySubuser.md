# LoopySubuser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Subuser ID: compressed 22 character UUID. | [optional] 
**parent** | **str** | Parent user ID: compressed 22 character UUID. Readonly field; set based of the logged in user. | [optional] 
**label** | **str** | Label for the sub-user for easy recognition. | [optional] 
**location** | [**LoopyLocation**](LoopyLocation.md) | Subuser location. | [optional] 
**username** | **str** | Subuser username. | [optional] 
**password** | **str** | Subuser password - only for setting. | [optional] 
**status** | [**LoopyStatus**](LoopyStatus.md) | Subuser status. | [optional] 
**create_time** | **str** | ISO8601 formatted create date. | [optional] 
**update_time** | **str** | ISO8601 formatted update date. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


