# swagger_client.ReportingApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loopy_loyalty_export_campaign**](ReportingApi.md#loopy_loyalty_export_campaign) | **POST** /export/{id} | Export campaign
[**loopy_loyalty_list_events_for_campaign**](ReportingApi.md#loopy_loyalty_list_events_for_campaign) | **POST** /events/analytics/transactions/{cid} | List events for campaign


# **loopy_loyalty_export_campaign**
> LoopySuccessResponse loopy_loyalty_export_campaign(id, body)

Export campaign

Exports the campaign with ID `{id}` to CSV. The user will received an email in their registered account email with CSV link upon completion. Can export either transactions or customers.

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
api_instance = swagger_client.ReportingApi()
id = 'id_example' # str | Campaign ID: compressed 22 character UUID.
body = swagger_client.LoopyCampaignExportRequest() # LoopyCampaignExportRequest | 

try: 
    # Export campaign
    api_response = api_instance.loopy_loyalty_export_campaign(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReportingApi->loopy_loyalty_export_campaign: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Campaign ID: compressed 22 character UUID. | 
 **body** | [**LoopyCampaignExportRequest**](LoopyCampaignExportRequest.md)|  | 

### Return type

[**LoopySuccessResponse**](LoopySuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_list_events_for_campaign**
> LoopyListEventsDataTableOutput loopy_loyalty_list_events_for_campaign(cid, body)

List events for campaign

Lists all the events for campaign with ID `{cid}`. Provide querystring `?count=true` to return only the count instead of the matching records.

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
api_instance = swagger_client.ReportingApi()
cid = 'cid_example' # str | Campaign ID: compressed 22 character UUID.
body = swagger_client.LoopyListEventsRequest() # LoopyListEventsRequest | 

try: 
    # List events for campaign
    api_response = api_instance.loopy_loyalty_list_events_for_campaign(cid, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReportingApi->loopy_loyalty_list_events_for_campaign: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| Campaign ID: compressed 22 character UUID. | 
 **body** | [**LoopyListEventsRequest**](LoopyListEventsRequest.md)|  | 

### Return type

[**LoopyListEventsDataTableOutput**](LoopyListEventsDataTableOutput.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

