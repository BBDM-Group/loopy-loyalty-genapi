# swagger_client.StampsRewardsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loopy_loyalty_add_stamps**](StampsRewardsApi.md#loopy_loyalty_add_stamps) | **POST** /card/cid/{cid}/addStamps/{stamps} | Add stamps (by card ID)
[**loopy_loyalty_add_stamps_by_unique_card_field**](StampsRewardsApi.md#loopy_loyalty_add_stamps_by_unique_card_field) | **POST** /uniquecard/campaignid/{campaignId}/{uniqueIdType}/{uniqueIdValue}/addStamps/{stamps} | Add stamps (by unique card data field)
[**loopy_loyalty_redeem_reward**](StampsRewardsApi.md#loopy_loyalty_redeem_reward) | **POST** /card/cid/{cid}/redeemReward/{rewardType}/{rewardsToRedeem} | Redeem Rewards (by card ID)
[**loopy_loyalty_redeem_reward_by_unique_card_field**](StampsRewardsApi.md#loopy_loyalty_redeem_reward_by_unique_card_field) | **POST** /uniquecard/campaignid/{campaignId}/{uniqueIdType}/{uniqueIdValue}/redeemReward/{rewardType}/{rewardsToRedeem} | Redeem Rewards (by unique card data field)


# **loopy_loyalty_add_stamps**
> LoopySuccessResponse loopy_loyalty_add_stamps(cid, stamps, body)

Add stamps (by card ID)

Add number of `{stamps}` to the card with ID `{cid}`. {stamps} can be negative to deduct stamps.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StampsRewardsApi()
cid = 'cid_example' # str | Card ID. Compressed 22 character UUID. The Card ID is returned from the '[List Cards](#operation/LoopyLoyalty_listCards)' or '[Enrol customer](#operation/LoopyLoyalty_enrolMember)'.
stamps = 'stamps_example' # str | Number of stamps to add or deduct.
body = swagger_client.LoopyAddStampsRequest() # LoopyAddStampsRequest | 

try: 
    # Add stamps (by card ID)
    api_response = api_instance.loopy_loyalty_add_stamps(cid, stamps, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StampsRewardsApi->loopy_loyalty_add_stamps: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| Card ID. Compressed 22 character UUID. The Card ID is returned from the &#39;[List Cards](#operation/LoopyLoyalty_listCards)&#39; or &#39;[Enrol customer](#operation/LoopyLoyalty_enrolMember)&#39;. | 
 **stamps** | **str**| Number of stamps to add or deduct. | 
 **body** | [**LoopyAddStampsRequest**](LoopyAddStampsRequest.md)|  | 

### Return type

[**LoopySuccessResponse**](LoopySuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_add_stamps_by_unique_card_field**
> LoopySuccessResponse loopy_loyalty_add_stamps_by_unique_card_field(campaign_id, unique_id_type, unique_id_value, stamps, body)

Add stamps (by unique card data field)

Add number of `{stamps}` to the card with `{uniqueIdType}` & `{uniqueIdValue}`. `{stamps}` can be negative to deduct stamps. Use this method when you do not know the card ID but want to stamp with your own unique identifier that is known in your system (i.e. email, member ID, mobile number, etc).

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StampsRewardsApi()
campaign_id = 'campaign_id_example' # str | Campaign ID. Compressed 22 character UUID.
unique_id_type = 'unique_id_type_example' # str | Unique ID type; email, phone or text.
unique_id_value = 'unique_id_value_example' # str | Unique ID value.
stamps = 'stamps_example' # str | Number of stamps to add or deduct.
body = swagger_client.LoopyAddStampsWithUniqueIdRequest() # LoopyAddStampsWithUniqueIdRequest | 

try: 
    # Add stamps (by unique card data field)
    api_response = api_instance.loopy_loyalty_add_stamps_by_unique_card_field(campaign_id, unique_id_type, unique_id_value, stamps, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StampsRewardsApi->loopy_loyalty_add_stamps_by_unique_card_field: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Campaign ID. Compressed 22 character UUID. | 
 **unique_id_type** | **str**| Unique ID type; email, phone or text. | 
 **unique_id_value** | **str**| Unique ID value. | 
 **stamps** | **str**| Number of stamps to add or deduct. | 
 **body** | [**LoopyAddStampsWithUniqueIdRequest**](LoopyAddStampsWithUniqueIdRequest.md)|  | 

### Return type

[**LoopySuccessResponse**](LoopySuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_redeem_reward**
> LoopySuccessResponse loopy_loyalty_redeem_reward(cid, reward_type, rewards_to_redeem, body)

Redeem Rewards (by card ID)

Redeems the number of rewards `{rewardsToRedeem}` of reward type `{rewardType}` for the card with ID `{cid}`. `{rewardType}` is the index of the reward number (i.e. first reward = 1, second reward = 2, etc).

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StampsRewardsApi()
cid = 'cid_example' # str | Card ID. Compressed 22 character UUID. The Card ID is returned from the '[List Cards](#operation/LoopyLoyalty_listCards)' or '[Enrol customer](#operation/LoopyLoyalty_enrolMember)'.
reward_type = 'reward_type_example' # str | Reward type to redeem; index of the reward number (i.e. first reward = 1, second reward = 2, etc).
rewards_to_redeem = 'rewards_to_redeem_example' # str | Number of reward to redeem.
body = swagger_client.LoopyRedeemRewardsRequest() # LoopyRedeemRewardsRequest | 

try: 
    # Redeem Rewards (by card ID)
    api_response = api_instance.loopy_loyalty_redeem_reward(cid, reward_type, rewards_to_redeem, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StampsRewardsApi->loopy_loyalty_redeem_reward: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| Card ID. Compressed 22 character UUID. The Card ID is returned from the &#39;[List Cards](#operation/LoopyLoyalty_listCards)&#39; or &#39;[Enrol customer](#operation/LoopyLoyalty_enrolMember)&#39;. | 
 **reward_type** | **str**| Reward type to redeem; index of the reward number (i.e. first reward &#x3D; 1, second reward &#x3D; 2, etc). | 
 **rewards_to_redeem** | **str**| Number of reward to redeem. | 
 **body** | [**LoopyRedeemRewardsRequest**](LoopyRedeemRewardsRequest.md)|  | 

### Return type

[**LoopySuccessResponse**](LoopySuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_redeem_reward_by_unique_card_field**
> LoopySuccessResponse loopy_loyalty_redeem_reward_by_unique_card_field(campaign_id, unique_id_type, unique_id_value, reward_type, rewards_to_redeem, body)

Redeem Rewards (by unique card data field)

Redeems the number of rewards `{rewardsToRedeem}` of reward type `{rewardType}` for the card with `{uniqueIdType}` & `{uniqueIdValue}`. `{rewardType}` is the index of the reward number (i.e. first reward = 1, second reward = 2, etc). Use this method when you do not know the card ID but want to redeem with your own unique identifier that is known in your system (i.e. email, member ID, mobile number, etc).

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StampsRewardsApi()
campaign_id = 'campaign_id_example' # str | Campaign ID. Compressed 22 character UUID.
unique_id_type = 'unique_id_type_example' # str | Unique ID type; email, phone or text.
unique_id_value = 'unique_id_value_example' # str | Unique ID value.
reward_type = 'reward_type_example' # str | Reward type to redeem; index of the reward number (i.e. first reward = 1, second reward = 2, etc).
rewards_to_redeem = 'rewards_to_redeem_example' # str | Number of reward to redeem.
body = swagger_client.LoopyRedeemRewardsWithUniqueIdRequest() # LoopyRedeemRewardsWithUniqueIdRequest | 

try: 
    # Redeem Rewards (by unique card data field)
    api_response = api_instance.loopy_loyalty_redeem_reward_by_unique_card_field(campaign_id, unique_id_type, unique_id_value, reward_type, rewards_to_redeem, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StampsRewardsApi->loopy_loyalty_redeem_reward_by_unique_card_field: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Campaign ID. Compressed 22 character UUID. | 
 **unique_id_type** | **str**| Unique ID type; email, phone or text. | 
 **unique_id_value** | **str**| Unique ID value. | 
 **reward_type** | **str**| Reward type to redeem; index of the reward number (i.e. first reward &#x3D; 1, second reward &#x3D; 2, etc). | 
 **rewards_to_redeem** | **str**| Number of reward to redeem. | 
 **body** | [**LoopyRedeemRewardsWithUniqueIdRequest**](LoopyRedeemRewardsWithUniqueIdRequest.md)|  | 

### Return type

[**LoopySuccessResponse**](LoopySuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

