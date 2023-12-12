from PySide6.QtWidgets import QTableWidgetItem

def addObjective(TableZone, Objectives):
  row = TableZone.table.rowCount()
  TableZone.table.insertRow(row)
  TableZone.table.setItem(row, 0, QTableWidgetItem(Objectives.startTime.text()))
  TableZone.table.setItem(row, 1, QTableWidgetItem(Objectives.endTime.text()))
  TableZone.table.setItem(row, 2, QTableWidgetItem(Objectives.minHour.text()))
  TableZone.table.setItem(row, 3, QTableWidgetItem(Objectives.zone.currentText()))
  TableZone.table.setItem(row, 4, QTableWidgetItem(Objectives.nextDay.currentText()))

def deleteLastObjective(TableZone):
  TableZone.table.removeRow(TableZone.table.rowCount()-1)
