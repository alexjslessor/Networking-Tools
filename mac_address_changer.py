import subprocess, argparse, re
This is a python3 with argparse instead or optparse implementation.

def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--interface', dest='interface', help='Interface to Change MAC Addresss')
	parser.add_argument('-m', '--mac', dest='new mac', help='New MAC Addresss')
	options = parser.parse_args()
	if not options.interface:
		parser.error('[-] Select Interface, use --help for more info.')
	elif not options.new_mac:
		parser.error('[-] Select Interface, use --help for more info.')
	return options

def change_mac(interface, new_mac):
	print('[+] Changing MAC Address for ' + interface + 'to' + new_mac)
	subprocess.call(['ifconfig', interface, 'down'])
	subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
	subprocess.call(['ifconfig', interface, 'up'])

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(['ifconfig', interface])
	mac_addresss_search_result = re.search(r'\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}', ifconfig_result)
	if mac_addresss_search_result:
		return mac_addresss_search_result.group(0)
	else:
		print('[-] Could not read MAC address. ')

options = get_arguments()
current_mac = get_current_mac(options.interface)
print('Current MAC = ' + str(current_mac))
change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
	print('[+] MAC address was successfully changed to. --> ' + current_mac)
else:
	print('[-] MAC address not changed. ')



