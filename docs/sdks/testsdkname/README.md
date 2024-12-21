# TestSDKName SDK

## Overview

Speakeasy API: The Subscriptions API manages subscriptions for CLI and registry events

The Speakeasy Platform Documentation
</docs>

### Available Operations

* [generate_code_sample_preview](#generate_code_sample_preview) - Generate Code Sample previews from a file and configuration parameters.
* [generate_code_sample_preview_async](#generate_code_sample_preview_async) - Initiate asynchronous Code Sample preview generation from a file and configuration parameters, receiving an async JobID response for polling.
* [get_code_sample_preview_async](#get_code_sample_preview_async) - Poll for the result of an asynchronous Code Sample preview generation.

## generate_code_sample_preview

This endpoint generates Code Sample previews from a file and configuration parameters.

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

    res = test_sdk_name.generate_code_sample_preview(languages=[
        "<value>",
        "<value>",
    ], schema_file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `languages`                                                         | List[*str*]                                                         | :heavy_check_mark:                                                  | A list of languages to generate code samples for                    |
| `schema_file`                                                       | [models.SchemaFile](../../models/schemafile.md)                     | :heavy_check_mark:                                                  | The OpenAPI file to be uploaded                                     |
| `package_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The name of the package                                             |
| `sdk_class_name`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The SDK class name                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GenerateCodeSamplePreviewResponse](../../models/generatecodesamplepreviewresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX, 5XX         | application/json |

## generate_code_sample_preview_async

This endpoint generates Code Sample previews from a file and configuration parameters, receiving an async JobID response for polling.

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

    res = test_sdk_name.generate_code_sample_preview_async(languages=[
        "<value>",
        "<value>",
        "<value>",
    ], schema_file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `languages`                                                         | List[*str*]                                                         | :heavy_check_mark:                                                  | A list of languages to generate code samples for                    |
| `schema_file`                                                       | [models.SchemaFile](../../models/schemafile.md)                     | :heavy_check_mark:                                                  | The OpenAPI file to be uploaded                                     |
| `package_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The name of the package                                             |
| `sdk_class_name`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The SDK class name                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GenerateCodeSamplePreviewAsyncResponseBody](../../models/generatecodesamplepreviewasyncresponsebody.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX, 5XX         | application/json |

## get_code_sample_preview_async

Poll for the result of an asynchronous Code Sample preview generation.

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

    res = test_sdk_name.get_code_sample_preview_async(job_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `job_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | The ID of the job to check the status and retrieve results          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetCodeSamplePreviewAsyncResponse](../../models/getcodesamplepreviewasyncresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX, 5XX         | application/json |