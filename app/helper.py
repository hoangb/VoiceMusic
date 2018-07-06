import os

class HelperFunctions:
    @staticmethod
    def parse_client_key_file():
        """
        Read client_key.txt file and return the private keys
        :return: Return a 2-item list that contains ClientID and ClientSecret
        """
        key_set = []
        client_key_path = os.path.dirname(os.path.abspath(__file__)) + "/client_key.txt"
        with open(client_key_path) as f:
            for i in [line.rstrip('\n') for line in f]:
                key_set.append(i.split("=")[1])
        return key_set

