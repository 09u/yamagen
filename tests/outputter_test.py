import unittest

from src.yamagen.yamagen import EmailAddress, Outputter


class OutputterTest(unittest.TestCase):

    def test_outputer(self):
        address1 = EmailAddress('info', 'test.com')
        address2 = EmailAddress('ofni', 'tset.moc')
        addresses = []
        addresses.append(address1)
        outputer1 = Outputter(addresses)

        self.assertIsNotNone(outputer1)

        self.assertEqual(outputer1.Message(), 'Outputter has 1 e-mail address.')

        addresses.append(address2)

        outputer2 = Outputter(addresses)
        
        self.assertIsNotNone(outputer2)

        self.assertEqual(outputer2.Message(), 'Outputter has 2 e-mail addresses.')
        self.assertEqual(outputer2.JSON(), '[{"0": "info@test.com"}, {"1": "ofni@tset.moc"}]')
