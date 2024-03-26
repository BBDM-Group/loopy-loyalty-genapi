# LoopyEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Event ID: compressed 22 character UUID. | [optional] 
**username** | **str** | Username of the user the event belongs to. | [optional] 
**campaign_id** | **str** | Campaign ID the card belongs to: compressed 22 character UUID. | [optional] 
**card_id** | **str** | Card ID of the card the event belongs to: compressed 22 character UUID. | [optional] 
**timestamp** | **str** | ISO8601 formatted date of when the event was created. | [optional] 
**event_type** | **int** | Event type (&#x60;0&#x60;:\&quot;Enrol\&quot;,&#x60;1&#x60;:\&quot;Stamp\&quot;,&#x60;2&#x60;:\&quot;ReceiveReward\&quot;,&#x60;3&#x60;:\&quot;RedeemReward\&quot;,&#x60;4&#x60;:\&quot;TapLink\&quot;,&#x60;5&#x60;:\&quot;WalletRegister\&quot;,&#x60;6&#x60;\&quot;WalletDeregister\&quot;,&#x60;7&#x60;:\&quot;AndroidPayRegister\&quot;,&#x60;8&#x60;:\&quot;DeleteCard\&quot;,&#x60;9&#x60;:\&quot;ForfeitReward\&quot;. | [optional] 
**quantity** | **int** | Quantity of the event. | [optional] 
**meta_data** | **dict(str, str)** | If the eventType is &#x60;2&#x60; (ReceiveReward) or &#x60;3&#x60; (RedeemReward), then this will contain the reward meta data. | [optional] 
**request_meta_data** | [**LoopyRequestMetaData**](LoopyRequestMetaData.md) | Request meta data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


