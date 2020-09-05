# Live Cartoonize

Cartoonize your own video through the input from the video camera. OpenCV is used to capture the video frames and these are then processed through internal layers to create a cartoonish avatar of your frame. This cartoonish avatar is created multiple times per second (FPS depends on the compute capability of Run Environment)

## Demo
![Cartoonize Demo](demo.gif)

## Installation

Cartoonize requires [OpenCV](https://github.com/opencv/opencv) v4.2+ to run.

Install the dependencies and run the main.py file to run a live demo of the cartoonize implementation

If you prefer a native install:
```sh
$ cd path/to/your/install/directory
$ git clone https://github.com/traveller-scientist/live-cartoonize.git
$ cd live-cartoonize 
$ pip3 install -r requirements.txt
$ python3 main.py
```

If you prefer a virtual environment (Unix or MacOS):
```sh
$ cd path/to/your/install/directory
$ git clone https://github.com/traveller-scientist/live-cartoonize.git
$ python3 -m venv live-cartoonize
$ cd live-cartoonize 
$ source bin/activate
$ pip3 install -r requirements.txt
$ python3 main.py
```

If you prefer a virtual environment (Windows - cmd):
```sh
$ cd path/to/your/install/directory
$ git clone https://github.com/traveller-scientist/live-cartoonize.git
$ python3 -m venv live-cartoonize
$ cd live-cartoonize 
$ Scripts\activate.bat
$ pip3 install -r requirements.txt
$ python3 main.py
```

To exit the OpenCV cartoonize window please press q on the keyboard 

To exit out of the virtual environment:
```sh
$ deactivate
```

License
----

MIT


**Free Software, Hell Yeah!**

For any doubts you can also connect with me on [LinkedIn] or [Instagram]

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [LinkedIn]: <https://www.linkedin.com/in/nitish-chhabra/>
   [Instagram]: <https://www.instagram.com/traveller_scientist/>