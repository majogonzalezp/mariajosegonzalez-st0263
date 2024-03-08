from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class listFilesSended(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, file: _Optional[_Iterable[str]] = ...) -> None: ...

class confirmation(_message.Message):
    __slots__ = ("status_code",)
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    status_code: str
    def __init__(self, status_code: _Optional[str] = ...) -> None: ...
