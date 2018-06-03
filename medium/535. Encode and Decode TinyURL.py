"""
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""

import string
import random


class Codec:
    def __init__(self):
        self.lookup = {}
        self.sub_url = "http://tinyurl.com/"

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        ss = string.ascii_letters + string.digits

        def to_6():
            result = []
            for _ in range(6):
                result += ss[random.randint(0, 61)]
            return "".join(result)

        key = to_6()
        while key in self.lookup:
            key = to_6()
        self.lookup[key] = longUrl
        return self.sub_url + key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.lookup[shortUrl[len(self.sub_url):]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
