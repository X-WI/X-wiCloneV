import os
import logging

class Config:
    
    API_ID = 28298577
    API_HASH = "143efc9236a955d630ede2642578b251"
    BOT_TOKEN = "5068899226:AAE4Mvrssd7mE3MqaimG8ziE32edmr_Mgh0"
    BOT_SESSION = "bot" 
    CAPTION = None
    FROM_CHANNEL = "@bdbdhdhvh"
    FILTER_TYPE = "document"
    OWNER_ID = "1903280447"
    LIMIT = 2
    SKIP_NO = 0
    SESSION = "BQBWwwbTREQ6bu1Opb_kHsRqpjvYZsw34NXM--FFIWaKIvIGUl4aq269KKGgxw7b7bRsIZ8gsLkRISDMnYT3xrbWS82PvR_PV3rL_bmuz_OeNFsa_Iql91cQM9FA4z1Huv_68sarER3NSCizwC2QkL4QtbmQ21bxZCMnpeb8iYxb-yBGkaqSqXWxbUzTUCABY74pcCr46HG9comat6Z-6IfwRaHgEprkDzjGkBXUFFcmoLde75qtKXMRpA77xYN_uI2qRekBcQKnmRXsGoI9Mmh4Q4DkKWzFpTF9c57VaxNdzvrRVw_ROSC5kz84iGdpF91D-BQ-5z28lcfi0VwCZ8b_AAAAAWHA4M8A"
    TO_CHANNEL = -1001641840781
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
