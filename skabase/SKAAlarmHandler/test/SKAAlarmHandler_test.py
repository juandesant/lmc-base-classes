#########################################################################################
# -*- coding: utf-8 -*-
#
# This file is part of the SKAAlarmHandler project
#
#
#
#########################################################################################
"""Contain the tests for the SKAAlarmHandler."""

# Standard imports
import sys
import os

# Imports
import re
import pytest

# Path
path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.insert(0, os.path.abspath(path))

# PROTECTED REGION ID(SKAAlarmHandler.test_additional_imports) ENABLED START #
# PROTECTED REGION END #    //  SKAAlarmHandler.test_additional_imports
# Device test case
# PROTECTED REGION ID(SKAAlarmHandler.test_SKAAlarmHandler_decorators) ENABLED START #
@pytest.mark.usefixtures("tango_context", "initialize_device")
# PROTECTED REGION END #    //  SKAAlarmHandler.test_SKAAlarmHandler_decorators
class TestSKAAlarmHandler(object):
    """Test case for packet generation."""

    properties = {
        'SubAlarmHandlers': '',
        'AlarmConfigFile': '',
        'SkaLevel': '4',
        'GroupDefinitions': '',
        'CentralLoggingTarget': '',
        'ElementLoggingTarget': '',
        'StorageLoggingTarget': 'localhost',
        }

    @classmethod
    def mocking(cls):
        """Mock external libraries."""
        # Example : Mock numpy
        # cls.numpy = SKAAlarmHandler.numpy = MagicMock()
        # PROTECTED REGION ID(SKAAlarmHandler.test_mocking) ENABLED START #
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_mocking

    def test_properties(self, tango_context):
        """Test the device properties"""
        # Test the properties
        # PROTECTED REGION ID(SKAAlarmHandler.test_properties) ENABLED START #
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_properties


    # PROTECTED REGION ID(SKAAlarmHandler.test_GetAlarmRule_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKAAlarmHandler.test_GetAlarmRule_decorators
    def test_GetAlarmRule(self, tango_context):
        """Test for GetAlarmRule"""
        # PROTECTED REGION ID(SKAAlarmHandler.test_GetAlarmRule) ENABLED START #
        assert tango_context.device.GetAlarmRule("") == ""
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_GetAlarmRule

    # PROTECTED REGION ID(SKAAlarmHandler.test_GetAlarmData_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKAAlarmHandler.test_GetAlarmData_decorators
    def test_GetAlarmData(self, tango_context):
        """Test for GetAlarmData"""
        # PROTECTED REGION ID(SKAAlarmHandler.test_GetAlarmData) ENABLED START #
        assert tango_context.device.GetAlarmData("") == ""
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_GetAlarmData

    # PROTECTED REGION ID(SKAAlarmHandler.test_GetAlarmAdditionalInfo_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKAAlarmHandler.test_GetAlarmAdditionalInfo_decorators
    def test_GetAlarmAdditionalInfo(self, tango_context):
        """Test for GetAlarmAdditionalInfo"""
        # PROTECTED REGION ID(SKAAlarmHandler.test_GetAlarmAdditionalInfo) ENABLED START #
        assert tango_context.device.GetAlarmAdditionalInfo("") == ""
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_GetAlarmAdditionalInfo

    # PROTECTED REGION ID(SKAAlarmHandler.test_GetAlarmStats_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKAAlarmHandler.test_GetAlarmStats_decorators
    def test_GetAlarmStats(self, tango_context):
        """Test for GetAlarmStats"""
        # PROTECTED REGION ID(SKAAlarmHandler.test_GetAlarmStats) ENABLED START #
        assert tango_context.device.GetAlarmStats() == ""
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_GetAlarmStats

    # PROTECTED REGION ID(SKAAlarmHandler.test_GetAlertStats_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKAAlarmHandler.test_GetAlertStats_decorators
    def test_GetAlertStats(self, tango_context):
        """Test for GetAlertStats"""
        # PROTECTED REGION ID(SKAAlarmHandler.test_GetAlertStats) ENABLED START #
        assert tango_context.device.GetAlertStats() == ""
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_GetAlertStats

    # PROTECTED REGION ID(SKAAlarmHandler.test_GetVersionInfo_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKAAlarmHandler.test_GetVersionInfo_decorators
    def test_GetVersionInfo(self, tango_context):
        """Test for GetVersionInfo"""
        # PROTECTED REGION ID(SKAAlarmHandler.test_GetVersionInfo) ENABLED START #
        versionPattern = re.compile(
            r'SKAAlarmHandler, lmcbaseclasses, [0-9].[0-9].[0-9], '
            r'A set of generic base devices for SKA Telescope.')
        versionInfo = tango_context.device.GetVersionInfo()
        assert (re.match(versionPattern, versionInfo[0])) is not None
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_GetVersionInfo

    # PROTECTED REGION ID(SKAAlarmHandler.test_statsNrAlerts_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKAAlarmHandler.test_statsNrAlerts_decorators
    def test_statsNrAlerts(self, tango_context):
        """Test for statsNrAlerts"""
        # PROTECTED REGION ID(SKAAlarmHandler.test_statsNrAlerts) ENABLED START #
        assert tango_context.device.statsNrAlerts == 0
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_statsNrAlerts

    # PROTECTED REGION ID(SKAAlarmHandler.test_statsNrAlarms_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKAAlarmHandler.test_statsNrAlarms_decorators
    def test_statsNrAlarms(self, tango_context):
        """Test for statsNrAlarms"""
        # PROTECTED REGION ID(SKAAlarmHandler.test_statsNrAlarms) ENABLED START #
        assert tango_context.device.statsNrAlarms == 0
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_statsNrAlarms

    # PROTECTED REGION ID(SKAAlarmHandler.test_statsNrNewAlarms_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKAAlarmHandler.test_statsNrNewAlarms_decorators
    def test_statsNrNewAlarms(self, tango_context):
        """Test for statsNrNewAlarms"""
        # PROTECTED REGION ID(SKAAlarmHandler.test_statsNrNewAlarms) ENABLED START #
        assert tango_context.device.statsNrNewAlarms == 0
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_statsNrNewAlarms

    # PROTECTED REGION ID(SKAAlarmHandler.test_statsNrUnackAlarms_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKAAlarmHandler.test_statsNrUnackAlarms_decorators
    def test_statsNrUnackAlarms(self, tango_context):
        """Test for statsNrUnackAlarms"""
        # PROTECTED REGION ID(SKAAlarmHandler.test_statsNrUnackAlarms) ENABLED START #
        assert tango_context.device.statsNrUnackAlarms == 0.0
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_statsNrUnackAlarms

    # PROTECTED REGION ID(SKAAlarmHandler.test_statsNrRtnAlarms_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKAAlarmHandler.test_statsNrRtnAlarms_decorators
    def test_statsNrRtnAlarms(self, tango_context):
        """Test for statsNrRtnAlarms"""
        # PROTECTED REGION ID(SKAAlarmHandler.test_statsNrRtnAlarms) ENABLED START #
        assert tango_context.device.statsNrRtnAlarms == 0.0
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_statsNrRtnAlarms

    # PROTECTED REGION ID(SKAAlarmHandler.test_buildState_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKAAlarmHandler.test_buildState_decorators
    def test_buildState(self, tango_context):
        """Test for buildState"""
        # PROTECTED REGION ID(SKAAlarmHandler.test_buildState) ENABLED START #
        buildPattern = re.compile(
            r'lmcbaseclasses, [0-9].[0-9].[0-9], '
            r'A set of generic base devices for SKA Telescope')
        assert (re.match(buildPattern, tango_context.device.buildState)) is not None
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_buildState

    # PROTECTED REGION ID(SKAAlarmHandler.test_versionId_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKAAlarmHandler.test_versionId_decorators
    def test_versionId(self, tango_context):
        """Test for versionId"""
        # PROTECTED REGION ID(SKAAlarmHandler.test_versionId) ENABLED START #
        versionIdPattern = re.compile(r'[0-9].[0-9].[0-9]')
        assert (re.match(versionIdPattern, tango_context.device.versionId)) is not None
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_versionId

    # PROTECTED REGION ID(SKAAlarmHandler.test_activeAlerts_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKAAlarmHandler.test_activeAlerts_decorators
    def test_activeAlerts(self, tango_context):
        """Test for activeAlerts"""
        # PROTECTED REGION ID(SKAAlarmHandler.test_activeAlerts) ENABLED START #
        assert tango_context.device.activeAlerts == ('',)
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_activeAlerts

    # PROTECTED REGION ID(SKAAlarmHandler.test_activeAlarms_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKAAlarmHandler.test_activeAlarms_decorators
    def test_activeAlarms(self, tango_context):
        """Test for activeAlarms"""
        # PROTECTED REGION ID(SKAAlarmHandler.test_activeAlarms) ENABLED START #
        assert tango_context.device.activeAlarms == ('',)
        # PROTECTED REGION END #    //  SKAAlarmHandler.test_activeAlarms
