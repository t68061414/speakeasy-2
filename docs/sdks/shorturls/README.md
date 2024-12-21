# ShortURLs
(*short_ur_ls*)

## Overview

REST APIs for managing short URLs

### Available Operations

* [create](#create) - Shorten a URL.

## create

Shorten a URL.

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

    res = test_sdk_name.short_ur_ls.create(url="https://probable-heating.com/")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `url`                                                               | *str*                                                               | :heavy_check_mark:                                                  | URL to shorten                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ShortURL](../../models/shorturl.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |