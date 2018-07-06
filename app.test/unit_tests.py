import unittest
from app import helper
from app import handle_speech as speech_module

class TestMethods(unittest.TestCase):
    def setUp(self):
        print("\n----> Running:", self._testMethodName)

    def tearDown(self):
        print("\n")




    def testcase_spotify_non_authorized_requests(self):
        import spotipy
        spotify = spotipy.Spotify()
        try:
            results = spotify.search(q='artist: Drake', type='artist')
            print(results)
        except Exception as e:
            print("Unauthorized: ".format(e))


    def testcase_parse_correct_client_values(self):
        client_key_path = "../app/client_key.txt"
        with open(client_key_path) as f:
            key_set = [line.rstrip('\n') for line in f]

        for i in key_set:
            i = i.split("=")[1]
            print(i)






if __name__ == '__main__':
    unittest.main()