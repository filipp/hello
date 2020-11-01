#!/usr/bin/env python
import os
import sys
import requests

def main(arg=None):
    repo = os.getenv("HELLO_REPO")
    assert repo is not None, "No repo configured!"

    templates = []
    for t in requests.get(repo).json():
        templates.append(t['name'])

    if arg is None:
        return templates

    if arg in templates:
        url = "{0}/{1}".format(repo.rstrip("/"), arg)
        template = requests.get(url).text
        return template
    else:
        error = "Template for {0} not found".format(arg)
        raise Exception(error)


if __name__ == '__main__':
    print(main(sys.argv[1]))
