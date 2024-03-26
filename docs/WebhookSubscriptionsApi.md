# swagger_client.WebhookSubscriptionsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loopy_loyalty_create_subscription**](WebhookSubscriptionsApi.md#loopy_loyalty_create_subscription) | **POST** /subscription | Create subscription
[**loopy_loyalty_delete_subscription**](WebhookSubscriptionsApi.md#loopy_loyalty_delete_subscription) | **DELETE** /subscription/{id} | Delete subscription
[**loopy_loyalty_get_sample_event**](WebhookSubscriptionsApi.md#loopy_loyalty_get_sample_event) | **GET** /subscription/{eventType}/{campaignId} | Get sample event


# **loopy_loyalty_create_subscription**
> IoId loopy_loyalty_create_subscription(body)

Create subscription

Creates a new subscription for an event in Loopy Loyalty.

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
api_instance = swagger_client.WebhookSubscriptionsApi()
body = swagger_client.LoopySubscriptionRequest() # LoopySubscriptionRequest | 

try: 
    # Create subscription
    api_response = api_instance.loopy_loyalty_create_subscription(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhookSubscriptionsApi->loopy_loyalty_create_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoopySubscriptionRequest**](LoopySubscriptionRequest.md)|  | 

### Return type

[**IoId**](IoId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_delete_subscription**
> object loopy_loyalty_delete_subscription(id, body)

Delete subscription

Deletes a subscription with ID `{id}`. The ID needs to be the same ID as returned from the create subscription method.

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
api_instance = swagger_client.WebhookSubscriptionsApi()
id = 'id_example' # str | The unique identifier to an object or record.
body = swagger_client.IoId() # IoId | 

try: 
    # Delete subscription
    api_response = api_instance.loopy_loyalty_delete_subscription(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhookSubscriptionsApi->loopy_loyalty_delete_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier to an object or record. | 
 **body** | [**IoId**](IoId.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_get_sample_event**
> LoopyEvent loopy_loyalty_get_sample_event(event_type, campaign_id)

Get sample event

Returns a sample event payload for event type `{eventType}` in campaign with ID `{campaignId}`.

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
api_instance = swagger_client.WebhookSubscriptionsApi()
event_type = 'event_type_example' # str | Event type to get the sample for.
campaign_id = 'campaign_id_example' # str | Campaign ID: compressed 22 character UUID.

try: 
    # Get sample event
    api_response = api_instance.loopy_loyalty_get_sample_event(event_type, campaign_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhookSubscriptionsApi->loopy_loyalty_get_sample_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type** | **str**| Event type to get the sample for. | 
 **campaign_id** | **str**| Campaign ID: compressed 22 character UUID. | 

### Return type

[**LoopyEvent**](LoopyEvent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

