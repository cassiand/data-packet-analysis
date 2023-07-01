# Cassian
# 5/19/22
# week 1 assignment
# functions:
# Updates: 5/29/22, added new obj belonging to NetworkCheck class and called functions. 5/30/22, added to the loop for the dictionary. 6/5/22 added commands to get attributes, imported new class from network check, added loop through packets
#  6/19/22, added new obj belonging to new AddedNetworkCheck class and called functions. 6/26/22 added log file and try/excepts, etc. for errors. 7/1/22 added calls to super functions, added recursive method, and anonymous functions
import numpy as np
import pandas as pd
from numpy import ndarray
from scapy.layers.inet import TCP, UDP
from scapy.layers.l2 import Ether

import CMIT235_Package.CMIT235_Tools as cm
# imported num py and package
from CMIT235_Package.NetworkCheck import NetworkCheck
from CMIT235_Package.NetworkCheck import NetworkData
from scapy.all import *
from scapy.config import conf
import CMIT235_Package.NewNetworkCheck
conf.use_pcap = True
from CMIT235_Package.NewNetworkCheck import newNetworkCheck
from CMIT235_Package.AddedNetworkCheck import AddedNetCheck
import logging
# import logging

logging.basicConfig(filename='CMIT235_MyTestProgram.log', level=logging.DEBUG)
# create log file
logging.info('This is the beginning of the program')
# info statement

CombinedList = cm.mySubList1 + cm.mySubList2 + cm.mySubList3
# concatenating sub lists
if not type(cm.mySubList1) is list:
    print('All sub lists must be type: list')
    logging.error('MyTest program error beginning at line 31. Not all sub lists are type: list')
if not type(cm.mySubList2) is list:
    print('All sub lists must be type: list')
    logging.error('MyTest program error beginning at line 31. Not all sub lists are type: list')
if not type(cm.mySubList3) is list:
    print('All sub lists must be type: list')
    logging.error('MyTest program error beginning at line 31. Not all sub lists are type: list')
else:
    print('The lists are', CombinedList)

# display list of combined lists

try:
    MyNpArray = np.array(CombinedList)
except ValueError:
    print('Value is not expected value')
    logging.error('ValueError raised at line 42. Passed value is not expected value')
    # log error
    sys.exit(1)
except TypeError:
    print('Object is an unsupported object type')
    logging.error('TypeError raised at line 42. Object is not a supported type')
    # log error
    sys.exit(1)

try:
    print('The minimum value is', np.min(MyNpArray))
    # output min value
except np.min(MyNpArray) > 99:
    # unless the value is 100+
    raise ValueError('The minimum cannot be over 100')

try:
    print('The maximum value is', np.max(MyNpArray))
    # output max value
except np.max(MyNpArray) < 0:
    # unless the value is less than 0
    raise ValueError('The maximum cannot be less than zero')


print('The unique list is', np.unique(MyNpArray))

if not type(np.unique(MyNpArray)) is ndarray:
    logging.error('The unique values are not type ndarray, error at line 73')
    sys.exit(2)
print()

for i in (cm.mySubList1, cm.mySubList2, cm.mySubList3):
    # iterate through the sub lists
    arr1 = np.array(i)
    if not type(arr1) is ndarray:
        logging.error('Error at line 78, passed sub lists are not all type ndarray')
        sys.exit(3)
    # assign arr1, convert to array
    print('This is a sublist:\n', i)

    arr1dim = np.ndim(i)
    # assign arr1dim, get shape of sub list
    print('The dimensions are:', arr1dim)

    arr1shape = np.shape(i)
    # assign arr1shape, get shape of sub list
    print('The shape is:', arr1shape)

    arr1Split = arr1[0:2:1]
    # split the array in half
    print('The split sub list is\n', arr1Split)

    lastSublist = arr1Split[-1]
    # get last element of second slice
    print('The last number is', lastSublist[-1])
    print('The first column is', arr1Split[:, 0])
    # get first column of arr
    print('The second row is', arr1Split[1, :])
    # get second row of arr
    print()

# week 2 start
logging.info('NetworkCheck area beginning a line 110')
# log info statement
myObj = NetworkCheck()
# create object
myObj_ins = isinstance(myObj, NetworkCheck)

try:
    myObj_ins is True
except myObj_ins is False:
    logging.error('Line 113, object is not instance of NetworkCheck()')
    sys.exit(4)


myNpArray = myObj.convertlist2nparray(CombinedList)
# call function to CombinedList
print('The array is:\n', myNpArray)

array_max = myObj.getMax(myNpArray)
# get max value of array
try:
    print('\nThe maximum is', array_max)
except array_max < 0:
    raise ValueError('The maximum of the array cannot be less than zero')

array_min = myObj.getMin(myNpArray)
# get min value of array
try:
    print('The minimum is', array_min)
except array_min > 100:
    raise ValueError('The minimum of the array cannot be more than 100')

unique_vals = myObj.getUniqueValues(CombinedList)
# get unique vals of combined list
if not type(unique_vals) is ndarray:
    print('Error: the unique values are not of type ndarray')
    sys.exit(5)

print('The unique values are:\n', unique_vals)


theDictionary = myObj.getDescriptiveInfo(cm.mySubList1, cm.mySubList2, cm.mySubList3)
# call dictionary function using each sub list
if not type(theDictionary) is dict:
    raise TypeError('The dictionary must be type dictionary')
# raise error
count = 1
# loop through dictionary
for i in range(3):
    # limit range to 3 for lists
    strCount = str(count)
    # assign strCount to current count #
    print("\nArray dimension:", theDictionary["dimensions"+strCount])
    # get value in 'dimensions' key according to count #
    print("Array shape:", theDictionary["shape"+strCount])
    # get value in 'shape' key according to count #
    print("Last item:", theDictionary["last item"+strCount])
    # get value in ''last item' key according to count #
    print("Column zero:", theDictionary["column zero"+strCount])
    # get value in 'column zero' key according to count #
    print("Second row:", theDictionary["second row"+strCount])
    # get value in 'second row' key according to count #
    count += 1
    # increment count to avoid repetition

# week 3 assignment start

NetData = NetworkData()
# create object

try:
    print(NetData.message1())
    # try to get priv attribute
except:
    print('Unable to get message 1')

try:
    print(NetData.getMessage1())
    # use getter command within class
except:
    print('Unable to get message 1')

try:
    print(NetData.message2)
except:
    print('Unable to get message 2')

try:
    print(NetData.getMessage2())
    # use getter command within class
except:
    print('Unable to get message 2')


print(NetData.message3)
print('\n')
print(f"{NetData.getMessage1():>25}{NetData.getMessage2():>25}{NetData.message3:>25}")
# print on one line and right justify by 25

try:
    packets = NetData.packets
# create variable for rdpcap(cm.pcap)
except IOError:
    raise Scapy_Exception('An error has occurred while opening the pcap file')
    sys.exit(6)

port_count = 1
# set to 1 to increment
# print errors if numbers are not integers
if not type(port_count) is int:
    print('Error: the port count is not an integer')
    sys.exit(7)
mac_count = 1
if not type(mac_count) is int:
    print('Error: the MAC count is not an integer')
    sys.exit(7)

for packet in packets:

    if packet.haslayer(UDP) or packet.haslayer(TCP):
        # if packet is udp or tcp
        if packet.dport == cm.port:
            print('Port:', NetData.get_port_ct(NetData.pcap, NetData.port))
            # execute get port ct function
            print('Port count:', port_count)
            port_count = port_count + 1
            # increment port count

    if packet[Ether].src == cm.spoofed_mac:
        print(NetData.get_sm_count(NetData.pcap, NetData.spoofed_mac))
        # execute sm count function
        print('Spoofed MAC count:', mac_count)
        mac_count = mac_count + 1
        # increment mac count

# start of week 4

newNetCheck = newNetworkCheck()
myObj = NetworkCheck()
# user overloaded checkCounts for protocol counts and print
try:
    count = myObj.checkCounts(cm.csv_data, cm.feature3)
except RuntimeError:
    print('There was an error executing the protocol count function')
    sys.exit(8)
print('---------------Protocol count is---------------')
print(count)


d = myObj.checkCounts(cm.csv_data, cm.feature1, cm.feature2, cm.feature3)
if not type(d) is dict:
    # check that dict is type dict
    raise TypeError('The dictionary is not of type dictionary')
    # if not then raise error

print('---------------Source IP count is---------------')
print(d[cm.feature1])
print('---------------Destination IP count is---------------')
print(d[cm.feature2])

# use overloaded checkCounts for all features and print the highest one
try:
    result = myObj.checkCounts(cm.csv_data, cm.feature1, cm.feature2, cm.feature3, cm.feature4, cm.feature5)
except RuntimeError:
    print('There was an error checking the count of all five features')
    sys.exit(9)

print('---------------Packets at issue is---------------')
print(result)


y = newNetworkCheck()
y_ins = isinstance(y, newNetworkCheck)
try:
    y_ins is True
except y_ins is False:
    logging.debug('The object y assigned to newNetworkCheck() is not an instance of newNetworkCheck(), identified using isinstance() with parameters y, newNetworkCheck. The expected outcome was True.')
    sys.exit(10)

# Parse the three lists for descriptive information
print("-----------------------Override Lists Descriptions-------------------------------")
myDict = y.getDescriptiveInfo(cm.mySubList1, cm.mySubList2, cm.mySubList3)
count = 1
# Loop through the dictionary
for i in range(3):
    strCount = str(count)
    print("-----------------------Lists Descriptions " + strCount + "-------------------------------")
    print("Array dimension", myDict["Dimension"+strCount])
    print("Array shape", myDict["Shape"+strCount])
    print("Mean of array", myDict["Mean"+strCount])
    print("Median of array", myDict["Median"+strCount])
    print("Standard deviation of array", myDict["Standard Deviation"+strCount])
    count += 1


# start of week 5
print('\nThe array is\n')
print(y.convertlist2nparray(CombinedList))

new_min = y.getMin(arr1)
print('\nThe minimum is', new_min)

new_max = y.getMax(arr1)
print('The maximum is', new_max)
print('The unique values are:', y.getUniqueValues(CombinedList))

addedNetCheck = AddedNetCheck()
# create object for addedNetCheck in new file
addedNetCheck_ins = isinstance(addedNetCheck, AddedNetCheck)
try:
    addedNetCheck_ins is True
except addedNetCheck_ins is False:
    logging.info('The object addedNetCheck assigned to AddedNetCheck() is not an instance of AddedNetCheck(). The expected outcome was True.')
    sys.exit(11)

new_mac_count = 0
for packet in packets:
    if packet[Ether].src == cm.spoofed_mac:
        new_mac_count = new_mac_count + 1
print('---------------Spoofed MAC count is---------------')
print(new_mac_count)
# call spoofed mac count method

print('---------------Ping flood count is---------------')
ping_count = addedNetCheck.getPingCount(packets)
print(ping_count)

print('---------------Protocol count is---------------')
print(d[cm.feature3])
# print myobj.checkcounts with parameter feature 3


# start of week 7

print("\nCalling NetworkCheck's getMin from NewNetworkCheck, the minimum is: ")
y.callSuper(cm.mySubList2)
# call super function

try:
    lambda x: issubclass(newNetworkCheck, NetworkCheck) is True
    print('It is a subclass of NetworkCheck.')
    # then print it IS a subclass
except lambda x: issubclass(newNetworkCheck, NetworkCheck) is False:
    print('It is NOT a subclass of NetworkCheck')
    logging.error('Line 350, newNetworkCheck is not a subclass of NetworkCheck')
    # log error
    sys.exit(12)
    # exit

print("\nCalling NetworkCheck's getMax method from AddedNetworkCheck, the maximum is: ")
addedNetCheck.callGrandparent(cm.mySubList3)
# call super function


try:
    lambda x: issubclass(AddedNetCheck, NetworkCheck) is True
    print('It is a subclass of NetworkCheck.')
except lambda x: issubclass(AddedNetCheck, NetworkCheck) is False:
    print('It is NOT a subclass of NetworkCheck')
    logging.error('Line 361, AddedNetCheck is not a subclass of NetworkCheck')
    # log error if not
    sys.exit(13)
    # exit


def repeat(n):
    if len(n) == 1:
        # if one item then print that item
        print(n)
    else:
        middle_index = len(n)//2
        # divide length into 2 to get halves
        first_half = n[:middle_index]
        second_half = n[middle_index:]
        return repeat(first_half), repeat(second_half)


repeat(cm.mySubList1[0])
# call repeat method to first sub list


