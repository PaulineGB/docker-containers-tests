import os
import unittest
import requests

class TestAuthorization(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_address = os.getenv('API_ADDRESS')
        cls.api_port = os.getenv('API_PORT')

    users = [
        ('alice', 'wonderland'),
        ('bob', 'builder')
    ]
    versions = ['v1', 'v2']

    def test_authorization(self):
        for username, password in self.users:
            for version in self.versions:
                response = requests.get(
                    url='http://{address}:{port}/{version}/sentiment'.format(
                        address=self.api_address,
                        port=self.api_port,
                        version=version
                    ),
                    params= {
                        'username': username,
                        'password': password,
                        'sentence': 'Hello there!'
                    }
                )

                self.output(username, password, response.status_code, version)
                self.assertEqual(response.status_code, 200)


    def output(self, username, password, status_code, version):
        output = '''
        ============================
            Authorization test
        ============================

        request done at "/{version}/sentiment"
        | username={username}
        | password={password}

        expected result = 200
        actual restult = {status_code}

        ==>  {test_status}

        '''

        # affichage des résultats
        test_status = 'SUCCESS' if status_code == 200 else 'FAILURE'
        print(output.format(
            test_status=test_status,
            status_code=status_code,
            username=username,
            password=password,
            version=version
        ))

        # impression dans un fichier
        if os.environ.get('LOG') == '1':
            with open('api_test.log', 'a') as file:
                file.write(output)

if __name__ == '__main__':
    unittest.main()
