from Kernel import Device


"""
GRBL device is a stub device. Serving as a placeholder. 
"""


class GrblDevice(Device):
    """
    """
    def __init__(self, root, uid=''):
        Device.__init__(self, root, uid)
        self.uid = uid
        self.device_name = "GRBL"
        self.location_name = "STUB"

        # Device specific stuff. Fold into proper kernel commands or delegate to subclass.
        self._device_log = ''
        self.current_x = 0
        self.current_y = 0

        self.hold_condition = lambda e: False
        self.pipe = None
        self.interpreter = None
        self.spooler = None

    def __repr__(self):
        return "GrblDevice(uid='%s')" % str(self.uid)

    @staticmethod
    def sub_register(device):
        pass

    def initialize(self, device, name=''):
        """
        Device initialize.

        :param device:
        :param name:
        :return:
        """
        self.uid = name
        self.open('module', 'Spooler')
