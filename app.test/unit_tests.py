import unittest


class TestMethods(unittest.TestCase):

    def test_receive_youtube_urls(self):
        import urllib as u
        from urllib import parse, request
        from bs4 import BeautifulSoup

        youtube_search_url = "https://www.youtube.com/results?search_query="
        build_url = "{}{}".format(youtube_search_url, u.parse.quote("drake i'm upset"))
        response = u.request.urlopen(build_url)
        display_result_html = response.read()
        soup = BeautifulSoup(display_result_html)

        first_result = soup.findAll(attrs={'class': 'yt-uix-tile-link'})[0]
        self.assertEqual("rIhx2wZ8jnA", first_result['href'].split("/watch?v=")[1])

    def test_yt_request_object(self):
        from app import handle_youtube_requests as youtube_requests
        query = youtube_requests.YoutubeHandle("Drake I'm upset")
        self.assertIn("rIhx2wZ8jnA", query.get_embedded_link_source())

    def test_try_run_voice_command(self):
        try:
            from app import handle_speech as speech_module

            start = speech_module.AudioHandle()
            start.record()
        except ImportWarning:
            pass

    def test_try_spotify_non_authorized_requests(self):
        import spotipy
        spotify = spotipy.Spotify()
        try:
            results = spotify.search(q='artist: Drake', type='artist')
            print(results)
        except Exception as e:
            print("Unauthorized: ".format(e))

    def test_parse_correct_client_values(self):
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
