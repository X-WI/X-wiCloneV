import os
import logging

class Config:    
    API_ID = 28298577
    API_HASH = "143efc9236a955d630ede2642578b251"
    OWNER_ID = "5163706369"
    SESSION = "BQBvZ14AT2IzyLnGe9gmRnFMVzQUVSBKLyTzbjjSYFMWLqmis-BzmmJW3Uzy9YOvz-FPZRp9yXZnkY7FHJsesYJN2CvbsA4ZHu1oJB1QKXo47hn_kP0EkJ8E0g07s5vlU6Aa6xp1iHW0eEbIy6_qj5tsKOtVxoIF1FNGrp-J3naTndcNb29O754GZHkslpboZxCtFgfMrMMSPWxPtS0fommU__FdJ315UhWbarWlBM8wLyHzJ8wLHlhE4YtBMcxQiup4m8Qajef3cwV2ODp3XuOfjO8jHg4rxUjwcx5MLB-MqfmZOtsbCTgtA4CWoU_jgexRNTsYxt7a0J5iBBn3Qt6qwRfLfQAAAAFHRbVuAA"


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
