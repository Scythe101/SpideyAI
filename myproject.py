#!/usr/bin/python3
import jetson_inference
import jetson_utils

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="Path of the image to process")
opt = parser.parse_args()

img = jetson_utils.loadImage(opt.filename)
net = jetson_inference.imageNet(model="spiders.onnx",labels="labels.txt",input_blob="input_0", output_blob="output_0")

class_idx, confidence = net.Classify(img)
class_desc = net.GetClassDesc(class_idx)
print("This spider is a "+ str(class_desc) +" (class #"+ str(class_idx) +") with " + str(confidence*100)+"% confidence")
if class_desc == "Black Widow":
    print("Female black widows (ones with a red, yellow, or white hourglass on their abdomen) are venomous. Their bites can cause pain, nausea, goosebumps, and swelling. Death as a result from a bite is uncommon.")
elif class_desc == "Blue Tarantula":
    print("Blue tarantulas are venomous. Bites can result in severe muscle cramps and inflammation, but its venom is not strong enough to kill a human.")
elif class_desc == "Bold Jumper":
    print("Bold jumpers are not dangerous. Their bites can result in itching and swelling, or no symptoms at all.")
elif class_desc == "Brown Recluse Spider":
    print("Brown recluse spiders are dangerous. Their bites commonly cause the skin surrounding the bite to die. Rarer symptoms include: fever, vomiting, nausea, and very rarely, bursting of red blood cells.")
elif class_desc == "Brown Grass Spider":
    print("Brown grass spiders are not dangerous to humans. Bites may result in itching or redness.")
elif class_desc == "Deinopis Spider":
    print("Deinopis spiders are not dangerous to humans.")
elif class_desc == "Golden Orb Weaver":
    print("Golden orb weaver spiders are not dangerous, and they rarely bite. Bites could cause muscle pain.")
elif class_desc == "Hobo Spider":
    print("Hobo spiders are widely believed to not be poisonous. Bites could cause nausea, headache, and fatigue.")
elif class_desc == "Huntsman Spider":
    print("Some species of huntsman spiders are venomous. Bites could result in pain, nausea, vomiting, headache, and heart palpitations.")
elif class_desc == "Ladybird Mimic Spider":
    print("Ladybird mimic spiders are not dangerous to humans.")
elif class_desc == "Peacock Spider":
    print("Peacock spiders are not dangerous to humans.")
elif class_desc == "Red Knee Tarantula":
    print("A red-kneed tarantula's bite is basically as bad a bee sting.")
elif class_desc == "Spiny-backed Orb-weaver":
    print("Spiny-backed orb-weavers are not dangerous to humans.")
elif class_desc == "White Kneed Tarantula":
    print("White-kneed tarantulas are not dangerous to humans.")
elif class_desc == "Yellow Garden Spider":
    print("Yellow garden spiders' bites are comporable to a bee sting.")