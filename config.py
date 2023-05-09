import os
import logging

class Config:    
    API_ID = 28298577
    API_HASH = "143efc9236a955d630ede2642578b251"
    OWNER_ID = "5163706369"
    SESSION = "BQGLytsAts7Y4iDR1zzBGicWv4Zcmfxr4c8g5GMdTX5NNEfoXFBQvmeeJfZ7ZQZHh3dQWjdONQVCVF0vQh7r3ELVVNcx30Zo2nbjwzR52l9pGNrS5Q9CWovRwCgDJ1J9DNLzqmJG2DBqPGoBih7VHrTOpK22DrC-GC4Q7yH-xSEXElUi9KQ4mUn4JHv0gJCZW3mgSIhl9RBz2Mj2oc9iu8rIcEFXm6S_hl8Se_bl9yYxnrpEyJeE66PKlrEHs-wr_f-7DYig-KVSE9_TCkx2pu5CABwiMfFwjApilSAVId7dyNDXMf9mm_bzbvZzuYUUKDg_SpSWpSxdTTTii6-bm62MyOEmqwAAAAF171rrAA"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
