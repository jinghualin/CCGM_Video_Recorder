from typing import Optional
from PySide6.QtCore import QObject, Property, Signal
class Media(QObject):
    def __init__(self, parent: Optional[QObject] = ...) -> None:
        super().__init__(parent)
        self._header_video_name :str = None
        self._tail_video_name: str = None
        