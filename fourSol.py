from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUi
from productDB import DBHandle
class OtherDlg:
    def __init__(self):
        self.dlg = loadUi('fdlg.ui')
        self.dbHandle = DBHandle()
        self.dlg.pushButtonInput.clicked.connect(self.dlgClose)
        self.dlg.exec()
    def dlgClose(self):
        j = self.dlg.lineEditJepoom.text()
        c = self.dlg.spinBoxCount.value()
        d = self.dlg.dateEditProduct.date()
        ds = f'{d.year()}-{d.month()}-{d.day()}'
        self.dbHandle.insertData(j,c,ds)
        self.dlg.close()
class MyDlg:
    def __init__(self):
        self.dlg = loadUi('four.ui')
        self.dbHandle = DBHandle()
        self.dlg.actioninput.triggered.connect(self.btnClick)
        self.dlg.actionview.triggered.connect(self.btnView)
        self.dlg.show()
    def btnClick(self):
        odlg = OtherDlg()
    def btnView(self):
        self.dlg.tableWidget.setRowCount( 0 )
        for j,c,d in self.dbHandle.selectData():
            self.addTableData(j,c,d)
    def addTableData(self,jepoom, pcount, pdate):
        nRow = self.dlg.tableWidget.rowCount()
        self.dlg.tableWidget.setRowCount( nRow+1 )
        self.dlg.tableWidget.setItem(nRow,0,QTableWidgetItem(jepoom))
        self.dlg.tableWidget.setItem(nRow,1,QTableWidgetItem(str(pcount)) )
        self.dlg.tableWidget.setItem(nRow,2,QTableWidgetItem(pdate))

app = QApplication( sys.argv )
my = MyDlg()
app.exec()

