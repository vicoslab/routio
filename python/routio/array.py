from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from builtins import super
from future import standard_library
standard_library.install_aliases()
from routio import _wrapper

class ArraySubscriber(_wrapper.Subscriber):

    def __init__(self, client, alias, callback):
        def _read(message):
            reader = _wrapper.MessageReader(message)
            return _wrapper.readArray(reader)

        super().__init__(client, alias, "array", lambda x: callback(_read(x)))

class ArrayPublisher(_wrapper.Publisher):

    def __init__(self, client, alias):
        super().__init__(client, alias, "array")

    def send(self, obj):
        writer = _wrapper.MessageWriter()
        _wrapper.writeArray(writer, obj)
        super().send(writer)

class TensorSubscriber(_wrapper.Subscriber):

    def __init__(self, client, alias, callback):
        def _read(message):
            reader = _wrapper.MessageReader(message)
            return _wrapper.readTensor(reader)

        super().__init__(client, alias, "tensor", lambda x: callback(_read(x)))

class TensorPublisher(_wrapper.Publisher):

    def __init__(self, client, alias):
        super().__init__(client, alias, "tensor")

    def send(self, obj):
        writer = _wrapper.MessageWriter()
        _wrapper.writeTensor(writer, obj)
        super().send(writer)