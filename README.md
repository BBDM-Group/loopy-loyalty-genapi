# swagger_client
No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build date: 2024-03-25T21:39:25.453+04:00
- Build package: class io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://developer.loopyloyalty.com/](https://developer.loopyloyalty.com/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = swagger_client.CampaignsApi
name = 'name_example' # str | Name of the campaign

try:
    # Campaign exists (by name)
    api_response = api_instance.loopy_loyalty_campaign_exists(name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CampaignsApi->loopy_loyalty_campaign_exists: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CampaignsApi* | [**loopy_loyalty_campaign_exists**](docs/CampaignsApi.md#loopy_loyalty_campaign_exists) | **GET** /campaign/exists/{name} | Campaign exists (by name)
*CampaignsApi* | [**loopy_loyalty_create_campaign**](docs/CampaignsApi.md#loopy_loyalty_create_campaign) | **POST** /campaign | Create campaign
*CampaignsApi* | [**loopy_loyalty_delete_campaign**](docs/CampaignsApi.md#loopy_loyalty_delete_campaign) | **DELETE** /campaign/{id} | Delete campaign
*CampaignsApi* | [**loopy_loyalty_get_campaign_by_id**](docs/CampaignsApi.md#loopy_loyalty_get_campaign_by_id) | **GET** /campaign/id/{id} | Get campaign (by id)
*CampaignsApi* | [**loopy_loyalty_get_campaign_by_name**](docs/CampaignsApi.md#loopy_loyalty_get_campaign_by_name) | **GET** /campaign/name/{name} | Get campaign (by name)
*CampaignsApi* | [**loopy_loyalty_list_campaigns**](docs/CampaignsApi.md#loopy_loyalty_list_campaigns) | **GET** /campaigns | List campaigns
*CampaignsApi* | [**loopy_loyalty_push_changes_to_cards**](docs/CampaignsApi.md#loopy_loyalty_push_changes_to_cards) | **POST** /campaign/{id}/push | Push latest campaign changes
*CampaignsApi* | [**loopy_loyalty_update_campaign**](docs/CampaignsApi.md#loopy_loyalty_update_campaign) | **PATCH** /campaign/{id} | Update campaign
*CardsApi* | [**loopy_loyalty_delete_card**](docs/CardsApi.md#loopy_loyalty_delete_card) | **DELETE** /card/cid/{id}/delete | Delete card (by ID)
*CardsApi* | [**loopy_loyalty_get_card_by_id**](docs/CardsApi.md#loopy_loyalty_get_card_by_id) | **GET** /card/{cid} | Get card (by ID)
*CardsApi* | [**loopy_loyalty_get_card_by_unique_id**](docs/CardsApi.md#loopy_loyalty_get_card_by_unique_id) | **GET** /uniquecard/campaignid/{campaignId}/{uniqueIdType}/{uniqueIdValue} | Get card (by unique ID)
*CardsApi* | [**loopy_loyalty_list_cards**](docs/CardsApi.md#loopy_loyalty_list_cards) | **POST** /card/cid/{cid} | List cards
*CardsApi* | [**loopy_loyalty_resync_card**](docs/CardsApi.md#loopy_loyalty_resync_card) | **PUT** /card/cid/{cid}/resync | Re-sync card
*CardsApi* | [**loopy_loyalty_send_message_to_all_cards**](docs/CardsApi.md#loopy_loyalty_send_message_to_all_cards) | **POST** /card/cid/{cid}/push | Send message to all cards
*CardsApi* | [**loopy_loyalty_send_message_to_individual_card**](docs/CardsApi.md#loopy_loyalty_send_message_to_individual_card) | **POST** /card/push | Send message to an individual card
*EnrolmentApi* | [**loopy_loyalty_enrol_member**](docs/EnrolmentApi.md#loopy_loyalty_enrol_member) | **POST** /enrol/{campaignId} | Enrol customer (public)
*EnrolmentApi* | [**loopy_loyalty_get_campaign_public**](docs/EnrolmentApi.md#loopy_loyalty_get_campaign_public) | **GET** /campaign/public/{id} | Get campaign (public)
*ImagesApi* | [**loopy_loyalty_create_image_assets**](docs/ImagesApi.md#loopy_loyalty_create_image_assets) | **POST** /imageAsset | Create image asset
*ImagesApi* | [**loopy_loyalty_get_stamp_image**](docs/ImagesApi.md#loopy_loyalty_get_stamp_image) | **GET** /images/stampImage/{id} | Gets stamp image (by ID)
*ImagesApi* | [**loopy_loyalty_get_strip_image**](docs/ImagesApi.md#loopy_loyalty_get_strip_image) | **GET** /images | Get strip image (by image configuration)
*ImagesApi* | [**loopy_loyalty_get_strip_image_default_template**](docs/ImagesApi.md#loopy_loyalty_get_strip_image_default_template) | **GET** /images/jsonTemplate | Get default strip image template
*ImagesApi* | [**loopy_loyalty_list_stamp_images**](docs/ImagesApi.md#loopy_loyalty_list_stamp_images) | **GET** /images/stampTemplates | List stamp images
*LocationsBeaconsApi* | [**loopy_loyalty_create_beacon**](docs/LocationsBeaconsApi.md#loopy_loyalty_create_beacon) | **POST** /beacon | Create beacon
*LocationsBeaconsApi* | [**loopy_loyalty_create_location**](docs/LocationsBeaconsApi.md#loopy_loyalty_create_location) | **POST** /location | Create location
*LocationsBeaconsApi* | [**loopy_loyalty_delete_beacon**](docs/LocationsBeaconsApi.md#loopy_loyalty_delete_beacon) | **DELETE** /beacon/{id} | Delete beacon
*LocationsBeaconsApi* | [**loopy_loyalty_delete_location**](docs/LocationsBeaconsApi.md#loopy_loyalty_delete_location) | **DELETE** /location/{id} | Delete location
*LocationsBeaconsApi* | [**loopy_loyalty_get_beacon**](docs/LocationsBeaconsApi.md#loopy_loyalty_get_beacon) | **GET** /beacon/{id} | Get beacon
*LocationsBeaconsApi* | [**loopy_loyalty_get_location**](docs/LocationsBeaconsApi.md#loopy_loyalty_get_location) | **GET** /location/{id} | Get location
*LocationsBeaconsApi* | [**loopy_loyalty_list_beacons**](docs/LocationsBeaconsApi.md#loopy_loyalty_list_beacons) | **GET** /beacons | List beacons
*LocationsBeaconsApi* | [**loopy_loyalty_list_locations**](docs/LocationsBeaconsApi.md#loopy_loyalty_list_locations) | **GET** /locations | List locations
*LocationsBeaconsApi* | [**loopy_loyalty_update_beacon**](docs/LocationsBeaconsApi.md#loopy_loyalty_update_beacon) | **PATCH** /beacon/{id} | Update beacon
*LocationsBeaconsApi* | [**loopy_loyalty_update_location**](docs/LocationsBeaconsApi.md#loopy_loyalty_update_location) | **PATCH** /location/{id} | Update location
*ReportingApi* | [**loopy_loyalty_export_campaign**](docs/ReportingApi.md#loopy_loyalty_export_campaign) | **POST** /export/{id} | Export campaign
*ReportingApi* | [**loopy_loyalty_list_events_for_campaign**](docs/ReportingApi.md#loopy_loyalty_list_events_for_campaign) | **POST** /events/analytics/transactions/{cid} | List events for campaign
*StampsRewardsApi* | [**loopy_loyalty_add_stamps**](docs/StampsRewardsApi.md#loopy_loyalty_add_stamps) | **POST** /card/cid/{cid}/addStamps/{stamps} | Add stamps (by card ID)
*StampsRewardsApi* | [**loopy_loyalty_add_stamps_by_unique_card_field**](docs/StampsRewardsApi.md#loopy_loyalty_add_stamps_by_unique_card_field) | **POST** /uniquecard/campaignid/{campaignId}/{uniqueIdType}/{uniqueIdValue}/addStamps/{stamps} | Add stamps (by unique card data field)
*StampsRewardsApi* | [**loopy_loyalty_redeem_reward**](docs/StampsRewardsApi.md#loopy_loyalty_redeem_reward) | **POST** /card/cid/{cid}/redeemReward/{rewardType}/{rewardsToRedeem} | Redeem Rewards (by card ID)
*StampsRewardsApi* | [**loopy_loyalty_redeem_reward_by_unique_card_field**](docs/StampsRewardsApi.md#loopy_loyalty_redeem_reward_by_unique_card_field) | **POST** /uniquecard/campaignid/{campaignId}/{uniqueIdType}/{uniqueIdValue}/redeemReward/{rewardType}/{rewardsToRedeem} | Redeem Rewards (by unique card data field)
*SubusersApi* | [**loopy_loyalty_create_subuser**](docs/SubusersApi.md#loopy_loyalty_create_subuser) | **POST** /subuser | Create subuser
*SubusersApi* | [**loopy_loyalty_delete_subuser**](docs/SubusersApi.md#loopy_loyalty_delete_subuser) | **DELETE** /subuser/{id} | Delete subuser
*SubusersApi* | [**loopy_loyalty_get_subuser**](docs/SubusersApi.md#loopy_loyalty_get_subuser) | **GET** /subuser/{id} | Gets subuser
*SubusersApi* | [**loopy_loyalty_list_sub_users**](docs/SubusersApi.md#loopy_loyalty_list_sub_users) | **GET** /subusers | List subusers
*SubusersApi* | [**loopy_loyalty_update_subuser**](docs/SubusersApi.md#loopy_loyalty_update_subuser) | **PATCH** /subuser/{id} | Update subuser
*WebhookSubscriptionsApi* | [**loopy_loyalty_create_subscription**](docs/WebhookSubscriptionsApi.md#loopy_loyalty_create_subscription) | **POST** /subscription | Create subscription
*WebhookSubscriptionsApi* | [**loopy_loyalty_delete_subscription**](docs/WebhookSubscriptionsApi.md#loopy_loyalty_delete_subscription) | **DELETE** /subscription/{id} | Delete subscription
*WebhookSubscriptionsApi* | [**loopy_loyalty_get_sample_event**](docs/WebhookSubscriptionsApi.md#loopy_loyalty_get_sample_event) | **GET** /subscription/{eventType}/{campaignId} | Get sample event


## Documentation For Models

 - [GooglerpcStatus](docs/GooglerpcStatus.md)
 - [IoId](docs/IoId.md)
 - [LoopyAddStampsRequest](docs/LoopyAddStampsRequest.md)
 - [LoopyAddStampsWithUniqueIdRequest](docs/LoopyAddStampsWithUniqueIdRequest.md)
 - [LoopyBeacon](docs/LoopyBeacon.md)
 - [LoopyBusiness](docs/LoopyBusiness.md)
 - [LoopyCampaign](docs/LoopyCampaign.md)
 - [LoopyCampaignExistsResponse](docs/LoopyCampaignExistsResponse.md)
 - [LoopyCampaignExportRequest](docs/LoopyCampaignExportRequest.md)
 - [LoopyCampaignForList](docs/LoopyCampaignForList.md)
 - [LoopyCampaignPublic](docs/LoopyCampaignPublic.md)
 - [LoopyCampaignType](docs/LoopyCampaignType.md)
 - [LoopyCard](docs/LoopyCard.md)
 - [LoopyCardUniqueIds](docs/LoopyCardUniqueIds.md)
 - [LoopyCreateImageAssetRequest](docs/LoopyCreateImageAssetRequest.md)
 - [LoopyCreateImageAssetResponse](docs/LoopyCreateImageAssetResponse.md)
 - [LoopyCustomFrontField](docs/LoopyCustomFrontField.md)
 - [LoopyDataField](docs/LoopyDataField.md)
 - [LoopyDataFieldType](docs/LoopyDataFieldType.md)
 - [LoopyDesign](docs/LoopyDesign.md)
 - [LoopyEnrolCustomerRequest](docs/LoopyEnrolCustomerRequest.md)
 - [LoopyEnrolCustomerResponse](docs/LoopyEnrolCustomerResponse.md)
 - [LoopyEvent](docs/LoopyEvent.md)
 - [LoopyExpiry](docs/LoopyExpiry.md)
 - [LoopyExportSegment](docs/LoopyExportSegment.md)
 - [LoopyFilterCondition](docs/LoopyFilterCondition.md)
 - [LoopyGetCardResponse](docs/LoopyGetCardResponse.md)
 - [LoopyGetImageResponse](docs/LoopyGetImageResponse.md)
 - [LoopyGetStripImageTemplateResponse](docs/LoopyGetStripImageTemplateResponse.md)
 - [LoopyIP](docs/LoopyIP.md)
 - [LoopyImageAssetType](docs/LoopyImageAssetType.md)
 - [LoopyImageType](docs/LoopyImageType.md)
 - [LoopyIndividualMessageRequest](docs/LoopyIndividualMessageRequest.md)
 - [LoopyLink](docs/LoopyLink.md)
 - [LoopyListBeaconsResponse](docs/LoopyListBeaconsResponse.md)
 - [LoopyListBeaconsRow](docs/LoopyListBeaconsRow.md)
 - [LoopyListCampaignsResponse](docs/LoopyListCampaignsResponse.md)
 - [LoopyListCampaignsRow](docs/LoopyListCampaignsRow.md)
 - [LoopyListCardsColumn](docs/LoopyListCardsColumn.md)
 - [LoopyListCardsDataTableInput](docs/LoopyListCardsDataTableInput.md)
 - [LoopyListCardsDataTableOutput](docs/LoopyListCardsDataTableOutput.md)
 - [LoopyListCardsOrder](docs/LoopyListCardsOrder.md)
 - [LoopyListCardsRequest](docs/LoopyListCardsRequest.md)
 - [LoopyListEventsDataTableInput](docs/LoopyListEventsDataTableInput.md)
 - [LoopyListEventsDataTableOutput](docs/LoopyListEventsDataTableOutput.md)
 - [LoopyListEventsOrder](docs/LoopyListEventsOrder.md)
 - [LoopyListEventsRequest](docs/LoopyListEventsRequest.md)
 - [LoopyListLocationsResponse](docs/LoopyListLocationsResponse.md)
 - [LoopyListLocationsRow](docs/LoopyListLocationsRow.md)
 - [LoopyListStampImagesResponse](docs/LoopyListStampImagesResponse.md)
 - [LoopyListSubusersResponse](docs/LoopyListSubusersResponse.md)
 - [LoopyListSubusersRow](docs/LoopyListSubusersRow.md)
 - [LoopyLocation](docs/LoopyLocation.md)
 - [LoopyMySqlEvent](docs/LoopyMySqlEvent.md)
 - [LoopyMySqlTransaction](docs/LoopyMySqlTransaction.md)
 - [LoopyPassType](docs/LoopyPassType.md)
 - [LoopyRedeemRewardsRequest](docs/LoopyRedeemRewardsRequest.md)
 - [LoopyRedeemRewardsWithUniqueIdRequest](docs/LoopyRedeemRewardsWithUniqueIdRequest.md)
 - [LoopyRequestMetaData](docs/LoopyRequestMetaData.md)
 - [LoopyResyncCardRequest](docs/LoopyResyncCardRequest.md)
 - [LoopyReward](docs/LoopyReward.md)
 - [LoopySendMessageRequest](docs/LoopySendMessageRequest.md)
 - [LoopyStatus](docs/LoopyStatus.md)
 - [LoopyStripImage](docs/LoopyStripImage.md)
 - [LoopySubscriptionEventType](docs/LoopySubscriptionEventType.md)
 - [LoopySubscriptionRequest](docs/LoopySubscriptionRequest.md)
 - [LoopySubuser](docs/LoopySubuser.md)
 - [LoopySuccessResponse](docs/LoopySuccessResponse.md)
 - [LoopyUpdateBeaconResponse](docs/LoopyUpdateBeaconResponse.md)
 - [LoopyUpdateLocationResponse](docs/LoopyUpdateLocationResponse.md)
 - [ProtobufAny](docs/ProtobufAny.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

support@loopyloyalty.com

