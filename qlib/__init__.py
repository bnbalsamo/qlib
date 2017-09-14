"""
qlib
"""
import redis
from abc import ABCMeta, abstractmethod

__author__ = "Brian Balsamo"
__email__ = "brian@brianbalsamo.com"
__version__ = "0.0.1"


class Queue(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, service_name, host, port=6379, dbnum=0):
        self.service_name = service_name
        self.redis = redis.StrictRedis(
            host=host,
            port=port,
            db=dbnum
        )


class UnreliablePriorityQueue(Queue):
    def __init__(self, service_name, host, port=6379, dbnum=0):
        super().__init__(service_name, host, port=port, dbnum=dbnum)

    def _gen_queue_key(self, priority):
        if int(priority) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            raise ValueError("Priority must be an int such that 0 < priority < 10")
        return self.service_name+"::"+str(priority)

    def _gen_queue_keys(self):
        return [self.service_name+"::"+str(x) for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]]

    def add_identifier(self, identifier, priority=9):
        return self.redis.lpush(self._gen_queue_key(priority), identifier)

    def retrieve_identifier(self, block=0):
        if block is not False:
            if block is True:
                block = 0
            q = self.redis.brpop(self._gen_queue_keys(), timeout=block)
            if q:
                return q[1].decode("utf-8")
            else:
                return None
        else:
            for x in self._gen_queue_keys():
                q = self.redis.rpop(x)
                if q:
                    return q.decode("utf-8")
            return None
