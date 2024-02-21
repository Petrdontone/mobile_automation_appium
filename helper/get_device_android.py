from ppadb.client import Client as AdbClient


def get_connected_device_capabilities():
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()

    for device in devices:
        device_state = device.get_state()
        if device_state == 'device':
            device_properties = device.get_properties()
            emulator_name = device_properties.get('ro.kernel.qemu.avd_name', 'Unknown').replace('_', ' ')
            update_capabilities = {
                'deviceName': emulator_name,
                'platformVersion': device_properties.get('ro.build.version.release', 'Unknown')
            }
            return update_capabilities
    return None