# qlib
[![Build Status](https://travis-ci.org/bnbalsamo/qlib.svg?branch=master)](https://travis-ci.org/bnbalsamo/qlib)  [![Coverage Status](https://coveralls.io/repos/github/bnbalsamo/qlib/badge.svg?branch=master)](https://coveralls.io/github/bnbalsamo/qlib?branch=master)

v0.0.1

A library, shared amongst repository microservices, which handles logic utilizing
"unreliable" priority queues.

## Wait a second, unreliable?

Unreliable in this sense means this library, by design, does not implement the redis
[reliable queue](https://redis.io/commands/rpoplpush) pattern. This is meant to simplify 
the code base in cases where a "reliable" queue isn't required because losing a task
is both a rare occurence, and not a breaking error when/if it does occur.
