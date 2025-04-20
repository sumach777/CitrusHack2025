import sounddevice as sd
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

class AudioProcessor:
    def __init__(self, audio_app):
        self.app = audio_app
        self.volume_interface = self._get_volume_interface()
        
    def _get_volume_interface(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        return cast(interface, POINTER(IAudioEndpointVolume))
    
    def process_audio(self):
        target_dB = self.app.get_volume()
        on_off = self.app.get_is_on()

        if not on_off:
            self.volume_interface.SetMute(1, None)
        else:
            self.volume_interface.SetMute(0, None)
            current_volume = self.volume_interface.GetMasterVolumeLevel()
            if abs(current_volume - target_dB) > 0.1:
                self.volume_interface.SetMasterVolumeLevel(target_dB, None)
        
        # Schedule next check
        self.app.root.after(100, self.process_audio)