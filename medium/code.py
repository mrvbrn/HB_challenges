"""TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl 
and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""

class Codec:
    def __init__(self):
        self.url_to_code={}
        self.code_to_url={}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        letters = string.ascii_letters+string.digits
        while longUrl not in self.url_to_code:
            code = "".join([random.choice(letters) for _ in range(6)])
            if code not in self.code_to_url:
                self.url_to_code[longUrl]=code
                self.code_to_url[code]=longUrl
            return self.url_to_code[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.code_to_url[shortUrl[-6:]]
        
