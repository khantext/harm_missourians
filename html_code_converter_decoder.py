"""HTML Code Converter/Decoder

This script allows the perpetrator to hack a web site by
converting and decoding its HTML code. It is of particular use for
unauthorized users who wish to harm Missourians.

It uses a multi-step process which allows the hacker to obtain
data that is not freely available.

Note that the state of Missouri will likely not take this matter
lightly. Further, that they may not rest until they clearly understand
your intentions.

This script requires that `requests` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * convert_and_decode_the_code - a multi-step process
    * harm_missourians - 'nuff said
"""

import requests


URL_TO_HACK = "https://web.archive.org/web/20210814172757/https://apps.dese.mo.gov/HQT/CredentialListerChecker.aspx"


def convert_and_decode_the_code(code):
    """Convert and decode the code to reveal its secrets."""
    return code.text


def harm_missourians(url_to_hack):
    """Perpetrate and attempt to steal the personal information
    of educators from the great state of Missouri.
    """
    r = requests.get(url_to_hack)
    revealed_data = convert_and_decode_the_code(code=r)
    print(revealed_data)


if __name__ == "__main__":
    harm_missourians(url_to_hack=URL_TO_HACK)