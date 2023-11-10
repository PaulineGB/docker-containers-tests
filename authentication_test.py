import os
import unittest
import requests

class TestAuthentication(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_address = os.getenv('API_ADDRESS')
        cls.api_port = os.getenv('API_PORT')

    users = [
        ('alice', 'wonderland'),
        ('bob', 'builder'),
        ('clementine', 'mandarine')
    ]

    def test_authentication(self):
        for username, password in self.users:
            response = requests.get(
                url='http://{address}:{port}/permissions'.format(
                    address=self.api_address,
                    port=self.api_port
                ),
                params= {
                    'username': username,
                    'password': password
                }
            )

            self.output(username, password, response.status_code)
            self.assertEqual(response.status_code, 200)

    def output(self, username, password, status_code):
        output = '''
        ============================
            Authentication test
        ============================

        request done at "/permissions"
        | username={username}
        | password={password}

        expected result = 200
        actual restult = {status_code}

        ==>  {test_status}

        '''

        # affichage des résultats
        test_status = 'SUCCESS' if status_code == 200 else 'FAILURE'
        print(output.format(
            status_code=status_code,
            test_status=test_status,
            username=username,
            password=password
        ))

        # impression dans un fichier
        if os.environ.get('LOG') == '1':
            with open('api_test.log', 'a') as file:
                file.write(output)

if __name__ == '__main__':
    unittest.main()
