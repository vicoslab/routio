
# Proof-of-concept test for different Python version communication

routio_router

docker run -ti --rm -v  "`realpath tests/python2/script.py`:/script.py:ro" -v /tmp/routio.sock:/tmp/routio.sock routio:old python script.py a b

docker run -ti --rm -v  "`realpath tests/python2/script.py`:/script.py:ro" -v /tmp/routio.sock:/tmp/routio.sock routio python script.py b a