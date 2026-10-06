import hou
from PySide6 import QtWidgets

def create_geo():
    pwin = hou.qt.mainWindow()
    
    presets = ["geo1", "asset", "fx", "model", "rnd"]

    item, is_ok = QtWidgets.QInputDialog.getItem(
        pwin, "Fast Geo", "Choose Name Geo:", presets, 0, False
    )

    if not is_ok or not item:
        return

    current_pane = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
    
    if current_pane and current_pane.currentNode(): parent_node = current_pane.currentNode().parent()
    else: parent_node = hou.node("/obj")

    if parent_node.path() == "/": parent_node = hou.node("/obj")

    existing_node = parent_node.node(item)
    
    if existing_node:
        hou.ui.displayMessage(f"Node with name '{item}' already exists in this context.")
        
        return

    with hou.undos.group("Create Preset Geo Node"):
        geo = parent_node.createNode("geo", item)
        
        geo.setSelected(False)
        geo.setSelectableInViewport(False)
        
        geo.moveToGoodPosition()
        geo.setConnectionDrawStyle(hou.nodeConnectionDrawStyle.Rounded)
    
create_geo()
