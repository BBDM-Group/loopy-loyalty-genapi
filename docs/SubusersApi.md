# swagger_client.SubusersApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loopy_loyalty_create_subuser**](SubusersApi.md#loopy_loyalty_create_subuser) | **POST** /subuser | Create subuser
[**loopy_loyalty_delete_subuser**](SubusersApi.md#loopy_loyalty_delete_subuser) | **DELETE** /subuser/{id} | Delete subuser
[**loopy_loyalty_get_subuser**](SubusersApi.md#loopy_loyalty_get_subuser) | **GET** /subuser/{id} | Gets subuser
[**loopy_loyalty_list_sub_users**](SubusersApi.md#loopy_loyalty_list_sub_users) | **GET** /subusers | List subusers
[**loopy_loyalty_update_subuser**](SubusersApi.md#loopy_loyalty_update_subuser) | **PATCH** /subuser/{id} | Update subuser


# **loopy_loyalty_create_subuser**
> IoId loopy_loyalty_create_subuser(body)

Create subuser

Creates a new subuser for a Loopy Loyalty account.

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
api_instance = swagger_client.SubusersApi()
body = swagger_client.LoopySubuser() # LoopySubuser | 

try: 
    # Create subuser
    api_response = api_instance.loopy_loyalty_create_subuser(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubusersApi->loopy_loyalty_create_subuser: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoopySubuser**](LoopySubuser.md)|  | 

### Return type

[**IoId**](IoId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_delete_subuser**
> LoopySuccessResponse loopy_loyalty_delete_subuser(id, body)

Delete subuser

Deletes an existing subuser with ID `{id}`.

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
api_instance = swagger_client.SubusersApi()
id = 'id_example' # str | The unique identifier to an object or record.
body = swagger_client.IoId() # IoId | 

try: 
    # Delete subuser
    api_response = api_instance.loopy_loyalty_delete_subuser(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubusersApi->loopy_loyalty_delete_subuser: %s\n" % e
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

# **loopy_loyalty_get_subuser**
> LoopySubuser loopy_loyalty_get_subuser(id)

Gets subuser

Gets an existing subuser with ID `{id}`.

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
api_instance = swagger_client.SubusersApi()
id = 'id_example' # str | The unique identifier to an object or record.

try: 
    # Gets subuser
    api_response = api_instance.loopy_loyalty_get_subuser(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubusersApi->loopy_loyalty_get_subuser: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier to an object or record. | 

### Return type

[**LoopySubuser**](LoopySubuser.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_list_sub_users**
> LoopyListSubusersResponse loopy_loyalty_list_sub_users()

List subusers

Lists all the subusers for a Loopy Loyalty account.

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
api_instance = swagger_client.SubusersApi()

try: 
    # List subusers
    api_response = api_instance.loopy_loyalty_list_sub_users()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubusersApi->loopy_loyalty_list_sub_users: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoopyListSubusersResponse**](LoopyListSubusersResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_update_subuser**
> LoopySubuser loopy_loyalty_update_subuser(id, body)

Update subuser

Updates an existing subuser with ID `{id}`.

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
api_instance = swagger_client.SubusersApi()
id = 'id_example' # str | Subuser ID: compressed 22 character UUID.
body = swagger_client.LoopySubuser() # LoopySubuser | 

try: 
    # Update subuser
    api_response = api_instance.loopy_loyalty_update_subuser(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubusersApi->loopy_loyalty_update_subuser: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subuser ID: compressed 22 character UUID. | 
 **body** | [**LoopySubuser**](LoopySubuser.md)|  | 

### Return type

[**LoopySubuser**](LoopySubuser.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

