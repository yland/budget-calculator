import json
import unittest

from main import app
# set our application to testing mode
app.testing = True


class Testmain(unittest.TestCase):

    def test_add_income(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sent = {'inc':'myincome','amt':100}
            response = client.post('/add_income', data=json.dumps(sent), content_type='application/json')

            # check result from server with expected data
            #data = json.loads(response.get_data(as_text=True))

            self.assertEqual(response.data,json.dumps(sent))
              