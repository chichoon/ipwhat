import os
import math

def calc_cidr(subnet):
	sn_large = 4294967295
	lst_subnet = list(map(int, subnet.split('.')))
	subnet1 = lst_subnet[0] * 256 * 256 * 256 + lst_subnet[1] * 256 * 256 + lst_subnet[2] * 256 + lst_subnet[3]
	str_host = str(bin(subnet1))
	return (str(str_host.count('1')))

def calc_host_subnet(subnet):
	sn_large = 4294967295
	lst_subnet = list(map(int, subnet.split('.')))
	subnet1 = lst_subnet[0] * 256 * 256 * 256 + lst_subnet[1] * 256 * 256 + lst_subnet[2] * 256 + lst_subnet[3]
	str_host = str(bin(sn_large ^ subnet1))
	return str(int(math.pow(2, str_host.count('1')) - 2))

def calc_host_num(network, broadcast):
	lst_network = list(map(int, network.split('.')))
	lst_broadcast = list(map(int, broadcast.split('.')))
	network1 = lst_network[0] * 256 * 256 * 256 + lst_network[1] * 256 * 256 + lst_network[2] * 256 + lst_network[3]
	broadcast1 = lst_broadcast[0] * 256 * 256 * 256 + lst_broadcast[1] * 256 * 256 + lst_broadcast[2] * 256 + lst_broadcast[3]
	return str(broadcast1 - network1 - 1)

def calc_host_addr(network, broadcast):
	lst_network = list(map(int, network.split('.')))
	lst_broadcast = list(map(int, broadcast.split('.')))
	host_addr_front = [
		lst_network[0],
		lst_network[1],
		lst_network[2],
		lst_network[3] + 1
	]
	host_addr_back = [
		lst_broadcast[0],
		lst_broadcast[1],
		lst_broadcast[2],
		lst_broadcast[3] - 1
	]
	return ['.'.join(list(map(str, host_addr_front))), '.'.join(list(map(str, host_addr_back)))]

def calc_broadcast_addr(network, subnet):
	lst_network = list(map(int, network.split('.')))
	lst_subnet = list(map(int, subnet.split('.')))
	lst_subnet[0] = lst_subnet[0] ^ 255
	lst_subnet[1] = lst_subnet[1] ^ 255
	lst_subnet[2] = lst_subnet[2] ^ 255
	lst_subnet[3] = lst_subnet[3] ^ 255
	lst_broadcast = [
		lst_network[0] ^ lst_subnet[0],
		lst_network[1] ^ lst_subnet[1],
		lst_network[2] ^ lst_subnet[2],
		lst_network[3] ^ lst_subnet[3]
	]
	return '.'.join(list(map(str, lst_broadcast)))


def calc_network_addr(ip, subnet):
	lst_ip = list(map(int, ip.split('.')))
	lst_subnet = list(map(int, subnet.split('.')))
	lst_network = [
		lst_ip[0] & lst_subnet[0],
		lst_ip[1] & lst_subnet[1],
		lst_ip[2] & lst_subnet[2],
		lst_ip[3] & lst_subnet[3]
	]
	return '.'.join(list(map(str, lst_network)))

def get_subnet(cidr):
	cidr_code = int(cidr)
	sn_large = 4294967295
	subnet = sn_large << (32 - cidr_code)
	lst_subnet = [
		subnet >> 24 & 255,
		subnet >> 16 & 255,
		subnet >> 8 & 255,
		subnet & 255
	]
	return '.'.join(list(map(str, lst_subnet)))

def get_ip(s):
	c = '/'
	if c in s:
		lst_str = s.split('/')
		ip = lst_str[0]
		cidr_code = lst_str[1]
	else:
		ip = s
		cidr_code = '0'
	return [ip, cidr_code]

def check_ip(s):
	c = '/'
	if c in s:
		lst_s_1 = s.split('/')
		lst_s = lst_s_1[0].split('.')
		cidr = int(lst_s_1[1])
		if (len(lst_s) != 4 or cidr > 32 or cidr < 0):
			return (0)
		else :
			return (1)
	else:
		lst_s = s.split('.')
		lst_s_int = list(map(int, lst_s))
		if (lst_s_int[0] == 10):
			return (3)
		elif (lst_s_int[0] == 172 and lst_s_int[1] >= 16 and lst_s_int[1] < 32):
			return (4)
		elif (lst_s_int[0] == 192 and lst_s_int[1] == 168):
			return (5)
		if (len(lst_s) != 4):
			return (0)
		else :
			return (2)
