import os
import unittest
import requests

class TestContent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_address = os.getenv('API_ADDRESS')
        cls.api_port = os.getenv('API_PORT')

    username = 'alice'
    password = 'wonderland'
    sentences = [
        ('life is beautiful', 'positive'),
        ('that sucks', 'negative')
    ]
    versions = ['v1', 'v2']

    def test_content(self):
        for version in self.versions:
            for sentence, score in self.sentences:
                response = requests.get(
                    url='http://{address}:{port}/{version}/sentiment'.format(
                        address=self.api_address,
                        port=self.api_port,
                        version=version
                    ),
                    params= {
                        'username': self.username,
                        'password': self.password,
                        'sentence': sentence
                    }
                )

                response_score = response.json()['score']
                return_score = 'positive' if response_score > 0 else 'negative'
                test_status = 'SUCCESS' if return_score == score else 'FAILURE'

                self.output(version, self.username, self.password, sentence, score, return_score, test_status)

                self.assertEqual(return_score, score)

    def output(self, version, username, password, sentence, score, return_score, test_status):
        output = '''
        ============================
            Content test
        ============================

        request done at "/{version}/sentiment"
        | username={username}
        | password={password}
        | sentence={sentence}

        expected result = {score}
        actual restult = {return_score}

        ==>  {test_status}

        '''

        # affichage des résultats
        print(output.format(
            version=version,
            username=username,
            password=password,
            sentence=sentence,
            score=score,
            return_score=return_score,
            test_status=test_status
        ))

        # impression dans un fichier
        if os.environ.get('LOG') == '1':
            with open('api_test.log', 'a') as file:
                file.write(output)

if __name__ == '__main__':
    unittest.main()