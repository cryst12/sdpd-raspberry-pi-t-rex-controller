# About

This repo is a part of the Software for Portable Devices (CS F314) course. In this project, you will take input from the GPIO pins of the Raspberry Pi, and make the TRex jump based on that.

# Pre-requisite

1. Install node.js (v6.x.x LTS) from https://nodejs.org/en/
2. npm should also have been installed. Run `npm install npm@latest -g` to update npm to the latest version. If you get an error, try `sudo npm install npm@latest -g`.
3. Run `git clone https://github.com/thepulkitagarwal/sdpd-t-rex-runner.git` or download a zip of that repository.
4. `cd` into the local copy of the repo on your terminal.
5. Run `npm install`. (Note: `npm warn` is not a problem. You can go ahead with the next step.)
6. Run `npm start`.
7. Open a separate terminal, `cd` into the local copy of the repo, and run `python raspiController.py`. (You might have a problem if you are using python3 instead of python 2)
8. Open your browser and go to <http://localhost:3000> and press space.
9. The TRex should automatically jump every 0.5 seconds.

# Setup

1. Run `git clone https://github.com/cryst12/sdpd-t-rex-controller.git` or download a zip of this repository.
2. `cd` into the local copy of the repo on your terminal and copy `raspiController.py` into a raspberry pi.


### For more information visit `https://github.com/thepulkitagarwal/sdpd-t-rex-runner.git`