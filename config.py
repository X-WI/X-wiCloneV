import os
import logging

class Config:
    
    API_ID = 28298577
    API_HASH = "143efc9236a955d630ede2642578b251"
    BOT_TOKEN = "5773135086:AAHQ0s6IDn697XQGcJaTa8U2CVCjGUn1ilI"
    BOT_SESSION = "bot" 
    CAPTION = "@HQFilms4U"
    FROM_CHANNEL = -1001667023505 #https://t.me/ ccgfdjhdjjgdsd
    FILTER_TYPE = "document"
    OWNER_ID = "5163706369"
    LIMIT = 2
    SKIP_NO = 0
    SESSION = "BQE7yJ4AMnvRMQBPSFlQ5Fs1eby7TAsAWgKHCvtauFl1DdDMGWJ3E4KHigL-oDyhjZf-Erq1MESTAKuL5aTEInC2t9K_EvqlKuZwq7_PhY2wRFPMkX8QWmd4a8N3U8RsBTCqjGd7RwwnH2ovtS0PRC2NHdAYX2OhBjEcluEz4T79waMG8e6-zcK8K6sF-88MZ9AvBfbdszL1T1bRYpv_9ZKNKoJqOIPa_ovYrj27Gm8N9rIEKJZBkF6-RvPUXFvCGE6y_gZVMJSIwv2eRPBrRcKf_yQ-N-0qNU1pchQpeCL0ZWKalE4dgYdUepkMVvuAHAuJFtTmeBFUTfIMZ1izlUFBtRd1BAAAAAFhHqYjAA"  
    TO_CHANNEL = -1001925446238
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
