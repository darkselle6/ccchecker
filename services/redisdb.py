import time
from aioredis import Redis
from datetime import datetime
import asyncio
import json
#from services.log import log

redis = Redis(host='redis-17214.c257.us-east-1-3.ec2.cloud.redislabs.com', port=17214, password='cK7LKcElC77E6dS961hoY5VEdtswignP', encoding= 'utf-8', decode_responses= True)

 
# # log.info("Redis Started")
# x = {
#   "ch": [
#     "✅",
#     "Corvus",
#     "20-Jan-2022"
#   ],
#   "ck": [
#     "✅",
#     "Crater",
#     "15-Jan-2022"
#   ],
#   "sa": [
#     "✅",
#     "Andromeda",
#     "16-Jan-2022"
#   ],
#   "sc": [
#     "✅",
#     "Antlia",
#     "20-Jan-2022"
#   ],
#   "sd": [
#     "✅",
#     "Apus",
#     "20-Dec-2021"
#   ],
#   "se": [
#     "✅",
#     "Aquarius",
#     "20-Dec-2021"
#   ],
#   "sf": [
#     "✅",
#     "Aquila",
#     "20-Dec-2021"
#   ],
#   "sg": [
#     "✅",
#     "Ara",
#     "20-Dec-2021"
#   ],
#   "sh": [
#     "✅",
#     "Aries",
#     "20-Dec-2021"
#   ],
#   "si": [
#     "✅",
#     "Auriga",
#     "20-Dec-2021"
#   ],
#   "sl": [
#     "✅",
#     "Bootes",
#     "21-Jan-2022"
#   ],
#   "sm": [
#     "✅",
#     "Caelum",
#     "20-Dec-2021"
#   ],
#   "sn": [
#     "✅",
#     "Camelopardalis",
#     "20-Jan-2022"
#   ],
#   "so": [
#     "✅",
#     "Cancer",
#     "20-Dec-2021"
#   ],
#   "sp": [
#     "✅",
#     "Venatici",
#     "20-Jan-2022"
#   ],
#   "sr": [
#     "✅",
#     "Canis",
#     "20-Dec-2021"
#   ],
#   "ss": [
#     "✅",
#     "Capricornus",
#     "20-Dec-2021"
#   ],
#   "st": [
#     "✅",
#     "Carina",
#     "20-Dec-2021"
#   ],
#   "su": [
#     "✅",
#     "Cassiopeia",
#     "20-Dec-2021"
#   ],
#   "sv": [
#     "✅",
#     "Centaurus",
#     "20-Dec-2021"
#   ],
#   "sw": [
#     "✅",
#     "Cepheus",
#     "20-Dec-2021"
#   ],
#   "sx": [
#     "✅",
#     "Cetus",
#     "20-Jan-2022"
#   ],
#   "mch": [
#     "✅",
#     "Mass Charge",
#     "20-Jan-2022"
#   ],
#   "sy": [
#     "✅",
#     "Circinus",
#     "20-Dec-2021"
#   ],
#   "sz": [
#     "✅",
#     "Columba",
#     "31-Dec-2021"
#   ],
#   "msk": [
#     "✅",
#     "Stripe Key Mass",
#     "24-Dec-2021"
#   ],
#   "za": [
#     "❌",
#     "Cygnus",
#     "21-Jan-2022",
#     "Api problems"
#   ],
#   "bt": [
#     "✅",
#     "Delphinus",
#     "19-Jan-2022"
#   ],
#   "zc": [
#     "✅",
#     "Dorado",
#     "17-Jan-2022"
#   ],
#   "ze": [
#     "✅",
#     "Draco",
#     "27-Dec-2021"
#   ],
#   "ad": [
#     "✅",
#     "Adyen",
#     "05-Jan-2022"
#   ],
#   "ba": [
#     "✅",
#     "Braintree",
#     "30-Dec-2021"
#   ],
#   "vbv": [
#     "✅",
#     "Braintree VBV Lookup",
#     "04-Jan-2022"
#   ],
#   "br": [
#     "✅",
#     "Braintree",
#     "04-Jan-2022"
#   ],
#   "sho": [
#     "✅",
#     "Shopify+b3",
#     "18-Jan-2022"
#   ],

#   "msa": [
#     "✅",
#     " Stripe Mass Check",
#     "18-Jan-2022"
#   ],
#   "mass": [
#     "✅",
#     "Mass Chk",
#     "18-Jan-2022"
#   ],
#   "au": [
#     "✅",
#     "Authorize",
#     "19-Jan-2022"
#   ]
# }
x = [5197853005]
xx = json.dumps(x)


try:
    # asyncio.run(redis.set("admins", rval))
    asyncio.run(redis.set("admins", xx))
    x  = asyncio.run(redis.get("admins"))
    # x = asyncio.run(redis.set(1317173146,time.time()))
    # x = asyncio.run(redis.set(1317173146,time.time()))
    print(x)
    # print(json.loads(x))
except Exception as e:
    print(e)