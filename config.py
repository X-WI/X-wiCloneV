import os
import logging

class Config:
    
    API_ID = 28298577
    API_HASH = "143efc9236a955d630ede2642578b251"
    BOT_TOKEN = "5068899226:AAE4Mvrssd7mE3MqaimG8ziE32edmr_Mgh0"
    BOT_SESSION = "bot" 
    CAPTION = "@HQFilms4U"
    FROM_CHANNEL = "@Databaseforfiles"
    FILTER_TYPE = "document"
    OWNER_ID = "1903280447"
    LIMIT = 2
    SKIP_NO = 0
    SESSION = "BQAbcBp7IplE9_BJIw05yKC7WZIoUDTFbnXfDLGyIYFpq76tfLLDtlqcfRyZ3rTBgtRxKrZhvsxh1DVzdhxekQuX73dmodoLM8WapEGu390jUb5vHP4y73RwgbHYFYiilMx_FFa60LHH6K1DGzhlk0dvnVn1X634zHvdpW0nmXYhMwH0nUghqSzgXPIJaE_AVHx2ZzMBv-XVluDZZJJIg2Tr2eCg8SNifCz22WJWGbM3VcGm-7VJt6S4wgoAyntndgJx9jvRvpCuOGBJ1h2YdypVh-KDRwpak_4CHubx1NTvYtDzgDzA4grO0UaO1JWURvBvl5I0zUWe2jC2IeSBgj0qAAAAAWHA4M8A"
    TO_CHANNEL = -1001563098453
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
