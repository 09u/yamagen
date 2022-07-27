import unittest

from src.yamagen.yamagen import EmailAddress


class EmailAddressTest(unittest.TestCase):

    def test_should_get_email_address(self):
        address = EmailAddress('info', 'test.com')

        # then
        self.assertIsNotNone(address)

        self.assertEqual(address.get(), 'info@test.com')
        self.assertEqual(str(address), 'info@test.com')

