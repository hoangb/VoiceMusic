import unittest

class TestMethods(unittest.TestCase):

    def testcase_run_voice_command(self):
        try:
            from app import handle_speech as speech_module

            start = speech_module.AudioHandle()
            start.record()
        except ImportWarning:
            pass

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

    def setUp(self):
        print("\n----> Running:", self._testMethodName)

    def tearDown(self):
        print("---->End.")


if __name__ == '__main__':
    unittest.main()