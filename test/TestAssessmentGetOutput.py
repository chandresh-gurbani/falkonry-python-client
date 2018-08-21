import os
import unittest
import json
import xmlrunner

host       = os.environ['FALKONRY_HOST_URL']               # host url
token      = os.environ['FALKONRY_TOKEN']                  # auth token
assessment = os.environ['FALKONRY_ASSESSMENT_SLIDING_ID']  # assessment id


class TestAssessmentGetOutput(unittest.TestCase):

    def setUp(self):
        pass

    @unittest.skip("streaming can only be done once ")
    def test_get_assessment_output(self):
        fclient = FClient(host=host, token=token,options=None)

        try:
            stream = fclient.get_output(assessment, {})
            for event in stream.events():
                print(json.dumps(json.loads(event.data)))

        except Exception as e:
            print(exception_handler(e))
            self.assertEqual(0, 1, 'Error getting output of a Assessment')

    @unittest.skip("streaming can only be done once ")
    def test_get_assessment_output_with_offset(self):
        fclient = FClient(host=host, token=token,options=None)
        try:
            stream = fclient.get_output(assessment, {"offset": 10})

            receivedOutput = False
            for event in stream.events():
                self.assertEqual(json.loads(event.data)['offset'] >= 10, True)
                print(json.dumps(json.loads(event.data)))
                receivedOutput = True
            self.assertEquals(receivedOutput, True)
        except Exception as e:
            print(exception_handler(e))
            self.assertEqual(0, 1, 'Error getting output of a Assessment')


    def test_get_assessment_historical_output(self):
        fclient = FClient(host=host, token=token,options=None)
        try:
            options = {'startTime':'2011-01-02T01:00:00.000Z','endTime':'2013-06-13T01:00:00.000Z','responseFormat':'application/json'}
            response = fclient.get_historical_output(assessment, options)
            '''If data is not readily available then, a tracker id will be sent with 202 status code. While falkonry will genrate ouptut data
             Client should do timely pooling on the using same method, sending tracker id (__id) in the query params
             Once data is available server will response with 200 status code and data in json/csv format.'''

            if response.status_code is 202:
                trackerResponse = Schemas.Tracker(tracker=json.loads(response.text))

                # get id from the tracker
                trackerId = trackerResponse.get_id()

                # use this tracker for checking the status of the process.
                options = {"trackerId": trackerId, "responseFormat":"application/json"}
                newResponse = fclient.get_historical_output(assessment, options)

                # if status is 202 call the same request again

            if response.status_code is 200:
                # if status is 200, output data will be present in response.text field
                self.assertEqual(len(response.text) > 0, True, 'Error getting historical output of a Assessment')
        except Exception as e:
            print(exception_handler(e))
            self.assertEqual(0, 1, 'Error getting output of a Assessment')

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(
            path.dirname(
                path.dirname(
                    path.abspath(__file__)
                )
            )
        )
        from falkonryclient import schemas as Schemas
        from falkonryclient import client as FClient
        from falkonryclient.helper.utils import exception_handler

    else:
        from ..falkonryclient import schemas as Schemas
        from ..falkonryclient import client as FClient
        from ..falkonryclient.helper.utils import exception_handler

    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='out'),
        failfast=False, buffer=False, catchbreak=False)
else:
    from falkonryclient import schemas as Schemas
    from falkonryclient import client as FClient
    from falkonryclient.helper.utils import exception_handler
