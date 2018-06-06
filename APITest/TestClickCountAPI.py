import unittest
import sys
import argparse
import random

import requests

_WEBAPP_ADDR = None
_WEBAPP_PORT = 80


class TestClickCountAPI(unittest.TestCase):

    def setUp( self ):
        self.webappBaseAddr = "{0}:{1}".format( _WEBAPP_ADDR, _WEBAPP_PORT )

    def tearDown( self ):
        pass

    # Validate the webapp 'healthcheck' GET API.
    def test_HealthCheck( self ):
        # Make a 'healthcheck' GET request and check its ok.
        url = "{}/clickCount/rest/healthcheck".format( self.webappBaseAddr )
        r = requests.get( url )
        self.assertTrue( r.ok )

        # Validate the request returned plain text.
        self.assertEqual( r.text, "ok" )

    # Validate the webapp 'click' GET API.
    def test_ClickGet( self ):
        # Make a 'click' GET request and check its ok.
        url = "{}/clickCount/rest/click".format( self.webappBaseAddr )
        r = requests.get( url )
        self.assertTrue( r.ok )

        # Validate the returned counter format.
        i = int( r.text )
        self.assertGreaterEqual( i, 0 )

    # Validate the webapp 'click' POST API.
    def test_ClickAdd( self ):
        # Make a 'click' POST request and check its ok.
        url = "{}/clickCount/rest/click".format( self.webappBaseAddr )
        r = requests.post( url )
        self.assertTrue( r.ok )

        # Validate the returned counter format.
        firstCounter = int( r.text )
        self.assertGreaterEqual( firstCounter, 0 )

        # Make some other 'click' POST requests and check the returned counter is well incremented.
        nbIters = random.randrange( 10, 50 )
        for i in range( nbIters ):
            r = requests.post( url )
            self.assertTrue( r.ok )
            self.assertTrue( int(r.text), firstCounter+i )

        # Check now with a GET that the counter is at the expected value.
        r = requests.get( url )
        self.assertTrue( r.ok )
        self.assertEqual( int(r.text), firstCounter+nbIters )

        # Validate the returned counter format.
        i = int( r.text )
        self.assertGreaterEqual( i, 0 )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument( '--webappAddr', default='localhost' )
    parser.add_argument( '--webappPort', default=80, type=int )
    parser.add_argument( 'unittest_args', nargs='*' )

    args = parser.parse_args()
    _WEBAPP_ADDR = args.webappAddr
    _WEBAPP_PORT = args.webappPort

    # Set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
    sys.argv[1:] = args.unittest_args
    unittest.main()
