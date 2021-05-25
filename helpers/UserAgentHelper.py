import numpy as np

class UserAgentHelper:

    def __init__(self):
        print("")
    
    def get_random_ua(self):
        random_ua = ''
        ua_file = '/var/www/ecomercy-api/api/scraper/helpers/user-agents.txt'
        try:
            with open(ua_file) as f:
                lines = f.readlines()
            if len(lines) > 0:
                prng = np.random.RandomState()
                index = prng.permutation(len(lines) - 1)
                idx = np.asarray(index, dtype=np.integer)[0]
                random_ua = lines[int(idx)]
        except Exception as ex:
            print('Exception in random_ua')
            print(str(ex))
        finally:
            return random_ua.replace('\n', '')