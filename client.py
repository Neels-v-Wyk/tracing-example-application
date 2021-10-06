# import psycopg2
import random
import time
import requests

from ddtrace import tracer
from random import shuffle

logins = [
    ('munozjames', '!FPj)W15!7'),
    ('hamiltonconnie', 'Z0d$Yezu+0'),
    ('vincent90', '__Z%3crh6U'),
    ('hector17', 'i!qXZJ%!#5'),
    ('monicamurphy', 'r_(*5Rv8)M'),
    ('wandarichards', '*3dX7YGeQP'),
    ('angela01', 'Yl$8WmGn46'),
    ('teresa45', '$A6UJeVCM#'),
    ('grayrobert', '_1QYuIv70C'),
    ('browndebbie', 'j7ULmwyl*0'),
    ('meyermelissa', '*a6q!Ducpw'),
    ('alyssaflowers', '&T%5+Dshbc'),
    ('patricia30', 'O_d0*YFe$K'),
    ('kristinabaxter', 'B)9tBsq02Q'),
    ('alicia92', 'YGMRxEgb#3'),
    ('lalexander', 'x5Q0a@k)+)'),
    ('deanstephanie', '_8H5WdQqym'),
    ('julia66', 'THQXpuO&%6'),
    ('ruizpatrick', '#+9#UN#uHM'),
    ('david87', 'u%3dM4UfI0'),
    ('padillatyler', 'Vp_6KFQuH+'),
    ('wellsjoseph', '3B3G)NpP^Y'),
    ('lindaherrera', 'D6E7csFM#1'),
    ('michael54', 'U5sL&2Jn^X'),
    ('aking', 'k)X3KjbV_8'),
    ('jeffreyfaulkner', 'w4D(ogjj$e'),
    ('debraaustin', 'ZD+wV9Mr2s'),
    ('jacksonedward', '&965zS4a80'),
    ('cruzmichelle', '!0ktPm&eJc'),
    ('galvanjohn', '3nYS(ola(8'),
]
shuffle(logins)

while True:
    start_time = time.time()
    login = random.choice(logins)
    r = requests.post('http://server:5000/api/login', json={'username': login[0], 'password': login[1]})
    end_time = time.time()

    print(f"Tried to log in with {login=}, response was {r.ok=}, and it took {end_time - start_time} seconds")
