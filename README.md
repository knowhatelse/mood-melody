# Mood Melody

## **About the project**
Mood Melody is a web application that recomends song based on the users emotion. <br>

The app was made in Flask - Python web framework (for the API) and in React.js (for the client part). <br>
Additionally I used DeepFace for the image analysis and the emotion gathering from it, and Pandas for searching and getting data from a CSV file.  <br>

The CSV file that contains the songs list has 28.372 records of songs from 1950 to 2019, and they are devided in 7 genres.

## **How it works?**
Basically, the user uploads an image that contains a facial expression of him.<br>
After uploading the image, the image is beining analyzed and get the dominant emotion from it. <br>
Since it can recognize seven emotion, to every emotions is assigned one or more music genres that are contained in the CSV file. <br>
After the music genre is deretmined, 10 random songs are being found in the CSV file and returned to the user.<br>

## **Status of the app**
The app is currently still in the process of development. <br>
To see the code and current state of the project, checkout the develop branch. <br>

## **TO DO:**
- Make a more better song recomender based on the emotion and on other song data from the CSV file for more accurate and better response. <br>
- Make a loading animation for file uploading. <br>
- Display the current state of the process of image analysis while the user waits for the response. <br>
- Add buttons so that in the end the user can try again with the same image or another one. <br>
- Display the recoginesd emotion to the user. <br>
