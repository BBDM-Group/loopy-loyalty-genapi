# LoopyCard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Card ID: compressed 22 character UUID. | [optional] 
**uid** | **str** | User ID of the user the card belongs to: compressed 22 character UUID. | [optional] 
**campaign_id** | **str** | Campaign ID the card belongs to: compressed 22 character UUID. | [optional] 
**pass_status** | [**LoopyPassType**](LoopyPassType.md) | The pass status of the pass (issued, installed, removed or invalidated). | [optional] 
**operating_system** | **str** | The operating system the pass installed in. | [optional] 
**current_stamp_image** | [**LoopyStripImage**](LoopyStripImage.md) | The current stamp image. Can be used to render the stamp image in another application. | [optional] 
**total_stamps_earned** | **str** | Lifetime stamps earned. | [optional] 
**total_rewards_earned** | **str** | Lifetime rewards earned. | [optional] 
**total_rewards_redeemed** | **str** | Lifetime rewards redeemed. | [optional] 
**last_stamp_earned_date** | **str** | ISO8601 formatted date of when the last stamp was earned. | [optional] 
**current_reward_status** | **dict(str, int)** | Map of the current rewards. Key is the reward index (starting at 1), value is the quantity of rewards the customer is entitled to at this point in time. | [optional] 
**last_reward_earned_date** | **str** | ISO8601 formatted date of when the last reward was earned. | [optional] 
**last_reward_redeemed_date** | **str** | ISO8601 formatted date of when the last reward was redeemed. | [optional] 
**customer_details** | **dict(str, str)** | Contains the customer details for the card record. | [optional] 
**create_year** | **int** | Helper field for the year the card was created. | [optional] 
**create_month** | **int** | Helper field for the month the card was created. | [optional] 
**create_day** | **int** | Helper field for the day the card was created. | [optional] 
**unique_ids** | [**LoopyCardUniqueIds**](LoopyCardUniqueIds.md) | Unique IDs for the card. Can be used to engage with the card. | [optional] 
**expiry** | **str** | Optional expiry date for the card. | [optional] 
**opt_out** | **bool** | Indicates if this customer opted out from receiving Lockscreen notifications on messaging. | [optional] 
**create_time** | **str** | ISO8601 formatted date of when the card was created. | [optional] 
**update_time** | **str** | ISO8601 formatted date of when the card was last updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


