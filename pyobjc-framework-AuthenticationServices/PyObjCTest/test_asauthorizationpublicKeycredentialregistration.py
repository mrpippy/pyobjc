import AuthenticationServices  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestASAuthorizationPublicKeyCredentialRegistration(TestCase):
    @min_sdk_level("12.0")
    def test_constants12_0(self):
        self.assertProtocolExists("ASAuthorizationPublicKeyCredentialRegistration")
