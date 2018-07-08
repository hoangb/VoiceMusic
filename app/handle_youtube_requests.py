import urllib as u
from urllib import parse, request
from bs4 import BeautifulSoup


class YoutubeHandle:
    _youtube_base_url = "https://www.youtube.com/"
    _youtube_search = "results?search_query="

    def __init__(self, query):
        """
        Initializing object will query for first youtube video and store its video_id
        """
        build_url = "{}{}".format(self._youtube_base_url + self._youtube_search, u.parse.quote(query + " official"))
        response = u.request.urlopen(build_url)

        display_result_html = response.read()
        soup = BeautifulSoup(display_result_html)

        first_result = soup.findAll(attrs={'class': 'yt-uix-tile-link'})[0]
        self.video_id = first_result['href'].split("/watch?v=")[1]

    def get_video_id(self):
        """
        :return: Queried video ID
        """
        return self.video_id

    def get_embedded_link_source(self):
        """
        :return: Generate a iframe suitable link
        """
        return "{}embed/{}".format(self._youtube_base_url, self.video_id);
