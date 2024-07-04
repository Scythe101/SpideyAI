# SpideyAI
SpideyAI is an AI model that can detect different types of spiders and give the user more information about the species of spider it detects.
<details><summary>Brief backstory</summary>I came up with this idea after being jump-scared by a spider in the middle of the night. I then decided it would be a good idea to know whether or not the spider could hurt me, and thought it would make for a fun AI project. Lastly, I looked at the classes ResNet18 was trained off of to make sure it can't do this by default, and it apparently doesn't have much data on spiders.</details>

This was made by re-training the ResNet-18 model with [this](https://www.kaggle.com/datasets/gpiosenka/yikes-spiders-15-species) dataset.
It can detect these types of spiders:
* Black Widow
* Blue Tarantula
* Bold Jumper
* Brown Grass Spider
* Brown Recluse Spider
* Deinopis Spider
* Golden Orb Weaver
* Hobo Spider
* Huntsman Spider
* Ladybird Mimic Spider
* Peacock Spider
* Red Knee Tarantula
* Spiny-backed Orb-weaver
* White Kneed Tarantula
* Yellow Garden Spider

## Installation
This project requires Python and the Jetson Inference library to be installed on your system.

First, clone the repo.
```sh
git clone https://github.com/Scythe101/SpideyAI
```
Then, change directories into the repo folder
```sh
cd SpideyAI
```
Lastly, run the Python script.
```sh
python3 spiders.py path/to/image/here
```

[Here is the link to a video demonstration](https://drive.google.com/file/d/1NKrWIcP5V33LlGLswXgGnfiJUF2rkQ5c/view?usp=sharing)