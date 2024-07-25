# Raspberry Pi 3B+/4B Camera QR Scanner
This will guide you through on how to install required libraries and dependencies to enable camera scanning on Rapsberry Pi

## Requirements:
- Raspberry Pi
- Micro SD card
- Raspberry Pi camera

## Process:

### DOWNLOAD OPENCV LIBRARY TO OPEN CAMERA QR CODE SCAN

1. Update the package list:
    ```sh
    sudo apt-get update
    ```

2. Install Python 3 and OpenCV:
    ```sh
    sudo apt-get install python3-opencv
    ```

3. Install required dependencies:
    ```sh
    sudo apt-get install libqt4-test python3-sip python3-pyqt5 libqtgui4 libjasper-dev libatlas-base-dev -y
    sudo apt-get install libhdf5-dev
    sudo apt-get install libatlas-base-dev
    sudo apt-get install libjasper-dev
    sudo apt-get install libqt5gui5 libqt5webkit5 libqt5test5
    sudo apt-get install libopenblas-dev
    ```

4. Upgrade `numpy` and `setuptools`:
    ```sh
    pip install -U numpy
    pip install --upgrade pip setuptools wheel
    ```

5. Install `opencv-python`:
    ```sh
    pip3 install opencv-python
    pip3 install opencv-contrib-python==4.5.1.48
    ```

6. Enable the camera:
    ```sh
    sudo modprobe bcm2835-v4l2
    ```

7. Reboot the system:
    ```sh
    reboot
    ```
## Example
### QR Identify and Decode

1. Open `QR-Decode.py`
    - Wait for the camera to search for QR Codes

2. Adding CSV File to store databases of QR Codes for future use:
    - Open `QR-Decode-With-CSV.py`
    - Capture the QR code
    - Save into `csv.txt` file
