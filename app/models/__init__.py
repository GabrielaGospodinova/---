# In-memory storage
festivals = []
artists = []
stages = []
performances = []

# ID counters
festival_id_counter = 1
artist_id_counter = 1
stage_id_counter = 1
performance_id_counter = 1

# Helper functions to get next ID
def get_next_festival_id():
    global festival_id_counter
    festival_id_counter += 1
    return festival_id_counter - 1

def get_next_artist_id():
    global artist_id_counter
    artist_id_counter += 1
    return artist_id_counter - 1

def get_next_stage_id():
    global stage_id_counter
    stage_id_counter += 1
    return stage_id_counter - 1

def get_next_performance_id():
    global performance_id_counter
    performance_id_counter += 1
    return performance_id_counter - 1 