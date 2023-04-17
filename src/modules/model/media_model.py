from typing import Optional
from PySide6.QtCore import QObject, Property, Signal


class Media(QObject):
    header_video_path_changed: Signal = Signal()
    music_path_changed: Signal = Signal()

    def __init__(self, parent: Optional[QObject] = ...) -> None:
        super().__init__(parent)
        self._header_video_path: str = None
        self._tail_video_name: str = None
        self._music_path: str = None

    @Property(str, notify=header_video_path_changed)
    def header_video_path(self) -> str:
        return self._header_video_path

    @header_video_path.setter
    def header_video_path(self, path) -> None:
        self._header_video_path = path

    @Property(str, notify=music_path_changed)
    def music_path(self) -> str:
        return self._music_path

    @music_path.setter
    def music_path(self, path: str) -> None:
        self._music_path = path
