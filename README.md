# ASL Interpreter Automated Scrape Script
Automated way to scrape the RID (Registry of Interpreters for the Deaf) in order to get all member's contact information so that they can be reached out to for jobs or know where one's skills as an American Sign Language (ASL) interpreter may be of great need.

Posted this also to show how one can easily make a single-file automated script. Took me ~2 hours to write the whole thing and following this format and using these packages, you'll see it's easy to do.

## Demo Video
https://github.com/user-attachments/assets/70340d60-726d-46b3-b3c0-3470f5e877a8

## Screenshots of Output
**Raw CSV**
<img width="1680" alt="Ex  Screenshot of raw CSV file " src="https://github.com/user-attachments/assets/eef1be21-8975-4564-a97d-a37c974aaed8" />

**CSV Open in Excel**
<img width="1403" alt="Ex  Screenshot of CSV file open in Excel" src="https://github.com/user-attachments/assets/9adebe61-7009-41cf-ba2b-0cc29f1c65f9" />


## To Run
Assuming you have python3 already installed, do the following:
1. Download latest version of [Visual Studio Code](https://code.visualstudio.com/) (for maximum ease).
2. Download this project via the zip option or git cloning.
3. Open up project in Visual Studio Code.
4. Open up terminal within VSCode.
5. Next install the packages via that terminal or console.
```
pip3 install -r requirements.txt
# If this fails because it can't find requireements.txt, make sure you are in the right directory or go to it, ex. "cd ~/Download/ASL-interpreter-automated-scrape" first?
# If this fails because "pip3" does not exist, try instead "python3 -m pip install -r requirements.txt"
```
6. Lastly run script with the following.
```
python3 python-asl-scrape.py
# If this doesn't run at all, verify you're in the right directory. Might need to "cd ~/Download/ASL-interpreter-automated-scrape" first?
```
7. Then wait until Google Chrome launches another window controlled by automated software, watch it do it's thing, and when it's all done, you should have a `output.csv` file completely filled out and completed in your local directory.
