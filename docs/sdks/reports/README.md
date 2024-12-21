# Reports
(*reports*)

## Overview

REST APIs for managing reports (lint reports, change reports, etc)

### Available Operations

* [upload_report](#upload_report) - Upload a report.
* [get_linting_report_signed_url](#get_linting_report_signed_url) - Get the signed access url for the linting reports for a particular document.
* [get_changes_report_signed_url](#get_changes_report_signed_url) - Get the signed access url for the change reports for a particular document.

## upload_report

Upload a report.

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

    res = test_sdk_name.reports.upload_report(data={}, file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `data`                                                              | [models.Report](../../models/report.md)                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `file`                                                              | [models.File](../../models/file.md)                                 | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UploadReportUploadedReport](../../models/uploadreportuploadedreport.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_linting_report_signed_url

Get the signed access url for the linting reports for a particular document.

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

    res = test_sdk_name.reports.get_linting_report_signed_url(document_checksum="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_checksum`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The checksum of the document to retrieve the signed access url for. |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetLintingReportSignedURLSignedAccess](../../models/getlintingreportsignedurlsignedaccess.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_changes_report_signed_url

Get the signed access url for the change reports for a particular document.

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

    res = test_sdk_name.reports.get_changes_report_signed_url(document_checksum="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_checksum`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The checksum of the document to retrieve the signed access url for. |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetChangesReportSignedURLSignedAccess](../../models/getchangesreportsignedurlsignedaccess.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |