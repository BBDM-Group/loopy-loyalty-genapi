# swagger_client.CardsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loopy_loyalty_delete_card**](CardsApi.md#loopy_loyalty_delete_card) | **DELETE** /card/cid/{id}/delete | Delete card (by ID)
[**loopy_loyalty_get_card_by_id**](CardsApi.md#loopy_loyalty_get_card_by_id) | **GET** /card/{cid} | Get card (by ID)
[**loopy_loyalty_get_card_by_unique_id**](CardsApi.md#loopy_loyalty_get_card_by_unique_id) | **GET** /uniquecard/campaignid/{campaignId}/{uniqueIdType}/{uniqueIdValue} | Get card (by unique ID)
[**loopy_loyalty_list_cards**](CardsApi.md#loopy_loyalty_list_cards) | **POST** /card/cid/{cid} | List cards
[**loopy_loyalty_resync_card**](CardsApi.md#loopy_loyalty_resync_card) | **PUT** /card/cid/{cid}/resync | Re-sync card
[**loopy_loyalty_send_message_to_all_cards**](CardsApi.md#loopy_loyalty_send_message_to_all_cards) | **POST** /card/cid/{cid}/push | Send message to all cards
[**loopy_loyalty_send_message_to_individual_card**](CardsApi.md#loopy_loyalty_send_message_to_individual_card) | **POST** /card/push | Send message to an individual card


# **loopy_loyalty_delete_card**
> LoopySuccessResponse loopy_loyalty_delete_card(id, body)

Delete card (by ID)

Deletes the card with ID `{id}`. This method is irreversible and will fully delete and invalidate the card & data.

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
api_instance = swagger_client.CardsApi()
id = 'id_example' # str | The unique identifier to an object or record.
body = swagger_client.IoId() # IoId | 

try: 
    # Delete card (by ID)
    api_response = api_instance.loopy_loyalty_delete_card(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CardsApi->loopy_loyalty_delete_card: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier to an object or record. | 
 **body** | [**IoId**](IoId.md)|  | 

### Return type

[**LoopySuccessResponse**](LoopySuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_get_card_by_id**
> LoopyGetCardResponse loopy_loyalty_get_card_by_id(cid, include_events=include_events, include_rewards=include_rewards)

Get card (by ID)

Gets card with ID `{cid}`.

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
api_instance = swagger_client.CardsApi()
cid = 'cid_example' # str | Card ID. Compressed 22 character UUID.
include_events = true # bool | Includes the card events when getting the card. (optional)
include_rewards = true # bool | Includes the card rewards when getting the card. (optional)

try: 
    # Get card (by ID)
    api_response = api_instance.loopy_loyalty_get_card_by_id(cid, include_events=include_events, include_rewards=include_rewards)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CardsApi->loopy_loyalty_get_card_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| Card ID. Compressed 22 character UUID. | 
 **include_events** | **bool**| Includes the card events when getting the card. | [optional] 
 **include_rewards** | **bool**| Includes the card rewards when getting the card. | [optional] 

### Return type

[**LoopyGetCardResponse**](LoopyGetCardResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_get_card_by_unique_id**
> LoopyGetCardResponse loopy_loyalty_get_card_by_unique_id(campaign_id, unique_id_type, unique_id_value)

Get card (by unique ID)

Gets card with unique ID of `{uniqueIdType}` & `{uniqueIdValue}`.

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
api_instance = swagger_client.CardsApi()
campaign_id = 'campaign_id_example' # str | Campaign ID. Compressed 22 character UUID.
unique_id_type = 'unique_id_type_example' # str | Unique ID type; `email`, `phone` or `text`.
unique_id_value = 'unique_id_value_example' # str | Unique ID value.

try: 
    # Get card (by unique ID)
    api_response = api_instance.loopy_loyalty_get_card_by_unique_id(campaign_id, unique_id_type, unique_id_value)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CardsApi->loopy_loyalty_get_card_by_unique_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Campaign ID. Compressed 22 character UUID. | 
 **unique_id_type** | **str**| Unique ID type; &#x60;email&#x60;, &#x60;phone&#x60; or &#x60;text&#x60;. | 
 **unique_id_value** | **str**| Unique ID value. | 

### Return type

[**LoopyGetCardResponse**](LoopyGetCardResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_list_cards**
> LoopyListCardsDataTableOutput loopy_loyalty_list_cards(cid, body)

List cards

Lists all the cards for campaign with ID `{cid}`. Provide querystring ``?count=true`` to return only the count instead of the matching records. If `count=true` then you can optionally set `filter` in the request to apply an additional filter to the count.

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
api_instance = swagger_client.CardsApi()
cid = 'cid_example' # str | Campaign ID: compressed 22 character UUID.
body = swagger_client.LoopyListCardsRequest() # LoopyListCardsRequest | 

try: 
    # List cards
    api_response = api_instance.loopy_loyalty_list_cards(cid, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CardsApi->loopy_loyalty_list_cards: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| Campaign ID: compressed 22 character UUID. | 
 **body** | [**LoopyListCardsRequest**](LoopyListCardsRequest.md)|  | 

### Return type

[**LoopyListCardsDataTableOutput**](LoopyListCardsDataTableOutput.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_resync_card**
> LoopySuccessResponse loopy_loyalty_resync_card(cid, body)

Re-sync card

Resync cards with ID `{cid}` with the Mobile Wallet. This is to be used when the card in wallet does not match the card or status in the Loopy Loyalty portal.

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
api_instance = swagger_client.CardsApi()
cid = 'cid_example' # str | Card ID. Compressed 22 character UUID.
body = swagger_client.LoopyResyncCardRequest() # LoopyResyncCardRequest | 

try: 
    # Re-sync card
    api_response = api_instance.loopy_loyalty_resync_card(cid, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CardsApi->loopy_loyalty_resync_card: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| Card ID. Compressed 22 character UUID. | 
 **body** | [**LoopyResyncCardRequest**](LoopyResyncCardRequest.md)|  | 

### Return type

[**LoopySuccessResponse**](LoopySuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_send_message_to_all_cards**
> LoopySuccessResponse loopy_loyalty_send_message_to_all_cards(cid, body)

Send message to all cards

Send message to all cards for campaign with ID `{cid}`. The payload can optionally contain a filter to narrow down the cards that will receive the message.

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
api_instance = swagger_client.CardsApi()
cid = 'cid_example' # str | Campaign ID: compressed 22 character UUID.
body = swagger_client.LoopySendMessageRequest() # LoopySendMessageRequest | 

try: 
    # Send message to all cards
    api_response = api_instance.loopy_loyalty_send_message_to_all_cards(cid, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CardsApi->loopy_loyalty_send_message_to_all_cards: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| Campaign ID: compressed 22 character UUID. | 
 **body** | [**LoopySendMessageRequest**](LoopySendMessageRequest.md)|  | 

### Return type

[**LoopySuccessResponse**](LoopySuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_send_message_to_individual_card**
> LoopySuccessResponse loopy_loyalty_send_message_to_individual_card(body)

Send message to an individual card

Sends a message to an individual card.

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
api_instance = swagger_client.CardsApi()
body = swagger_client.LoopyIndividualMessageRequest() # LoopyIndividualMessageRequest | 

try: 
    # Send message to an individual card
    api_response = api_instance.loopy_loyalty_send_message_to_individual_card(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CardsApi->loopy_loyalty_send_message_to_individual_card: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoopyIndividualMessageRequest**](LoopyIndividualMessageRequest.md)|  | 

### Return type

[**LoopySuccessResponse**](LoopySuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

