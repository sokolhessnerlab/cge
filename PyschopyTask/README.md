# PsychoPy Tasks (NOTE: the files in this repo are dated and not what is used for our online study)

- We first stored the task on Github as we were programming the study before pushing it online. Once we pushed it online, we needed to move the study out of Github since Pavlovia uses Gitlab.
- The versions of the task that you see in this directory are not the most recent, but we will keep them here for reference/future use if necessary.
- Midway through programming, we switched from doing ospan to digit span.



## Details for how to access and update the study with Gitlab
1. To access the study's repo on Gitlab: go to https://pavlovia.org/sokolhessnerlab/cgtgamblingspantasks. 
2. Click on "view code", this will take you to the Gitlab repo.
3. The study folder is also stored on mahi mahi in the lab. Editing to the task will need to take place on a local computer and then changes get pushed online (its like Github). 

### When you want to make changes to the task
1. open the .psyexp file in Psychopy and make your changes using Builder interface
2. then save.
3. Then you will need to update the .js script (not ideal) because of a silly work around we had to implement to load resources. Below is how you do that.

### Editing JS script
You really don't want to be making many manual edits to the JS script because each time you make changes to the .psyexp file and save, those manual edits will go away so you'll be making those manual edits over and over again. There is once case when you need to make a manual edit to the .js script each time you make a change to the study in builder.

When you make an edit to the .psyexp file in PsychoPy builder, press save. Upon saving, PsychoPy will automatically update the .JS script. Because we had to manually load resources during a “before the experiment” in a code snippet, Psychopy puts this code before the study is even initialized (not sure why this happens – hoping it changes with future updates/bug fixes).

To fix this, the load resources code in the .js script needs to be moved down several lines.

When you press save, the .js script will pop up and look like this:

<img width="1034" alt="incorrectJScode" src="https://user-images.githubusercontent.com/19710394/189238371-8bbc1373-1f66-4447-8dae-52019d46e245.png">

### Step 1 to fix this is to move the code to the correct location:

<img width="888" alt="correctJSlocation" src="https://user-images.githubusercontent.com/19710394/189238435-c28ab26c-7c9f-4c29-88af-b9214e4e3f90.png">


### Step 2 is to comment out the incorrect psychoJS.start() code right below our code we just moved:


<img width="958" alt="commentOutCode" src="https://user-images.githubusercontent.com/19710394/189238461-c1fe2c82-5da4-472e-b5ec-7fab3adce456.png">


### To push changes to Pavlovia, press the green button (shown below) and then enter in your commit (just like Github). The synchronization should only take a few seconds unless there are a bunch of changes. 

<img width="533" alt="pushToPavloviaButton" src="https://user-images.githubusercontent.com/19710394/189238508-b4a8c18d-b8d0-4f56-8cc9-275cdfacdaec.png">


