import random
import time
import gradio as gr

face = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

def big(symbol, size=200):
    # makes the dice large and centered
    return f"<div style='text-align:center; font-size:{size}px; line-height:1.2;'>{symbol}</div>"
def dice_roll():
    return random.randint(1, 6)

def reset():
    return big("⚀"), ""

def roll():
    result = dice_roll()
    delay = 0.05 
    
    for _ in range(15):  # _ means we don't care about the loop countdown
 # yeild a random face do not wait whole loop to finish and a rolling message
        yield big(random.choice(face)), "Rolling...🎲"
        time.sleep(delay)
        delay +=0.015
        
        # list is used because it is easy way to map number with symbols
    yield big(face[result-1]), f"## You rolled a {result}!"
    
    # custom theme
theme = gr.themes.Monochrome(
        primary_hue = "sky",
        secondary_hue = "blue",
        neutral_hue = "slate",
        font = gr.themes.GoogleFont("Poppins"),
        radius_size = "lg",   
    )
    
with gr.Blocks(title = "Dice Roller", theme=theme) as demo:
    gr.Markdown("# Dice Roller 🎲")
    
    with gr.Row():
        with gr.Column():
            output = gr.HTML(big("⚀"))
            result = gr.Markdown("")
            roll_button = gr.Button("Start Rolling🎲", variant="primary",size = "lg")
            reset_button = gr.Button("🔄Reset")
    roll_button.click(fn=roll,
                      inputs= None,
                      outputs = [output, result])
    reset_button.click(fn=reset,
                       inputs= None,
                       outputs = [output, result])
demo.launch(share=True)
        
        
        

