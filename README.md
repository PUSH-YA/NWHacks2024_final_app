# NWHacks2024 project
## Project: Sign Collaborative
This project included:
- training convolution neural network with adam optimiser and binary cross entropy loss
- system verification mechanism
- computer vision for predicting ASL signs in real time
- converting text to speech as well as speech to text using multithreading for asynchronous execution

in 24 hours!


### Our menu page: 
![small-1](https://github.com/PUSH-YA/NWHacks2024_final_app/assets/91928008/94e26c23-8752-431b-b16c-203ce116930e)

### ASL to text/speech translation in real time
|![small](https://github.com/PUSH-YA/NWHacks2024_final_app/assets/91928008/8c3f9059-06fd-4df3-a2b1-2477c536b1b3)|![small-1](https://github.com/PUSH-YA/NWHacks2024_final_app/assets/91928008/91a8b28c-4b77-4449-9a65-c35388612ae6)|
|---|---|

### Speech recogintion app for visually impaired community who can still communicate using these apps:
![small-1](https://github.com/PUSH-YA/NWHacks2024_final_app/assets/91928008/49373951-ed4a-44d7-b61c-e85476b91131)


## Inspiration
We have people in our family who have hearing impairments and use ASL to communicate however, some of us realise that we do not know ASL properly and are in the process of learning. We wanted to make this app to raise awareness for people to learn ASL to bridge the gap between ableism and disableism. 

## What it does 
This app uses a convolutional neural net using keras to recognise the image in front of it and convert ASL to text and then if the user wants, convert that text to speech for more convenience. The app also helps convert speech to text for people who are visually impaired as the app recognises background noise, adjusts for it and then processes the audio adjusting for the background noise to recognise the audio and convert that to speech. We also have system verification in place for the user to avoid the hassle of dealing with downloading dependencies. 


## How we built it
We built the model using keras and convolution neural net with softmax activation for multiclass classification and adam loss. This model is then used on a software made using the following libraries/frameworks: tkinter, pyttsx3, cv2 and speech recognition. These helped us show the camera feed, use those frames for recognising the ASL, converting text to speech and speech to text. This was all made to ensure cross-platformness among different devices with Python. 

## Challenges we ran into
The biggest challenge we ran into was ensuring that tkinter works cohesively among different layouts and make the os paths work relative to the current path. There were other issues with threads and deadlocks to ensure that speech recognition and text to speech worked on different threads. 

## Accomplishments that we're proud of
Being able to make a working product that fits our requirements of the apps

## What we learned
AI and models, how to implement the model prediction in real time with our app, solve major git merging issues, 

## What's next for Sign collaborative
Integration into different API environments, a more accurate machine learning model 

