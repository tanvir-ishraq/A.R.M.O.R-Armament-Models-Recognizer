from fastai.vision.all import *
import gradio as gr

#to use load_learner() in windows: #get updated code from discord group
# import pathlib
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath

cap_labels = (
    '2S19 Msta artillery', 
    'BM-21 Grad artillery', 
    'BMP-2 vehicle', 
    'BTR-80 vehicle', 
    'Bayraktar TB2 UCAV drone', 
    'CH-5 Rainbow UCAV drone', 
    'G6 Rhino artillery', 
    'Hermes 900 drone', 
    'Heron TP drone', 
    'Humvee vehicle', 
    'LAV-25 vehicle', 
    'Leopard 2 tank', 
    'M1 Abrams tank', 
    'M109 artillery', 
    'M113 vehicle', 
    'M270 MLRS artillery', 
    'MQ-9 Reaper UCAV drone', 
    'MRAP vehicle', 
    'RQ-4 Global Hawk UCAV drone', 
    'T-72 tank', 
    'Type 99 tank', 
    'Smerch artillery'
)

model = load_learner('models/ARMOR-classifier-v4.pkl')

def recognize_image(image):
  pred, idx, probs = model.predict(image) #predict() returns category, it's index, probablity of all catg.
  # print(pred)
  return dict(zip(cap_labels, map(float, probs))) # for all categories

#input output gradio formatting set:
image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label(num_top_classes=5) 

examples = [
    'test_images/unknown_00.jpeg',
    'test_images/unknown_01.jpg',
    'test_images/unknown_02.jpg',
    'test_images/unknown_03.webp',
    'test_images/unknown_04.jpg'
    ]

#interface with i/o
iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False) # share=True for colab