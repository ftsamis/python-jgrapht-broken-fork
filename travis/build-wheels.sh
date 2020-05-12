#!/bin/bash
set -e -x

cd /io

# Compile wheels
for PYBIN in /opt/python/cp3*/bin; do
    "${PYBIN}/python" setup.py bdist_wheel
done

# Install packages and test
for PYBIN in /opt/python/cp3*/bin/; do
    "${PYBIN}/pip" install python-jgrapht --no-index -f /io/dist
    (cd /io; "${PYBIN}/pytest")
done

