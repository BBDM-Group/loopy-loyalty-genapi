# swagger_client.ImagesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loopy_loyalty_create_image_assets**](ImagesApi.md#loopy_loyalty_create_image_assets) | **POST** /imageAsset | Create image asset
[**loopy_loyalty_get_stamp_image**](ImagesApi.md#loopy_loyalty_get_stamp_image) | **GET** /images/stampImage/{id} | Gets stamp image (by ID)
[**loopy_loyalty_get_strip_image**](ImagesApi.md#loopy_loyalty_get_strip_image) | **GET** /images | Get strip image (by image configuration)
[**loopy_loyalty_get_strip_image_default_template**](ImagesApi.md#loopy_loyalty_get_strip_image_default_template) | **GET** /images/jsonTemplate | Get default strip image template
[**loopy_loyalty_list_stamp_images**](ImagesApi.md#loopy_loyalty_list_stamp_images) | **GET** /images/stampTemplates | List stamp images


# **loopy_loyalty_create_image_assets**
> LoopySuccessResponse loopy_loyalty_create_image_assets(body)

Create image asset

Creates a new Loopy Loyalty image asset.

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
api_instance = swagger_client.ImagesApi()
body = swagger_client.LoopyCreateImageAssetRequest() # LoopyCreateImageAssetRequest | 

try: 
    # Create image asset
    api_response = api_instance.loopy_loyalty_create_image_assets(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ImagesApi->loopy_loyalty_create_image_assets: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoopyCreateImageAssetRequest**](LoopyCreateImageAssetRequest.md)|  | 

### Return type

[**LoopySuccessResponse**](LoopySuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_get_stamp_image**
> object loopy_loyalty_get_stamp_image(id)

Gets stamp image (by ID)

Gets a default built-in stamp image by ID. The ID can be retrieved from the '[List stamp images](#operation/LoopyLoyalty_listStampImages)' method. Method will serve the image up as a file with Content-Type `svg+xml`.

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
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | The unique identifier to an object or record.

try: 
    # Gets stamp image (by ID)
    api_response = api_instance.loopy_loyalty_get_stamp_image(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ImagesApi->loopy_loyalty_get_stamp_image: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier to an object or record. | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_get_strip_image**
> LoopyGetImageResponse loopy_loyalty_get_strip_image(width=width, height=height, padding=padding, total_stamps=total_stamps, stamp_image=stamp_image, unstamp_image=unstamp_image, stamp_image_url=stamp_image_url, unstamp_image_url=unstamp_image_url, background_colour=background_colour, background_opacity=background_opacity, background_url=background_url, stamp_colour=stamp_colour, stamp_opacity=stamp_opacity, unstamp_colour=unstamp_colour, unstamp_opacity=unstamp_opacity, placeholders=placeholders, placeholder_colour=placeholder_colour, placeholder_opacity=placeholder_opacity, placeholder_border_colour=placeholder_border_colour, placeholder_border_opacity=placeholder_border_opacity, rewards_placeholders=rewards_placeholders, reward_border_colour=reward_border_colour, reward_border_opacity=reward_border_opacity, reward_background_colour=reward_background_colour, reward_background_opacity=reward_background_opacity, reward_positions=reward_positions, stamped_status=stamped_status, image_type=image_type)

Get strip image (by image configuration)

Returns or renders a stamped strip image based on the provided stamp configuration. To be requested in the format: https://api.loopyloyalty.com/images?json={URL encoded StripImage JSON Object}. Returns a different content-type based on the `stripImage.imageType` parameter: `svg` (image/svg+xml), `png` (image/png), `json` (json). `svg` is the fastest and preferred image type. [Sample URL](https://api.loopyloyalty.com/images?json=%7B%22width%22%3A1125%2C%22height%22%3A432%2C%22padding%22%3A40%2C%22totalStamps%22%3A10%2C%22stampImage%22%3A%22coffee-2%22%2C%22unstampImage%22%3A%22coffee-2%22%2C%22backgroundColor%22%3A%22%23FF6D00%22%2C%22backgroundOpacity%22%3A1%2C%22backgroundURL%22%3A%22https%3A%2F%2Fs3.amazonaws.com%2Fpasskit-api-core-production%2Fll-stamps%2Fc9a3e1b59dfcc2ba50b7c2d6d7c47219-b.png%22%2C%22stampColor%22%3A%22%23ffffff%22%2C%22stampOpacity%22%3A1%2C%22unstampColor%22%3A%22%23FFFFFF%22%2C%22unstampOpacity%22%3A0.25%2C%22placeholders%22%3Atrue%2C%22placeholderColor%22%3A%22%23a97b50%22%2C%22placeholderOpacity%22%3A1%2C%22placeholderBorderColor%22%3A%22%23FFD600%22%2C%22placeholderBorderOpacity%22%3A1%2C%22rewardsPlaceholders%22%3Atrue%2C%22rewardBorderColor%22%3A%22%23EBFF10%22%2C%22rewardBorderOpacity%22%3A1%2C%22rewardBackgroundColor%22%3A%22%23808548%22%2C%22rewardBackgroundOpacity%22%3A1%2C%22rewardPositions%22%3A0%2C%22stampedStatus%22%3A3%2C%22imageType%22%3A%22svg%22%7D).

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
api_instance = swagger_client.ImagesApi()
width = 56 # int | Width of the strip image; default to `1125` (px). (optional)
height = 56 # int | Height of the stripe image; defaults to `432` (px). (optional)
padding = 1.2 # float | Padding between stamps and the image edge; defaults to `40` (px). (optional)
total_stamps = 56 # int | Total number of stamps to be rendered on the card. Can be between 1-30; defaults to `10`. (optional)
stamp_image = 'stamp_image_example' # str | Stamp image id. This needs to come from the pre-defined list of stamp images; defaults to `bagel`. (optional)
unstamp_image = 'unstamp_image_example' # str | Unstamp image id. This needs to come from the pre-defined list of stamp images; defaults to `bagel`. (optional)
stamp_image_url = 'stamp_image_url_example' # str | URL for a stamp image to use. If provided will be used instead of `stampImage`; defaults to blank. (optional)
unstamp_image_url = 'unstamp_image_url_example' # str | URL for a unstamp image to use. If provided will be used instead of `unstampImage`; defaults to blank. (optional)
background_colour = 'background_colour_example' # str | Hexcode for background colour; defaults to `#401A6B`. (optional)
background_opacity = 1.2 # float | Opacity for the background, needs to be between 0.00-1.00; defaults to `1`. (optional)
background_url = 'background_url_example' # str | URL for the background image to use; defaults to blank. (optional)
stamp_colour = 'stamp_colour_example' # str | Hexcode for stamp colour; defaults to `#FFFFFF`. (optional)
stamp_opacity = 1.2 # float | Opacity for the stamp image, needs to be between 0.00-1.00; defaults to `1`. (optional)
unstamp_colour = 'unstamp_colour_example' # str | Hexcode for unstamped colour; defaults to `#FFFFFF`. (optional)
unstamp_opacity = 1.2 # float | Opacity for the unstamped image, needs to be between 0.00-1.00; defaults to `0.25`. (optional)
placeholders = true # bool | Indicates if stamp placeholders should be rendered; defaults to `true`. (optional)
placeholder_colour = 'placeholder_colour_example' # str | Hexcode for placeholder colour; defaults to `#6B1D5E`. (optional)
placeholder_opacity = 1.2 # float | Opacity for the placeholder, needs to be between 0.00-1.00; defaults to `1`. (optional)
placeholder_border_colour = 'placeholder_border_colour_example' # str | Hexcode for placeholder border colour; defaults to `#177BE3`. (optional)
placeholder_border_opacity = 1.2 # float | Opacity for the placeholder border, needs to be between 0.00-1.00; defaults to `1`. (optional)
rewards_placeholders = true # bool | Indicates if reward place holders should be rendered; defaults to `true`. (optional)
reward_border_colour = 'reward_border_colour_example' # str | Hexcode for reward border colour; defaults to `#EBFF10`. (optional)
reward_border_opacity = 1.2 # float | Opacity for the reward border, needs to be between 0.00-1.00; defaults to `1`. (optional)
reward_background_colour = 'reward_background_colour_example' # str | Hexcode for reward background colour; defaults to `#808548`. (optional)
reward_background_opacity = 1.2 # float | Opacity for the reward background, needs to be between 0.00-1.00; defaults to `1`. (optional)
reward_positions = 789 # int | Bitmask to indicate the positions of the rewards (for multiple reward card); defaults to `584` (which is stamp 3, 6 & 9). (optional)
stamped_status = 789 # int | Bitmask to indicate which positions on the stamp card have been stamped; defaults to `3` (stamp 1 & 2). (optional)
image_type = 'svg' # str | Indicates the image type to be rendered; defaults to `SVG`.   - svg: Renders the image as SVG (preferred).  - png: Renders the image as PNG.  - json: Returns the image as JSON object with image as bytes string. (optional) (default to svg)

try: 
    # Get strip image (by image configuration)
    api_response = api_instance.loopy_loyalty_get_strip_image(width=width, height=height, padding=padding, total_stamps=total_stamps, stamp_image=stamp_image, unstamp_image=unstamp_image, stamp_image_url=stamp_image_url, unstamp_image_url=unstamp_image_url, background_colour=background_colour, background_opacity=background_opacity, background_url=background_url, stamp_colour=stamp_colour, stamp_opacity=stamp_opacity, unstamp_colour=unstamp_colour, unstamp_opacity=unstamp_opacity, placeholders=placeholders, placeholder_colour=placeholder_colour, placeholder_opacity=placeholder_opacity, placeholder_border_colour=placeholder_border_colour, placeholder_border_opacity=placeholder_border_opacity, rewards_placeholders=rewards_placeholders, reward_border_colour=reward_border_colour, reward_border_opacity=reward_border_opacity, reward_background_colour=reward_background_colour, reward_background_opacity=reward_background_opacity, reward_positions=reward_positions, stamped_status=stamped_status, image_type=image_type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ImagesApi->loopy_loyalty_get_strip_image: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **width** | **int**| Width of the strip image; default to &#x60;1125&#x60; (px). | [optional] 
 **height** | **int**| Height of the stripe image; defaults to &#x60;432&#x60; (px). | [optional] 
 **padding** | **float**| Padding between stamps and the image edge; defaults to &#x60;40&#x60; (px). | [optional] 
 **total_stamps** | **int**| Total number of stamps to be rendered on the card. Can be between 1-30; defaults to &#x60;10&#x60;. | [optional] 
 **stamp_image** | **str**| Stamp image id. This needs to come from the pre-defined list of stamp images; defaults to &#x60;bagel&#x60;. | [optional] 
 **unstamp_image** | **str**| Unstamp image id. This needs to come from the pre-defined list of stamp images; defaults to &#x60;bagel&#x60;. | [optional] 
 **stamp_image_url** | **str**| URL for a stamp image to use. If provided will be used instead of &#x60;stampImage&#x60;; defaults to blank. | [optional] 
 **unstamp_image_url** | **str**| URL for a unstamp image to use. If provided will be used instead of &#x60;unstampImage&#x60;; defaults to blank. | [optional] 
 **background_colour** | **str**| Hexcode for background colour; defaults to &#x60;#401A6B&#x60;. | [optional] 
 **background_opacity** | **float**| Opacity for the background, needs to be between 0.00-1.00; defaults to &#x60;1&#x60;. | [optional] 
 **background_url** | **str**| URL for the background image to use; defaults to blank. | [optional] 
 **stamp_colour** | **str**| Hexcode for stamp colour; defaults to &#x60;#FFFFFF&#x60;. | [optional] 
 **stamp_opacity** | **float**| Opacity for the stamp image, needs to be between 0.00-1.00; defaults to &#x60;1&#x60;. | [optional] 
 **unstamp_colour** | **str**| Hexcode for unstamped colour; defaults to &#x60;#FFFFFF&#x60;. | [optional] 
 **unstamp_opacity** | **float**| Opacity for the unstamped image, needs to be between 0.00-1.00; defaults to &#x60;0.25&#x60;. | [optional] 
 **placeholders** | **bool**| Indicates if stamp placeholders should be rendered; defaults to &#x60;true&#x60;. | [optional] 
 **placeholder_colour** | **str**| Hexcode for placeholder colour; defaults to &#x60;#6B1D5E&#x60;. | [optional] 
 **placeholder_opacity** | **float**| Opacity for the placeholder, needs to be between 0.00-1.00; defaults to &#x60;1&#x60;. | [optional] 
 **placeholder_border_colour** | **str**| Hexcode for placeholder border colour; defaults to &#x60;#177BE3&#x60;. | [optional] 
 **placeholder_border_opacity** | **float**| Opacity for the placeholder border, needs to be between 0.00-1.00; defaults to &#x60;1&#x60;. | [optional] 
 **rewards_placeholders** | **bool**| Indicates if reward place holders should be rendered; defaults to &#x60;true&#x60;. | [optional] 
 **reward_border_colour** | **str**| Hexcode for reward border colour; defaults to &#x60;#EBFF10&#x60;. | [optional] 
 **reward_border_opacity** | **float**| Opacity for the reward border, needs to be between 0.00-1.00; defaults to &#x60;1&#x60;. | [optional] 
 **reward_background_colour** | **str**| Hexcode for reward background colour; defaults to &#x60;#808548&#x60;. | [optional] 
 **reward_background_opacity** | **float**| Opacity for the reward background, needs to be between 0.00-1.00; defaults to &#x60;1&#x60;. | [optional] 
 **reward_positions** | **int**| Bitmask to indicate the positions of the rewards (for multiple reward card); defaults to &#x60;584&#x60; (which is stamp 3, 6 &amp; 9). | [optional] 
 **stamped_status** | **int**| Bitmask to indicate which positions on the stamp card have been stamped; defaults to &#x60;3&#x60; (stamp 1 &amp; 2). | [optional] 
 **image_type** | **str**| Indicates the image type to be rendered; defaults to &#x60;SVG&#x60;.   - svg: Renders the image as SVG (preferred).  - png: Renders the image as PNG.  - json: Returns the image as JSON object with image as bytes string. | [optional] [default to svg]

### Return type

[**LoopyGetImageResponse**](LoopyGetImageResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_get_strip_image_default_template**
> LoopyGetStripImageTemplateResponse loopy_loyalty_get_strip_image_default_template()

Get default strip image template

Returns the default strip image template. The default template can be used to configure the payload to pass to the '[Get strip image](#operation/LoopyLoyalty_getStripImage)' method in order to render a strip image for use within your platform or application.

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
api_instance = swagger_client.ImagesApi()

try: 
    # Get default strip image template
    api_response = api_instance.loopy_loyalty_get_strip_image_default_template()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ImagesApi->loopy_loyalty_get_strip_image_default_template: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoopyGetStripImageTemplateResponse**](LoopyGetStripImageTemplateResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loopy_loyalty_list_stamp_images**
> LoopyListStampImagesResponse loopy_loyalty_list_stamp_images()

List stamp images

Lists all the default built-in stamp images that are provided by Loopy Loyalty. This endpoint does not return stamp images that were uploaded by the user.

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
api_instance = swagger_client.ImagesApi()

try: 
    # List stamp images
    api_response = api_instance.loopy_loyalty_list_stamp_images()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ImagesApi->loopy_loyalty_list_stamp_images: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoopyListStampImagesResponse**](LoopyListStampImagesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

