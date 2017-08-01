#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        SKABaseDevice.py
#
#  Project :     SKABASE
#
# This file is part of Tango device class.
# 
# Tango is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tango is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tango.  If not, see <http://www.gnu.org/licenses/>.
# 
#
#  $Author :      cam$
#
#  $Revision :    $
#
#  $Date :        $
#
#  $HeadUrl :     $
# ============================================================================
#            This file is generated by POGO
#     (Program Obviously used to Generate tango Object)
# ############################################################################

__all__ = ["SKABaseDevice", "SKABaseDeviceClass", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(SKABaseDevice.additionnal_import) ENABLED START -----#

#----- PROTECTED REGION END -----#	//	SKABaseDevice.additionnal_import

# Device States Description
# ON : 
# OFF : 
# FAULT : 
# INIT : 
# ALARM : 
# UNKNOWN : 
# STANDBY : Equates to LOW-POWER mode.\nThis is the initial transition from INIT \nif the device supports a low-power mode.


class SKABaseDevice (PyTango.Device_4Impl):
    """A generic base device for SKA."""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(SKABaseDevice.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	SKABaseDevice.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        SKABaseDevice.init_device(self)
        #----- PROTECTED REGION ID(SKABaseDevice.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(SKABaseDevice.delete_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        self.attr_buildState_read = ""
        self.attr_versionId_read = ""
        self.attr_centralLoggingLevel_read = 0
        self.attr_elementLoggingLevel_read = 0
        self.attr_storageLoggingLevel_read = 0
        self.attr_healthState_read = ''
        self.attr_adminMode_read = ''
        self.attr_controlMode_read = ''
        self.attr_simulationMode_read = False
        self.attr_testMode_read = ""
        #----- PROTECTED REGION ID(SKABaseDevice.init_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(SKABaseDevice.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.always_executed_hook

    # -------------------------------------------------------------------------
    #    SKABaseDevice read/write attribute methods
    # -------------------------------------------------------------------------
    
    def read_buildState(self, attr):
        self.debug_stream("In read_buildState()")
        #----- PROTECTED REGION ID(SKABaseDevice.buildState_read) ENABLED START -----#
        attr.set_value(self.attr_buildState_read)
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.buildState_read
        
    def read_versionId(self, attr):
        self.debug_stream("In read_versionId()")
        #----- PROTECTED REGION ID(SKABaseDevice.versionId_read) ENABLED START -----#
        attr.set_value(self.attr_versionId_read)
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.versionId_read
        
    def read_centralLoggingLevel(self, attr):
        self.debug_stream("In read_centralLoggingLevel()")
        #----- PROTECTED REGION ID(SKABaseDevice.centralLoggingLevel_read) ENABLED START -----#
        attr.set_value(self.attr_centralLoggingLevel_read)
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.centralLoggingLevel_read
        
    def read_elementLoggingLevel(self, attr):
        self.debug_stream("In read_elementLoggingLevel()")
        #----- PROTECTED REGION ID(SKABaseDevice.elementLoggingLevel_read) ENABLED START -----#
        attr.set_value(self.attr_elementLoggingLevel_read)
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.elementLoggingLevel_read
        
    def read_storageLoggingLevel(self, attr):
        self.debug_stream("In read_storageLoggingLevel()")
        #----- PROTECTED REGION ID(SKABaseDevice.storageLoggingLevel_read) ENABLED START -----#
        attr.set_value(self.attr_storageLoggingLevel_read)
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.storageLoggingLevel_read
        
    def write_storageLoggingLevel(self, attr):
        self.debug_stream("In write_storageLoggingLevel()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(SKABaseDevice.storageLoggingLevel_write) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.storageLoggingLevel_write
        
    def read_healthState(self, attr):
        self.debug_stream("In read_healthState()")
        #----- PROTECTED REGION ID(SKABaseDevice.healthState_read) ENABLED START -----#
        attr.set_value(self.attr_healthState_read)
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.healthState_read
        
    def read_adminMode(self, attr):
        self.debug_stream("In read_adminMode()")
        #----- PROTECTED REGION ID(SKABaseDevice.adminMode_read) ENABLED START -----#
        attr.set_value(self.attr_adminMode_read)
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.adminMode_read
        
    def write_adminMode(self, attr):
        self.debug_stream("In write_adminMode()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(SKABaseDevice.adminMode_write) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.adminMode_write
        
    def read_controlMode(self, attr):
        self.debug_stream("In read_controlMode()")
        #----- PROTECTED REGION ID(SKABaseDevice.controlMode_read) ENABLED START -----#
        attr.set_value(self.attr_controlMode_read)
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.controlMode_read
        
    def write_controlMode(self, attr):
        self.debug_stream("In write_controlMode()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(SKABaseDevice.controlMode_write) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.controlMode_write
        
    def read_simulationMode(self, attr):
        self.debug_stream("In read_simulationMode()")
        #----- PROTECTED REGION ID(SKABaseDevice.simulationMode_read) ENABLED START -----#
        attr.set_value(self.attr_simulationMode_read)
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.simulationMode_read
        
    def write_simulationMode(self, attr):
        self.debug_stream("In write_simulationMode()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(SKABaseDevice.simulationMode_write) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.simulationMode_write
        
    def read_testMode(self, attr):
        self.debug_stream("In read_testMode()")
        #----- PROTECTED REGION ID(SKABaseDevice.testMode_read) ENABLED START -----#
        attr.set_value(self.attr_testMode_read)
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.testMode_read
        
    def write_testMode(self, attr):
        self.debug_stream("In write_testMode()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(SKABaseDevice.testMode_write) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.testMode_write
        
    
    
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(SKABaseDevice.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.read_attr_hardware


    # -------------------------------------------------------------------------
    #    SKABaseDevice command methods
    # -------------------------------------------------------------------------
    

    #----- PROTECTED REGION ID(SKABaseDevice.programmer_methods) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	SKABaseDevice.programmer_methods

class SKABaseDeviceClass(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(SKABaseDevice.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	SKABaseDevice.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        'SkaLevel':
            [PyTango.DevShort, 
            "Indication of importance of the device in the SKA hierarchy \nto support drill-down navigation: 1..6, with 1 highest.\nDefault is 4, making provision for \nEltMaster, EltAlarms, EltTelState = 1\nSubEltMaster = 2\nSubarray, Capability = 2/3\nOthers = 4 (or 5 or 6)",
            [4]],
        'ManagedDevices':
            [PyTango.DevVarStringArray, 
            "List of devices managed by a master. \nA proxy client will be opened for each of the managed devices.\nA group may be instantiated for the Managed Devices.\n(NOTE: Possible that SKAGroup may be used for this in future instead of \nputting the ManagedDevices here.)",
            [] ],
        'CentralLoggingTarget':
            [PyTango.DevString, 
            "Pre-configured logging target CentralLogger DS",
            [] ],
        'ElementLoggingTarget':
            [PyTango.DevString, 
            "Pre-configured logging target ElementLogger DS",
            [] ],
        'StorageLoggingTarget':
            [PyTango.DevString, 
            "Pre-configured logging target for syslog",
            ["localhost"] ],
        'CentralLoggingLevelDefault':
            [PyTango.DevLong, 
            "Default logging level to Central logging target\n(0=OFF, 1=FATAL, 2=ERROR, 3=WARNING, 4=INFO, 5=DEBUG)\n\nDefault: 2",
            [] ],
        'ElementLoggingLevelDefault':
            [PyTango.DevLong, 
            "Default logging level to Element logging target\n(0=OFF, 1=FATAL, 2=ERROR, 3=WARNING, 4=INFO, 5=DEBUG)\n\nDefault: 3",
            [] ],
        'StorageLoggingLevelStorage':
            [PyTango.DevLong, 
            "Default logging level to Syslog logging target\n(0=OFF, 1=FATAL, 2=ERROR, 3=WARNING, 4=INFO, 5=DEBUG)\n\nDefault: 4",
            [] ],
        }


    #    Command definitions
    cmd_list = {
        }


    #    Attribute definitions
    attr_list = {
        'buildState':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'description': "Build state of this device",
                'Polling period': "60000",
            } ],
        'versionId':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'description': "Build state of this device",
                'Polling period': "60000",
            } ],
        'centralLoggingLevel':
            [[PyTango.DevLong,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'description': "Current logging level to Central logging target for this device - \ninitialises to CentralLoggingLevelDefault on startup",
            } ],
        'elementLoggingLevel':
            [[PyTango.DevLong,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'description': "Current logging level to Element logging target for this device - \ninitialises to ElementLoggingLevelDefault on startup",
            } ],
        'storageLoggingLevel':
            [[PyTango.DevLong,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "Current logging level to Syslog for this device - \ninitialises from  StorageLoggingLevelDefault on first execution of device.\nNeeds to be READ_WRITE To make it memorized - but writing this attribute should \ndo the same as command SetStorageLoggingLevel to ensure the targets and adjustments\nare made correctly",
                'Memorized':"true_without_hard_applied"
            } ],
        'healthState':
            [[,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'description': "The health state reported for this device. It interprets the current device condition \nand condition of all managed devices to set this. Most possibly an aggregate attribute.",
            } ],
        'adminMode':
            [[,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "The admin mode reported for this device. It may interpret the current device condition \nand condition of all managed devices to set this. Most possibly an aggregate attribute.",
                'Memorized':"true_without_hard_applied"
            } ],
        'controlMode':
            [[,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "The control mode of the device. REMOTE, LOCAL\nTANGO Device accepts only from a ‘local’ client and ignores commands and queries received from TM\nor any other ‘remote’ clients. The Local clients has to release LOCAL control before REMOTE clients\ncan take control again.",
                'Memorized':"true_without_hard_applied"
            } ],
        'simulationMode':
            [[PyTango.DevBoolean,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "Reports the simulation mode of the device. Some devices may implement both modes,\nwhile others will have simulators that set simulationMode to True while the real\ndevices always set simulationMode to False.",
                'Memorized':"true_without_hard_applied"
            } ],
        'testMode':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "The test mode of the device. \nEither no test mode (empty string) or an indication of the test mode.",
                'Memorized':"true_without_hard_applied"
            } ],
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(SKABaseDeviceClass, SKABaseDevice, 'SKABaseDevice')
        #----- PROTECTED REGION ID(SKABaseDevice.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	SKABaseDevice.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
