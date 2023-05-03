import os
import logging

class Config:    
    API_ID = 28298577
    API_HASH = "143efc9236a955d630ede2642578b251"
    OWNER_ID = "5163706369"
    SESSION = "BQGLytsAiiFTvQBTgSLVTTUTQSLplW4jJZ1ue454uw6lAkFHhODXCDcx1m6Jv9ZwbDChPXpXfSYQAKnT3lt3H1lXUXxf4A2v5lnBd70WUIdky1lDmq_kDRYztBctWQIuYT6U-Cma9QMiSU8AL0NHOfgd4IwHLisDsttRj2-q-OKgf7zde5UR0fvSmWLbtX7pEYnDXwxuoSQxVBF4XpModSKoc_V_2vyM5lRBc8Ic9C2U5z0vHVS-eT1fDkojupxZuAYRYwfK9bfezBMk_vda0-6UEgMTeHKZR3y0LzobENSwZVtvloUq67XlVdHGzvFyhVYEPDzsYdp62T0XL0GdFyf9xwYYEQAAAAF171rrAA"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
