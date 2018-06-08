pushd "$(dirname ${BASH_SOURCE[0]})"
python3 -m unittest config/tests.py
popd