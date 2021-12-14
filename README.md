# Air Ukulele

In this project, I made an “Air Ukulele”. This “Air Ukulele” draws inspiration from ukulele and theremin, and plays single notes and chords of different pitches based on the proximity of the hand to the fingerboard.

# Design Inspiration
- The inspiration of this project comes from the urge to try out different instruments without having to spend hundreds or thousands of dollars in order to play one. I wanted to create the experience of creating music without the need to save up for a long time and wait for forever before being able to do so.
- There are three main parts in the Air Ukulele. The first component is the “fret”, represented by a proximity sensor. Instead of having four different strings and multiple frets like a traditional ukulele, the Air Ukulele recognizes pitches by the distance of the user’s hand to the proximity sensor. It resembles that of a theremin and adds a playful character to the Air Ukulele. The second component is the chord-switching button, represented by a qwiic button. By turning the qwiic button on, the LED will light up, signifying that the Air Ukulele has switched to chords mode, which will play the major chord of the corresponding pitch. The last component is the joystick. The joystick is used as a “strumming” tool, using the movability of the joystick to simulate the motion of a hand strumming on the instrument. All three of these parts work together to create the output sound.

# Paper and Design Prototypes
## Rough Idea:
- My rough idea is as pictured, a cardboard ukulele that resembles the shape and size of an ukelele in real life. Here's a picture of my inspiration:
- ![image](https://user-images.githubusercontent.com/35357433/145910125-a75cff0b-4f2f-44e2-8e05-db217fa8d838.png)

## Paper Prototype 1:
- In this stage, I envisioned the finished product to be very similar to a real ukulele, with fake strings and frets. Under each "fret", there would be a proximity sensor to detect whether or not the user intends to press there.
- I also envisioned to use a camera to detect the motion and speed of user's hand gestures and classify whether the user intends to enter fingerpicking or chord modes. 
- ![IMG_0373](https://user-images.githubusercontent.com/35357433/145911022-78d5dc03-c76d-4cab-91d7-6e72da598267.jpg)

## Paper Prototype 2:
- Based on my previous design, I would need tenths of proximity sensors, which I decided was not very economical. I then had an inspiration from the instrument [theremin](https://en.wikipedia.org/wiki/Theremin) and decided to use one proximity sensor to measure pitches. 
- ![IMG_0374](https://user-images.githubusercontent.com/35357433/145911514-3689cfd4-d4d5-4494-96fa-6b7664570d70.jpg)

## Paper Prototype 3:
- Though I liked the idea of using a camera and computer vision to classify different motions of user's gestures, I decided that it might not be practical to do so because it can create a lot of lag in a program that requires fast feedback (otherwise the user would have to pause every time before playing a new note or switching to a new mode). I then turned my attention to a joystick, which embodies motion itself and is a great alternative. I decided to replace the camera with a joystick and call it a "strum" every time the joystick is pushed down.
- ![IMG_0375](https://user-images.githubusercontent.com/35357433/145911993-e5b106e3-f4ca-4e1d-903a-e965bd35d725.jpg)

## Paper Protype 4: 
- Because I switched to using one proximity sensor instead of multiple, I now can't detect if user wants to press multiple notes to play a chord. I decided to add a button to switch back and forth from single note mode to chords mode. I placed the button on the buttom of the fingerboard because it makes sense to delegate the mode switching toe left hand, as in real ukulele playing, the left hand deals with all functions relating to selecting the notes to play. 
- ![IMG_0376](https://user-images.githubusercontent.com/35357433/145912295-bea8fa8b-9ad8-4d8b-876a-1253c1cf3652.jpg)

# State Diagram
![IMG_0372](https://user-images.githubusercontent.com/35357433/145909280-70f3cc91-6e10-4c67-bf55-27342230eee1.jpg)

# Assembly
## Parts:
- 1 x Raspberry Pi 4
- 1 x Adafruit APDS9960 Proximity, Light, RBG, Gesture Sensor
- 1 s Webcam with Speaker
- 1 x SparkFun Qwiic Button - Green LED
- 1 x SparkFun Qwiic Joystick
- 1 x SparkFun Qwiic Cable Kit

## Implementation:
### Part 1:
- I was planning to download guitar/ukulele single note and chord audio online, but I wasn’t able to because most sites only have chord audios but not single note audios. Because of that, I looked for an alternative option, which is to play frequency sounds / Midi via a Python library. However, this method wouldn’t work well with guitar chords either because guitar chords are more like very fast 32nd notes rather than regular chords where all notes happen at the same time, which isn’t easy to simulate using Python. I ended up creating a score on Musescore with all the notes and sounds I would need, and I manually cut them later in an Audio Editing software. 
- I only create notes from one octave (with sharps and flats) because otherwise the user's hand would have to extend very far in order to reach the higher registers. In order to maintain user experience, I decided to keep it in a shorter range.
- <img width="478" alt="Screen Shot 2021-12-13 at 7 15 39 PM" src="https://user-images.githubusercontent.com/35357433/145909561-3ea50e88-4609-4ea3-8e5c-786e99cb5fe1.png">

### Part 2:
- I integrated the proximity sensor and the joystick, and played a note according to the proximity metric every time the joystick is turned near all the way up or down on the horizontal axis (allowing 3 points of difference in either direction). 
- I also controlled the range of proximity distance that the sensor picks up and recognizes. I limited it to about the length of half of my arm so that the user doesn’t have to stick their arms straight in order to catch the highest pitch that is available in the program. For proximity higher than the indicated highest range, I simply play the highest note available. Each note has an equal distance of proximity gap. 
- While testing, I realized that playing the audio via the webcam speaker is much quieter than what I hear when I play them on my computer. To fix that, I used a Python library to increase each of the audio by 20 dB. (via increaseAudio.py)

### Part 3:
- After testing and making sure the previous two steps work, I added the chord button. Each time the chord button is pressed, the ukulele switches the chord mode on and off. When the chord mode is on, the LED lights up as a feedback to the user. 

## Stages of Assembly:
* I forgot to take pictures as how I built - sorry about that!
### Step 1 - cut out the shape:
- In step 1, I used my ukulele at home to draw out the shape on a cardboard, and cut out two of it as front and back of the ukulele.

### Step 2 - simulate sensors and test
- In this step, I drew the locations of the sensors on the front board of the ukulele, and I tested it in order to make sure that the position still feels comfortable as a physical product.

### Step 3 - cut out openings for sensors
- In this step, I cut out openings for the sensors and taped the sensors on. I made sure that I had enough room to allow wires in the back and that all sensors sit firmly on the cardboard. Each of the sensor and the Raspberry Pi board and daisy-chained together.

### Step 4 - connect the two boards and make it 3D
- This was the most challenging process of the building experience. My plan was to use a long strip of cardboard, fold its width 3-way and use 2 outer ⅓ widths to glue to the front and back sides of the ukulele, leaving the middle ⅓ width as the height of the ukulele. However, the cardboard is much thicker than I anticipated, and it was very hard to use that to follow the curve of the ukulele board. Because of that, my sides ended up looking uneven and I had to use a lot of glue and tape in order to have all sides of the ukulele sticking firmly together. 
- I decided to add cotton balls on the sides of the ukulele in order to mask the unevenness of the side boards, and I added two “eyes” on the front board to add on to the playful element. 

## Executing the Program:
- After logging into the pi via ssh, cd into the directory and run python run.py on the command line

## Final Product:
https://user-images.githubusercontent.com/35357433/145913730-b3d78e47-befd-4a50-be49-6e5ce5052ada.mov
