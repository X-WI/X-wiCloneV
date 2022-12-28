import os
import logging

class Config:
    
    API_ID = 7961171
    API_HASH = "b2d798626afaf5f1e4bdb33988e3d377"
    BOT_TOKEN = "5456442427:AAFkdG2kRm0L5WOpPFwGs0T7-PfSfxk8hQk"
    BOT_SESSION = "bot" 
    CAPTION = "@HQFilms4U"
    FROM_CHANNEL = "@Databaseforfiles"
    FILTER_TYPE = "document"
    OWNER_ID = "1903280447"
    LIMIT = 2
    SKIP_NO = 0
    SESSION = "BQAqF1SaLd6nvP30wx4BgHcB2R3MbDTgONmSValVw4uIWhnS1ePLD3sPiHFuDaY5VndwwNrntpWb1monSUJ2jKPkWWsdCCDFeh7VOFT9Q0HhDvTaHQCyk_Lr5ydvRY_A620qI86UfxluYVQAu7F07XAmVgLXo_k_Ko2A7eUWYkqmWOwASxC_sSX_Eq1JQDudo8ZhHetCYhPmYXzns21DVu-U0LRDfRPnoyoPy5IdS-VxT9swnosNDC-ftVINkECS1g86YBKZkXc3yjDdCBnD3dxy9H4e1jU26ssA0XtJAkZZV1Qu-HSIqrEJXnGbkKlsaNm0E0JX5-wngehRfVntXXJgAAAAAT2AioUA" 
    TO_CHANNEL = -1001520485890
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
