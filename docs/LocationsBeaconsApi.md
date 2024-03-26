# swagger_client.LocationsBeaconsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loopy_loyalty_create_beacon**](LocationsBeaconsApi.md#loopy_loyalty_create_beacon) | **POST** /beacon | Create beacon
[**loopy_loyalty_create_location**](LocationsBeaconsApi.md#loopy_loyalty_create_location) | **POST** /location | Create location
[**loopy_loyalty_delete_beacon**](LocationsBeaconsApi.md#loopy_loyalty_delete_beacon) | **DELETE** /beacon/{id} | Delete beacon
[**loopy_loyalty_delete_location**](LocationsBeaconsApi.md#loopy_loyalty_delete_location) | **DELETE** /location/{id} | Delete location
[**loopy_loyalty_get_beacon**](LocationsBeaconsApi.md#loopy_loyalty_get_beacon) | **GET** /beacon/{id} | Get beacon
[**loopy_loyalty_get_location**](LocationsBeaconsApi.md#loopy_loyalty_get_location) | **GET** /location/{id} | Get location
[**loopy_loyalty_list_beacons**](LocationsBeaconsApi.md#loopy_loyalty_list_beacons) | **GET** /beacons | List beacons
[**loopy_loyalty_list_locations**](LocationsBeaconsApi.md#loopy_loyalty_list_locations) | **GET** /locations | List locations
[**loopy_loyalty_update_beacon**](LocationsBeaconsApi.md#loopy_loyalty_update_beacon) | **PATCH** /beacon/{id} | Update beacon
[**loopy_loyalty_update_location**](LocationsBeaconsApi.md#loopy_loyalty_update_location) | **PATCH** /location/{id} | Update location


# **loopy_loyalty_create_beacon**
> IoId loopy_loyalty_create_beacon(body)

Create beacon

Creates a new beacon for a Loopy Loyalty account.

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
api_instance = swagger_client.LocationsBeaconsApi()
body = swagger_client.LoopyBeacon() # LoopyBeacon | 

try: 
    # Create beacon
    api_response = api_instance.loopy_loyalty_create_beacon(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LocationsBeaconsApi->loopy_loyalty_create_beacon: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoopyBeacon**](LoopyBeacon.md)|  | 

### Return type

[**IoId**](IoId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_create_location**
> IoId loopy_loyalty_create_location(body)

Create location

Creates a new location for a Loopy Loyalty account.

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
api_instance = swagger_client.LocationsBeaconsApi()
body = swagger_client.LoopyLocation() # LoopyLocation | 

try: 
    # Create location
    api_response = api_instance.loopy_loyalty_create_location(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LocationsBeaconsApi->loopy_loyalty_create_location: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoopyLocation**](LoopyLocation.md)|  | 

### Return type

[**IoId**](IoId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_delete_beacon**
> LoopySuccessResponse loopy_loyalty_delete_beacon(id, body)

Delete beacon

Deletes an existing beacon with ID `{id}`.

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
api_instance = swagger_client.LocationsBeaconsApi()
id = 'id_example' # str | The unique identifier to an object or record.
body = swagger_client.IoId() # IoId | 

try: 
    # Delete beacon
    api_response = api_instance.loopy_loyalty_delete_beacon(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LocationsBeaconsApi->loopy_loyalty_delete_beacon: %s\n" % e
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

# **loopy_loyalty_delete_location**
> LoopySuccessResponse loopy_loyalty_delete_location(id, body)

Delete location

Deletes an existing location with ID `{id}`.

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
api_instance = swagger_client.LocationsBeaconsApi()
id = 'id_example' # str | The unique identifier to an object or record.
body = swagger_client.IoId() # IoId | 

try: 
    # Delete location
    api_response = api_instance.loopy_loyalty_delete_location(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LocationsBeaconsApi->loopy_loyalty_delete_location: %s\n" % e
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

# **loopy_loyalty_get_beacon**
> LoopyBeacon loopy_loyalty_get_beacon(id)

Get beacon

Gets an existing beacon with ID `{id}`.

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
api_instance = swagger_client.LocationsBeaconsApi()
id = 'id_example' # str | The unique identifier to an object or record.

try: 
    # Get beacon
    api_response = api_instance.loopy_loyalty_get_beacon(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LocationsBeaconsApi->loopy_loyalty_get_beacon: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier to an object or record. | 

### Return type

[**LoopyBeacon**](LoopyBeacon.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_get_location**
> LoopyLocation loopy_loyalty_get_location(id)

Get location

Gets an existing location with ID `{id}`.

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
api_instance = swagger_client.LocationsBeaconsApi()
id = 'id_example' # str | The unique identifier to an object or record.

try: 
    # Get location
    api_response = api_instance.loopy_loyalty_get_location(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LocationsBeaconsApi->loopy_loyalty_get_location: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier to an object or record. | 

### Return type

[**LoopyLocation**](LoopyLocation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_list_beacons**
> LoopyListBeaconsResponse loopy_loyalty_list_beacons()

List beacons

Lists all the beacons for a Loopy Loyalty account.

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
api_instance = swagger_client.LocationsBeaconsApi()

try: 
    # List beacons
    api_response = api_instance.loopy_loyalty_list_beacons()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LocationsBeaconsApi->loopy_loyalty_list_beacons: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoopyListBeaconsResponse**](LoopyListBeaconsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_list_locations**
> LoopyListLocationsResponse loopy_loyalty_list_locations()

List locations

Lists all the locations for a Loopy Loyalty account.

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
api_instance = swagger_client.LocationsBeaconsApi()

try: 
    # List locations
    api_response = api_instance.loopy_loyalty_list_locations()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LocationsBeaconsApi->loopy_loyalty_list_locations: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoopyListLocationsResponse**](LoopyListLocationsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_update_beacon**
> LoopyUpdateBeaconResponse loopy_loyalty_update_beacon(id, body)

Update beacon

Updates an existing beacon with ID `{id}`.

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
api_instance = swagger_client.LocationsBeaconsApi()
id = 'id_example' # str | Beacon ID. compressed 22 character UUID; auto generated.
body = swagger_client.LoopyBeacon() # LoopyBeacon | 

try: 
    # Update beacon
    api_response = api_instance.loopy_loyalty_update_beacon(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LocationsBeaconsApi->loopy_loyalty_update_beacon: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Beacon ID. compressed 22 character UUID; auto generated. | 
 **body** | [**LoopyBeacon**](LoopyBeacon.md)|  | 

### Return type

[**LoopyUpdateBeaconResponse**](LoopyUpdateBeaconResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_update_location**
> LoopyUpdateLocationResponse loopy_loyalty_update_location(id, body)

Update location

Updates an existing location with ID `{id}`.

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
api_instance = swagger_client.LocationsBeaconsApi()
id = 'id_example' # str | Location ID. compressed 22 character UUID; auto generated.
body = swagger_client.LoopyLocation() # LoopyLocation | 

try: 
    # Update location
    api_response = api_instance.loopy_loyalty_update_location(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LocationsBeaconsApi->loopy_loyalty_update_location: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Location ID. compressed 22 character UUID; auto generated. | 
 **body** | [**LoopyLocation**](LoopyLocation.md)|  | 

### Return type

[**LoopyUpdateLocationResponse**](LoopyUpdateLocationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

