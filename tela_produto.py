from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_MainWindow(object):
    def conectar(self):
        return mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "crud_loja"
        )
    
    def atualizar(self):
        linha_selecionada = self.tableProdutp.currentRow()
        
        id = self.tableProdutp.item(linha_selecionada, 0).text()
        nome = self.lineEditNome.text()
        descricao = self.lineEditDescricao.text()
        preco = self.lineEditPreco.text()
        quantidade = self.lineEditQuantidade.text()

        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("UPDATE produtos SET nome = %s, descricao = %s, preco = %s, quantidade = %s WHERE id = %s", (nome, descricao, preco, quantidade, id))
        conexao.commit()
        conexao.close()

        self.listar()
    
    def listar(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos")
        resultado = cursor.fetchall()
        self.tableProdutp.setRowCount(len(resultado))
        for i, linha in enumerate(resultado):
            for j, valor in enumerate(linha):
                self.tableProdutp.setItem(i, j, QtWidgets.QTableWidgetItem(str(valor)))
        conexao.close()

    
    def adicionar(self):
        nome = self.lineEditNome.text()
        descricao = self.lineEditDescricao.text()
        preco = self.lineEditPreco.text()
        quantidade = self.lineEditQuantidade.text()

        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO produtos (nome, descricao, preco, quantidade) VALUES (%s, %s, %s, %s)", (nome, descricao, preco, quantidade))
        conexao.commit()
        conexao.close()

        self.listar()
    
    def deletar(self):
        linha = self.tableProdutp.currentRow()
        id_produto = self.tableProdutp.item(linha, 0).text()
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
        conexao.commit()
        conexao.close

        self.listar()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 585)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.labelTitulo = QtWidgets.QLabel(self.centralwidget)
        self.labelTitulo.setGeometry(QtCore.QRect(270, 10, 301, 41))
        self.labelTitulo.setObjectName("labelTitulo")
        
        self.labelNome = QtWidgets.QLabel(self.centralwidget)
        self.labelNome.setGeometry(QtCore.QRect(30, 70, 81, 21))
        self.labelNome.setObjectName("labelNome")
       
        self.labelDescricao = QtWidgets.QLabel(self.centralwidget)
        self.labelDescricao.setGeometry(QtCore.QRect(10, 120, 101, 21))
        self.labelDescricao.setObjectName("labelDescricao")
       
        self.labelPreco = QtWidgets.QLabel(self.centralwidget)
        self.labelPreco.setGeometry(QtCore.QRect(40, 170, 71, 21))
        self.labelPreco.setObjectName("labelPreco")
        
        self.labelQuantidade = QtWidgets.QLabel(self.centralwidget)
        self.labelQuantidade.setGeometry(QtCore.QRect(0, 220, 111, 21))
        self.labelQuantidade.setObjectName("labelQuantidade")
        
        self.lineEditNome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNome.setGeometry(QtCore.QRect(110, 70, 311, 20))
        self.lineEditNome.setObjectName("lineEditNome")
       
        self.lineEditDescricao = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDescricao.setGeometry(QtCore.QRect(112, 120, 311, 20))
        self.lineEditDescricao.setObjectName("lineEditDescricao")
       
        self.lineEditPreco = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPreco.setGeometry(QtCore.QRect(112, 170, 311, 20))
        self.lineEditPreco.setObjectName("lineEditPreco")
       
        self.lineEditQuantidade = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditQuantidade.setGeometry(QtCore.QRect(112, 220, 311, 20))
        self.lineEditQuantidade.setObjectName("lineEditQuantidade")
        
        self.BtnAdicionar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnAdicionar.setGeometry(QtCore.QRect(470, 140, 91, 31))
        self.BtnAdicionar.setMinimumSize(QtCore.QSize(91, 0))
        self.BtnAdicionar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BtnAdicionar.setStyleSheet("image: url(icon/add.ico);\n"
"background-color: rgb(165, 177, 252);")
        self.BtnAdicionar.setText("")
        self.BtnAdicionar.setObjectName("BtnAdicionar")
        
        self.BtnEditar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnEditar.setGeometry(QtCore.QRect(590, 140, 91, 31))
        self.BtnEditar.setStyleSheet("image: url(icon/edit.ico); \n"
"background-color: rgb(253, 255, 131);\n"
"")
        self.BtnEditar.setText("")
        self.BtnEditar.setObjectName("BtnEditar")
        
        self.BtnExcluir = QtWidgets.QPushButton(self.centralwidget)
        self.BtnExcluir.setGeometry(QtCore.QRect(700, 140, 91, 31))
        self.BtnExcluir.setStyleSheet("image: url(icon/delete.ico);\n"
"background-color: rgb(255, 114, 114);")
        self.BtnExcluir.setText("")
        self.BtnExcluir.setObjectName("BtnExcluir")
        
        self.BtnRecarregar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnRecarregar.setGeometry(QtCore.QRect(654, 270, 91, 31))
        self.BtnRecarregar.setStyleSheet("image: url(icon/reload.ico);\n"
"background-color: rgb(103, 255, 113);")
        self.BtnRecarregar.setText("")
        self.BtnRecarregar.setObjectName("BtnRecarregar")
        
        self.tableProdutp = QtWidgets.QTableWidget(self.centralwidget)
        self.tableProdutp.setGeometry(QtCore.QRect(110, 260, 531, 281))
        self.tableProdutp.setObjectName("tableProdutp")
        self.tableProdutp.setColumnCount(5)
        self.tableProdutp.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableProdutp.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableProdutp.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableProdutp.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableProdutp.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableProdutp.setHorizontalHeaderItem(4, item)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        MainWindow.setMenuBar(self.menubar)
        self.actionAdicionar = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/add.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionAdicionar.setIcon(icon)
        self.actionAdicionar.setObjectName("actionAdicionar")
        self.actionEditar = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/edit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionEditar.setIcon(icon1)
        self.actionEditar.setObjectName("actionEditar")
        self.actionExcluir = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/delete.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionExcluir.setIcon(icon2)
        self.actionExcluir.setObjectName("actionExcluir")
        self.actionAtualizar = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/reload.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionAtualizar.setIcon(icon3)
        self.actionAtualizar.setObjectName("actionAtualizar")
        self.menuArquivo.addAction(self.actionAdicionar)
        self.menuArquivo.addAction(self.actionEditar)
        self.menuArquivo.addAction(self.actionExcluir)
        self.menuArquivo.addAction(self.actionAtualizar)
        self.menubar.addAction(self.menuArquivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.listar()

        self.BtnAdicionar.clicked.connect(self.adicionar)
        self.BtnEditar.clicked.connect(self.atualizar)
        self.BtnRecarregar.clicked.connect(self.listar)
        self.BtnExcluir.clicked.connect(self.deletar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitulo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Cadastro de Produtos</span></p></body></html>"))
        self.labelNome.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Nome:</span></p></body></html>"))
        self.labelDescricao.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Descrição:</span></p></body></html>"))
        self.labelPreco.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Preço:</span></p></body></html>"))
        self.labelQuantidade.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Quantidade:</span></p></body></html>"))
        self.lineEditNome.setPlaceholderText(_translate("MainWindow", "Nome do Produto"))
        self.lineEditDescricao.setPlaceholderText(_translate("MainWindow", "Descrição do Produto"))
        self.lineEditPreco.setPlaceholderText(_translate("MainWindow", "Preço do Produto"))
        self.lineEditQuantidade.setPlaceholderText(_translate("MainWindow", "Quantidade do Produto"))
        self.BtnAdicionar.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Cadastrar Produto</span></p></body></html>"))
        self.BtnAdicionar.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.BtnEditar.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Editar Produto</span></p></body></html>"))
        self.BtnExcluir.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Excluir Produto</span></p></body></html>"))
        self.BtnRecarregar.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Recarregar Produtos</span></p></body></html>"))
        item = self.tableProdutp.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableProdutp.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableProdutp.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Descrição"))
        item = self.tableProdutp.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Preço"))
        item = self.tableProdutp.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Quantidade"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.actionAdicionar.setText(_translate("MainWindow", "Adicionar"))
        self.actionEditar.setText(_translate("MainWindow", "Editar"))
        self.actionExcluir.setText(_translate("MainWindow", "Excluir"))
        self.actionAtualizar.setText(_translate("MainWindow", "Atualizar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
