import os
import logging

class Config:    
    API_ID = 28298577
    API_HASH = "143efc9236a955d630ede2642578b251"
    OWNER_ID = "5163706369"
    SESSION = "BQGLytsAIXjUSY_RdoJv5zhB7E-v9dUWmtQyYO-xymuy0Pyfqy7kcUCrnH8Gt2K6nj-M8FJ71m0fdI-mGxmxGjBRxgGzc72a7Tv62VL-v6B-RdIDN6OxnI2fP8O6vtD1lwo2t02VkypRpxbEfsPHS_LPWDR9jalpck3h2GRg2hKSoOGLy_dT5NsSNVBe4hLTqf2E4_O_phi8Py8SIFkKETsESC4vQFonXUeBYs_CXCpbxwR3ESnmfPIYzpRcaWUNlSfg6WbWXjlpAh8lUBFkk4kem1O74qr85APsnCmWvFfCxkSjT3Tf0m0LKN4QXOZ6o6s-qIWTHt7wKZzANjzGb-uisL9_rwAAAAF171rrAA"
    
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
