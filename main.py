import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
from ogc import add_text_to_gif
import os
import sys
import shutil

def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)


exe_dir_before = os.path.dirname(sys.executable)
exe_dir = os.path.join(exe_dir_before, '../../..')
output_file_path = os.path.join(exe_dir, 'output.gif')
#output_file_path = 'output.gif'

def move_file(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        print(f"File moved from '{source_path}' to '{destination_path}'.")
    except Exception as e:
        print(f"Error: {e}")

move_file(resource_path('output.gif'), exe_dir)

class OmoriGifCreator:
    def __init__(self, master):
        self.master = master
        self.master.title("Omori Gif Creator")
        self.master.geometry("500x450")

        self.title_screen = Frame(self.master)
        self.omori_screen = Frame(self.master)
        self.aubrey_screen = Frame(self.master)
        self.kel_screen = Frame(self.master)
        self.basil_screen = Frame(self.master)
        self.dream_world_aubrey_screen = Frame(self.master)
        self.dream_world_omori_screen = Frame(self.master)
        self.dream_world_kel_screen = Frame(self.master)
        self.sunny_screen = Frame(self.master)
        self.rw_aubrey_screen = Frame(self.master)
        self.rw_kel_screen = Frame(self.master)

        self.init_title_screen()
        self.init_omori_screen()
        self.init_aubrey_screen()
        self.init_kel_screen()
        self.init_basil_screen()
        self.init_dream_world_aubrey_screen()
        self.init_dream_world_omori_screen()
        self.init_dream_world_kel_screen()
        self.init_sunny_screen()
        self.init_rw_aubrey_screen()
        self.init_rw_kel_screen()

        self.show_screen(self.title_screen)


    def init_title_screen(self):
        Button(self.title_screen, text='Omori', width=10, command=lambda: self.show_screen(self.omori_screen)).pack()
        Button(self.title_screen, text='Aubrey', width=10, command=lambda: self.show_screen(self.aubrey_screen)).pack()
        Button(self.title_screen, text='Kel', width=10, command=lambda: self.show_screen(self.kel_screen)).pack()
        Button(self.title_screen, text='Basil', width=10, command=lambda: self.show_screen(self.basil_screen)).pack()
        #Button(self.title_screen, text='Mari', width=10).pack()
        #Button(self.title_screen, text='Hero', width=10).pack()
        Label(self.title_screen, text="Press '|' at anytime to close the application").pack()


    def init_omori_screen(self):
        Button(self.omori_screen, text='Sunny', width=12, command=lambda: self.show_screen(self.sunny_screen)).pack()
        Button(self.omori_screen, text='Omori', width=12, command=lambda: self.show_screen(self.dream_world_omori_screen)).pack()

        Button(self.omori_screen, text="Back", width=3, command=lambda: self.show_screen(self.title_screen)).place(relx=0, rely=0)


    def init_dream_world_omori_screen(self):
        self.top_text_input = Label(self.dream_world_omori_screen, text='Top Text:')
        self.top_text_input.pack()
        self.top_text_input_box1 = Entry(self.dream_world_omori_screen)
        self.top_text_input_box1.pack()

        self.bottom_text_input = Label(self.dream_world_omori_screen, text='Bottom Text:')
        self.bottom_text_input.pack()
        self.bottom_text_input_box1 = Entry(self.dream_world_omori_screen)
        self.bottom_text_input_box1.pack()

        Button(self.dream_world_omori_screen, text="Save", width=3, command=lambda: self.on_save_pressed(topt=self.top_text_input_box1.get(), bottomt=self.bottom_text_input_box1.get())).pack()

        self.emotion_label_dw_omori = Label(self.dream_world_omori_screen, text='neutral')
        self.emotion_label_dw_omori.pack()

        self.frame1 = Frame(self.dream_world_omori_screen)
        self.frame2 = Frame(self.dream_world_omori_screen)

        self.frame1.pack()
        self.frame2.pack()

        Button(self.frame1, text="Neutral", width=3, command=lambda: self.on_save_pressed(True, 'omori-neutral', self.emotion_label_dw_omori)).pack(side='left', padx=5)
        Button(self.frame1, text="Happy", width=3, command=lambda: self.on_save_pressed(True, 'omori-happy', self.emotion_label_dw_omori)).pack(side='left', padx=5)
        Button(self.frame1, text="Ecstatic", width=3, command=lambda: self.on_save_pressed(True, 'omori-ecstatic', self.emotion_label_dw_omori)).pack(side='left', padx=5)
        Button(self.frame1, text="Manic", width=3, command=lambda: self.on_save_pressed(True, 'omori-manic', self.emotion_label_dw_omori)).pack(side='left', padx=5)
        Button(self.frame1, text="Sad", width=3, command=lambda: self.on_save_pressed(True, 'omori-sad', self.emotion_label_dw_omori)).pack(side='left', padx=5)
        #Button(self.frame1, text="Depressed", width=3, font=('Arial', 10), command=lambda: self.on_save_pressed(True, 'omori-depressed', self.emotion_label_dw_omori)).pack(side='left', padx=5)
        Button(self.frame1, text="Miserable", width=3, command=lambda: self.on_save_pressed(True, 'omori-miserable', self.emotion_label_dw_omori)).pack(side='left', padx=5)
        Button(self.frame1, text="Angry", width=3, command=lambda: self.on_save_pressed(True, 'omori-angry', self.emotion_label_dw_omori)).pack(side='left', padx=5)
        Button(self.frame2, text="Enraged", width=3, command=lambda: self.on_save_pressed(True, 'omori-enraged', self.emotion_label_dw_omori)).pack(side='left', padx=5)
        Button(self.frame2, text="Furious", width=3, command=lambda: self.on_save_pressed(True, 'omori-furious', self.emotion_label_dw_omori)).pack(side='left', padx=5)
        
        self.gif_path = 'omori/omori-dw-neutral.gif'
        self.first_load = True
        self.i = 0
        self.current_screen = self.dream_world_omori_screen
        #self.load_gif()
        self.selected_emotion = 'omori-neutral'
        #self.master.after(100, self.on_save_pressed, True, self.selected_emotion)
        Button(self.dream_world_omori_screen, text="Back", width=3, command=lambda: self.show_screen(self.omori_screen)).place(relx=0, rely=0)


    def init_aubrey_screen(self):
        Button(self.aubrey_screen, text='Real World Aubrey', width=12, command=lambda: self.show_screen(self.rw_aubrey_screen)).pack()
        Button(self.aubrey_screen, text='Dream World Aubrey', width=12, command=lambda: self.show_screen(self.dream_world_aubrey_screen, 'aubrey-neutral')).pack()

        Button(self.aubrey_screen, text="Back", width=3, command=lambda: self.show_screen(self.title_screen)).place(relx=0, rely=0)


    def init_dream_world_aubrey_screen(self):
        #self.gif_label.pack(expand=True)

        self.top_text_input = Label(self.dream_world_aubrey_screen, text='Top Text:')
        self.top_text_input.pack()
        self.top_text_input_box2 = Entry(self.dream_world_aubrey_screen)
        self.top_text_input_box2.pack()

        self.bottom_text_input = Label(self.dream_world_aubrey_screen, text='Bottom Text:')
        self.bottom_text_input.pack()
        self.bottom_text_input_box2 = Entry(self.dream_world_aubrey_screen)
        self.bottom_text_input_box2.pack()

        Button(self.dream_world_aubrey_screen, text="Save", width=3, command=lambda: self.on_save_pressed(topt=self.top_text_input_box2.get(), bottomt=self.bottom_text_input_box2.get())).pack()

        self.emotion_label_dw_aubrey = Label(self.dream_world_aubrey_screen, text='neutral')
        self.emotion_label_dw_aubrey.pack()

        self.frame1 = Frame(self.dream_world_aubrey_screen)
        self.frame2 = Frame(self.dream_world_aubrey_screen)

        self.frame1.pack()
        self.frame2.pack()

        Button(self.frame1, text="Neutral", width=3, command=lambda: self.on_save_pressed(True, 'aubrey-neutral', self.emotion_label_dw_aubrey)).pack(side='left', padx=5)
        Button(self.frame1, text="Happy", width=3, command=lambda: self.on_save_pressed(True, 'aubrey-happy', self.emotion_label_dw_aubrey)).pack(side='left', padx=5)
        #Button(self.frame1, text="Ecstatic", width=3, command=lambda: self.on_save_pressed(True, 'ec', self.emotion_label_dw_aubrey)).pack(side='left', padx=5)
        Button(self.frame1, text="Sad", width=3, command=lambda: self.on_save_pressed(True, 'aubrey-sad', self.emotion_label_dw_aubrey)).pack(side='left', padx=5)
        Button(self.frame1, text="Depressed", width=3, font=('Arial', 10), command=lambda: self.on_save_pressed(True, 'aubrey-depressed', self.emotion_label_dw_aubrey)).pack(side='left', padx=5)
        Button(self.frame1, text="Angry", width=3, command=lambda: self.on_save_pressed(True, 'aubrey-angry', self.emotion_label_dw_aubrey)).pack(side='left', padx=5)
        Button(self.frame1, text="Enraged", width=3, command=lambda: self.on_save_pressed(True, 'aubrey-enraged', self.emotion_label_dw_aubrey)).pack(side='left', padx=5)
        Button(self.frame2, text="Afraid", width=3, command=lambda: self.on_save_pressed(True, 'aubrey-afraid', self.emotion_label_dw_aubrey)).pack(side='left', padx=5)
        #Button(self.frame2, text="Stressed Out", width=3, font=('Arial', 8)).pack(side='left', padx=5)
        
        self.gif_path = 'aubrey/aubrey-dw-neutral.gif'
        self.first_load = True
        self.i = 0
        self.current_screen = self.dream_world_aubrey_screen
        #self.load_gif()
        self.selected_emotion = 'aubrey-neutral'
        self.inputted_top_text = ''
        self.inputted_bottom_text = ''
        #self.master.after(100, self.on_save_pressed, True, self.selected_emotion)
        Button(self.dream_world_aubrey_screen, text="Back", width=3, command=lambda: self.show_screen(self.aubrey_screen)).place(relx=0, rely=0)

    
    def init_kel_screen(self):
        Button(self.kel_screen, text='Real World Kel', width=12, command=lambda: self.show_screen(self.rw_kel_screen)).pack()
        Button(self.kel_screen, text='Dream World Kel', width=12, command=lambda: self.show_screen(self.dream_world_kel_screen)).pack()

        Button(self.kel_screen, text="Back", width=3, command=lambda: self.show_screen(self.title_screen)).place(relx=0, rely=0)


    def init_dream_world_kel_screen(self):
        #self.gif_label.pack(expand=True)

        self.top_text_input = Label(self.dream_world_kel_screen, text='Top Text:')
        self.top_text_input.pack()
        self.top_text_input_box3 = Entry(self.dream_world_kel_screen)
        self.top_text_input_box3.pack()

        self.bottom_text_input = Label(self.dream_world_kel_screen, text='Bottom Text:')
        self.bottom_text_input.pack()
        self.bottom_text_input_box3 = Entry(self.dream_world_kel_screen)
        self.bottom_text_input_box3.pack()

        Button(self.dream_world_kel_screen, text="Save", width=3, command=lambda: self.on_save_pressed(topt=self.top_text_input_box3.get(), bottomt=self.bottom_text_input_box3.get())).pack()

        self.emotion_label_dw_kel = Label(self.dream_world_kel_screen, text='neutral')
        self.emotion_label_dw_kel.pack()

        self.frame1 = Frame(self.dream_world_kel_screen)
        self.frame2 = Frame(self.dream_world_kel_screen)

        self.frame1.pack()
        self.frame2.pack()

        Button(self.frame1, text="Neutral", width=3, command=lambda: self.on_save_pressed(True, 'kel-neutral', self.emotion_label_dw_kel)).pack(side='left', padx=5)
        Button(self.frame1, text="Happy", width=3, command=lambda: self.on_save_pressed(True, 'kel-happy', self.emotion_label_dw_kel)).pack(side='left', padx=5)
        #Button(self.frame1, text="Ecstatic", width=3, command=lambda: self.on_save_pressed(True, 'ec', self.emotion_label_dw_kel)).pack(side='left', padx=5)
        Button(self.frame1, text="Sad", width=3, command=lambda: self.on_save_pressed(True, 'kel-sad', self.emotion_label_dw_kel)).pack(side='left', padx=5)
        Button(self.frame1, text="Depressed", width=3, font=('Arial', 10), command=lambda: self.on_save_pressed(True, 'kel-depressed', self.emotion_label_dw_kel)).pack(side='left', padx=5)
        Button(self.frame1, text="Angry", width=3, command=lambda: self.on_save_pressed(True, 'kel-angry', self.emotion_label_dw_kel)).pack(side='left', padx=5)
        Button(self.frame1, text="Enraged", width=3, command=lambda: self.on_save_pressed(True, 'kel-enraged', self.emotion_label_dw_kel)).pack(side='left', padx=5)
        Button(self.frame2, text="Afraid", width=3, command=lambda: self.on_save_pressed(True, 'kel-afraid', self.emotion_label_dw_kel)).pack(side='left', padx=5)
        #Button(self.frame2, text="Stressed Out", width=3, font=('Arial', 8)).pack(side='left', padx=5)
        
        self.gif_path = 'kel/kel-dw-neutral.gif'
        self.first_load = True
        self.i = 0
        self.current_screen = self.dream_world_kel_screen
        #self.load_gif()
        self.selected_emotion = 'kel-neutral'
        self.inputted_top_text = ''
        self.inputted_bottom_text = ''
        #self.master.after(100, self.on_save_pressed, True, self.selected_emotion)
        Button(self.dream_world_kel_screen, text="Back", width=3, command=lambda: self.show_screen(self.kel_screen)).place(relx=0, rely=0)


    def init_basil_screen(self):
        #self.gif_label.pack(expand=True)

        self.top_text_input = Label(self.basil_screen, text='Top Text:')
        self.top_text_input.pack()
        self.top_text_input_box4 = Entry(self.basil_screen)
        self.top_text_input_box4.pack()

        self.bottom_text_input = Label(self.basil_screen, text='Bottom Text:')
        self.bottom_text_input.pack()
        self.bottom_text_input_box4 = Entry(self.basil_screen)
        self.bottom_text_input_box4.pack()

        Button(self.basil_screen, text="Save", width=3, command=lambda: self.on_save_pressed(topt=self.top_text_input_box4.get(), bottomt=self.bottom_text_input_box4.get())).pack()

        self.emotion_label_basil = Label(self.basil_screen, text='neutral')
        self.emotion_label_basil.pack()

        self.frame1 = Frame(self.basil_screen)

        self.frame1.pack()

        Button(self.frame1, text="Neutral", width=3, command=lambda: self.on_save_pressed(True, 'basil-neutral', self.emotion_label_basil)).pack(side='left', padx=5)
        Button(self.frame1, text="Happy", width=3, command=lambda: self.on_save_pressed(True, 'basil-happy', self.emotion_label_basil)).pack(side='left', padx=5)
        #Button(self.frame1, text="Ecstatic", width=3, command=lambda: self.on_save_pressed(True, 'basil-ecstatic', self.emotion_label_basil)).pack(side='left', padx=5)
        #Button(self.frame1, text="Manic", width=3, command=lambda: self.on_save_pressed(True, 'basil-manic', self.emotion_label_basil)).pack(side='left', padx=5)
        #Button(self.frame1, text="Sad", width=3, command=lambda: self.on_save_pressed(True, 'basil-sad', self.emotion_label_basil)).pack(side='left', padx=5)
        Button(self.frame1, text="Depressed", width=3, font=('Arial', 10), command=lambda: self.on_save_pressed(True, 'basil-depressed', self.emotion_label_basil)).pack(side='left', padx=5)
        #Button(self.frame1, text="Miserable", width=3, command=lambda: self.on_save_pressed(True, 'basil-miserable', self.emotion_label_basil)).pack(side='left', padx=5)
        #Button(self.frame1, text="Angry", width=3, command=lambda: self.on_save_pressed(True, 'basil-angry', self.emotion_label_basil)).pack(side='left', padx=5)
        #Button(self.frame2, text="Enraged", width=3, command=lambda: self.on_save_pressed(True, 'basil-enraged', self.emotion_label_basil)).pack(side='left', padx=5)
        #Button(self.frame2, text="Furious", width=3, command=lambda: self.on_save_pressed(True, 'basil-furious', self.emotion_label_basil)).pack(side='left', padx=5)
        Button(self.frame1, text="Afraid", width=3, command=lambda: self.on_save_pressed(True, 'basil-afraid', self.emotion_label_basil)).pack(side='left', padx=5)
        #Button(self.frame2, text="Stressed Out", width=3, font=('Arial', 8), command=lambda: self.on_save_pressed(True, 'basil-stressedout', self.emotion_label_basil)).pack(side='left', padx=5)
        
        self.gif_path = 'basil/basil-dw-neutral.gif'
        self.first_load = True
        self.i = 0
        self.current_screen = self.basil_screen
        #self.load_gif()
        self.selected_emotion = 'basil-neutral'
        self.inputted_top_text = ''
        self.inputted_bottom_text = ''
        #self.master.after(100, self.on_save_pressed, True, self.selected_emotion)
        Button(self.basil_screen, text="Back", width=3, command=lambda: self.show_screen(self.title_screen)).place(relx=0, rely=0)


    def init_sunny_screen(self):
        #self.gif_label.pack(expand=True)

        self.top_text_input = Label(self.sunny_screen, text='Top Text:')
        self.top_text_input.pack()
        self.top_text_input_box5 = Entry(self.sunny_screen)
        self.top_text_input_box5.pack()

        self.bottom_text_input = Label(self.sunny_screen, text='Bottom Text:')
        self.bottom_text_input.pack()
        self.bottom_text_input_box5 = Entry(self.sunny_screen)
        self.bottom_text_input_box5.pack()

        Button(self.sunny_screen, text="Save", width=3, command=lambda: self.on_save_pressed(topt=self.top_text_input_box5.get(), bottomt=self.bottom_text_input_box5.get())).pack()

        self.emotion_label_sunny = Label(self.sunny_screen, text='neutral')
        self.emotion_label_sunny.pack()

        self.frame1 = Frame(self.sunny_screen)

        self.frame1.pack()

        Button(self.frame1, text="Neutral", width=3, command=lambda: self.on_save_pressed(True, 'sunny-neutral', self.emotion_label_sunny)).pack(side='left', padx=5)
        Button(self.frame1, text="Angry", width=3, command=lambda: self.on_save_pressed(True, 'sunny-angry', self.emotion_label_sunny)).pack(side='left', padx=5)
        Button(self.frame1, text="Stabbed", width=3, command=lambda: self.on_save_pressed(True, 'sunny-stabbed', self.emotion_label_sunny)).pack(side='left', padx=5)
        Button(self.frame1, text="Afraid", width=3, command=lambda: self.on_save_pressed(True, 'omori-afraid', self.emotion_label_sunny)).pack(side='left', padx=5)
        Button(self.frame1, text="Stressed Out", width=3, font=('Arial', 8), command=lambda: self.on_save_pressed(True, 'omori-stressedout', self.emotion_label_sunny)).pack(side='left', padx=5)

        self.gif_path = 'sunny/sunny-dw-neutral.gif'
        self.first_load = True
        self.i = 0
        self.current_screen = self.sunny_screen
        #self.load_gif()
        self.selected_emotion = 'sunny-neutral'
        self.inputted_top_text = ''
        self.inputted_bottom_text = ''
        #self.master.after(100, self.on_save_pressed, True, self.selected_emotion)
        Button(self.sunny_screen, text="Back", width=3, command=lambda: self.show_screen(self.omori_screen)).place(relx=0, rely=0)


    def init_rw_aubrey_screen(self):
        #self.gif_label.pack(expand=True)

        self.top_text_input = Label(self.rw_aubrey_screen, text='Top Text:')
        self.top_text_input.pack()
        self.top_text_input_box6 = Entry(self.rw_aubrey_screen)
        self.top_text_input_box6.pack()

        self.bottom_text_input = Label(self.rw_aubrey_screen, text='Bottom Text:')
        self.bottom_text_input.pack()
        self.bottom_text_input_box6 = Entry(self.rw_aubrey_screen)
        self.bottom_text_input_box6.pack()

        Button(self.rw_aubrey_screen, text="Save", width=3, command=lambda: self.on_save_pressed(topt=self.top_text_input_box6.get(), bottomt=self.bottom_text_input_box6.get())).pack()

        self.emotion_label_aubrey = Label(self.rw_aubrey_screen, text='neutral')
        self.emotion_label_aubrey.pack()

        self.frame1 = Frame(self.rw_aubrey_screen)
        self.frame2 = Frame(self.rw_aubrey_screen)

        self.frame1.pack()
        self.frame2.pack()

        Button(self.frame1, text="Neutral", width=3, command=lambda: self.on_save_pressed(True, 'aubrey-neutralrw', self.emotion_label_aubrey)).pack(side='left', padx=5)
        Button(self.frame1, text="Happy", width=3, command=lambda: self.on_save_pressed(True, 'aubrey-happyrw', self.emotion_label_aubrey)).pack(side='left', padx=5)
        Button(self.frame1, text="Sad", width=3, command=lambda: self.on_save_pressed(True, 'aubrey-sadrw', self.emotion_label_aubrey)).pack(side='left', padx=5)
        Button(self.frame1, text="Depressed", width=3, font=('Arial', 8), command=lambda: self.on_save_pressed(True, 'aubrey-depressedrw', self.emotion_label_aubrey)).pack(side='left', padx=5)
        Button(self.frame1, text="Angry", width=3, command=lambda: self.on_save_pressed(True, 'aubrey-angryrw', self.emotion_label_aubrey)).pack(side='left', padx=5)
        Button(self.frame1, text="Afraid", width=3, command=lambda: self.on_save_pressed(True, 'aubrey-afraidrw', self.emotion_label_aubrey)).pack(side='left', padx=5)

        self.gif_path = 'aubrey/aubrey-dw-neutralrw.gif'
        self.first_load = True
        self.i = 0
        self.current_screen = self.rw_aubrey_screen
        #self.load_gif()
        self.selected_emotion = 'aubrey-neutralrw'
        self.inputted_top_text = ''
        self.inputted_bottom_text = ''
        #self.master.after(100, self.on_save_pressed, True, self.selected_emotion)
        Button(self.rw_aubrey_screen, text="Back", width=3, command=lambda: self.show_screen(self.aubrey_screen)).place(relx=0, rely=0)


    def init_rw_kel_screen(self):
        #self.gif_label.pack(expand=True)

        self.top_text_input = Label(self.rw_kel_screen, text='Top Text:')
        self.top_text_input.pack()
        self.top_text_input_box7 = Entry(self.rw_kel_screen)
        self.top_text_input_box7.pack()

        self.bottom_text_input = Label(self.rw_kel_screen, text='Bottom Text:')
        self.bottom_text_input.pack()
        self.bottom_text_input_box7 = Entry(self.rw_kel_screen)
        self.bottom_text_input_box7.pack()

        Button(self.rw_kel_screen, text="Save", width=3, command=lambda: self.on_save_pressed(topt=self.top_text_input_box7.get(), bottomt=self.bottom_text_input_box7.get())).pack()

        self.emotion_label_kel = Label(self.rw_kel_screen, text='neutral')
        self.emotion_label_kel.pack()

        self.frame1 = Frame(self.rw_kel_screen)
        self.frame2 = Frame(self.rw_kel_screen)

        self.frame1.pack()
        self.frame2.pack()

        Button(self.frame1, text="Neutral", width=3, command=lambda: self.on_save_pressed(True, 'kel-neutralrw', self.emotion_label_kel)).pack(side='left', padx=5)
        Button(self.frame1, text="Neutral 2", width=3, command=lambda: self.on_save_pressed(True, 'kel-neutral2rw', self.emotion_label_kel)).pack(side='left', padx=5)
        Button(self.frame1, text="Happy", width=3, command=lambda: self.on_save_pressed(True, 'kel-happyrw', self.emotion_label_kel)).pack(side='left', padx=5)
        Button(self.frame1, text="Ecstatic", width=3, command=lambda: self.on_save_pressed(True, 'kel-ecstaticrw', self.emotion_label_kel)).pack(side='left', padx=5)
        Button(self.frame1, text="Sad", width=3, command=lambda: self.on_save_pressed(True, 'kel-sadrw', self.emotion_label_kel)).pack(side='left', padx=5)
        Button(self.frame1, text="Angry", width=3, command=lambda: self.on_save_pressed(True, 'kel-angryrw', self.emotion_label_kel)).pack(side='left', padx=5)
        Button(self.frame1, text="Enraged", width=3, command=lambda: self.on_save_pressed(True, 'kel-enragedrw', self.emotion_label_kel)).pack(side='left', padx=5)
        Button(self.frame1, text="Afraid", width=3, command=lambda: self.on_save_pressed(True, 'kel-afraidrw', self.emotion_label_kel)).pack(side='left', padx=5)

        self.gif_path = 'kel/kel-dw-neutralrw.gif'
        self.first_load = True
        self.i = 0
        self.current_screen = self.rw_kel_screen
        self.load_gif()
        self.selected_emotion = 'kel-neutralrw'
        self.inputted_top_text = ''
        self.inputted_bottom_text = ''
        #self.master.after(100, self.on_save_pressed, True, self.selected_emotion)
        Button(self.rw_kel_screen, text="Back", width=3, command=lambda: self.show_screen(self.kel_screen)).place(relx=0, rely=0)


    def get_top_text(self, character):
        char_name = character.split('-')[0]
        if char_name == 'aubrey':
            return


    def mimic_double_press(self, is_default=False, emotion=''):
        if not is_default:
            #print(self.top_text_input_box.get())
            add_text_to_gif(self.select_gif(self.selected_emotion), output_file_path, self.inputted_top_text, self.inputted_bottom_text)
            #time.sleep(1)
            self.change_gif()
            #self.master.after(1000, self.change_gif)
            #print('ah')
        elif emotion != '':
            self.change_gif(self.select_gif(emotion))


    def on_save_pressed(self, is_default=False, emotion='', the_label=None, topt='', bottomt=''):
        #print(self.top_text_input_box.get())
        #add_text_to_gif('omori-kel-omori.gif', 'output.gif', self.top_text_input_box.get(), self.bottom_text_input_box.get())
        #time.sleep(1)
        if the_label is not None:
            the_label.configure(text=emotion.split('-')[1].replace('rw', ''))
        self.inputted_top_text = topt
        self.inputted_bottom_text = bottomt
        if not is_default:
            self.change_gif()
            self.master.after(100, self.mimic_double_press)
        elif emotion != '':
            self.selected_emotion = emotion
            self.change_gif(self.select_gif(emotion))
            self.master.after(100, self.mimic_double_press, True, emotion)


    def select_gif(self, emotion):
        e_split = emotion.split('-')
        return e_split[0] + '/' + e_split[0] + '-dw-' + e_split[1] + '.gif'


    def load_gif(self):
        #if hasattr(self, 'gif_label') and self.gif_label.winfo_exists():
            #self.gif_label.destroy()
        
        self.stop_gif = False
        
        if not self.first_load:
            self.master.after_cancel(self.play_gif)
            self.gif_label.destroy()
            self.stop_gif = True
            self.i += 1
            #print(self.i)
            
            #time.sleep(2)
            #del self.gif_frames[:]
            #self.dream_world_aubrey_screen.pack_forget()
            #self.init_dream_world_aubrey_screen('omori-kel-omori.gif')
            #self.show_screen(self.dream_world_aubrey_screen)
            #time.sleep(1)
            #print("WOWWWW")

        self.first_load = False

        gif = Image.open(resource_path(self.gif_path))
        #print(gif.n_frames)
        gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]
        # Create a label to display the GIF
        #self.gif_label.configure(image=gif_frames[0])
        self.gif_label = Label(self.current_screen, image=gif_frames[0])
        self.gif_label.pack()

        #self.stop_gif = False
        #time.sleep(1)
        #self.i = 2
        #print(self.i)
        if self.i == 2:
            self.stop_gif = False
            self.i = 0
        else:
            #self.load_gif()
            pass
        
        # Start playing the GIF
        self.play_gif(1, gif_frames)

    def play_gif(self, frame_index, gif_frames):
        #print(self.stop_gif)
        if self.stop_gif:
            #print("STOPPING GIF")
            return
        # Update the label with the current frame
        self.gif_label.configure(image=gif_frames[frame_index])

        # Move to the next frame after a delay (adjust the delay as needed)
        next_frame_index = (frame_index + 1) % len(gif_frames)
        self.master.after(100, lambda: self.play_gif(next_frame_index, gif_frames))

    
    def change_gif(self, new_path=output_file_path):
        # Change the GIF path and reload the new GIF
        self.gif_path = new_path
        self.load_gif()


    def show_screen(self, screen, emotion=''):
        # hide all screens
        self.title_screen.pack_forget()
        self.omori_screen.pack_forget()
        self.aubrey_screen.pack_forget()
        self.kel_screen.pack_forget()
        self.basil_screen.pack_forget()
        self.dream_world_aubrey_screen.pack_forget()
        self.dream_world_omori_screen.pack_forget()
        self.dream_world_kel_screen.pack_forget()
        self.sunny_screen.pack_forget()
        self.rw_aubrey_screen.pack_forget()
        self.rw_kel_screen.pack_forget()

        self.current_screen = screen
        self.on_save_pressed(True, emotion)

        # Show the selected screen
        screen.pack(expand=True, fill=tk.BOTH)


def quit_application(event, the_root):
    the_root.destroy()


def main():
    root = Tk()
    app = OmoriGifCreator(root)
    root.bind('|', lambda event: quit_application(event, root))
    root.mainloop()

if __name__ == "__main__":
    main()
