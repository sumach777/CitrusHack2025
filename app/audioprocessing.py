import sounddevice as sd
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import time


Sample_rate = 4410
channels = 1
target_dB = -20.0 # get from user input, must be within min, max
switch = 1
max_dB = -40.0 # max for hearing 80 dBSPL(converted)
min_db = -60.0
block_size = 1024

#accessing system speakers
def main():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    current_volume = volume.GetMasterVolumeLevel()
    
    if current_volume != target_dB:
        volume.SetMasterVolumeLevel(target_dB, None)
        


if __name__ == "__main__":
    main()
    
