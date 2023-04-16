from pathlib import Path

from typing import Optional
from PySide6.QtCore import QObject, Property, Signal

class Preach(QObject):
    """Class prividing data to QML UI about preach info and preacher"""

    def __init__(self, parent: Optional[QObject] = ...) -> None:
        """Constructor"""
        super().__init__(parent)
        self._preach_date = None
        self._preach_title:str=None
        self._bible:str = None
        self._preacher_name :str = None
        self._head_description:str = None

    
    @Property(str)
    def preach_date(self):
        return self._preach_date

    @preach_date.setter
    def preach_date(self, date)-> None:
        self._preach_date = date
    
    @Property(str)
    def tail_description(self):
        return """
        曼海姆华人基督教会\n
        date主日讲道《{self._preach_title}》\n
        {self._preacher_name}\n\n
        更多讲道和信息请关注官方主页：\n
        www.ccgm-mannheim.de"""

