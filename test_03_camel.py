from unittest import TestCase
camel = __import__('03_camel')

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):
        self.assertTrue(camel.camel('Hello world'))
        self.assertEqual('helloWorld', camel.camel('Hello world'))
        self.assertEqual('thisIsATestSentence', camel.camel('tHis is A Test sEnTEnCe'))
        self.assertEqual('whatIsTheMeaningOfLife', camel.camel('What is the Meaning of Life'))

    def test_camelcase_special_characters(self):
        self.assertIn('ValueError', camel.camel('Hello world***'))
        self.assertIn('ValueError', camel.camel('$pecia! C%aracters'))
        self.assertIn('ValueError', camel.camel('882424824825'))
        with self.assertRaises(TypeError):
            camel.camel(882424824825)
