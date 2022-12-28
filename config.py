import os
import logging

class Config:
    
    API_ID = 7961171
    API_HASH = "b2d798626afaf5f1e4bdb33988e3d377"
    BOT_TOKEN = "5456442427:AAFkdG2kRm0L5WOpPFwGs0T7-PfSfxk8hQk"
    BOT_SESSION = "bot" 
    CAPTION = "@HQFilms4U"
    FROM_CHANNEL = -1001739094949
    FILTER_TYPE = "document"
    OWNER_ID = "1903280447"
    SESSION = "BQApALVWt7H5irNNBjQqgg9pv41x18w2FqIEFnof3EGR5zP-cHkZwurnv79QGdx9HmPkg_dykLU2mQbyu48eYtP9LG_gOVentcJG6lMG51Od-rszYH1bw1hQoTAh1vXcet5d3u5z-kDuGzO3H-87NrBOeaq3IyVebTZZA0BXPEC6XqYVbUE00Skii5znbICcIDV67xeO8RPpUp6tLZAImpt7YcH21gne8DXUtInBgA2-yzEj_pVB06IFcG2SGjll6j9BvOtmQ_Bgpqr6OodAGxKKbCe0AhvJjqc3QbVdk5ny29VrBdKgSgxKJvSCSWW5PEqf2Dm4pYiwdhpaJovYlDEtAAAAAT2AioUA"
    TO_CHANNEL = -1001520485890
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
