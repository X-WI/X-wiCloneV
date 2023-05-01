import os
import logging

class Config:
    
    API_ID = 28298577
    API_HASH = "143efc9236a955d630ede2642578b251"
    BOT_TOKEN = "5068899226:AAGrSpHXOetSe-q_YSL4Sa6ghs2hhdn2Ls4"
    BOT_SESSION = "bot" 
    CAPTION = "@HQFilms4U"
    FROM_CHANNEL = "@ccgfdjhdjjgdsd" #https://t.me/ ccgfdjhdjjgdsd
    FILTER_TYPE = "document"
    OWNER_ID = "5163706369"
    LIMIT = 2
    SKIP_NO = 0
    SESSION = "AgD6-pAAZhxCSeHVma067tyno87XQKvHC_nUoidLAYJ-qxl9_u5-u6qgAE8CxpbTrqDj1dOhy9QOkiy7zTBhsJ9c9gLFNrJx_yIeh4coPVuwNhvnmyI03JRPNR7Fl6UJhMF5l_JW2p_iNQwvIBzwmsr77WmI3KCtBgC_PV315C3wv82ZCiQhmnBQhVS-Kzyt1_3EG3wt9Be-1TRejdkdn-hN75QBT9z9slKktcUe6_sfzoYIWcDuL9yajo1NIOE3JCghHTpoazFx7jesKAIT3jbEOvYvTc0AddfWTGzFLRbOKnBPao6Lk7nToNdbpQGpkqmu1XSmWu_sO8Ghj65yQHEjMKnsXwAAAAEzx-gBAA"
    TO_CHANNEL = -1001986761426
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
