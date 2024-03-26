# LoopyStripImage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** | Width of the strip image; default to &#x60;1125&#x60; (px). | [optional] 
**height** | **int** | Height of the stripe image; defaults to &#x60;432&#x60; (px). | [optional] 
**padding** | **float** | Padding between stamps and the image edge; defaults to &#x60;40&#x60; (px). | [optional] 
**total_stamps** | **int** | Total number of stamps to be rendered on the card. Can be between 1-30; defaults to &#x60;10&#x60;. | [optional] 
**stamp_image** | **str** | Stamp image id. This needs to come from the pre-defined list of stamp images; defaults to &#x60;bagel&#x60;. | [optional] 
**unstamp_image** | **str** | Unstamp image id. This needs to come from the pre-defined list of stamp images; defaults to &#x60;bagel&#x60;. | [optional] 
**stamp_image_url** | **str** | URL for a stamp image to use. If provided will be used instead of &#x60;stampImage&#x60;; defaults to blank. | [optional] 
**unstamp_image_url** | **str** | URL for a unstamp image to use. If provided will be used instead of &#x60;unstampImage&#x60;; defaults to blank. | [optional] 
**background_colour** | **str** | Hexcode for background colour; defaults to &#x60;#401A6B&#x60;. | [optional] 
**background_opacity** | **float** | Opacity for the background, needs to be between 0.00-1.00; defaults to &#x60;1&#x60;. | [optional] 
**background_url** | **str** | URL for the background image to use; defaults to blank. | [optional] 
**stamp_colour** | **str** | Hexcode for stamp colour; defaults to &#x60;#FFFFFF&#x60;. | [optional] 
**stamp_opacity** | **float** | Opacity for the stamp image, needs to be between 0.00-1.00; defaults to &#x60;1&#x60;. | [optional] 
**unstamp_colour** | **str** | Hexcode for unstamped colour; defaults to &#x60;#FFFFFF&#x60;. | [optional] 
**unstamp_opacity** | **float** | Opacity for the unstamped image, needs to be between 0.00-1.00; defaults to &#x60;0.25&#x60;. | [optional] 
**placeholders** | **bool** | Indicates if stamp placeholders should be rendered; defaults to &#x60;true&#x60;. | [optional] 
**placeholder_colour** | **str** | Hexcode for placeholder colour; defaults to &#x60;#6B1D5E&#x60;. | [optional] 
**placeholder_opacity** | **float** | Opacity for the placeholder, needs to be between 0.00-1.00; defaults to &#x60;1&#x60;. | [optional] 
**placeholder_border_colour** | **str** | Hexcode for placeholder border colour; defaults to &#x60;#177BE3&#x60;. | [optional] 
**placeholder_border_opacity** | **float** | Opacity for the placeholder border, needs to be between 0.00-1.00; defaults to &#x60;1&#x60;. | [optional] 
**rewards_placeholders** | **bool** | Indicates if reward place holders should be rendered; defaults to &#x60;true&#x60;. | [optional] 
**reward_border_colour** | **str** | Hexcode for reward border colour; defaults to &#x60;#EBFF10&#x60;. | [optional] 
**reward_border_opacity** | **float** | Opacity for the reward border, needs to be between 0.00-1.00; defaults to &#x60;1&#x60;. | [optional] 
**reward_background_colour** | **str** | Hexcode for reward background colour; defaults to &#x60;#808548&#x60;. | [optional] 
**reward_background_opacity** | **float** | Opacity for the reward background, needs to be between 0.00-1.00; defaults to &#x60;1&#x60;. | [optional] 
**reward_positions** | **int** | Bitmask to indicate the positions of the rewards (for multiple reward card); defaults to &#x60;584&#x60; (which is stamp 3, 6 &amp; 9). | [optional] 
**stamped_status** | **int** | Bitmask to indicate which positions on the stamp card have been stamped; defaults to &#x60;3&#x60; (stamp 1 &amp; 2). | [optional] 
**image_type** | [**LoopyImageType**](LoopyImageType.md) | Indicates the image type to be rendered; defaults to &#x60;SVG&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


