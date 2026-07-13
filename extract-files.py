#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/lancelot',
    'hardware/mediatek',
    'vendor/xiaomi/mt6768-common',
]

blob_fixups: blob_fixups_user_type = {
    'vendor/bin/mnld': blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'lancelot',
    'xiaomi',
    blob_fixups=blob_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'mt6768-common', module.vendor
    )
    utils.run()
