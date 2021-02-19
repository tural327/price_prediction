from PyQt5 import QtWidgets
from model_py import Ui_Price
import pandas as pd
import numpy as np
import pickle
filename = 'pred.sav'
loaded_model = pickle.load(open(filename, 'rb'))
tur = pd.read_csv('val.csv')
X = tur.drop('Unnamed: 0',axis=1)
import sys
class BMI_calculater(QtWidgets.QMainWindow, Ui_Price):
    def __init__(self):
        super(BMI_calculater, self).__init__()
        self.uif = Ui_Price()
        self.uif.setupUi(self)
        self.uif.calculate.pressed.connect(self.Bmi_calculate)

    def Bmi_calculate(self):
        def predict_price(UNDER_CONSTRUCTION, RERA, BHK_NO, SQUARE_FT, READY_TO_MOVE, RESALE, location, POSTED_BY,
                          BHK_OR_RK):
            loc_index = np.where(X.columns == location)[0][0]
            loc_POSTED_BY = np.where(X.columns == POSTED_BY)[0][0]
            loc_BHK_OR_RK = np.where(X.columns == BHK_OR_RK)[0][0]

            x = np.zeros(len(X.columns))
            x[0] = UNDER_CONSTRUCTION
            x[1] = RERA
            x[2] = BHK_NO
            x[3] = SQUARE_FT
            x[4] = READY_TO_MOVE
            x[5] = RESALE
            if loc_index >= 0:
                x[loc_index] = 1
            if loc_POSTED_BY >= 0:
                x[loc_POSTED_BY] = 1
            if loc_BHK_OR_RK >= 0:
                x[loc_BHK_OR_RK] = 1

            return loaded_model.predict([x])[0]
        a0 = str(self.uif.under_constr.currentText())
        if a0 =='yes':
            UNDER_CONSTRUCTION = 0
        else:
            UNDER_CONSTRUCTION = 1
        a1 = str(self.uif.RERA.currentText())
        if a1 =='yes':
            RERA = 0
        else:
            RERA = 1
        BHK_NO = float(self.uif.BHK_no.text())
        SQUARE_FT = float(self.uif.sqrft.text())
        a2 = str(self.uif.ready_to_move.currentText())
        if a2 =='yes':
            READY_TO_MOVE = 0
        else:
            READY_TO_MOVE = 1
        a3 = str(self.uif.resale.currentText())
        if a3 =='yes':
            RESALE = 0
        else:
            RESALE = 1
        location = str(self.uif.city.currentText())
        POSTED_BY = str(self.uif.builder.currentText())
        BHK_OR_RK = str(self.uif.bhk_bk.currentText())
        test = predict_price(UNDER_CONSTRUCTION,RERA,BHK_NO,SQUARE_FT,READY_TO_MOVE,RESALE,location,POSTED_BY,BHK_OR_RK)
        self.uif.pushButton.setText(str(test))
        #print('Weight {} , height {}'.format(weight,height))

app = QtWidgets.QApplication(sys.argv)

bmic = BMI_calculater()

bmic.show()

app.exec_()

### pyuic5 2.ui -o base.py



