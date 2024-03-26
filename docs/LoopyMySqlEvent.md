# LoopyMySqlEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Event ID: compressed 22 character UUID. | [optional] 
**card_id** | **str** | Card ID of the card the event belongs to: compressed 22 character UUID. | [optional] 
**username** | **str** | Username of the user the event belongs to. | [optional] 
**type** | **int** | Event type (&#x60;0&#x60;:\&quot;Enrol\&quot;,&#x60;1&#x60;:\&quot;Stamp\&quot;,&#x60;2&#x60;:\&quot;ReceiveReward\&quot;,&#x60;3&#x60;:\&quot;RedeemReward\&quot;,&#x60;4&#x60;:\&quot;TapLink\&quot;,&#x60;5&#x60;:\&quot;WalletRegister\&quot;,&#x60;6&#x60;\&quot;WalletDeregister\&quot;,&#x60;7&#x60;:\&quot;AndroidPayRegister\&quot;,&#x60;8&#x60;:\&quot;DeleteCard\&quot;,&#x60;9&#x60;:\&quot;ForfeitReward\&quot;. | [optional] 
**quantity** | **int** | Quantity of the event. | [optional] 
**location_name** | **str** | Location name where the reward was redeemed or earned - set in case of eventType is &#x60;2&#x60; (ReceiveReward) or &#x60;3&#x60; (RedeemReward). | [optional] 
**reward_name** | **str** | Reward name where the reward was redeemed or earned - set in case of eventType is &#x60;2&#x60; (ReceiveReward) or &#x60;3&#x60; (RedeemReward). | [optional] 
**s_lat** | **float** | Scan latitude. | [optional] 
**s_lon** | **float** | Scan longitude. | [optional] 
**ip** | **str** | IP address of the event. | [optional] 
**ua** | **str** | User agent details. | [optional] 
**referrer** | **str** | Referrer details. | [optional] 
**created** | **str** | ISO8601 formatted date of when the event was created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


