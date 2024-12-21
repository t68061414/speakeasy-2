<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
import test_sdk_name_test_package
from test_sdk_name_test_package import TestSDKName

async def main():
    async with TestSDKName(
        security=test_sdk_name_test_package.Security(
            api_key=os.getenv("TESTSDKNAME_API_KEY", ""),
        ),
    ) as test_sdk_name:

        res = await test_sdk_name.generate_code_sample_preview_async(languages=[
            "<value>",
            "<value>",
        ], schema_file={
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->