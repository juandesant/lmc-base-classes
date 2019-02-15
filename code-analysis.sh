#!/usr/bin/env bash
echo "STATIC CODE ANALYSIS"
echo "===================="
echo

echo "MODULE ANALYSIS"
echo "---------------"
pylint --rcfile=rcfile skabase/SKABaseDevice

echo "TESTS ANALYSIS"
echo "--------------"
pylint test
