## Introduction

hello is a boilerplate repository.

## Requirements

- nginx with _autoindex_ on and _autoindex_format_ set to _json_ for the repo directory:

    server {
        listen       8080;
        server_name  localhost;

        location / {
            root   /Users/filipp/Projects/hello/templates;
            autoindex on;
            autoindex_format json;
        }
    }

- the _requests_ HTTP client library (which everyone probably already has installed). _pip install -r requirements.txt_ to install.

## Setup

- Put your boilerplate on a web server
- Export an environment variabled called _HELLO_REPO_ which points to the directory that contains your boilerplate templates


## Usage

Run _hello.py_ with boilerplate name or without the name to get a list of available templates

The boilerplate templates get rendered with all your environment variables as context so feel free to use stuff like $HOME or $PWD or $USER or whatever inside them.

'Nuff said.

## FAQ

- Why not do this as a snippet collection for <insert editor name here>?
- I keep switching between 4 different editors so I needed something a bit more universal.

## License

Copyright © 2020 Filipp Lepalaan <filipp@mac.com>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.
