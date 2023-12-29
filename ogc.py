from PIL import Image, ImageDraw, ImageFont
import os
import sys

def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)


def add_text_with_outline(draw, position, text, font, text_color, outline_color, outline_width):
    if text == '':
        return
    for offset in range(-outline_width, outline_width + 1):
        for i in range(-outline_width, outline_width + 1):
            draw.text((position[0] + i, position[1] + offset), text, font=font, fill=outline_color)

    draw.text(position, text, font=font, fill=text_color)

def add_centered_text(draw, width, height, text, font, text_color, outline_color, outline_width, top_text):
    if text == '':
        return
    text_width, text_height = draw.textsize(text, font)
    x = (width - text_width) // 2
    #y = (height - text_height) // 2
    y = 10
    if not top_text:
        y = 190

    add_text_with_outline(draw, (x, y), text, font, text_color, outline_color, outline_width)

def add_wrapped_text(draw, width, height, text, font, text_color, outline_color, outline_width, top_text):
    if text == '':
        return
    max_width = width - 20
    lines = []

    words = text.split()
    current_line = words[0]
    for word in words[1:]:
        test_line = current_line + " " + word
        if draw.textsize(test_line, font)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)

    line_height = draw.textsize(lines[0], font)[1]
    #y = (height - len(lines) * line_height) // 2
    y = 10

    for line in lines:
        add_text_with_outline(draw, ((width - draw.textsize(line, font)[0]) // 2, y), line, font, text_color, outline_color, outline_width)
        y += line_height

def add_text_to_gif(input_path, output_path, text, text2, font_size=20, color=(255, 255, 255)):
    #gif = Image.open(input_path)
    gif = Image.open(resource_path(input_path))
    
    modified_frames = []

    font = ImageFont.truetype(resource_path("Arial_Bold.ttf"), font_size)

    for frame in range(gif.n_frames):
        gif.seek(frame)
        current_frame = gif.copy()

        draw = ImageDraw.Draw(current_frame)
        #draw.text((50, 10), text, font=font, fill=color, stroke_width=2)
        #add_text_with_outline(draw, (2, 10), text, font, color, (0, 0, 0,), 1)
        width, height = current_frame.size
        #add_centered_text(draw, width, height, text, font, color, (0, 0, 0), 1, True)
        add_wrapped_text(draw, width, height, text, font, color, (0, 0, 0), 1, True)

        #draw2.text((50, 90), text2, font=font, fill=color)
        add_centered_text(draw, width, height, text2, font, color, (0, 0, 0), 1, False)

        modified_frames.append(current_frame)

    modified_frames[0].save(
        output_path,
        save_all=True,
        append_images=modified_frames[1:],
        duration=gif.info['duration'],
        loop=gif.info['loop']
    )

if __name__ == "__main__":
    input_gif_path = "kel/kel-dw-afraidrw.gif"
    output_gif_path = "output.gif"
    text_to_add = "Top Text"
    text_to_add2 = "Bottom Text"

    add_text_to_gif(input_gif_path, output_gif_path, text_to_add, text_to_add2)

    print(f"Modified GIF saved to {output_gif_path}")
