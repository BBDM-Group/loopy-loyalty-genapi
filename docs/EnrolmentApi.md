# swagger_client.EnrolmentApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loopy_loyalty_enrol_member**](EnrolmentApi.md#loopy_loyalty_enrol_member) | **POST** /enrol/{campaignId} | Enrol customer (public)
[**loopy_loyalty_get_campaign_public**](EnrolmentApi.md#loopy_loyalty_get_campaign_public) | **GET** /campaign/public/{id} | Get campaign (public)


# **loopy_loyalty_enrol_member**
> LoopyEnrolCustomerResponse loopy_loyalty_enrol_member(campaign_id, body)

Enrol customer (public)

Enrols a new customer into the loyalty program with ID `{campaignId}`.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnrolmentApi()
campaign_id = 'campaign_id_example' # str | The ID of the campaign. The Loopy Loyalty campaign ID can be found in the URL bar when looking at the campaign overview (https://app.loopyloyalty.com/overview/{campaignId}).
body = swagger_client.LoopyEnrolCustomerRequest() # LoopyEnrolCustomerRequest | 

try: 
    # Enrol customer (public)
    api_response = api_instance.loopy_loyalty_enrol_member(campaign_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EnrolmentApi->loopy_loyalty_enrol_member: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The ID of the campaign. The Loopy Loyalty campaign ID can be found in the URL bar when looking at the campaign overview (https://app.loopyloyalty.com/overview/{campaignId}). | 
 **body** | [**LoopyEnrolCustomerRequest**](LoopyEnrolCustomerRequest.md)|  | 

### Return type

[**LoopyEnrolCustomerResponse**](LoopyEnrolCustomerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_get_campaign_public**
> LoopyCampaignPublic loopy_loyalty_get_campaign_public(id)

Get campaign (public)

Gets the campaign details for campaign with `{id}`. Can be used to render a custom enrolment page.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnrolmentApi()
id = 'id_example' # str | The unique identifier to an object or record.

try: 
    # Get campaign (public)
    api_response = api_instance.loopy_loyalty_get_campaign_public(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EnrolmentApi->loopy_loyalty_get_campaign_public: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier to an object or record. | 

### Return type

[**LoopyCampaignPublic**](LoopyCampaignPublic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

