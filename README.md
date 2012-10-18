# ForEachDevice #
forEach device is just a helper pyhton/shellScript to execute adb commands on each connected devices automatically.
So, you should use adb commands combined with forEachDevice.

## Requirements
* adb (Android Debug Bridge) should be in system path
* You should have Python installed
* Operational System: Linux

## Example of use ##
To install and replace if already installed  a apk on each connected device

	forEachDevice install -r path_to_apk_file



