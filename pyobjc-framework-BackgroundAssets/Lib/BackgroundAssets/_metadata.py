# This file is generated by objective.metadata
#
# Last update: Fri Jun 24 17:54:53 2022
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$BADownloaderExtensionMetadataKeyApplicationCacheLocationURL$BADownloaderExtensionMetadataKeyApplicationIdentifier$BADownloaderExtensionMetadataKeyApplicationLocationURL$BADownloaderExtensionMetadataKeyLocalizedApplicationName$BADownloaderPriorityDefault@q$BADownloaderPriorityMax@q$BADownloaderPriorityMin@q$kBADownloaderInfoDictionaryApplicationCacheLocationURLKey$kBADownloaderInfoDictionaryApplicationIdentifierKey$kBADownloaderInfoDictionaryApplicationLocationURLKey$kBADownloaderInfoDictionaryLocalizedApplicationNameKey$"""
enums = """$BADownloadStateCreated@0$BADownloadStateDownloading@2$BADownloadStateFailed@-1$BADownloadStateFinished@3$BADownloadStateWaiting@1$"""
misc.update({"BADownloadState": NewType("BADownloadState", int)})
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"BAApplicationExtensionInfo",
        b"downloadSizeRestricted",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"BADownloadManager",
        b"cancelDownload:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"BADownloadManager",
        b"fetchCurrentDownloadsWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"BADownloadManager",
        b"performWithExclusiveControl:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"BADownloadManager",
        b"performWithExclusiveControlBeforeDate:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"BADownloadManager",
        b"scheduleDownload:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"BADownloadManager",
        b"startForegroundDownload:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NSObject",
        b"applicationDidInstallWithMetadata:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"applicationDidUpdateWithMetadata:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"backgroundDownloadDidFail:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"backgroundDownloadDidFinish:fileURL:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"checkForUpdatesWithMetadata:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"download:didReceiveChallenge:completionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"q"},
                            2: {"type": b"@"},
                        },
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"download:didWriteBytes:totalBytesWritten:totalBytesExpectedToWrite:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"q"},
                4: {"type": b"q"},
                5: {"type": b"q"},
            },
        },
    )
    r(
        b"NSObject",
        b"download:failedWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"download:finishedWithFileURL:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"downloadDidBegin:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"downloadDidPause:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"extensionWillTerminate",
        {"required": False, "retval": {"type": b"v"}},
    )
    r(
        b"NSObject",
        b"receivedAuthenticationChallenge:download:completionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"q"},
                            2: {"type": b"@"},
                        },
                    },
                    "type": b"@?",
                },
            },
        },
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
