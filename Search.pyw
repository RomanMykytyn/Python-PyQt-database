from PyQt5.QtCore import (Qt, QDate, QRegExp)
from PyQt5.QtGui import (QFont, QRegExpValidator)
from PyQt5.QtSql import (QSqlTableModel, QSqlDatabase)
from PyQt5.QtWidgets import (QPushButton, QTextEdit, QLineEdit, QDateEdit, QComboBox, QSpinBox, QLabel,
                             QHBoxLayout, QVBoxLayout, QGroupBox, QWidget, QApplication, QTableView, QAbstractItemView,
                             QGridLayout, QSizePolicy, QFileDialog, QDialog, QMainWindow)
import sys, time, datetime, winreg


class MyWindow(QWidget):
    def __init__(self, parent=None):
        #super(MyWindow, self).__init__(parent)
        QWidget.__init__(self, parent)
        
        
        
        global file_name
        self.file_name = ["111",""]
        #self.connect()
        self.file_name[1] = self.get_reg('path')
        print(self.file_name[0])
        #if self.file_name[0] != "" and self.file_name[0] != "111"
        

        print(self.file_name[1])


        global model_base
        self.model_base = QSqlTableModel(self)
        self.model_base.setTable('workbd_rar')
        self.model_base.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model_base.select()

        global model_client
        self.model_client = QSqlTableModel(self)
        self.model_client.setTable('client')
        self.model_client.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model_client.select()

        self.model_base.setHeaderData(1, Qt.Horizontal,'№')
        self.model_base.setHeaderData(2, Qt.Horizontal,'Клієнт')
        self.model_base.setHeaderData(3, Qt.Horizontal, 'Пристрій')
        self.model_base.setHeaderData(4, Qt.Horizontal, 'Дата отримання')
        self.model_base.setHeaderData(12, Qt.Horizontal, 'Дата видачі')

        global view_base
        self.view_base = QTableView()
        self.view_base.setModel(self.model_base)
        self.view_base.setShowGrid(True)
        self.view_base.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.view_base.setSelectionMode(QAbstractItemView.SingleSelection)
        self.view_base.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.view_base.setColumnHidden(0, True)
        self.view_base.setColumnHidden(5, True)
        self.view_base.setColumnHidden(6, True)
        self.view_base.setColumnHidden(7, True)
        self.view_base.setColumnHidden(8, True)
        self.view_base.setColumnHidden(9, True)
        self.view_base.setColumnHidden(10, True)
        self.view_base.setColumnHidden(11, True)
        self.view_base.setColumnHidden(13, True)
        #self.view_base = None
        global topbox
        global size
        global box_search
        self.mainbox = QVBoxLayout()
        self.topbox = QHBoxLayout()
        #global font
        self.font = QFont()
        self.font.setBold(True)
        self.size = QSizePolicy()
        self.size.setHorizontalPolicy(QSizePolicy.Maximum)
        self.size.setHorizontalStretch(200)
        self.box_search = QGroupBox('Налаштування пошуку')
        self.box_search.setSizePolicy(self.size)
        self.box_search.setFont(self.font)
        #self.topbox.insertStretch(10, 10)
        self.info_box = QGroupBox('Інформація')
        self.info_box.setFont(self.font)
        self.font.setBold(False)
        self.size2 = QSizePolicy()
        self.size2.setHorizontalPolicy(QSizePolicy.Minimum)
        self.size2.setHorizontalStretch(1000)
        self.view_base.setSizePolicy(self.size2)

        self.nomer_in = QLabel()
        self.nomer_in.setFont(self.font)
        self.nomer_in.setText('Номер пристрою')
        self.e_nomer_in = QLineEdit()
        #self.e_nomer_in.setSizePolicy(self.size)
        self.e_nomer_in.setFont(self.font)
        self.valid_2 = QRegExpValidator(QRegExp("[0-9][0-9][0-9][0-9][0-9]"))
        self.e_nomer_in.setValidator(self.valid_2)
        #self.e_nomer_in.setMaximum(50000)
        #self.e_nomer_in.clear()

        global e_surname_in
        self.surname_in = QLabel()
        self.surname_in.setFont(self.font)
        self.surname_in.setText('Прізвище')
        self.e_surname_in = QComboBox()
        #self.e_surname_in.setSizePolicy(self.size)
        self.e_surname_in.setFont(self.font)
        #self.connect()
        #self.e_surname_in.setModel(self.model_client)
        #self.e_surname_in.setModelColumn(self.model_client.fieldIndex('surname'))


        self.date_in_in = QLabel()
        self.date_in_in.setFont(self.font)
        self.date_in_in.setText('Дата прийому\n(дд.мм.рррр)')
        self.z_date_in_in = QLineEdit()
#z_date_in_in.setDate(QDate(0000, 10, 10))
#z_date_in_in.setMinimumDate(QDate(2010, 10, 10))
#z_date_in_in.setDate(QDate(2010, 10, 10))
#z_date_in_in.setSpecialValueText("")
        #self.z_date_in_in.setSizePolicy(self.size)
        self.z_date_in_in.setFont(self.font)
        self.valid = QRegExpValidator(QRegExp("(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)\d\d"))
        self.z_date_in_in.setValidator(self.valid)
#z_date_in_in.setCalendarPopup(True)
        self.po_date_in_in = QLineEdit()
        #self.po_date_in_in.setSizePolicy(self.size)
        self.po_date_in_in.setFont(self.font)
        self.po_date_in_in.setValidator(self.valid)
#po_date_in_in.setCalendarPopup(True)

        self.date_out_out = QLabel()
        self.date_out_out.setFont(self.font)
        self.date_out_out.setText('Дата видачі\n(дд.мм.рррр)')
        self.z_date_out_out = QLineEdit()
        #self.z_date_out_out.setSizePolicy(self.size)
        self.z_date_out_out.setFont(self.font)
        self.z_date_out_out.setValidator(self.valid)
#z_date_out_out.setCalendarPopup(True)
        self.po_date_out_out = QLineEdit()
        #self.po_date_out_out.setSizePolicy(self.size)
        self.po_date_out_out.setFont(self.font)
        self.po_date_out_out.setValidator(self.valid)
#po_date_out_out.setCalendarPopup(True)

        self.add_button = QPushButton('Вибрати базу')
        #self.add_button.setSizePolicy(self.size)
        self.add_button.setFont(self.font)
        self.add_button.clicked.connect(self.add_file)
        self.search_button = QPushButton('Пошук')
        #self.search_button.setSizePolicy(self.size)
        self.search_button.clicked.connect(self.search)
        #self.view_base.clicked.connect(self.click)

        self.search = QGridLayout()
#search.setVerticalSpacing(-100)
        self.search.setHorizontalSpacing(15)
        self.search.setColumnMinimumWidth(1, 50)
        self.search.setColumnStretch(0, 10)
        self.search.setColumnStretch(1, 10)
        self.search.addWidget(self.nomer_in,0,0,Qt.AlignBottom)
        self.search.addWidget(self.e_nomer_in,1,0)
        self.search.addWidget(self.surname_in,3,0,Qt.AlignBottom)
        self.search.addWidget(self.e_surname_in,4,0)
        self.search.addWidget(self.date_in_in,0,1,Qt.AlignBottom)
        self.search.addWidget(self.z_date_in_in,1,1)
        self.search.addWidget(self.po_date_in_in,2,1,Qt.AlignTop)
        self.search.addWidget(self.date_out_out,3,1,Qt.AlignBottom)
        self.search.addWidget(self.z_date_out_out,4,1)
        self.search.addWidget(self.po_date_out_out,5,1,Qt.AlignTop)
        self.search.addWidget(self.add_button,1,2)
        self.search.addWidget(self.search_button,4,2)

        self.l_number=QLabel()
        self.l_number.setFont(self.font)
        self.l_number.setText('Номер')
        self.le_number=QLineEdit()
        self.le_number.setFont(self.font)
        self.le_number.setReadOnly(True)
              
        self.l_device=QLabel()
        self.l_device.setFont(self.font)
        self.l_device.setText('Пристрій')
        self.le_device=QLineEdit()
        self.le_device.setFont(self.font)
        self.le_device.setReadOnly(True)
                           
        self.l_client=QLabel()
        self.l_client.setFont(self.font)
        self.l_client.setText('Прізвище')
        self.le_client=QLineEdit()
        self.le_client.setFont(self.font)
        self.le_client.setReadOnly(True)

        self.l_client_name=QLabel()
        self.l_client_name.setFont(self.font)
        self.l_client_name.setText("Ім'я")
        self.le_client_name=QLineEdit()
        self.le_client_name.setFont(self.font)
        self.le_client_name.setReadOnly(True)

        self.l_client_secondname=QLabel()
        self.l_client_secondname.setFont(self.font)
        self.l_client_secondname.setText('По батькові')
        self.le_client_secondname=QLineEdit()
        self.le_client_secondname.setFont(self.font)
        self.le_client_secondname.setReadOnly(True)

        self.l_client_city=QLabel()
        self.l_client_city.setFont(self.font)
        self.l_client_city.setText('Місто')
        self.le_client_city=QLineEdit()
        self.le_client_city.setFont(self.font)
        self.le_client_city.setReadOnly(True)

        self.l_client_post=QLabel()
        self.l_client_post.setFont(self.font)
        self.l_client_post.setText('Пошта №')
        self.le_client_post=QLineEdit()
        self.le_client_post.setFont(self.font)
        self.le_client_post.setReadOnly(True)

        self.l_client_phone=QLabel()
        self.l_client_phone.setFont(self.font)
        self.l_client_phone.setText('Телефон')
        self.le_client_phone=QLineEdit()
        self.le_client_phone.setFont(self.font)
        self.le_client_phone.setReadOnly(True)
              
        self.l_client_note=QLabel()
        self.l_client_note.setFont(self.font)
        self.l_client_note.setText('Примітка \nпо клієнту')
        self.le_client_note=QTextEdit()
        self.le_client_note.setFont(self.font)
        self.le_client_note.setReadOnly(True)
              
                               
        self.l_date_in=QLabel()
        self.l_date_in.setFont(self.font)
        self.l_date_in.setText('Дата отримання')
        self.le_date_in=QLineEdit()
        self.le_date_in.setFont(self.font)
        self.le_date_in.setReadOnly(True)
              
        self.l_date_repair=QLabel()
        self.l_date_repair.setFont(self.font)
        self.l_date_repair.setText('Дата ремонту')
        self.le_date_repair=QLineEdit()
        self.le_date_repair.setFont(self.font)
        self.le_date_repair.setReadOnly(True)

        self.l_engineer=QLabel()
        self.l_engineer.setFont(self.font)
        self.l_engineer.setText('Інженер')
        self.le_engineer=QLineEdit()
        self.le_engineer.setFont(self.font)
        self.le_engineer.setReadOnly(True)

        self.l_date_out=QLabel()
        self.l_date_out.setFont(self.font)
        self.l_date_out.setText('Виданий з ремонту')
        self.le_date_out=QLineEdit()
        self.le_date_out.setFont(self.font)
        self.le_date_out.setReadOnly(True)

        self.l_rapair_note=QLabel()
        self.l_rapair_note.setFont(self.font)
        self.l_rapair_note.setText('Перелік робіт')
        self.le_rapair_note=QTextEdit()
        self.le_rapair_note.setFont(self.font)
        self.le_rapair_note.setReadOnly(True)

        self.l_price=QLabel()
        self.l_price.setFont(self.font)
        self.l_price.setText('Ціна ремонту')
        self.le_price=QLineEdit()
        self.le_price.setFont(self.font)
        self.le_price.setReadOnly(True)

        self.l_pay=QLabel()
        self.l_pay.setFont(self.font)
        self.l_pay.setText('Дата оплати')
        self.le_pay=QLineEdit()
        self.le_pay.setFont(self.font)
        self.le_pay.setReadOnly(True)

        self.l_send=QLabel()
        self.l_send.setFont(self.font)
        self.l_send.setText('Дата видачі')
        self.le_send=QLineEdit()
        self.le_send.setFont(self.font)
        self.le_send.setReadOnly(True)

        self.l_note=QLabel()
        self.l_note.setFont(self.font)
        self.l_note.setText('Примітка \nпо пристрою')
        self.le_note=QTextEdit()
        self.le_note.setFont(self.font)
        self.le_note.setReadOnly(True)

        self.bt_search = QPushButton('Пошук')
        self.bt_addbase = QPushButton('Відкрити базу')

        self.main=QGridLayout()
        self.main.setColumnStretch(1,100)
        self.main.setColumnStretch(3,100)
        self.main.setColumnStretch(5,150)
        self.main.setColumnMinimumWidth(1,150)
        self.main.setVerticalSpacing(20)
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
        self.main.addWidget(self.l_client_note,6,4)
        self.main.addWidget(self.le_client_note,6,5,2,1)

        self.main.addWidget(self.l_date_in,0,2)
        self.main.addWidget(self.le_date_in,0,3)
        self.main.addWidget(self.l_date_repair,1,2)
        self.main.addWidget(self.le_date_repair,1,3)
        self.main.addWidget(self.l_engineer,2,2)
        self.main.addWidget(self.le_engineer,2,3)
        self.main.addWidget(self.l_date_out,3,2)
        self.main.addWidget(self.le_date_out,3,3)
        self.main.addWidget(self.l_rapair_note,3,4)
        self.main.addWidget(self.le_rapair_note,3,5,3,1)
        self.main.addWidget(self.l_price,4,2)
        self.main.addWidget(self.le_price,4,3)
        self.main.addWidget(self.l_pay,5,2)
        self.main.addWidget(self.le_pay,5,3)
        self.main.addWidget(self.l_send,6,2)
        self.main.addWidget(self.le_send,6,3)
        self.main.addWidget(self.l_note,0,4)
        self.main.addWidget(self.le_note,0,5,3,1)

        self.box_search.setLayout(self.search)
        self.topbox.addWidget(self.view_base)
        self.topbox.addWidget(self.box_search)
        self.info_box.setLayout(self.main)
        self.mainbox.addLayout(self.topbox)
        self.mainbox.addWidget(self.info_box)
        self.setLayout(self.mainbox)
        self.e_surname_in.setModel(self.model_client)
        self.e_surname_in.setModelColumn(self.model_client.fieldIndex('surname'))
        self.connect()
        


    def add_file(self):
        file = QFileDialog( caption='Вибір файла', directory='c:\\', filter='*.db')
        file.setFileMode(QFileDialog.ExistingFile)
        result = file.exec()
        if result == QDialog.Accepted:
            file_temp = file.selectedFiles()
            self.file_name[1] = file_temp[0]
            print(self.file_name[1])
            #self.topbox.removeWidget(self.view_base)
            #self.view_base.setParent(None)
            self.connect()
            self.set_reg(self.file_name[1])
            #MyWindow()

    def connect(self):
        self.topbox.removeWidget(self.view_base)
        self.view_base.setParent(None)
        global db
        self.db=QSqlDatabase.addDatabase('QSQLITE')
        print(self.file_name[1])
        self.db.setDatabaseName(self.file_name[1])
        self.db.open()

        #global model_base
        self.model_base = QSqlTableModel(self)
        self.model_base.setTable('workbd_rar')
        self.model_base.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model_base.select()

        #global view_base
        self.view_base = QTableView()
        self.view_base.setModel(self.model_base)
        self.view_base.setShowGrid(True)
        self.view_base.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.view_base.setSelectionMode(QAbstractItemView.SingleSelection)
        self.view_base.setSelectionBehavior(QAbstractItemView.SelectRows)
        #self.view_base.setFont(self.font)
        self.view_base.setColumnHidden(0, True)
        self.view_base.setColumnHidden(5, True)
        self.view_base.setColumnHidden(6, True)
        self.view_base.setColumnHidden(7, True)
        self.view_base.setColumnHidden(8, True)
        self.view_base.setColumnHidden(9, True)
        self.view_base.setColumnHidden(10, True)
        self.view_base.setColumnHidden(11, True)
        self.view_base.setColumnHidden(13, True)
        self.view_base.clicked.connect(self.click)

        self.model_base.setHeaderData(1, Qt.Horizontal,'№')
        self.model_base.setHeaderData(2, Qt.Horizontal,'Клієнт')
        self.model_base.setHeaderData(3, Qt.Horizontal, 'Пристрій')
        self.model_base.setHeaderData(4, Qt.Horizontal, 'Дата отримання')
        self.model_base.setHeaderData(12, Qt.Horizontal, 'Дата видачі')
        self.size.setHorizontalPolicy(QSizePolicy.Maximum)
        self.box_search.setSizePolicy(self.size)

        #global model_client
        self.model_client = QSqlTableModel(self)
        self.model_client.setTable('client')
        self.model_client.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model_client.select()

        self.e_surname_in.setModel(self.model_client)
        self.e_surname_in.setModelColumn(self.model_client.fieldIndex('surname'))
        self.e_surname_in.insertItem(0, "")
        #self.topbox.removeWidget(self.view_base)
        #self.topbox.removeWidget(self.view_base)
        self.box_search.setSizePolicy(self.size)
        self.size2 = QSizePolicy()
        self.size2.setHorizontalPolicy(QSizePolicy.Minimum)
        self.size2.setHorizontalStretch(1000)
        self.view_base.setSizePolicy(self.size2)
        self.topbox.insertWidget(0, self.view_base)
        #self.topbox.addWidget(self.box_search)
        return True

    def search(self):
        filter_string = ''
        if self.e_nomer_in.text() != '':
            filter_string = filter_string + 'id_number == ' + self.e_nomer_in.text() + ' and '
        if self.e_surname_in.currentText() != '':
            filter_string = filter_string + 'surname == ' + '"' + self.e_surname_in.currentText() + '"' + ' and '
        if self.z_date_in_in.text() != '' and self.po_date_in_in.text() == '':
            filter_string = filter_string + 'device_in_date == ' + '"' + self.z_date_in_in.text() + '"' + ' and '
        if self.z_date_in_in.text() != '' and self.po_date_in_in.text() != '':
            temp = self.date_list(self.z_date_in_in.text(), self.po_date_in_in.text())
            #print(temp)
            filter_string = filter_string + 'device_in_date IN ' + '(' + temp + ')' + ' and '
            #print(filter_string)
        if self.z_date_out_out.text() != '' and self.po_date_out_out.text() == '':
            filter_string = filter_string + 'send_date == ' + '"' + self.z_date_out_out.text() + '"' + ' and '
        if self.z_date_out_out.text() != '' and self.po_date_out_out.text() != '':
            temp = self.date_list(self.z_date_out_out.text(), self.po_date_out_out.text())
            filter_string = filter_string + 'send_date IN ' + '(' + temp + ')' + ' and '
        filter_string = filter_string[0:-5]
        self.model_base.setFilter(filter_string)
        self.model_base.select()
        print(filter_string)
        #print(self.po_date_in_in.text())

    def date_list(self, z, po):
        z_strukt = time.strptime(z, '%d.%m.%Y')
        #print(z_strukt[1])
        po_strukt = time.strptime(po, '%d.%m.%Y')
        z_date = datetime.date(z_strukt[0], z_strukt[1], z_strukt[2])
        #print(z_date)
        po_date = datetime.date(po_strukt[0], po_strukt[1], po_strukt[2])
        note = [z]
        while z_date < po_date:
            z_date = z_date + datetime.timedelta(days=1)
            note.append(z_date.strftime('%d.%m.%Y'))
            if len(note) > 500:
                break
        str_note = str(note)
        str_note = str_note[1:-1]
        #print(str_note)
        return str_note

    def click(self):
        self.le_number.setText(str(self.model_base.record(self.view_base.currentIndex().row()).value(1)))
        self.le_device.setText(str(self.model_base.record(self.view_base.currentIndex().row()).value(3)))
        self.le_date_in.setText(str(self.model_base.record(self.view_base.currentIndex().row()).value(4)))
        self.le_date_repair.setText(str(self.model_base.record(self.view_base.currentIndex().row()).value(6)))
        self.le_engineer.setText(self.model_base.record(self.view_base.currentIndex().row()).value(7))
        self.le_date_out.setText(str(self.model_base.record(self.view_base.currentIndex().row()).value(8)))
        self.le_rapair_note.setText(str(self.model_base.record(self.view_base.currentIndex().row()).value(9)))
        self.le_price.setText(str(self.model_base.record(self.view_base.currentIndex().row()).value(10)))
        self.le_pay.setText(str(self.model_base.record(self.view_base.currentIndex().row()).value(11)))
        self.le_send.setText(str(self.model_base.record(self.view_base.currentIndex().row()).value(12)))
        self.le_note.setText(str(self.model_base.record(self.view_base.currentIndex().row()).value(5)))
        row=self.model_client.rowCount()-1 
        while row>=0:
            if self.model_base.record(self.view_base.currentIndex().row()).value(2)==self.model_client.record(row).value(1):
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
        s = '111'
        print(s)

    def set_reg(self, value):
        try:
            winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\DVBvending\Settings')
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\DVBvending\Settings', 0, winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, 'path', 0, winreg.REG_SZ, value)
            winreg.CloseKey(registry_key)
            return True
        except WindowsError:
            return False

    def get_reg(self, name):
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\DVBvending\Settings', 0, winreg.KEY_READ)
            temp = winreg.QueryValueEx(registry_key, name)
            winreg.CloseKey(registry_key)
            value = temp[0]
            return value
        except WindowsError:
            return None
        
        
            


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    #global window
    window = MyWindow()
    window. setWindowTitle('Пошук в базі ДВБ-вендінг.')
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())


