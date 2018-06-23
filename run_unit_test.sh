pushd "$(dirname ${BASH_SOURCE[0]})"
python3 -m unittest settings.tests.KivySettingsTest
popd