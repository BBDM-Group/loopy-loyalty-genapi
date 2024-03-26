# LoopyListEventsDataTableInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | Initial paging row start number, 0 based: i.e. 0 for the first row, 10 for the 11th row, etc. | [optional] 
**length** | **str** | Number of rows to return. | [optional] 
**search** | **str** | A search term that is applied to username field of the event. The search value is prepended an appended with a wildcard; meaning it will return all event records where the username contains &#x60;{search}&#x60;. i.e. providing &#x60;{search}&#x60; &#x3D; Peter will return all card records that contain the term Peter in the username. | [optional] 
**order** | [**LoopyListEventsOrder**](LoopyListEventsOrder.md) | The order to apply to the query. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


