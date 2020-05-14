import redis
from bitmath import Byte, best_prefix

redis_pre_ccpa = redis.Redis()
redis_post_ccpa = redis.Redis(db=1)

binary_keys = redis_pre_ccpa.keys("*")
user_count = 0
keys = []
pre_ccpa_memory_usage = 0
post_ccpa_memory_usage = 0

for k in binary_keys:
    key_string = k.decode("utf-8")
    if ":" not in key_string:
        user_count += 1
    keys.append(key_string)

for key in keys:
    pre_ccpa_memory_usage += redis_pre_ccpa.memory_usage(key)
    post_ccpa_memory_usage += redis_post_ccpa.memory_usage(key)

scale = round(post_ccpa_memory_usage/pre_ccpa_memory_usage, 2)
pre_ccpa_memory_usage = (Byte(pre_ccpa_memory_usage)).best_prefix()
post_ccpa_memory_usage = (Byte(post_ccpa_memory_usage)).best_prefix()

print("number of users: {}".format(user_count))
print("pre ccpa memory usage: {}".format(pre_ccpa_memory_usage))
print("post ccpa memory usage: {}".format(post_ccpa_memory_usage))
print("scale = {}".format(scale))