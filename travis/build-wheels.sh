#!/bin/bash
set -e -x

# Compile wheels
for PYBIN in /opt/python/cp3*/bin; do
    "${PYBIN}/pip" install -r /io/requirements.txt
    "${PYBIN}/pip" wheel /io/ --no-deps -w wheelhouse/
done

# Install packages and test
for PYBIN in /opt/python/cp3*/bin/; do
    "${PYBIN}/pip" install python-jgrapht --no-index -f /io/wheelhouse
    (cd "$HOME"; "${PYBIN}/pytest")
done

