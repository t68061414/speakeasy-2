# Subscriptions
(*subscriptions*)

## Overview

REST APIs for managing subscriptions

### Available Operations

* [ignore_subscription_namespace](#ignore_subscription_namespace) - Ignored a namespace for a subscription
* [activate_subscription_namespace](#activate_subscription_namespace) - Activate an ignored namespace for a subscription

## ignore_subscription_namespace

Ignored a namespace for a subscription

### Example Usage

```python
import os
import test_sdk_name_test_package
from test_sdk_name_test_package import TestSDKName

with TestSDKName(
    security=test_sdk_name_test_package.Security(
        api_key=os.getenv("TESTSDKNAME_API_KEY", ""),
    ),
) as test_sdk_name:

    test_sdk_name.subscriptions.ignore_subscription_namespace(subscription_id="<id>", namespace_name="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscription_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The existing subscription ID                                        |
| `namespace_name`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The namespace name                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## activate_subscription_namespace

Activate an ignored namespace for a subscription

### Example Usage

```python
import os
import test_sdk_name_test_package
from test_sdk_name_test_package import TestSDKName

with TestSDKName(
    security=test_sdk_name_test_package.Security(
        api_key=os.getenv("TESTSDKNAME_API_KEY", ""),
    ),
) as test_sdk_name:

    test_sdk_name.subscriptions.activate_subscription_namespace(subscription_id="<id>", namespace_name="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscription_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The existing subscription ID                                        |
| `namespace_name`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The namespace name                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |