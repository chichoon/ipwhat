from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal, QObject, QThread, Qt
from PyQt5.QtWidgets import *
import sys
import os
from ipwhat_func import check_ip, get_ip, get_subnet, calc_network_addr
from ipwhat_func import calc_broadcast_addr, calc_host_addr, calc_host_num
from ipwhat_func import calc_host_subnet, calc_cidr

ip_addr = '0.0.0.0'
subnet_mask = '0.0.0.0'
network_addr = '0.0.0.0'
broadcast_addr = '0.0.0.0'
host_addr_front = '0.0.0.0'
host_addr_back = '0.0.0.0'
num_of_host = '0'
if_private = 0
if_subnet = 0
if_private_str = 'Not a private ip'

class App(QMainWindow):
	tray_icon = None
	def __init__(self):
		super().__init__()
		self.widget = QWidget()
		self.ledt = QLineEdit()
		self.initUI()
		self.initActions()
		self.setFixedSize(400, 400)

	def __exit__(self, exc_type, exc_val, exc_tb):
		pass

	def initUI(self):
		global newfile

		self.layout1 = QVBoxLayout()
		self.layout2 = QVBoxLayout()
		self.layout3 = QVBoxLayout()
		self.layout4 = QHBoxLayout()
		self.main_layout = QVBoxLayout()

		self.ip_edit = QLineEdit(self)
		self.myname = QLabel('made by jiychoi\n(jiychoi@student.42seoul.kr)')
		self.ip_show = QLabel(''.join([
			'\n',
			'IP Address : ', ip_addr, '\n',
			'Subnet Mask : ', subnet_mask, '\n',
			'Network Address : ', network_addr, '\n',
			'Broadcast Address : ', broadcast_addr, '\n',
			'Host address range : ', host_addr_front, '\n',
			'                           ~', host_addr_back, '\n',
			'Number of hosts : ', num_of_host, '\n',
			'\n*** ', if_private_str, ' ***\n'])
		)
		self.calcbtn = QPushButton('Calculate!')
		self.quitbtn = QPushButton('Quit')
		self.layout1.addWidget(self.ip_edit)
		self.layout2.addWidget(self.myname)
		self.layout3.addWidget(self.ip_show)
		self.layout4.addWidget(self.calcbtn)
		self.layout4.addWidget(self.quitbtn)
		self.main_layout.addLayout(self.layout1)
		self.main_layout.addLayout(self.layout2)
		self.main_layout.addLayout(self.layout3)
		self.main_layout.addLayout(self.layout4)
		self.widget.setLayout(self.main_layout)
		self.setCentralWidget(self.widget)

		self.setWindowTitle('IPWhat')
		self.setGeometry(0, 0, 200, 600)
		self.setWindowIcon(QIcon('icon.png'))
		self.show()

	def initActions(self):
		self.calcbtn.clicked.connect(self.toggleCalc)
		self.quitbtn.clicked.connect(self.toggleQuit)
		self.ip_edit.returnPressed.connect(self.toggleCalc)

	def toggleCalc(self):
		input_str = self.ip_edit.text()
		if (check_ip(input_str) == 1):
			ip_cidr = get_ip(input_str)
			subnet_mask = get_subnet(ip_cidr[1])
			network_addr = calc_network_addr(ip_cidr[0], subnet_mask)
			broadcast_addr = calc_broadcast_addr(network_addr, subnet_mask)
			host_addr = calc_host_addr(network_addr, broadcast_addr)
			host_addr_front = host_addr[0]
			host_addr_back = host_addr[1]
			num_of_host = calc_host_num(network_addr, broadcast_addr)
			self.ip_show.setText(''.join([
				'\n',
				'IP Address : ', ip_cidr[0], '\n',
				'Subnet Mask : ', subnet_mask, '\n',
				'Network Address : ', network_addr, '\n',
				'Broadcast Address : ', broadcast_addr, '\n',
				'Host address range : ', host_addr_front, '\n',
				'                           ~', host_addr_back, '\n',
				'Number of hosts : ', num_of_host, '\n'])
			)
		elif (check_ip(input_str) == 2):
			ip_cidr = get_ip(input_str)
			num_of_host = calc_host_subnet(ip_cidr[0])
			cidr = calc_cidr(ip_cidr[0])
			self.ip_show.setText(''.join([
				'Number of hosts : ', num_of_host, '\n',
				'CIDR : ', cidr, '\n'
			]))
		elif (check_ip(input_str) == 3):
			ip_cidr = get_ip(input_str)
			self.ip_show.setText(''.join([
				'\n',
				'IP Address : ', ip_cidr[0], '\n',
				'Private IP in Class A\n',])
			)
		elif (check_ip(input_str) == 4):
			ip_cidr = get_ip(input_str)
			self.ip_show.setText(''.join([
				'\n',
				'IP Address : ', ip_cidr[0], '\n',
				'Private IP in Class B\n',])
			)
		elif (check_ip(input_str) == 5):
			ip_cidr = get_ip(input_str)
			self.ip_show.setText(''.join([
				'\n',
				'IP Address : ', ip_cidr[0], '\n',
				'Private IP in Class C\n',])
			)
		else :
			self.ip_show.setText('\nNot a valid IP!\n\n')

	def toggleQuit(self):
		sys.exit()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()
	window.show()
	sys.exit(app.exec_())
