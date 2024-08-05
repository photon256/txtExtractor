#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "29570994"))
    API_HASH = os.environ.get("API_HASH", "0480448e375c4d248fb32535e01f3438")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6851245012")
