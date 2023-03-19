import pickle
import numpy as np
from application import Ui_laptopPrice_obj
from PyQt5 import QtWidgets
import sys

usd_rate = 335.50

def predicts():
        with open('predictor.pickle', 'rb') as f:
            model = pickle.load(f)
        # Step 3: Prepare input data

        """Index(['Ram', 'Weight', 'Touchscreen', 'IPS', 'Company_Acer', 'Company_Apple',
       'Company_Asus', 'Company_Dell', 'Company_HP', 'Company_Lenovo',
       'Company_MSI', 'Company_Other', 'Company_Toshiba',
       'TypeName_2 in 1 Convertible', 'TypeName_Gaming', 'TypeName_Netbook',
       'TypeName_Notebook', 'TypeName_Ultrabook', 'TypeName_Workstation',
       'OpSys_Linux', 'OpSys_Mac', 'OpSys_Other', 'OpSys_Windows',
       'cpu_name_AMD', 'cpu_name_Intel Core i3', 'cpu_name_Intel Core i5',
       'cpu_name_Intel Core i7', 'cpu_name_Other', 'gpu_name_AMD',
       'gpu_name_Intel', 'gpu_name_Nvidia'],
      dtype='object')"""
        input_data = [[]]
        input_data[0].append(ui.spinBox.value())
        input_data[0].append(ui.doubleSpinBox.value())
        if ui.checkBox.isChecked() == True:
              input_data[0].append(1)
        else:
              input_data[0].append(0)

        if ui.checkBox_2.isChecked() == True:
              input_data[0].append(1)
        else:
              input_data[0].append(0)
              
        for i in range(0,9):
              if ui.comboBox.currentIndex() == i:
                    input_data[0].append(1)
              else:
                    input_data[0].append(0)
            
        for i in range(0,6):
              if ui.comboBox_2.currentIndex() == i:
                    input_data[0].append(1)
              else:
                    input_data[0].append(0)

        for i in range(0,4):
              if ui.comboBox_3.currentIndex() == i:
                    input_data[0].append(1)
              else:
                    input_data[0].append(0)

        for i in range(0,5):
              if ui.comboBox_4.currentIndex() == i:
                    input_data[0].append(1)
              else:
                    input_data[0].append(0)

        for i in range(0,3):
              if ui.comboBox_5.currentIndex() == i:
                    input_data[0].append(1)
              else:
                    input_data[0].append(0)
              
        predictions = model.predict(input_data)
        price = round(predictions[0], 2)*usd_rate
        
        ui.lcdNumber.display(price)





app = QtWidgets.QApplication(sys.argv)
laptopPrice_obj = QtWidgets.QDialog()
ui = Ui_laptopPrice_obj()
ui.setupUi(laptopPrice_obj)
ui.pushButton_2.clicked.connect(predicts) # type: ignore
laptopPrice_obj.show()







sys.exit(app.exec_())