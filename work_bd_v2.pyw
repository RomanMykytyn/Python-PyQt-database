from PyQt5.QtCore import Qt, QDate, QEvent
from PyQt5.QtWidgets import (QApplication, QDialog, QDialogButtonBox,
                             QHBoxLayout, QVBoxLayout, QMessageBox, QPushButton,
                             QTableView, QWidget, QComboBox, QLabel,
                             QDateEdit, QCalendarWidget, QMessageBox, QAbstractItemView,
                             QMenuBar,QAction, QMainWindow, QSizePolicy, QLineEdit,
                             QTextEdit, QInputDialog, QTabWidget, QSpinBox, QCheckBox,
                             QLineEdit, QGridLayout, QBoxLayout)
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase

import time



def connect():
       global db
       db=QSqlDatabase.addDatabase('QSQLITE')
       db.setDatabaseName('work_bd.db')
       db.setConnectOptions('QSQLITE_BUSY_TIMEOUT=10000')
       if not db.open():
              a=db.isOpen()
              print(a)
              QMessageBox.critical(None,"Cannot open database",
                                   "Unable to establish a database connection",
                                   QMessageBox.Cancel)
              return False
       return True
       
      

class work_bd(QMainWindow):
       def __init__(self, tableName, parent=None):
              super(work_bd, self).__init__(parent)
              connect()
              widget=QWidget()
              self.setCentralWidget(widget)             
              self.model = QSqlTableModel(self)
              self.model.setTable(tableName)
              self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
              
              global model_client
              self.model_client = QSqlTableModel(self)
              self.model_client.setTable('client')
              self.model_client.setEditStrategy(QSqlTableModel.OnManualSubmit)
              self.model_client.select()
              while self.model_client.canFetchMore() == True:
                     self.model_client.fetchMore()

              global model_device
              self.model_device = QSqlTableModel(self)
              self.model_device.setTable('device')
              self.model_device.setEditStrategy(QSqlTableModel.OnManualSubmit)
              self.model_device.select()

              self.model_engineer = QSqlTableModel(self)
              self.model_engineer.setTable('engineer')
              self.model_engineer.setEditStrategy(QSqlTableModel.OnManualSubmit)
              self.model_engineer.select()

              global model_rar
              self.model_rar=QSqlTableModel(self)
              self.model_rar.setTable('workbd_rar')
              self.model_rar.setEditStrategy(QSqlTableModel.OnManualSubmit)
              self.model_rar.select()
                            
              self.model.setHeaderData(0, Qt.Horizontal,'ID')
              self.model.setHeaderData(1, Qt.Horizontal,'№')
              self.model.setHeaderData(2, Qt.Horizontal,'Клієнт')
              self.model.setHeaderData(3, Qt.Horizontal,'Пристрій')
              self.model.setHeaderData(4, Qt.Horizontal,'Дата')
              self.model.setHeaderData(5, Qt.Horizontal,'Примітка')
              self.model.setHeaderData(6, Qt.Horizontal,'Дата ремонту')
              self.model.setHeaderData(7, Qt.Horizontal,'Інженер')
              self.model.setHeaderData(8, Qt.Horizontal,'Дата видачі з ремонту')
              self.model.setHeaderData(9, Qt.Horizontal,'Звіт по ремонту')
              self.model.setHeaderData(10, Qt.Horizontal,'Ціна ремонту')
              self.model.setHeaderData(11, Qt.Horizontal,'Дата оплати')
              self.model.setHeaderData(12, Qt.Horizontal,'Дата відправлення')
                     
              self.view = QTableView()
              self.view.setModel(self.model)
              self.view.setColumnWidth(1,50)
              self.view.setColumnWidth(5,200)
              self.view.setShowGrid(True)
              self.view.setSelectionMode(QAbstractItemView.SingleSelection)
              self.view.setSelectionBehavior(QAbstractItemView.SelectRows)
              self.view.setWordWrap(True)
              self.view.resizeRowsToContents()
              self.view.setColumnHidden(0, True)
              self.view.setColumnHidden(6, True)
              self.view.setColumnHidden(7, True)
              self.view.setColumnHidden(8, True)
              self.view.setColumnHidden(9, True)
              self.view.setColumnHidden(10, True)
              self.view.setColumnHidden(11, True)
              self.view.setColumnHidden(12, True)
              self.view.setColumnHidden(13, True)
              
              self.view_repair=QTableView()
              self.view_repair.setModel(self.model)
              self.view_repair.setShowGrid(True)
              self.view_repair.setSelectionMode(QAbstractItemView.SingleSelection)
              self.view_repair.setSelectionBehavior(QAbstractItemView.SelectRows)
              self.view_repair.setWordWrap(True)
              self.view_repair.resizeRowsToContents()
              self.view_repair.setColumnHidden(0, True)
              self.view_repair.setColumnHidden(4, True)
              self.view_repair.setColumnHidden(5, True)
              self.view_repair.setColumnHidden(8, True)
              self.view_repair.setColumnHidden(9, True)
              self.view_repair.setColumnHidden(10, True)
              self.view_repair.setColumnHidden(11, True)
              self.view_repair.setColumnHidden(12, True)
              self.view_repair.setColumnHidden(13, True)

              self.view_finished=QTableView()
              self.view_finished.setModel(self.model)
              self.view_finished.setShowGrid(True)
              self.view_finished.setSelectionMode(QAbstractItemView.SingleSelection)
              self.view_finished.setSelectionBehavior(QAbstractItemView.SelectRows)
              self.view_finished.setWordWrap(True)
              self.view_finished.resizeRowsToContents()
              self.view_finished.setColumnHidden(0, True)
              self.view_finished.setColumnHidden(4, True)
              self.view_finished.setColumnHidden(5, True)
              self.view_finished.setColumnHidden(6, True)
              self.view_finished.setColumnHidden(7, True)
              
              self.view_finished.setColumnHidden(11, True)
              self.view_finished.setColumnHidden(12, True)
              self.view_finished.setColumnHidden(13, True)

              self.view_prepaid=QTableView()
              self.view_prepaid.setModel(self.model)
              self.view_prepaid.setShowGrid(True)
              self.view_prepaid.setSelectionMode(QAbstractItemView.SingleSelection)
              self.view_prepaid.setSelectionBehavior(QAbstractItemView.SelectRows)
              self.view_prepaid.setWordWrap(True)
              self.view_prepaid.resizeRowsToContents()
              self.view_prepaid.setColumnHidden(0, True)
              self.view_prepaid.setColumnHidden(4, True)
              self.view_prepaid.setColumnHidden(5, True)
              self.view_prepaid.setColumnHidden(6, True)
              self.view_prepaid.setColumnHidden(7, True)
              self.view_prepaid.setColumnHidden(8, True)
              self.view_prepaid.setColumnHidden(9, True)
              self.view_prepaid.setColumnHidden(10, True)
              self.view_prepaid.setColumnHidden(12, True)
              self.view_prepaid.setColumnHidden(13, True)

              self.view_given=QTableView()
              self.view_given.setModel(self.model)
              self.view_given.setShowGrid(True)
              self.view_given.setSelectionMode(QAbstractItemView.SingleSelection)
              self.view_given.setSelectionBehavior(QAbstractItemView.SelectRows)
              self.view_given.setWordWrap(True)
              self.view_given.resizeRowsToContents()
              self.view_given.setColumnHidden(0, True)
              self.view_given.setColumnHidden(4, True)
              self.view_given.setColumnHidden(5, True)
              self.view_given.setColumnHidden(6, True)
              self.view_given.setColumnHidden(7, True)
              self.view_given.setColumnHidden(8, True)
              self.view_given.setColumnHidden(9, True)
              self.view_given.setColumnHidden(10, True)
              self.view_given.setColumnHidden(11, True)
              self.view_given.setColumnHidden(13, True)

              self.bt_1=QPushButton('Прийняти пристрій')
              self.bt_2=QPushButton('Видалити')
              self.bt_exit=QPushButton('Вихід')
              self.bt_repair=QPushButton('Ремонт')
              self.bt_info=QPushButton('Інформація')
              self.bt_giveout=QPushButton('Видати пристрій')
              self.bt_giveout.hide()

              buttonBox=QVBoxLayout()
              buttonBox.addWidget(self.bt_1)
              buttonBox.addWidget(self.bt_repair)
              buttonBox.addWidget(self.bt_giveout)
              buttonBox.addWidget(self.bt_info)
              buttonBox.addWidget(self.bt_2)
              buttonBox.addWidget(self.bt_exit)
              buttonBox.setSpacing(15)
              buttonBox.addStretch(1)
              buttonBox.insertSpacing(4,35)

              self.bt_1.clicked.connect(self.f_bt_1)
              self.bt_2.clicked.connect(self.delete)
              self.bt_exit.clicked.connect(sys.exit)
              self.bt_repair.clicked.connect(self.f_repair)
              self.bt_info.clicked.connect(self.f_info)
              self.bt_giveout.clicked.connect(self.f_giveout)

              self.tab=QTabWidget()
              self.tab.addTab(self.view,'Прийняті пристрої')
              self.tab.addTab(self.view_repair,'Ремонт')
              self.tab.addTab(self.view_finished,'Відремонтовані пристрої')
              self.tab.addTab(self.view_prepaid,'Оплачений ремонт')
              self.tab.addTab(self.view_given,'Виданий клієнту')
              self.tab.currentChanged.connect(self.changeTab)
              #self.select_row_tab()
              self.changeTab(0)

              mainLayout=QHBoxLayout()
              mainLayout.addWidget(self.tab)
              mainLayout.addLayout(buttonBox)
              widget.setLayout(mainLayout)

              self.actexit=QAction('Вихід',self,triggered=self.close)
              self.addClient=QAction('Відкрити клієнтську базу даних',
                                     self,triggered=self.baseClient)
              self.addDevice=QAction('Відкрити базу даних пристоїв',
                                     self,triggered=self.baseDevice)
              self.addEngineer=QAction('Відкрити базу даних інженерів',
                                     self,triggered=self.baseEngineer)
              self.archiv=QAction('Архів',self,triggered=self.baseArchiv)

              self.menufile=self.menuBar().addMenu('Файл')
              self.menufile.addAction(self.addClient)
              self.menufile.addAction(self.addDevice)
              self.menufile.addAction(self.addEngineer)
              self.menufile.addAction(self.archiv)
              self.menufile.addSeparator()
              self.menufile.addAction(self.actexit)

              self.setWindowTitle('База даних "ДВБ Вендінг"')
              
              #self.adjustSize()
              self.setGeometry(40,40,800,300)
              #db.close()

              '''row=self.model.rowCount()
              date=time.gmtime()
              month_now=date[1]
              
              while row >= 0:
                     if self.model.record(row).value(12):
                            month=self.model.record(row).value(12)
                            month=int(month[3:5])
                            if month != month_now:
                                   
                                   row_rar=self.model_rar.rowCount()
                                   self.model_rar.insertRow(row_rar)
                                   count=1
                                   
                                   while count<=12:
                                          self.model_rar.setData(self.model_rar.index(row_rar, count),
                                                                 self.model.record(row).value(count))
                                          count=count+1
                                   self.model_rar.submitAll()
                                   self.model.removeRow(row)
                                   self.model.submitAll()
                                   self.select_row_tab()
                     row=row-1'''
             
              
       def f_info(self):
              connect()
              self.dialog_window=QWidget(window, Qt.Dialog)
              self.dialog_window.setWindowTitle('Загальна інформація')
              self.dialog_window.setWindowModality(Qt.WindowModal)
              self.dialog_window.setAttribute(Qt.WA_DeleteOnClose, True)

              self.bt_edit=QPushButton('Правка')
              self.bt_edit.clicked.connect(self.f_edit)
              self.bt_edit.setCheckable(True)
              #bt_edit.setChecked(True)
              bt_exit=QPushButton('Вихід')
              bt_exit.clicked.connect(self.dialog_window.close)
              self.buttons=QDialogButtonBox(Qt.Horizontal)
              self.buttons.addButton(self.bt_edit,QDialogButtonBox.ActionRole)
              self.buttons.addButton(bt_exit,QDialogButtonBox.ActionRole)

              #self.model_client.select()
              #while self.model_client.canFetchMore():
                  #self.model_client.fetchMore()

              self.l_number=QLabel()
              self.l_number.setText('№')
              self.le_number=QLineEdit()
              self.le_number.setReadOnly(True)
              
              self.l_device=QLabel()
              self.l_device.setText('Пристрій')
              self.le_device=QLineEdit()
              self.le_device.setReadOnly(True)
              
             
              self.l_client=QLabel()
              self.l_client.setText('Прізвище')
              self.le_client=QLineEdit()
              self.le_client.setReadOnly(True)

              self.l_client_name=QLabel()
              self.l_client_name.setText("Ім'я")
              self.le_client_name=QLineEdit()
              self.le_client_name.setReadOnly(True)

              self.l_client_secondname=QLabel()
              self.l_client_secondname.setText('По батькові')
              self.le_client_secondname=QLineEdit()
              self.le_client_secondname.setReadOnly(True)

              self.l_client_city=QLabel()
              self.l_client_city.setText('Місто')
              self.le_client_city=QLineEdit()
              self.le_client_city.setReadOnly(True)

              self.l_client_post=QLabel()
              self.l_client_post.setText('Пошта №')
              self.le_client_post=QLineEdit()
              self.le_client_post.setReadOnly(True)

              self.l_client_phone=QLabel()
              self.l_client_phone.setText('Телефон')
              self.le_client_phone=QLineEdit()
              self.le_client_phone.setReadOnly(True)
              
              self.l_client_note=QLabel()
              self.l_client_note.setText('Примітка \nпо клієнту')
              self.le_client_note=QTextEdit()
              self.le_client_note.setReadOnly(True)
              
                               
              self.l_date_in=QLabel()
              self.l_date_in.setText('Дата отримання')
              self.le_date_in=QLineEdit()
              self.le_date_in.setReadOnly(True)
              
              self.l_date_repair=QLabel()
              self.l_date_repair.setText('Дата ремонту')
              self.le_date_repair=QLineEdit()
              self.le_date_repair.setReadOnly(True)

              self.l_engineer=QLabel()
              self.l_engineer.setText('Інженер')
              self.le_engineer=QLineEdit()
              self.le_engineer.setReadOnly(True)

              self.l_date_out=QLabel()
              self.l_date_out.setText('Виданий з ремонту')
              self.le_date_out=QLineEdit()
              self.le_date_out.setReadOnly(True)

              self.l_rapair_note=QLabel()
              self.l_rapair_note.setText('Перелік робіт')
              self.le_rapair_note=QTextEdit()
              self.le_rapair_note.setReadOnly(True)

              self.l_price=QLabel()
              self.l_price.setText('Ціна ремонту')
              self.le_price=QLineEdit()
              self.le_price.setReadOnly(True)

              self.l_pay=QLabel()
              self.l_pay.setText('Дата оплати')
              self.le_pay=QLineEdit()
              self.le_pay.setReadOnly(True)

              self.l_send=QLabel()
              self.l_send.setText('Дата видачі')
              self.le_send=QLineEdit()
              self.le_send.setReadOnly(True)

              self.l_note=QLabel()
              self.l_note.setText('Примітка \nпо пристрою')
              self.le_note=QTextEdit()
              self.le_note.setReadOnly(True)
             
              
              if self.bt_repair.text()=='Ремонт':
                     self.le_number.setText(str(self.model.record(self.view.currentIndex().row()).value(1)))
                     self.le_device.setText(str(self.model.record(self.view.currentIndex().row()).value(3)))
                     self.le_date_in.setText(str(self.model.record(self.view.currentIndex().row()).value(4)))
                     self.le_date_repair.setText(str(self.model.record(self.view.currentIndex().row()).value(6)))
                     self.le_note.setText(str(self.model.record(self.view.currentIndex().row()).value(5)))
                     self.le_rapair_note.setEnabled(False)
                     self.le_date_repair.setEnabled(False)
                     self.le_engineer.setEnabled(False)
                     self.le_date_out.setEnabled(False)
                     self.le_price.setEnabled(False)
                     self.le_pay.setEnabled(False)
                     self.le_send.setEnabled(False)
                     row=self.model_client.rowCount()-1
                     while row>=0:
                            if self.model.record(self.view.currentIndex().row()).value(2)==self.model_client.record(row).value(1):
                                   self.le_client.setText(self.model_client.record(row).value(1))
                                   self.le_client_name.setText(self.model_client.record(row).value(2))
                                   self.le_client_secondname.setText(self.model_client.record(row).value(3))
                                   self.le_client_city.setText(self.model_client.record(row).value(4))
                                   self.le_client_post.setText(str(self.model_client.record(row).value(5)))
                                   self.le_client_phone.setText(str(self.model_client.record(row).value(6)))
                                   self.le_client_note.setText(self.model_client.record(row).value(7))
                                   break
                            row=row-1
              elif self.bt_repair.text()=='Відремонтований':
                     self.le_number.setText(str(self.model.record(self.view_repair.currentIndex().row()).value(1)))
                     self.le_device.setText(str(self.model.record(self.view_repair.currentIndex().row()).value(3)))
                     self.le_date_in.setText(str(self.model.record(self.view_repair.currentIndex().row()).value(4)))
                     self.le_date_repair.setText(str(self.model.record(self.view_repair.currentIndex().row()).value(6)))
                     self.le_engineer.setText(self.model.record(self.view_repair.currentIndex().row()).value(7))
                     self.le_rapair_note.setText(str(self.model.record(self.view_repair.currentIndex().row()).value(9)))
                     self.le_note.setText(str(self.model.record(self.view_repair.currentIndex().row()).value(5)))
                     self.le_rapair_note.setEnabled(False)
                     self.le_date_out.setEnabled(False)
                     self.le_price.setEnabled(False)
                     self.le_pay.setEnabled(False)
                     self.le_send.setEnabled(False)
                     row=self.model_client.rowCount()-1
                     while row>=0:
                            if self.model.record(self.view_repair.currentIndex().row()).value(2)==self.model_client.record(row).value(1):
                                   self.le_client.setText(self.model_client.record(row).value(1))
                                   self.le_client_name.setText(self.model_client.record(row).value(2))
                                   self.le_client_secondname.setText(self.model_client.record(row).value(3))
                                   self.le_client_city.setText(self.model_client.record(row).value(4))
                                   self.le_client_post.setText(str(self.model_client.record(row).value(5)))
                                   self.le_client_phone.setText(str(self.model_client.record(row).value(6)))
                                   self.le_client_note.setText(self.model_client.record(row).value(7))
                                   break
                            row=row-1
              elif self.bt_repair.text()=='Оплачений':
                     self.le_number.setText(str(self.model.record(self.view_finished.currentIndex().row()).value(1)))
                     self.le_device.setText(str(self.model.record(self.view_finished.currentIndex().row()).value(3)))
                     self.le_date_in.setText(str(self.model.record(self.view_finished.currentIndex().row()).value(4)))
                     self.le_date_repair.setText(str(self.model.record(self.view_finished.currentIndex().row()).value(6)))
                     self.le_engineer.setText(self.model.record(self.view_finished.currentIndex().row()).value(7))
                     self.le_date_out.setText(str(self.model.record(self.view_finished.currentIndex().row()).value(8)))
                     self.le_rapair_note.setText(str(self.model.record(self.view_finished.currentIndex().row()).value(9)))
                     self.le_price.setText(str(self.model.record(self.view_finished.currentIndex().row()).value(10)))
                     self.le_note.setText(str(self.model.record(self.view_finished.currentIndex().row()).value(5)))
                     self.le_rapair_note.setReadOnly(False)
                     self.le_price.setReadOnly(False)
                     self.le_pay.setEnabled(False)
                     self.le_send.setEnabled(False)
                     row=self.model_client.rowCount()-1
                     while row>=0:
                            if self.model.record(self.view_finished.currentIndex().row()).value(2)==self.model_client.record(row).value(1):
                                   self.le_client.setText(self.model_client.record(row).value(1))
                                   self.le_client_name.setText(self.model_client.record(row).value(2))
                                   self.le_client_secondname.setText(self.model_client.record(row).value(3))
                                   self.le_client_city.setText(self.model_client.record(row).value(4))
                                   self.le_client_post.setText(str(self.model_client.record(row).value(5)))
                                   self.le_client_phone.setText(str(self.model_client.record(row).value(6)))
                                   self.le_client_note.setText(self.model_client.record(row).value(7))
                                   break
                            row=row-1
                     
              elif self.bt_repair.text()=='Видати':
                     self.le_number.setText(str(self.model.record(self.view_prepaid.currentIndex().row()).value(1)))
                     self.le_device.setText(str(self.model.record(self.view_prepaid.currentIndex().row()).value(3)))
                     self.le_date_in.setText(str(self.model.record(self.view_prepaid.currentIndex().row()).value(4)))
                     self.le_date_repair.setText(str(self.model.record(self.view_prepaid.currentIndex().row()).value(6)))
                     self.le_engineer.setText(self.model.record(self.view_prepaid.currentIndex().row()).value(7))
                     self.le_date_out.setText(str(self.model.record(self.view_prepaid.currentIndex().row()).value(8)))
                     self.le_rapair_note.setText(str(self.model.record(self.view_prepaid.currentIndex().row()).value(9)))
                     self.le_price.setText(str(self.model.record(self.view_prepaid.currentIndex().row()).value(10)))
                     self.le_pay.setText(str(self.model.record(self.view_prepaid.currentIndex().row()).value(11)))
                     self.le_note.setText(str(self.model.record(self.view_prepaid.currentIndex().row()).value(5)))
                     self.le_rapair_note.setReadOnly(False)
                     self.le_price.setReadOnly(False)
                     if self.le_send.setText(str(self.model.record(self.view_given.currentIndex().row()).value(12))):
                            self.le_send.setEnabled(True)
                     else : self.le_send.setEnabled(False)
                     
                     row=self.model_client.rowCount()-1 
                     while row>=0:
                            if self.model.record(self.view_prepaid.currentIndex().row()).value(2)==self.model_client.record(row).value(1):
                                   self.le_client.setText(self.model_client.record(row).value(1))
                                   self.le_client_name.setText(self.model_client.record(row).value(2))
                                   self.le_client_secondname.setText(self.model_client.record(row).value(3))
                                   self.le_client_city.setText(self.model_client.record(row).value(4))
                                   self.le_client_post.setText(str(self.model_client.record(row).value(5)))
                                   self.le_client_phone.setText(str(self.model_client.record(row).value(6)))
                                   self.le_client_note.setText(self.model_client.record(row).value(7))
                                   break
                            row=row-1
              elif self.bt_repair.text()=='Оплатити':
                     
                     self.le_number.setText(str(self.model.record(self.view_given.currentIndex().row()).value(1)))
                     self.le_device.setText(str(self.model.record(self.view_given.currentIndex().row()).value(3)))
                     self.le_date_in.setText(str(self.model.record(self.view_given.currentIndex().row()).value(4)))
                     self.le_date_repair.setText(str(self.model.record(self.view_given.currentIndex().row()).value(6)))
                     self.le_engineer.setText(self.model.record(self.view_given.currentIndex().row()).value(7))
                     self.le_date_out.setText(str(self.model.record(self.view_given.currentIndex().row()).value(8)))
                     self.le_rapair_note.setText(str(self.model.record(self.view_given.currentIndex().row()).value(9)))
                     self.le_price.setText(str(self.model.record(self.view_given.currentIndex().row()).value(10)))
                     self.le_pay.setText(str(self.model.record(self.view_given.currentIndex().row()).value(11)))
                     self.le_send.setText(str(self.model.record(self.view_given.currentIndex().row()).value(12)))
                     self.le_note.setText(str(self.model.record(self.view_given.currentIndex().row()).value(5)))
                     self.le_pay.setEnabled(False)
                     row=self.model_client.rowCount()-1 
                     while row>=0:
                            if self.model.record(self.view_given.currentIndex().row()).value(2)==self.model_client.record(row).value(1):
                                   self.le_client.setText(self.model_client.record(row).value(1))
                                   self.le_client_name.setText(self.model_client.record(row).value(2))
                                   self.le_client_secondname.setText(self.model_client.record(row).value(3))
                                   self.le_client_city.setText(self.model_client.record(row).value(4))
                                   self.le_client_post.setText(str(self.model_client.record(row).value(5)))
                                   self.le_client_phone.setText(str(self.model_client.record(row).value(6)))
                                   self.le_client_note.setText(self.model_client.record(row).value(7))
                                   break
                            row=row-1
              self.main=QGridLayout()
              self.main.setColumnStretch(1,1)
              self.main.setColumnMinimumWidth(1,150)
              self.main.addWidget(self.l_number,0,0)
              self.main.addWidget(self.le_number,0,1)
              self.main.addWidget(self.l_device,1,0)
              self.main.addWidget(self.le_device,1,1)
              self.main.addWidget(self.l_client,2,0)
              self.main.addWidget(self.le_client,2,1)
              self.main.addWidget(self.l_client_name,3,0)
              self.main.addWidget(self.le_client_name,3,1)
              self.main.addWidget(self.l_client_secondname,4,0)
              self.main.addWidget(self.le_client_secondname,4,1)
              self.main.addWidget(self.l_client_city,5,0)
              self.main.addWidget(self.le_client_city,5,1)
              self.main.addWidget(self.l_client_post,6,0)
              self.main.addWidget(self.le_client_post,6,1)
              self.main.addWidget(self.l_client_phone,7,0)
              self.main.addWidget(self.le_client_phone,7,1)
              self.main.addWidget(self.l_client_note,8,0)
              self.main.addWidget(self.le_client_note,8,1)

              self.main.addWidget(self.l_date_in,0,2)
              self.main.addWidget(self.le_date_in,0,3)
              self.main.addWidget(self.l_date_repair,1,2)
              self.main.addWidget(self.le_date_repair,1,3)
              self.main.addWidget(self.l_engineer,2,2)
              self.main.addWidget(self.le_engineer,2,3)
              self.main.addWidget(self.l_date_out,3,2)
              self.main.addWidget(self.le_date_out,3,3)
              self.main.addWidget(self.l_rapair_note,4,2)
              self.main.addWidget(self.le_rapair_note,4,3)
              self.main.addWidget(self.l_price,5,2)
              self.main.addWidget(self.le_price,5,3)
              self.main.addWidget(self.l_pay,6,2)
              self.main.addWidget(self.le_pay,6,3)
              self.main.addWidget(self.l_send,7,2)
              self.main.addWidget(self.le_send,7,3)
              self.main.addWidget(self.l_note,8,2)
              self.main.addWidget(self.le_note,8,3)
              
              self.beg_main=QVBoxLayout()
              self.beg_main.addLayout(self.main)
              self.beg_main.addWidget(self.buttons)
              self.dialog_window.setLayout(self.beg_main)
              self.dialog_window.move(10,10)
              self.dialog_window.show()
              db.close()
                     
       def f_info_edit(self):
              self.dialog_window_edit=QWidget(window, Qt.Dialog)
              self.dialog_window_edit.setWindowTitle('Загальна інформація')
              self.dialog_window_edit.setWindowModality(Qt.WindowModal)
              self.dialog_window_edit.setAttribute(Qt.WA_DeleteOnClose, True)

              self.bt_edit=QPushButton('Правка')
              self.bt_edit.clicked.connect(self.f_edit)
              #self.bt_edit.setCheckable(True)
              #bt_edit.setChecked(True)
              bt_exit=QPushButton('Вихід')
              bt_exit.clicked.connect(self.dialog_window_edit.close)
              self.buttons=QDialogButtonBox(Qt.Horizontal)
              self.buttons.addButton(self.bt_edit,QDialogButtonBox.ActionRole)
              self.buttons.addButton(bt_exit,QDialogButtonBox.ActionRole)

              
              self.l_number=QLabel()
              self.l_number.setText('№')
              self.le_number=QLineEdit()
              #self.le_number.setReadOnly(True)

              self.l_device=QLabel()
              self.l_device.setText('Пристрій')
              self.cb_device=QComboBox()
              self.cb_device.setModel(self.model_device)
              self.cb_device.setModelColumn(self.model_device.fieldIndex('device'))

              self.l_client=QLabel()
              self.l_client.setText('Прізвище')
              self.cb_client=QComboBox()
              self.cb_client.setModel(self.model_client)
              self.cb_client.setModelColumn(self.model_client.fieldIndex('surname'))
              self.cb_client.currentIndexChanged[int].connect(self.cbChanged)

              self.l_client_name=QLabel()
              self.l_client_name.setText("Ім'я")
              self.le_client_name=QLineEdit()
              self.le_client_name.setEnabled(False)

              self.l_client_secondname=QLabel()
              self.l_client_secondname.setText('По батькові')
              self.le_client_secondname=QLineEdit()
              self.le_client_secondname.setEnabled(False)

              self.l_client_city=QLabel()
              self.l_client_city.setText('Місто')
              self.le_client_city=QLineEdit()
              self.le_client_city.setEnabled(False)

              self.l_client_post=QLabel()
              self.l_client_post.setText('Пошта №')
              self.le_client_post=QLineEdit()
              self.le_client_post.setEnabled(False)

              self.l_client_phone=QLabel()
              self.l_client_phone.setText('Телефон')
              self.le_client_phone=QLineEdit()
              self.le_client_phone.setEnabled(False)
              
              self.l_client_note=QLabel()
              self.l_client_note.setText('Примітка \nпо клієнту')
              self.le_client_note=QTextEdit()
              self.le_client_note.setEnabled(False)
                               
              self.l_date_in=QLabel()
              self.l_date_in.setText('Дата отримання')
              self.date_in=QDateEdit()
              self.date_in.setCalendarPopup(True)

              self.l_date_repair=QLabel()
              self.l_date_repair.setText('Дата ремонту')
              self.date_repair=QDateEdit()
              self.date_repair.setCalendarPopup(True)

              self.l_engineer=QLabel()
              self.l_engineer.setText('Інженер')
              self.engineer=QComboBox()
              self.engineer.setModel(self.model_engineer)
              self.engineer.setModelColumn(self.model_engineer.fieldIndex('engineer_surname'))

              self.l_date_out=QLabel()
              self.l_date_out.setText('Виданий з ремонту')
              self.date_out=QDateEdit()
              self.date_out.setCalendarPopup(True)

              self.l_rapair_note=QLabel()
              self.l_rapair_note.setText('Перелік робіт')
              self.le_rapair_note=QTextEdit()
              self.le_rapair_note.setReadOnly(True)

              self.l_price=QLabel()
              self.l_price.setText('Ціна ремонту')
              self.le_price=QLineEdit()
              self.le_price.setReadOnly(True)

              self.l_pay=QLabel()
              self.l_pay.setText('Дата оплати')
              self.pay=QDateEdit()
              self.pay.setCalendarPopup(True)

              self.l_send=QLabel()
              self.l_send.setText('Дата видачі')
              self.send=QDateEdit()
              self.send.setCalendarPopup(True)

              self.l_note=QLabel()
              self.l_note.setText('Примітка \nпо пристрою')
              self.le_note=QTextEdit()
              #self.le_note.setReadOnly(True)
              
              if self.bt_repair.text()=='Ремонт':
                     self.le_number.setText(str(self.model.record(self.view.currentIndex().row()).value(1)))
                     x=self.model.record(self.view.currentIndex().row()).value(4)
                     self.date_in.setDate(QDate(int(x[6:]),int(x[3:5]),int(x[:2])))
                     self.le_rapair_note.setEnabled(False)
                     self.date_repair.setEnabled(False)
                     self.engineer.setEnabled(False)
                     self.date_out.setEnabled(False)
                     self.le_price.setEnabled(False)
                     self.pay.setEnabled(False)
                     self.send.setEnabled(False)
                     
                     self.le_note.setText(str(self.model.record(self.view.currentIndex().row()).value(5)))
                     row=self.model_device.rowCount()-1
                     while row>=0:
                            if self.model.record(self.view.currentIndex().row()).value(3)==self.model_device.record(row).value(1):
                                   self.cb_device.setCurrentIndex(row)
                                   break
                            row=row-1
                     row=self.model_client.rowCount()-1
                     while row>=0:
                            if self.model.record(self.view.currentIndex().row()).value(2)==self.model_client.record(row).value(1):
                                   self.cb_client.setCurrentIndex(row)
                                   self.le_client_name.setText(self.model_client.record(row).value(2))
                                   self.le_client_secondname.setText(self.model_client.record(row).value(3))
                                   self.le_client_city.setText(self.model_client.record(row).value(4))
                                   self.le_client_post.setText(str(self.model_client.record(row).value(5)))
                                   self.le_client_phone.setText(str(self.model_client.record(row).value(6)))
                                   self.le_client_note.setText(self.model_client.record(row).value(7))
                                   break
                            row=row-1


              elif self.bt_repair.text()=='Відремонтований':
                     self.le_number.setText(str(self.model.record(self.view_repair.currentIndex().row()).value(1)))
                     x=self.model.record(self.view_repair.currentIndex().row()).value(4)
                     self.date_in.setDate(QDate(int(x[6:]),int(x[3:5]),int(x[:2])))
                     x=self.model.record(self.view_repair.currentIndex().row()).value(6)
                     self.date_repair.setDate(QDate(int(x[6:]),int(x[3:5]),int(x[:2])))
                     self.le_rapair_note.setEnabled(False)
                     self.date_out.setEnabled(False)
                     self.le_price.setEnabled(False)
                     self.pay.setEnabled(False)
                     self.send.setEnabled(False)
                     self.le_note.setText(str(self.model.record(self.view_repair.currentIndex().row()).value(5)))
                     row=self.model_engineer.rowCount()-1
                     while row>=0:
                            if self.model.record(self.view_repair.currentIndex().row()).value(7)==self.model_engineer.record(row).value(1):
                                   self.engineer.setCurrentIndex(row)
                                   break
                            row=row-1
                     row=self.model_device.rowCount()-1
                     while row>=0:
                            if self.model.record(self.view_repair.currentIndex().row()).value(3)==self.model_device.record(row).value(1):
                                   self.cb_device.setCurrentIndex(row)
                                   break
                            row=row-1
                     row=self.model_client.rowCount()-1
                     while row>=0:
                            if self.model.record(self.view_repair.currentIndex().row()).value(2)==self.model_client.record(row).value(1):
                                   self.cb_client.setCurrentIndex(row)
                                   self.le_client_name.setText(self.model_client.record(row).value(2))
                                   self.le_client_secondname.setText(self.model_client.record(row).value(3))
                                   self.le_client_city.setText(self.model_client.record(row).value(4))
                                   self.le_client_post.setText(str(self.model_client.record(row).value(5)))
                                   self.le_client_phone.setText(str(self.model_client.record(row).value(6)))
                                   self.le_client_note.setText(self.model_client.record(row).value(7))
                                   break
                            row=row-1
              elif self.bt_repair.text()=='Оплачений':
                     self.le_number.setText(str(self.model.record(self.view_finished.currentIndex().row()).value(1)))
                     x=self.model.record(self.view_finished.currentIndex().row()).value(4)
                     self.date_in.setDate(QDate(int(x[6:]),int(x[3:5]),int(x[:2])))
                     x=self.model.record(self.view_finished.currentIndex().row()).value(6)
                     self.date_repair.setDate(QDate(int(x[6:]),int(x[3:5]),int(x[:2])))
                     x=self.model.record(self.view_finished.currentIndex().row()).value(8)
                     self.date_out.setDate(QDate(int(x[6:]),int(x[3:5]),int(x[:2])))
                     self.le_price.setText(str(self.model.record(self.view_finished.currentIndex().row()).value(10)))
                     self.le_rapair_note.setReadOnly(False)
                     self.le_price.setReadOnly(False)
                     self.pay.setEnabled(False)
                     self.send.setEnabled(False)

                     self.le_rapair_note.setText(str(self.model.record(self.view_finished.currentIndex().row()).value(9)))
                     self.le_note.setText(str(self.model.record(self.view_finished.currentIndex().row()).value(5)))
                     row=self.model_engineer.rowCount()-1
                     while row>=0:
                            if self.model.record(self.view_finished.currentIndex().row()).value(7)==self.model_engineer.record(row).value(1):
                                   self.engineer.setCurrentIndex(row)
                                   break
                            row=row-1
                     row=self.model_device.rowCount()-1
                     while row>=0:
                            if self.model.record(self.view_finished.currentIndex().row()).value(3)==self.model_device.record(row).value(1):
                                   self.cb_device.setCurrentIndex(row)
                                   break
                            row=row-1
                     
                     row=self.model_client.rowCount()-1 
                     while row>=0:
                            if self.model.record(self.view_finished.currentIndex().row()).value(2)==self.model_client.record(row).value(1):
                                   self.cb_client.setCurrentIndex(row)
                                   self.le_client_name.setText(self.model_client.record(row).value(2))
                                   self.le_client_secondname.setText(self.model_client.record(row).value(3))
                                   self.le_client_city.setText(self.model_client.record(row).value(4))
                                   self.le_client_post.setText(str(self.model_client.record(row).value(5)))
                                   self.le_client_phone.setText(str(self.model_client.record(row).value(6)))
                                   self.le_client_note.setText(self.model_client.record(row).value(7))
                                   break
                            row=row-1
                     
              elif self.bt_repair.text()=='Видати':
                     self.le_number.setText(str(self.model.record(self.view_prepaid.currentIndex().row()).value(1)))
                     x=self.model.record(self.view_prepaid.currentIndex().row()).value(4)
                     self.date_in.setDate(QDate(int(x[6:]),int(x[3:5]),int(x[:2])))
                     x=self.model.record(self.view_prepaid.currentIndex().row()).value(6)
                     self.date_repair.setDate(QDate(int(x[6:]),int(x[3:5]),int(x[:2])))
                     x=self.model.record(self.view_prepaid.currentIndex().row()).value(8)
                     self.date_out.setDate(QDate(int(x[6:]),int(x[3:5]),int(x[:2])))
                     self.le_rapair_note.setReadOnly(False)
                     self.le_price.setText(str(self.model.record(self.view_prepaid.currentIndex().row()).value(10)))
                     self.le_price.setReadOnly(False)
                     x=self.model.record(self.view_prepaid.currentIndex().row()).value(11)
                     self.pay.setDate(QDate(int(x[6:]),int(x[3:5]),int(x[:2])))
                     self.le_rapair_note.setText(str(self.model.record(self.view_prepaid.currentIndex().row()).value(9)))
                     self.le_note.setText(str(self.model.record(self.view_prepaid.currentIndex().row()).value(5)))
                     self.le_rapair_note.setReadOnly(False)
                     self.le_price.setReadOnly(False)
                     self.send.setEnabled(False)
                     row=self.model_engineer.rowCount()-1
                     while row>=0:
                            if self.model.record(self.view_prepaid.currentIndex().row()).value(7)==self.model_engineer.record(row).value(1):
                                   self.engineer.setCurrentIndex(row)
                                   break
                            row=row-1
                     row=self.model_device.rowCount()-1
                     while row>=0:
                            if self.model.record(self.view_prepaid.currentIndex().row()).value(3)==self.model_device.record(row).value(1):
                                   self.cb_device.setCurrentIndex(row)
                                   break
                            row=row-1
                     
                     self.le_note.setText(str(self.model.record(self.view.currentIndex().row()).value(5)))
                     row=self.model_client.rowCount()-1 
                     while row>=0:
                            if self.model.record(self.view_prepaid.currentIndex().row()).value(2)==self.model_client.record(row).value(1):
                                   self.cb_client.setCurrentIndex(row)
                                   self.le_client_name.setText(self.model_client.record(row).value(2))
                                   self.le_client_secondname.setText(self.model_client.record(row).value(3))
                                   self.le_client_city.setText(self.model_client.record(row).value(4))
                                   self.le_client_post.setText(str(self.model_client.record(row).value(5)))
                                   self.le_client_phone.setText(str(self.model_client.record(row).value(6)))
                                   self.le_client_note.setText(self.model_client.record(row).value(7))
                                   break
                            row=row-1
              elif self.bt_repair.text()=='Оплатити':
                     
                     self.le_number.setText(str(self.model.record(self.view_given.currentIndex().row()).value(1)))
                     x=self.model.record(self.view_given.currentIndex().row()).value(4)
                     self.date_in.setDate(QDate(int(x[6:]),int(x[3:5]),int(x[:2])))
                     x=self.model.record(self.view_given.currentIndex().row()).value(6)
                     self.date_repair.setDate(QDate(int(x[6:]),int(x[3:5]),int(x[:2])))
                     x=self.model.record(self.view_given.currentIndex().row()).value(8)
                     self.date_out.setDate(QDate(int(x[6:]),int(x[3:5]),int(x[:2])))
                     self.le_rapair_note.setReadOnly(False)
                     self.le_price.setText(str(self.model.record(self.view_given.currentIndex().row()).value(10)))
                     self.le_price.setReadOnly(False)
                     #x=self.model.record(self.view_given.currentIndex().row()).value(11)
                     #self.pay.setDate(QDate(int(x[6:]),int(x[3:5]),int(x[:2])))
                     x=self.model.record(self.view_given.currentIndex().row()).value(12)
                     self.send.setDate(QDate(int(x[6:]),int(x[3:5]),int(x[:2])))

                     self.le_rapair_note.setText(str(self.model.record(self.view_given.currentIndex().row()).value(9)))
                     self.le_note.setText(str(self.model.record(self.view_given.currentIndex().row()).value(5)))
                     self.pay.setEnabled(False)
                     #self.send.setEnabled(False)
                     row=self.model_engineer.rowCount()-1
                     while row>=0:
                            if self.model.record(self.view_given.currentIndex().row()).value(7)==self.model_engineer.record(row).value(1):
                                   self.engineer.setCurrentIndex(row)
                                   break
                            row=row-1
                     row=self.model_device.rowCount()-1
                     while row>=0:
                            if self.model.record(self.view_given.currentIndex().row()).value(3)==self.model_device.record(row).value(1):
                                   self.cb_device.setCurrentIndex(row)
                                   break
                            row=row-1
                     
                     self.le_note.setText(str(self.model.record(self.view.currentIndex().row()).value(5)))
                     row=self.model_client.rowCount()-1 
                     while row>=0:
                            if self.model.record(self.view_given.currentIndex().row()).value(2)==self.model_client.record(row).value(1):
                                   self.cb_client.setCurrentIndex(row)
                                   self.le_client_name.setText(self.model_client.record(row).value(2))
                                   self.le_client_secondname.setText(self.model_client.record(row).value(3))
                                   self.le_client_city.setText(self.model_client.record(row).value(4))
                                   self.le_client_post.setText(str(self.model_client.record(row).value(5)))
                                   self.le_client_phone.setText(str(self.model_client.record(row).value(6)))
                                   self.le_client_note.setText(self.model_client.record(row).value(7))
                                   break
                            row=row-1

              self.main_edit=QGridLayout()
              self.main_edit.setColumnStretch(1,1)
              self.main_edit.setColumnMinimumWidth(1,150)
              self.main_edit.addWidget(self.l_number,0,0)
              self.main_edit.addWidget(self.le_number,0,1)
              self.main_edit.addWidget(self.l_device,1,0)
              self.main_edit.addWidget(self.cb_device,1,1)
              self.main_edit.addWidget(self.l_client,2,0)
              self.main_edit.addWidget(self.cb_client,2,1)
              self.main_edit.addWidget(self.l_client_name,3,0)
              self.main_edit.addWidget(self.le_client_name,3,1)
              self.main_edit.addWidget(self.l_client_secondname,4,0)
              self.main_edit.addWidget(self.le_client_secondname,4,1)
              self.main_edit.addWidget(self.l_client_city,5,0)
              self.main_edit.addWidget(self.le_client_city,5,1)
              self.main_edit.addWidget(self.l_client_post,6,0)
              self.main_edit.addWidget(self.le_client_post,6,1)
              self.main_edit.addWidget(self.l_client_phone,7,0)
              self.main_edit.addWidget(self.le_client_phone,7,1)
              self.main_edit.addWidget(self.l_client_note,8,0)
              self.main_edit.addWidget(self.le_client_note,8,1)

              self.main_edit.addWidget(self.l_date_in,0,2)
              self.main_edit.addWidget(self.date_in,0,3)
              self.main_edit.addWidget(self.l_date_repair,1,2)
              self.main_edit.addWidget(self.date_repair,1,3)
              self.main_edit.addWidget(self.l_engineer,2,2)
              self.main_edit.addWidget(self.engineer,2,3)
              self.main_edit.addWidget(self.l_date_out,3,2)
              self.main_edit.addWidget(self.date_out,3,3)
              self.main_edit.addWidget(self.l_rapair_note,4,2)
              self.main_edit.addWidget(self.le_rapair_note,4,3)
              self.main_edit.addWidget(self.l_price,5,2)
              self.main_edit.addWidget(self.le_price,5,3)
              self.main_edit.addWidget(self.l_pay,6,2)
              self.main_edit.addWidget(self.pay,6,3)
              self.main_edit.addWidget(self.l_send,7,2)
              self.main_edit.addWidget(self.send,7,3)
              self.main_edit.addWidget(self.l_note,8,2)
              self.main_edit.addWidget(self.le_note,8,3)

              self.beg_main=QVBoxLayout()
              self.beg_main.addLayout(self.main_edit)
              self.beg_main.addWidget(self.buttons)
              self.dialog_window_edit.setLayout(self.beg_main)
              self.dialog_window_edit.move(10,10)
              self.dialog_window_edit.show()
              #db.close()
              
       def cbChanged(self,row):
              #db.open()
              self.le_client_name.setText(self.model_client.record(row).value(2))
              self.le_client_secondname.setText(self.model_client.record(row).value(3))
              self.le_client_city.setText(self.model_client.record(row).value(4))
              self.le_client_post.setText(str(self.model_client.record(row).value(5)))
              self.le_client_phone.setText(str(self.model_client.record(row).value(6)))
              self.le_client_note.setText(self.model_client.record(row).value(7))
              #db.close()
              
       def f_edit(self):
              db.open()
              if self.bt_edit.isChecked():
                     self.dialog_window.close()
                     self.f_info_edit()
                     
              else:
                     
                     if self.bt_repair.text()=='Ремонт':
                            self.model.setData(self.model.index(self.view.currentIndex().row(),1),
                                               int(self.le_number.text()))
                            self.model.setData(self.model.index(self.view.currentIndex().row(),4),
                                               self.date_in.date().toString('dd.MM.yyyy'))
                            self.model.setData(self.model.index(self.view.currentIndex().row(),2),
                                               self.cb_client.currentText())
                            self.model.setData(self.model.index(self.view.currentIndex().row(), 13),
                                               self.cb_client.currentIndex()+1)
                            self.model.setData(self.model.index(self.view.currentIndex().row(),3),
                                               self.cb_device.currentText())
                            self.model.setData(self.model.index(self.view.currentIndex().row(),5),
                                               self.le_note.toPlainText())
                            
                            #self.dialog_window.close()
                            
                           
                     elif self.bt_repair.text()=='Відремонтований':
                            self.model.setData(self.model.index(self.view_repair.currentIndex().row(),1),
                                               int(self.le_number.text()))
                            self.model.setData(self.model.index(self.view_repair.currentIndex().row(),4),
                                               self.date_in.date().toString('dd.MM.yyyy'))
                            self.model.setData(self.model.index(self.view_repair.currentIndex().row(),2),
                                               self.cb_client.currentText())
                            self.model.setData(self.model.index(self.view_repair.currentIndex().row(), 13),
                                               self.cb_client.currentIndex()+1)
                            self.model.setData(self.model.index(self.view_repair.currentIndex().row(),3),
                                               self.cb_device.currentText())
                            self.model.setData(self.model.index(self.view_repair.currentIndex().row(),5),
                                               self.le_note.toPlainText())
                            self.model.setData(self.model.index(self.view_repair.currentIndex().row(),6),
                                               self.date_repair.date().toString('dd.MM.yyyy'))
                            self.model.setData(self.model.index(self.view_repair.currentIndex().row(),7),
                                               self.engineer.currentText())
                            
                     elif self.bt_repair.text()=='Оплачений':
                            self.model.setData(self.model.index(self.view_finished.currentIndex().row(),1),
                                               int(self.le_number.text()))
                            self.model.setData(self.model.index(self.view_finished.currentIndex().row(),4),
                                               self.date_in.date().toString('dd.MM.yyyy'))
                            self.model.setData(self.model.index(self.view_finished.currentIndex().row(),2),
                                               self.cb_client.currentText())
                            self.model.setData(self.model.index(self.view_finished.currentIndex().row(), 13),
                                               self.cb_client.currentIndex()+1)
                            self.model.setData(self.model.index(self.view_finished.currentIndex().row(),3),
                                               self.cb_device.currentText())
                            self.model.setData(self.model.index(self.view_finished.currentIndex().row(),5),
                                               self.le_note.toPlainText())
                            self.model.setData(self.model.index(self.view_finished.currentIndex().row(),6),
                                               self.date_repair.date().toString('dd.MM.yyyy'))
                            self.model.setData(self.model.index(self.view_finished.currentIndex().row(),7),
                                               self.engineer.currentText())
                            self.model.setData(self.model.index(self.view_finished.currentIndex().row(),8),
                                               self.date_out.date().toString('dd.MM.yyyy'))
                            self.model.setData(self.model.index(self.view_finished.currentIndex().row(),9),
                                               self.le_rapair_note.toPlainText())
                            self.model.setData(self.model.index(self.view_finished.currentIndex().row(),10),
                                               int(self.le_price.text()))
                     elif self.bt_repair.text()=='Видати':
                            self.model.setData(self.model.index(self.view_prepaid.currentIndex().row(),1),
                                               int(self.le_number.text()))
                            self.model.setData(self.model.index(self.view_prepaid.currentIndex().row(),4),
                                               self.date_in.date().toString('dd.MM.yyyy'))
                            self.model.setData(self.model.index(self.view_prepaid.currentIndex().row(),2),
                                               self.cb_client.currentText())
                            self.model.setData(self.model.index(self.view_prepaid.currentIndex().row(), 13),
                                               self.cb_client.currentIndex()+1)
                            self.model.setData(self.model.index(self.view_prepaid.currentIndex().row(),3),
                                               self.cb_device.currentText())
                            self.model.setData(self.model.index(self.view_prepaid.currentIndex().row(),5),
                                               self.le_note.toPlainText())
                            self.model.setData(self.model.index(self.view_prepaid.currentIndex().row(),6),
                                               self.date_repair.date().toString('dd.MM.yyyy'))
                            self.model.setData(self.model.index(self.view_prepaid.currentIndex().row(),7),
                                               self.engineer.currentText())
                            self.model.setData(self.model.index(self.view_prepaid.currentIndex().row(),8),
                                               self.date_out.date().toString('dd.MM.yyyy'))
                            self.model.setData(self.model.index(self.view_prepaid.currentIndex().row(),9),
                                               self.le_rapair_note.toPlainText())
                            self.model.setData(self.model.index(self.view_prepaid.currentIndex().row(),10),
                                               int(self.le_price.text()))
                            self.model.setData(self.model.index(self.view_prepaid.currentIndex().row(),11),
                                               self.pay.date().toString('dd.MM.yyyy'))
                     elif self.bt_repair.text()=='Оплатити':
                            self.model.setData(self.model.index(self.view_given.currentIndex().row(),1),
                                               int(self.le_number.text()))
                            self.model.setData(self.model.index(self.view_given.currentIndex().row(),4),
                                               self.date_in.date().toString('dd.MM.yyyy'))
                            self.model.setData(self.model.index(self.view_given.currentIndex().row(),2),
                                               self.cb_client.currentText())
                            self.model.setData(self.model.index(self.view_given.currentIndex().row(), 13),
                                               self.cb_client.currentIndex()+1)
                            self.model.setData(self.model.index(self.view_given.currentIndex().row(),3),
                                               self.cb_device.currentText())
                            self.model.setData(self.model.index(self.view_given.currentIndex().row(),5),
                                               self.le_note.toPlainText())
                            self.model.setData(self.model.index(self.view_given.currentIndex().row(),6),
                                               self.date_repair.date().toString('dd.MM.yyyy'))
                            self.model.setData(self.model.index(self.view_given.currentIndex().row(),7),
                                               self.engineer.currentText())
                            self.model.setData(self.model.index(self.view_given.currentIndex().row(),8),
                                               self.date_out.date().toString('dd.MM.yyyy'))
                            self.model.setData(self.model.index(self.view_given.currentIndex().row(),9),
                                               self.le_rapair_note.toPlainText())
                            self.model.setData(self.model.index(self.view_given.currentIndex().row(),10),
                                               int(self.le_price.text()))
                            self.model.setData(self.model.index(self.view_given.currentIndex().row(),12),
                                               self.send.date().toString('dd.MM.yyyy'))
                     self.model.submitAll()
                     self.dialog_window_edit.close()
                     #self.f_info()
                     #print('work mode')
              db.close()
              
       def changeTab(self,ind):
              db.open()
              if ind == 0:
                     self.bt_repair.show()
                     self.bt_giveout.hide()
                     self.bt_2.show()
                     self.bt_repair.setText('Ремонт')
                     self.model.setFilter('repair_date ISNULL')
                     self.model.select()
              elif ind == 1:
                     self.bt_repair.show()
                     self.bt_giveout.hide()
                     self.bt_2.hide()
                     self.bt_repair.setText('Відремонтований')
                     self.model.setFilter('redy_device_date ISNULL and engineer NOTNULL')
                     self.model.select()
              elif ind == 2:
                     self.bt_repair.show()
                     self.bt_giveout.show()
                     self.bt_2.hide()
                     self.bt_repair.setText('Оплачений')
                     self.model.setFilter('redy_device_date NOTNULL and pay_date ISNULL and send_date ISNULL')
                     self.model.select()
              elif ind == 3:
                     self.bt_repair.show()
                     self.bt_giveout.hide()
                     self.bt_2.hide()
                     self.bt_repair.setText('Видати')
                     self.model.setFilter('redy_device_date NOTNULL and pay_date NOTNULL and send_date ISNULL')
                     self.model.select()
              elif ind ==4:
                     self.bt_repair.show()
                     self.bt_giveout.hide()
                     self.bt_2.hide()
                     self.bt_repair.setText('Оплатити')
                     self.model.setFilter('redy_device_date NOTNULL and pay_date ISNULL and send_date NOTNULL')
                     self.model.select()
              db.close()       
       
       def f_bt_1(self):
              connect()
              global dialog_window
              dialog_window=QWidget(window, Qt.Dialog)
              dialog_window.setWindowTitle('Прийняти пристрій')
              dialog_window.setWindowModality(Qt.WindowModal)
              #dialog_window.resize(100,200)
              dialog_window.setAttribute(Qt.WA_DeleteOnClose, True)
              bt_add=QPushButton('Прийняти пристрій')
              bt_exit=QPushButton('Вихід')
              bt_add.clicked.connect(self.add_new_device)
              bt_exit.clicked.connect(dialog_window.close)

              self.cb_client=QComboBox()
              #self.model_client.select()
              #while self.model_client.canFetchMore():
                  #self.model_client.fetchMore()
              self.cb_client.setModel(self.model_client)
              self.cb_client.setModelColumn(self.model_client.fieldIndex('surname'))
             
              self.cb_device=QComboBox()
              self.model_device.select()
              self.cb_device.setModel(self.model_device)
              self.cb_device.setModelColumn(self.model_device.fieldIndex('device'))
              
              l_client=QLabel()
              l_client.setText('Клієнт')

              l_device=QLabel()
              l_device.setText('Пристрій')

              l_note=QLabel()
              l_note.setText('Примітка')

              l_insert_number=QLabel('Ввести номер')

              self.ch_insert_number=QCheckBox()
              self.ch_insert_number.setCheckState(2)
              self.ch_insert_number.stateChanged.connect(self.ch_number)
              self.insert_number=QSpinBox()
              self.insert_number.clear()
              self.insert_number.setDisabled(False)
              self.insert_number.setMaximum(200000)

              self.edit_note=QTextEdit()
              self.edit_note.setTabChangesFocus(True)

              HB_insert_number=QHBoxLayout()
              HB_insert_number.addWidget(self.ch_insert_number)
              HB_insert_number.addWidget(self.insert_number)
              
              vlayout=QVBoxLayout()
              vlayout.addWidget(l_client)
              vlayout.addWidget(self.cb_client)
              vlayout.addWidget(l_device)
              vlayout.addWidget(self.cb_device)
              vlayout.addWidget(l_insert_number)
              vlayout.addLayout(HB_insert_number)
              vlayout.addWidget(l_note)
              vlayout.addWidget(self.edit_note)
              
              Box_b=QHBoxLayout()
              Box_b.addWidget(bt_add)
              Box_b.addWidget(bt_exit)
              main=QVBoxLayout()
              main.addLayout(vlayout)
              main.addLayout(Box_b)
              dialog_window.setLayout(main)
              dialog_window.show()

              
              
       def delete(self):
              connect()
              answer=QMessageBox.question(self,'Видалення запису','Ви підтверджуєте видалення запису?',
                                          QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
              if answer==QMessageBox.Yes:
                     self.model.removeRow(self.view.currentIndex().row())
                     self.model.submitAll()
                     #self.select_row_tab()
              db.close()
                     
      
       def add_new_device(self):
              db.open()
                           
              row=self.model.rowCount()       
              if self.ch_insert_number.checkState():
                     id_number=self.insert_number.value()
              else :
                     if row==0: id_number=1
                     else : id_number=(self.model.record(row-1).value(1))+1
              self.model.insertRow(row)
              self.model.setData(self.model.index(row, 1), id_number)
              self.model.setData(self.model.index(row, 2), self.cb_client.currentText())
              self.model.setData(self.model.index(row, 13),self.cb_client.currentIndex()+1)
              
              self.model.setData(self.model.index(row, 3), self.cb_device.currentText())
              self.model.setData(self.model.index(row, 4), time.strftime('%d.%m.%Y'))
              self.model.setData(self.model.index(row, 5), self.edit_note.toPlainText())
              self.model.submitAll()
              #self.select_row_tab()
              dialog_window.close()
              db.close()
              
       def ch_number(self):
              #db.open()
              if self.ch_insert_number.checkState():
                     self.insert_number.setDisabled(False)
              else : self.insert_number.setDisabled(True)
              #db.close()
                                                
       def f_repair(self):
              connect()
              if self.bt_repair.text()=='Ремонт':
                     row=(self.model_engineer.rowCount())-1
                     items=[]
                     while row >= 0:
                            items.append(self.model_engineer.record(row).value(1))
                            row=row-1
                     item, ok = QInputDialog.getItem(self, "Ремонт",
                                                     "Вибрати прізвище", items, 0, False)
                     if ok and item:
                            self.model.setData(self.model.index(self.view.currentIndex().row()
                                                                , 7), item)
                            self.model.setData(self.model.index(self.view.currentIndex().row()
                                                                , 6), time.strftime('%d.%m.%Y'))
                     self.model.submitAll()
                     #self.select_row_tab()
                     
              elif self.bt_repair.text()=='Відремонтований':
                     global dialog_window
                     dialog_window=QWidget(self, Qt.Dialog)
                     dialog_window.setWindowTitle('Відремонтований')
                     dialog_window.setWindowModality(Qt.WindowModal)
                     dialog_window.setAttribute(Qt.WA_DeleteOnClose, True)
              
                     bt_repair=QPushButton('Відремонтований')
                     bt_exit=QPushButton('Вихід')
                     bt_repair.clicked.connect(self.paid)
                     bt_exit.clicked.connect(dialog_window.close)
                     l_works=QLabel('Перелік робіт та комплектація')
                     l_price=QLabel('Ціна за ремонт')
              
                     self.works_note=QTextEdit()
                     self.price=QSpinBox()
                     self.price.setMaximum(2000)
              
                     vlayout=QVBoxLayout()
                     vlayout.addWidget(l_works)
                     vlayout.addWidget(self.works_note)
                     vlayout.addWidget(l_price)
                     vlayout.addWidget(self.price)

                     Box_b=QHBoxLayout()
                     Box_b.addWidget(bt_repair)
                     Box_b.addWidget(bt_exit)
                     main=QVBoxLayout()
                     main.addLayout(vlayout)
                     main.addLayout(Box_b)
                     dialog_window.setLayout(main)
                     dialog_window.show()
            
              elif self.bt_repair.text()=='Оплачений':
                     self.model.setData(self.model.index(self.view_finished.currentIndex().row()
                                                         , 11), time.strftime('%d.%m.%Y'))
                     self.model.submitAll()
                     #self.select_row_tab()
              elif self.bt_repair.text()=='Видати':
                     self.model.setData(self.model.index(self.view_prepaid.currentIndex().row()
                                                         , 12), time.strftime('%d.%m.%Y'))
                     if self.model.record(self.view_prepaid.currentIndex().row()).value(11):
                            row=self.model_rar.rowCount()       
                            self.model_rar.insertRow(row)
                            x=1
                            while(x<=13):
                                   self.model_rar.setData(self.model_rar.index(row, x),
                                                          (self.model.record(self.view_prepaid.currentIndex().row()).value(x)))
                                   x=x+1
                     self.model.removeRow(self.view_prepaid.currentIndex().row())
                     self.model_rar.submitAll()
                     self.model.submitAll()
                     
                     #self.select_row_tab()
              elif self.bt_repair.text()=='Оплатити':
                     self.model.setData(self.model.index(self.view_given.currentIndex().row()
                                                         , 11), time.strftime('%d.%m.%Y'))
                     row=self.model_rar.rowCount()
                     self.model_rar.insertRow(row)
                     x=1
                     while(x<=13):
                            self.model_rar.setData(self.model_rar.index(row, x),
                                                   (self.model.record(self.view_given.currentIndex().row()).value(x)))
                            x=x+1
                     self.model.removeRow(self.view_given.currentIndex().row())
                     self.model_rar.submitAll()
                     self.model.submitAll()
                     
                     #self.select_row_tab()
              db.close()

                     #'''row=self.model_client.rowCount()
                     #self.model_client.insertRow(row)
                     #self.model_client.setData(self.model_client.index(row, 1), self.surname.text())
                     #self.model_client.setData(self.model_client.index(row, 2), self.firstname.text())
                     #self.model_client.setData(self.model_client.index(row, 3), self.secondname.text())
                     #self.model_client.setData(self.model_client.index(row, 4), self.city.text())
                     #self.model_client.setData(self.model_client.index(row, 5), self.postoffice.text())
                     #self.model_client.setData(self.model_client.index(row, 6), self.phonenumber.text())
                     #self.model_client.setData(self.model_client.index(row, 7), self.comment.toPlainText())
                     #if row == 0:
                            #self.model_client.setData(self.model_client.index(row, 8), 1)
                     #else :
                            #self.model_client.setData(self.model_client.index(row, 8),
                                                      #(self.model_client.record(row-1).value(8))+1)
                     #self.model_client.submitAll();'''
              

       def f_giveout(self):
              connect()
              self.model.setData(self.model.index(self.view_finished.currentIndex().row()
                                                         , 12), time.strftime('%d.%m.%Y'))
              self.model.submitAll()
              #self.select_row_tab()
              db.close()
                   
       def paid(self):
              db.open()
              self.model.setData(self.model.index(self.view_repair.currentIndex().row()
                                                  , 9), self.works_note.toPlainText())
              self.model.setData(self.model.index(self.view_repair.currentIndex().row()
                                                  , 8), time.strftime('%d.%m.%Y'))
              self.model.setData(self.model.index(self.view_repair.currentIndex().row()
                                                  , 10), self.price.value())
              
              self.model.submitAll()
              #self.select_row_tab()
              dialog_window.close()
              db.close()

       '''def select_row_tab(self):
              row=self.model.rowCount()
              while row >= 0:
                     if self.model.record(row).value(6):
                            #print('test1')
                            self.view.setRowHidden(row, True)
                            self.view_repair.setRowHidden(row, False)
                     else : self.view_repair.setRowHidden(row, True)
                     if self.model.record(row).value(8):
                            #print('test2')
                            self.view_repair.setRowHidden(row, True)
                            self.view_finished.setRowHidden(row,False)
                     else: self.view_finished.setRowHidden(row,True)
                     if self.model.record(row).value(11):
                            self.view_finished.setRowHidden(row, True)
                            self.view_prepaid.setRowHidden(row, False)
                     else : self.view_prepaid.setRowHidden(row, True)
                     if self.model.record(row).value(12):
                            #print('value 12 is true')
                            self.view_prepaid.setRowHidden(row, True)
                            self.view_finished.setRowHidden(row, True)
                            self.view_given.setRowHidden(row, False)                            
                     else : self.view_given.setRowHidden(row, True)
                     row=row-1'''


                        
#===============================

       def baseClient(self):
              connect()
              dialog_window=QWidget(window, Qt.Dialog)
              dialog_window.setWindowTitle('Добавити клієнта')
              dialog_window.setWindowModality(Qt.WindowModal)
              dialog_window.setAttribute(Qt.WA_DeleteOnClose, True)
              #self.model_client.select()
              #while self.model_client.canFetchMore():
              #self.model_client.fetchMore()
              
              self.model_client.setHeaderData(1, Qt.Horizontal,'Прізвище')
              self.model_client.setHeaderData(2, Qt.Horizontal,"Ім'я")
              self.model_client.setHeaderData(3, Qt.Horizontal, 'По батькові')
              self.model_client.setHeaderData(4, Qt.Horizontal, 'Місто')
              self.model_client.setHeaderData(5, Qt.Horizontal, 'Пошта №')
              self.model_client.setHeaderData(6, Qt.Horizontal, 'Телефон')
              self.model_client.setHeaderData(7, Qt.Horizontal, 'Примітка')
              
                  
              self.view_client = QTableView()
              self.view_client.setModel(self.model_client)
              #self.view.setColumnWidth(1,150)
              #self.view.setColumnWidth(2,100)
              self.view_client.setShowGrid(True)
              self.view_client.setSelectionMode(QAbstractItemView.SingleSelection)
              self.view_client.setSelectionBehavior(QAbstractItemView.SelectRows)
              self.view_client.selectRow(258)
              self.view_client.setColumnHidden(0, True)
              self.view_client.setColumnHidden(8, True)
              #self.view_client.setReadOnly(True)

              bt_add_client=QPushButton('+')
              bt_del_client=QPushButton('-')
              bt_edit_client=QPushButton('Правка')
              bt_exit=QPushButton('Вихід')
              bt_add_client.clicked.connect(self.add_client)
              bt_del_client.clicked.connect(self.del_client)
              bt_edit_client.clicked.connect(self.edit_client)
              bt_exit.clicked.connect(dialog_window.close)
              
              vlayout=QVBoxLayout()
              vlayout.addWidget(bt_add_client, Qt.AlignRight)
              vlayout.addWidget(bt_del_client)
              vlayout.addWidget(bt_edit_client)
              vlayout.addWidget(bt_exit)
              main=QHBoxLayout()
              main.addWidget(self.view_client)
              main.addLayout(vlayout)
              dialog_window.setLayout(main)
              dialog_window.show()
              #db.close()
                      

       def del_client(self):
              connect()
              answer=QMessageBox.question(self,'Видалення запису',
                                          'Ви підтверджуєте видалення запису?',
                                          QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
              if answer==QMessageBox.Yes:
                     self.model_client.removeRow(self.view_client.currentIndex().row())
                     self.model_client.submitAll()
              db.close()       

#===========================              
       def add_client(self):
              global dialog_window
              dialog_window=QWidget(window, Qt.Dialog)
              dialog_window.setWindowTitle('Додати клієнта в базу даних')
              dialog_window.setWindowModality(Qt.WindowModal)
              #dialog_window.resize(100,200)
              dialog_window.setAttribute(Qt.WA_DeleteOnClose, True)
              
              bt_add=QPushButton('Додати клієнта')
              bt_exit=QPushButton('Вихід')
              bt_add.clicked.connect(self.addtobase_client)
              bt_exit.clicked.connect(dialog_window.close)
              self.surname=QLineEdit()
              self.firstname=QLineEdit()
              self.secondname=QLineEdit()
              self.city=QLineEdit()
              self.postoffice=QLineEdit()
              self.phonenumber=QLineEdit()
              self.comment=QTextEdit()
              self.comment.setTabChangesFocus(True)
              
              
              l_surname=QLabel()
              l_surname.setText('Прізвище')
              l_firstname=QLabel()
              l_firstname.setText("Ім'я")
              l_secondname=QLabel()
              l_secondname.setText('По батькові')
              l_city=QLabel()
              l_city.setText('Місто')
              l_postoffice=QLabel()
              l_postoffice.setText('Пошта №')
              l_phonenumber=QLabel()
              l_phonenumber.setText('Телефон')
              l_comment=QLabel()
              l_comment.setText('Примітка')

              vlayout=QVBoxLayout()
              vlayout.addWidget(l_surname)
              vlayout.addWidget(self.surname)
              vlayout.addWidget(l_firstname)
              vlayout.addWidget(self.firstname)
              vlayout.addWidget(l_secondname)
              vlayout.addWidget(self.secondname)
              vlayout.addWidget(l_city)
              vlayout.addWidget(self.city)
              vlayout.addWidget(l_postoffice)
              vlayout.addWidget(self.postoffice)
              vlayout.addWidget(l_phonenumber)
              vlayout.addWidget(self.phonenumber)
              vlayout.addWidget(l_comment)
              vlayout.addWidget(self.comment)
              
              Box_b=QHBoxLayout()
              Box_b.addWidget(bt_add)
              Box_b.addWidget(bt_exit)
              
              main=QVBoxLayout()
              main.addLayout(vlayout)
              main.addLayout(Box_b)
              dialog_window.setLayout(main)
              dialog_window.show()
              #db.close()
              
       def addtobase_client(self):
              if self.surname.text() !='' or self.firstname.text() !='':
                     row=self.model_client.rowCount()
                     temp=row
                     self.model_client.insertRow(row)
                     if self.surname.text() !='':
                            self.model_client.setData(self.model_client.index(row, 1), self.surname.text())
                     if self.firstname.text() !='':
                            self.model_client.setData(self.model_client.index(row, 2), self.firstname.text())
                     if self.secondname.text() !='':
                            self.model_client.setData(self.model_client.index(row, 3), self.secondname.text())
                     if self.city.text() !='':
                            self.model_client.setData(self.model_client.index(row, 4), self.city.text())
                     if self.postoffice.text() !='':
                            self.model_client.setData(self.model_client.index(row, 5), self.postoffice.text())
                     if self.phonenumber.text() !='':
                            self.model_client.setData(self.model_client.index(row, 6), self.phonenumber.text())
                     if self.comment.toPlainText() !='':
                            self.model_client.setData(self.model_client.index(row, 7), self.comment.toPlainText())
                     #db.close()
                     row=row-1
                     while row!=0:
                            if self.surname.text()!=self.model_client.record(row).value(1):
                                   row=row-1
                            else:
                                   dialog=QMessageBox.critical(self,'','Це прізвище вже є в базі клієнтів.',
                                                               QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
                                   if dialog==QMessageBox.Ok:
                                          self.model_client.removeRow(temp)
                                          break
              
                     if row == 0:
                            connect()
                            self.model_client.submitAll();
                            dialog_window.close()
                            while self.model_client.canFetchMore() == True:
                                   self.model_client.fetchMore()
                            db.close()
                     
              

       def edit_client(self):
              connect()
              global dialog_window
              dialog_window=QWidget(window, Qt.Dialog)
              dialog_window.setWindowTitle('Правка')
              dialog_window.setWindowModality(Qt.WindowModal)
              #dialog_window.resize(100,200)
              dialog_window.setAttribute(Qt.WA_DeleteOnClose, True)
              bt_save=QPushButton('Зберегти')
              bt_exit=QPushButton('Вихід')
              bt_save.clicked.connect(self.save_client)
              bt_exit.clicked.connect(dialog_window.close)

              self.surname=QLineEdit()
              self.surname.setText(str(self.model_client.record(self.view_client.currentIndex().row()).value(1)))
              self.firstname=QLineEdit()
              self.firstname.setText(str(self.model_client.record(self.view_client.currentIndex().row()).value(2)))
              self.secondname=QLineEdit()
              self.secondname.setText(str(self.model_client.record(self.view_client.currentIndex().row()).value(3)))
              self.city=QLineEdit()
              self.city.setText(str(self.model_client.record(self.view_client.currentIndex().row()).value(4)))
              self.postoffice=QLineEdit()
              self.postoffice.setText(str(self.model_client.record(self.view_client.currentIndex().row()).value(5)))
              self.phonenumber=QLineEdit()
              self.phonenumber.setText(str(self.model_client.record(self.view_client.currentIndex().row()).value(6)))
              self.comment=QTextEdit()
              self.comment.setTabChangesFocus(True)
              self.comment.setText(str(self.model_client.record(self.view_client.currentIndex().row()).value(7)))
              
              l_surname=QLabel()
              l_surname.setText('Прізвище')
              l_firstname=QLabel()
              l_firstname.setText("Ім'я")
              l_secondname=QLabel()
              l_secondname.setText('По батькові')
              l_city=QLabel()
              l_city.setText('Місто')
              l_postoffice=QLabel()
              l_postoffice.setText('Пошта №')
              l_phonenumber=QLabel()
              l_phonenumber.setText('Телефон')
              l_comment=QLabel()
              l_comment.setText('Примітка')

              vlayout=QVBoxLayout()
              vlayout.addWidget(l_surname)
              vlayout.addWidget(self.surname)
              vlayout.addWidget(l_firstname)
              vlayout.addWidget(self.firstname)
              vlayout.addWidget(l_secondname)
              vlayout.addWidget(self.secondname)
              vlayout.addWidget(l_city)
              vlayout.addWidget(self.city)
              vlayout.addWidget(l_postoffice)
              vlayout.addWidget(self.postoffice)
              vlayout.addWidget(l_phonenumber)
              vlayout.addWidget(self.phonenumber)
              vlayout.addWidget(l_comment)
              vlayout.addWidget(self.comment)
              
              Box_b=QHBoxLayout()
              Box_b.addWidget(bt_save)
              Box_b.addWidget(bt_exit)
              
              main=QVBoxLayout()
              main.addLayout(vlayout)
              main.addLayout(Box_b)
              dialog_window.setLayout(main)
              dialog_window.show()
              db.close()

       def save_client(self):
              connect()
              self.model_client.setData(self.model.index((self.view_client.currentIndex().row()), 1),
                                        (self.surname.text()))
              self.model_client.setData(self.model.index((self.view_client.currentIndex().row()), 2),
                                        self.firstname.text())
              self.model_client.setData(self.model.index((self.view_client.currentIndex().row()), 3),
                                        self.secondname.text())
              self.model_client.setData(self.model.index((self.view_client.currentIndex().row()), 4),
                                        self.city.text())
              self.model_client.setData(self.model.index((self.view_client.currentIndex().row()), 5),
                                        self.postoffice.text())
              self.model_client.setData(self.model.index((self.view_client.currentIndex().row()), 6),
                                        self.phonenumber.text())
              self.model_client.setData(self.model.index((self.view_client.currentIndex().row()), 7),
                                        self.comment.toPlainText())
              self.model_client.submitAll();
              db.close()
              dialog_window.close()
#==========================================
       def baseDevice(self):
              connect()
              dialog_window=QWidget(window, Qt.Dialog)
              dialog_window.setWindowTitle('Добавити пристрій')
              dialog_window.setWindowModality(Qt.WindowModal)
              dialog_window.setAttribute(Qt.WA_DeleteOnClose, True)
              
              '''self.model_device = QSqlTableModel(self)
              self.model_device.setTable('device')
              self.model_device.setEditStrategy(QSqlTableModel.OnManualSubmit)
              self.model_device.select()'''
              
              self.model_device.setHeaderData(1, Qt.Horizontal,'Пристрій')
                             
              self.view_device = QTableView()
              self.view_device.setModel(self.model_device)
              self.view_device.setShowGrid(True)
              self.view_device.setSelectionMode(QAbstractItemView.SingleSelection)
              self.view_device.setSelectionBehavior(QAbstractItemView.SelectRows)
              self.view_device.setColumnHidden(0, True)

              bt_add_device=QPushButton('+')
              bt_del_device=QPushButton('-')
              bt_edit_device=QPushButton('Правка')
              bt_exit=QPushButton('Вихід')
              bt_add_device.clicked.connect(self.add_device)
              bt_del_device.clicked.connect(self.del_device)
              bt_edit_device.clicked.connect(self.edit_device)
              bt_exit.clicked.connect(dialog_window.close)
              
              vlayout=QVBoxLayout()
              vlayout.addWidget(bt_add_device)
              vlayout.addWidget(bt_del_device)
              vlayout.addWidget(bt_edit_device)
              vlayout.addWidget(bt_exit)
              main=QHBoxLayout()
              main.addWidget(self.view_device)
              main.addLayout(vlayout)
              dialog_window.setLayout(main)
              dialog_window.show()
              db.close()

       def edit_device(self):
              connect()
              
              text, ok=QInputDialog.getText(self,'База даних пристроїв',
                                            'Правити назву пристрою', QLineEdit.Normal,
                                            self.model_device.record(self.view_device.currentIndex().row()).value(1))
              if ok and text !='':
                     
                     self.model_device.setData(self.model_device.index((self.view_device.currentIndex().row()), 1),text)
                     self.model_device.submitAll();
              db.close()       
                      

       def del_device(self):
              connect()
              answer=QMessageBox.question(self,'Видалення запису',
                                          'Ви підтверджуєте видалення запису?',
                                          QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
              if answer==QMessageBox.Yes:
                     self.model_device.removeRow(self.view_device.currentIndex().row())
                     self.model_device.submitAll()
              db.close()       
       def add_device(self):
              connect()
              text, ok=QInputDialog.getText(self,'База даних пристроїв',
                                            'Введіть назву пристрою')
              if ok and text !='':
                     self.model_device.select()
                     row=self.model_device.rowCount()
                     self.model_device.insertRow(row)
                     self.model_device.setData(self.model_device.index(row, 1),text)
                     self.model_device.submitAll();
              #dialog_window.close()
              db.close()       
                     
#==========================================
       def baseEngineer(self):
              dialog_window=QWidget(window, Qt.Dialog)
              dialog_window.setWindowTitle('Добавити інженера')
              dialog_window.setWindowModality(Qt.WindowModal)
              dialog_window.setAttribute(Qt.WA_DeleteOnClose, True)
              
              '''self.model_engineer = QSqlTableModel(self)
              self.model_engineer.setTable('engineer')
              self.model_engineer.setEditStrategy(QSqlTableModel.OnManualSubmit)
              self.model_engineer.select()'''
              
              self.model_engineer.setHeaderData(1, Qt.Horizontal,'Прізвище І П')
                             
              self.view_engineer = QTableView()
              self.view_engineer.setModel(self.model_engineer)
              self.view_engineer.setShowGrid(True)
              self.view_engineer.setSelectionMode(QAbstractItemView.SingleSelection)
              self.view_engineer.setSelectionBehavior(QAbstractItemView.SelectRows)
              self.view_engineer.setColumnHidden(0, True)

              bt_add_engineer=QPushButton('+')
              bt_del_engineer=QPushButton('-')
              bt_edit_engineer=QPushButton('Правка')
              bt_edit_engineer.clicked.connect(self.edit_engineer)
              bt_exit=QPushButton('Вихід')
              bt_add_engineer.clicked.connect(self.add_engineer)
              bt_del_engineer.clicked.connect(self.del_engineer)
              bt_exit.clicked.connect(dialog_window.close)
              
              vlayout=QVBoxLayout()
              vlayout.addWidget(bt_add_engineer)
              vlayout.addWidget(bt_del_engineer)
              vlayout.addWidget(bt_edit_engineer)
              vlayout.addWidget(bt_exit)
              main=QHBoxLayout()
              main.addWidget(self.view_engineer)
              main.addLayout(vlayout)
              dialog_window.setLayout(main)
              dialog_window.show()
              #db.close()

       def edit_engineer(self):
              connect()
              text, ok=QInputDialog.getText(self,'База даних пристроїв',
                                            'Правити', QLineEdit.Normal,
                                            self.model_engineer.record(self.view_engineer.currentIndex().row()).value(1))
              if ok and text !='':
                     self.model_engineer
                     self.model_engineer.setData(self.model_engineer.index((self.view_engineer.currentIndex().row()), 1),text)
                     self.model_engineer.submitAll();
              db.close()        

       def del_engineer(self):
              connect()
              answer=QMessageBox.question(self,'Видалення запису',
                                          'Ви підтверджуєте видалення запису?',
                                          QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
              if answer==QMessageBox.Yes:
                     self.model_engineer.removeRow(self.view_engineer.currentIndex().row())
                     self.model_engineer.submitAll()
              db.close()       
                     
       def add_engineer(self):
              connect()
              text, ok=QInputDialog.getText(self,'База даних інженерів',
                                            'Введіть Прізвище І П')
              if ok and text !='':
                     row=self.model_engineer.rowCount()
                     self.model_engineer.insertRow(row)
                     self.model_engineer.setData(self.model_engineer.index(row, 1),text)
                     self.model_engineer.submitAll();
              #dialog_window.close()
              db.close()       
#==========================================
       def baseArchiv(self):
              connect()
              dialog_archiv=QWidget(window, Qt.Dialog)
              dialog_archiv.setWindowTitle('Архів')
              dialog_archiv.setWindowModality(Qt.WindowModal)
              dialog_archiv.setAttribute(Qt.WA_DeleteOnClose, True)

              self.model_rar.setHeaderData(1, Qt.Horizontal,'№')
              self.model_rar.setHeaderData(2, Qt.Horizontal,'Клієнт')
              self.model_rar.setHeaderData(3, Qt.Horizontal, 'Пристрій')
              self.model_rar.setHeaderData(4, Qt.Horizontal, 'Дата отримання')
              self.model_rar.setHeaderData(8, Qt.Horizontal, 'Дата видачі')
              self.model_rar.select()
                     
              self.view_rar = QTableView()
              self.view_rar.setModel(self.model_rar)
              #self.view.setColumnWidth(1,150)
              #self.view.setColumnWidth(2,100)
              self.view_rar.setShowGrid(True)
              #self.view_rar.resizeRowsToContents()
              self.view_rar.setSelectionMode(QAbstractItemView.SingleSelection)
              self.view_rar.setSelectionBehavior(QAbstractItemView.SelectRows)
              self.view_rar.setColumnHidden(0, True)
              self.view_rar.setColumnHidden(5, True)
              self.view_rar.setColumnHidden(6, True)
              self.view_rar.setColumnHidden(7, True)
              self.view_rar.setColumnHidden(9, True)
              self.view_rar.setColumnHidden(10, True)
              self.view_rar.setColumnHidden(11, True)
              self.view_rar.setColumnHidden(12, True)
              self.view_rar.setColumnHidden(13, True)
              #self.view_rar.setReadOnly(True)

              bt_search=QPushButton('Пошук')
              bt_info=QPushButton('Інформація')
              bt_info.clicked.connect(self.rar_info)
              bt_exit=QPushButton('Вихід')
              bt_exit.clicked.connect(dialog_archiv.close)
              
              vlayout=QVBoxLayout()
              #vlayout.insertSpacing(50,50)
              vlayout.addWidget(bt_search, Qt.AlignCenter)
              vlayout.addWidget(bt_info, Qt.AlignCenter)
              vlayout.addWidget(bt_exit, Qt.AlignCenter)
              vlayout.setSpacing(25)
              vlayout.addStretch(50)
              vlayout.insertSpacing(5,50)

              main=QHBoxLayout()
              main.addWidget(self.view_rar)
              main.addLayout(vlayout)
              dialog_archiv.setLayout(main)
              dialog_archiv.show()
              #db.close()

       def rar_info(self):
              #connect()
              self.dialog_window=QWidget(window, Qt.Dialog)
              self.dialog_window.setWindowTitle('Загальна інформація')
              self.dialog_window.setWindowModality(Qt.WindowModal)
              self.dialog_window.setAttribute(Qt.WA_DeleteOnClose, True)

              self.l_number=QLabel()
              self.l_number.setText('№')
              self.le_number=QLineEdit()
              self.le_number.setReadOnly(True)
              
              self.l_device=QLabel()
              self.l_device.setText('Пристрій')
              self.le_device=QLineEdit()
              self.le_device.setReadOnly(True)
                           
              self.l_client=QLabel()
              self.l_client.setText('Прізвище')
              self.le_client=QLineEdit()
              self.le_client.setReadOnly(True)

              self.l_client_name=QLabel()
              self.l_client_name.setText("Ім'я")
              self.le_client_name=QLineEdit()
              self.le_client_name.setReadOnly(True)

              self.l_client_secondname=QLabel()
              self.l_client_secondname.setText('По батькові')
              self.le_client_secondname=QLineEdit()
              self.le_client_secondname.setReadOnly(True)

              self.l_client_city=QLabel()
              self.l_client_city.setText('Місто')
              self.le_client_city=QLineEdit()
              self.le_client_city.setReadOnly(True)

              self.l_client_post=QLabel()
              self.l_client_post.setText('Пошта №')
              self.le_client_post=QLineEdit()
              self.le_client_post.setReadOnly(True)

              self.l_client_phone=QLabel()
              self.l_client_phone.setText('Телефон')
              self.le_client_phone=QLineEdit()
              self.le_client_phone.setReadOnly(True)
              
              self.l_client_note=QLabel()
              self.l_client_note.setText('Примітка \nпо клієнту')
              self.le_client_note=QTextEdit()
              self.le_client_note.setReadOnly(True)
              
                               
              self.l_date_in=QLabel()
              self.l_date_in.setText('Дата отримання')
              self.le_date_in=QLineEdit()
              self.le_date_in.setReadOnly(True)
              
              self.l_date_repair=QLabel()
              self.l_date_repair.setText('Дата ремонту')
              self.le_date_repair=QLineEdit()
              self.le_date_repair.setReadOnly(True)

              self.l_engineer=QLabel()
              self.l_engineer.setText('Інженер')
              self.le_engineer=QLineEdit()
              self.le_engineer.setReadOnly(True)

              self.l_date_out=QLabel()
              self.l_date_out.setText('Виданий з ремонту')
              self.le_date_out=QLineEdit()
              self.le_date_out.setReadOnly(True)

              self.l_rapair_note=QLabel()
              self.l_rapair_note.setText('Перелік робіт')
              self.le_rapair_note=QTextEdit()
              self.le_rapair_note.setReadOnly(True)

              self.l_price=QLabel()
              self.l_price.setText('Ціна ремонту')
              self.le_price=QLineEdit()
              self.le_price.setReadOnly(True)

              self.l_pay=QLabel()
              self.l_pay.setText('Дата оплати')
              self.le_pay=QLineEdit()
              self.le_pay.setReadOnly(True)

              self.l_send=QLabel()
              self.l_send.setText('Дата видачі')
              self.le_send=QLineEdit()
              self.le_send.setReadOnly(True)

              self.l_note=QLabel()
              self.l_note.setText('Примітка \nпо пристрою')
              self.le_note=QTextEdit()
              self.le_note.setReadOnly(True)

              self.le_number.setText(str(self.model_rar.record(self.view_rar.currentIndex().row()).value(1)))
              self.le_device.setText(str(self.model_rar.record(self.view_rar.currentIndex().row()).value(3)))
              self.le_date_in.setText(str(self.model_rar.record(self.view_rar.currentIndex().row()).value(4)))
              self.le_date_repair.setText(str(self.model_rar.record(self.view_rar.currentIndex().row()).value(6)))
              self.le_engineer.setText(self.model_rar.record(self.view_rar.currentIndex().row()).value(7))
              self.le_date_out.setText(str(self.model_rar.record(self.view_rar.currentIndex().row()).value(8)))
              self.le_rapair_note.setText(str(self.model_rar.record(self.view_rar.currentIndex().row()).value(9)))
              self.le_price.setText(str(self.model_rar.record(self.view_rar.currentIndex().row()).value(10)))
              self.le_pay.setText(str(self.model_rar.record(self.view_rar.currentIndex().row()).value(11)))
              self.le_send.setText(str(self.model_rar.record(self.view_rar.currentIndex().row()).value(12)))
              self.le_note.setText(str(self.model_rar.record(self.view_rar.currentIndex().row()).value(5)))
              #self.model_client.select()
              #while self.model_client.canFetchMore():
              #self.model_client.fetchMore()
              row=self.model_rar.rowCount()-1 
              while row>=0:
                     if self.model_rar.record(self.view_rar.currentIndex().row()).value(2)==self.model_client.record(row).value(1):
                            #print(row)
                            #print(str(self.model_client.record(row).value(13)))
                            self.le_client.setText(str(self.model_client.record(row).value(1)))
                            self.le_client_name.setText(self.model_client.record(row).value(2))
                            self.le_client_secondname.setText(self.model_client.record(row).value(3))
                            self.le_client_city.setText(self.model_client.record(row).value(4))
                            self.le_client_post.setText(str(self.model_client.record(row).value(5)))
                            self.le_client_phone.setText(str(self.model_client.record(row).value(6)))
                            self.le_client_note.setText(self.model_client.record(row).value(7))
                            break
                     row=row-1
              self.main=QGridLayout()
              self.main.setColumnStretch(1,1)
              self.main.setColumnMinimumWidth(1,150)
              self.main.addWidget(self.l_number,0,0)
              self.main.addWidget(self.le_number,0,1)
              self.main.addWidget(self.l_device,1,0)
              self.main.addWidget(self.le_device,1,1)
              self.main.addWidget(self.l_client,2,0)
              self.main.addWidget(self.le_client,2,1)
              self.main.addWidget(self.l_client_name,3,0)
              self.main.addWidget(self.le_client_name,3,1)
              self.main.addWidget(self.l_client_secondname,4,0)
              self.main.addWidget(self.le_client_secondname,4,1)
              self.main.addWidget(self.l_client_city,5,0)
              self.main.addWidget(self.le_client_city,5,1)
              self.main.addWidget(self.l_client_post,6,0)
              self.main.addWidget(self.le_client_post,6,1)
              self.main.addWidget(self.l_client_phone,7,0)
              self.main.addWidget(self.le_client_phone,7,1)
              self.main.addWidget(self.l_client_note,8,0)
              self.main.addWidget(self.le_client_note,8,1)

              self.main.addWidget(self.l_date_in,0,2)
              self.main.addWidget(self.le_date_in,0,3)
              self.main.addWidget(self.l_date_repair,1,2)
              self.main.addWidget(self.le_date_repair,1,3)
              self.main.addWidget(self.l_engineer,2,2)
              self.main.addWidget(self.le_engineer,2,3)
              self.main.addWidget(self.l_date_out,3,2)
              self.main.addWidget(self.le_date_out,3,3)
              self.main.addWidget(self.l_rapair_note,4,2)
              self.main.addWidget(self.le_rapair_note,4,3)
              self.main.addWidget(self.l_price,5,2)
              self.main.addWidget(self.le_price,5,3)
              self.main.addWidget(self.l_pay,6,2)
              self.main.addWidget(self.le_pay,6,3)
              self.main.addWidget(self.l_send,7,2)
              self.main.addWidget(self.le_send,7,3)
              self.main.addWidget(self.l_note,8,2)
              self.main.addWidget(self.le_note,8,3)
              
              self.beg_main=QVBoxLayout()
              self.beg_main.addLayout(self.main)
              self.dialog_window.setLayout(self.beg_main)
              self.dialog_window.show()
              #db.close()

#==========================================

if __name__=='__main__':
       import sys
       
       app = QApplication(sys.argv)
       #if not connect():
              #sys.exit(1)
       window = work_bd('workbd')
       window.show()
       sys.exit(app.exec_())

                            
