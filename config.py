import os
from os import getenv
import logging

class Config:
    
    API_ID = 16448144
    API_HASH = "1073665850700150caf0e0cbb68216a2"
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    BOT_SESSION = "bot" 
    FROM_CHANNEL = -1001667023505 #https://t.me/ ccgfdjhdjjgdsd
    FILTER_TYPE = "document"
    OWNER_ID = "5163706369"
    SESSION = getenv("SESSION", "")
    TO_CHANNEL = -1001925446238    
#    FILTERGROUP_1_ID = -1001589825618
#    FILTERGROUP_2_ID = -1001556192813
    SEARCHCHANNEL_ID = -1001556192813
    ADMINS = [5163706369, 'TheLx0980', 1533128706]
    GROUPS = [-1001556192813, -1001589825618]

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
