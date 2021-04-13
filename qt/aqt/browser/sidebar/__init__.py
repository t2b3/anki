# Copyright: Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
import sys

import aqt
from anki.utils import isMac
from aqt.theme import theme_manager


def _want_right_border() -> bool:
    return not isMac or theme_manager.night_mode


from .item import SidebarItem, SidebarItemType
from .model import SidebarModel
from .searchbar import SidebarSearchBar
from .toolbar import SidebarTool, SidebarToolbar
from .tree import SidebarStage, SidebarTreeView

# alias for the legacy pathname
sys.modules["aqt.sidebar"] = sys.modules["aqt.browser.sidebar"]
aqt.sidebar = sys.modules["aqt.browser.sidebar"]  # type: ignore
