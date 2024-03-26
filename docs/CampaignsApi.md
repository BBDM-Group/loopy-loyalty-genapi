# swagger_client.CampaignsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loopy_loyalty_campaign_exists**](CampaignsApi.md#loopy_loyalty_campaign_exists) | **GET** /campaign/exists/{name} | Campaign exists (by name)
[**loopy_loyalty_create_campaign**](CampaignsApi.md#loopy_loyalty_create_campaign) | **POST** /campaign | Create campaign
[**loopy_loyalty_delete_campaign**](CampaignsApi.md#loopy_loyalty_delete_campaign) | **DELETE** /campaign/{id} | Delete campaign
[**loopy_loyalty_get_campaign_by_id**](CampaignsApi.md#loopy_loyalty_get_campaign_by_id) | **GET** /campaign/id/{id} | Get campaign (by id)
[**loopy_loyalty_get_campaign_by_name**](CampaignsApi.md#loopy_loyalty_get_campaign_by_name) | **GET** /campaign/name/{name} | Get campaign (by name)
[**loopy_loyalty_list_campaigns**](CampaignsApi.md#loopy_loyalty_list_campaigns) | **GET** /campaigns | List campaigns
[**loopy_loyalty_push_changes_to_cards**](CampaignsApi.md#loopy_loyalty_push_changes_to_cards) | **POST** /campaign/{id}/push | Push latest campaign changes
[**loopy_loyalty_update_campaign**](CampaignsApi.md#loopy_loyalty_update_campaign) | **PATCH** /campaign/{id} | Update campaign


# **loopy_loyalty_campaign_exists**
> LoopyCampaignExistsResponse loopy_loyalty_campaign_exists(name)

Campaign exists (by name)

Checks if a campaign with name `{name}` exists.

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
api_instance = swagger_client.CampaignsApi()
name = 'name_example' # str | Name of the campaign

try: 
    # Campaign exists (by name)
    api_response = api_instance.loopy_loyalty_campaign_exists(name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CampaignsApi->loopy_loyalty_campaign_exists: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the campaign | 

### Return type

[**LoopyCampaignExistsResponse**](LoopyCampaignExistsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_create_campaign**
> IoId loopy_loyalty_create_campaign(body)

Create campaign

Creates a new campaign (card design).

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
api_instance = swagger_client.CampaignsApi()
body = swagger_client.LoopyCampaign() # LoopyCampaign | 

try: 
    # Create campaign
    api_response = api_instance.loopy_loyalty_create_campaign(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CampaignsApi->loopy_loyalty_create_campaign: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoopyCampaign**](LoopyCampaign.md)|  | 

### Return type

[**IoId**](IoId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_delete_campaign**
> LoopySuccessResponse loopy_loyalty_delete_campaign(id, body)

Delete campaign

Deletes the campaign with ID `{id}`. This method is irreversible and will fully delete and invalidate all cards and data in the campaign.

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
api_instance = swagger_client.CampaignsApi()
id = 'id_example' # str | The unique identifier to an object or record.
body = swagger_client.IoId() # IoId | 

try: 
    # Delete campaign
    api_response = api_instance.loopy_loyalty_delete_campaign(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CampaignsApi->loopy_loyalty_delete_campaign: %s\n" % e
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

# **loopy_loyalty_get_campaign_by_id**
> LoopyCampaign loopy_loyalty_get_campaign_by_id(id)

Get campaign (by id)

Gets the campaign with ID `{id}`.

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
api_instance = swagger_client.CampaignsApi()
id = 'id_example' # str | The unique identifier to an object or record.

try: 
    # Get campaign (by id)
    api_response = api_instance.loopy_loyalty_get_campaign_by_id(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CampaignsApi->loopy_loyalty_get_campaign_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier to an object or record. | 

### Return type

[**LoopyCampaign**](LoopyCampaign.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_get_campaign_by_name**
> LoopyCampaign loopy_loyalty_get_campaign_by_name(name)

Get campaign (by name)

Gets the campaign with name `{name}`.

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
api_instance = swagger_client.CampaignsApi()
name = 'name_example' # str | Name of the campaign

try: 
    # Get campaign (by name)
    api_response = api_instance.loopy_loyalty_get_campaign_by_name(name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CampaignsApi->loopy_loyalty_get_campaign_by_name: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the campaign | 

### Return type

[**LoopyCampaign**](LoopyCampaign.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_list_campaigns**
> LoopyListCampaignsResponse loopy_loyalty_list_campaigns()

List campaigns

Lists all the campaigns for the user.

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
api_instance = swagger_client.CampaignsApi()

try: 
    # List campaigns
    api_response = api_instance.loopy_loyalty_list_campaigns()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CampaignsApi->loopy_loyalty_list_campaigns: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoopyListCampaignsResponse**](LoopyListCampaignsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_push_changes_to_cards**
> LoopySuccessResponse loopy_loyalty_push_changes_to_cards(id, body)

Push latest campaign changes

Pushes the latest campaign and design changes to all existing cards in the campaign with ID `{id}`. This method can only be executed every 10 minutes.

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
api_instance = swagger_client.CampaignsApi()
id = 'id_example' # str | The unique identifier to an object or record.
body = swagger_client.IoId() # IoId | 

try: 
    # Push latest campaign changes
    api_response = api_instance.loopy_loyalty_push_changes_to_cards(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CampaignsApi->loopy_loyalty_push_changes_to_cards: %s\n" % e
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

# **loopy_loyalty_update_campaign**
> LoopyCampaign loopy_loyalty_update_campaign(id, body)

Update campaign

Updates an existing campaign with ID `{id}`.

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
api_instance = swagger_client.CampaignsApi()
id = 'id_example' # str | Campaign ID: compressed 22 character UUID.
body = swagger_client.LoopyCampaign() # LoopyCampaign | 

try: 
    # Update campaign
    api_response = api_instance.loopy_loyalty_update_campaign(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CampaignsApi->loopy_loyalty_update_campaign: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Campaign ID: compressed 22 character UUID. | 
 **body** | [**LoopyCampaign**](LoopyCampaign.md)|  | 

### Return type

[**LoopyCampaign**](LoopyCampaign.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

