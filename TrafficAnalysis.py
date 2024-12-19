#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
import os
from PIL import Image, ImageTk

_location = os.path.dirname(__file__)

import TrafficAnalysis_support

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran: return        
    try: TrafficAnalysis_support.root.tk.call('source',
                os.path.join(_location, 'themes', 'default.tcl'))
    except: pass
    style = ttk.Style()
    style.theme_use('default')
    style.configure('.', font = "TkDefaultFont")
    if sys.platform == "win32":
       style.theme_use('winnative')    

    global _images
    _images = (
         tk.PhotoImage("img_close", data='''R0lGODlhDAAMAIQUADIyMjc3Nzk5OT09PT
                 8/P0JCQkVFRU1NTU5OTlFRUVZWVmBgYGF hYWlpaXt7e6CgoLm5ucLCwszMzNbW
                 1v//////////////////////////////////// ///////////yH5BAEKAB8ALA
                 AAAAAMAAwAAAUt4CeOZGmaA5mSyQCIwhCUSwEIxHHW+ fkxBgPiBDwshCWHQfc5
                  KkoNUtRHpYYAADs= '''),
         tk.PhotoImage("img_close_white", data='''R0lGODlhDAAMAPQfAM3NzcjI
                yMbGxsLCwsDAwL29vbq6urKysrGxsa6urqmpqZ+fn56enpaWloSEhF9fX0ZGR
                j09PTMzMykpKQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///yH
                5BAEKAB8ALAAAAAAMAAwAAAUt4CeOZGmaA5mSyQCIwhCUSwEIxHHW+fkxBgPi
                BDwshCWHQfc5KkoNUtRHpYYAADs='''),
         tk.PhotoImage("img_closeactive", data='''R0lGODlhDAAMAIQcALwuEtIzFL46
                 INY0Fdk2FsQ8IdhAI9pAIttCJNlKLtpLL9pMMMNTP cVTPdpZQOBbQd60rN+1rf
                 Czp+zLxPbMxPLX0vHY0/fY0/rm4vvx8Pvy8fzy8P//////// ///////yH5BAEK
                 AB8ALAAAAAAMAAwAAAVHYLQQZEkukWKuxEgg1EPCcilx24NcHGYWFhx P0zANBE
                 GOhhFYGSocTsax2imDOdNtiez9JszjpEg4EAaA5jlNUEASLFICEgIAOw== '''),
         tk.PhotoImage("img_closepressed", data='''R0lGODlhDAAMAIQeAJ8nD64qELE
                 rELMsEqIyG6cyG7U1HLY2HrY3HrhBKrlCK6pGM7lD LKtHM7pKNL5MNtiViNaon
                  +GqoNSyq9WzrNyyqtuzq+O0que/t+bIwubJw+vJw+vTz+zT z////////yH5BAE
                 KAB8ALAAAAAAMAAwAAAVJIMUMZEkylGKuwzgc0kPCcgl123NcHWYW Fs6Gp2mYB
                 IRgR7MIrAwVDifjWO2WwZzpxkxyfKVCpImMGAeIgQDgVLMHikmCRUpMQgA7 ''')
        )
    if _bgmode == "dark":
        style.element_create("close", "image", "img_close_white",
           ('active', 'pressed',  'img_closepressed'),
           ('active', 'alternate', 'img_closeactive'), border=8, sticky='')
    else:
        style.element_create("close", "image", "img_close",
           ('active', 'pressed',  'img_closepressed'),
           ('active', 'alternate', 'img_closeactive'), border=8, sticky='')

    style.layout("ClosetabNotebook", [("ClosetabNotebook.client",
                                 {"sticky": "nswe"})])
    style.layout("ClosetabNotebook.Tab", [
        ("ClosetabNotebook.tab",
          { "sticky": "nswe",
            "children": [
                ("ClosetabNotebook.padding", {
                    "side": "top",
                    "sticky": "nswe",
                    "children": [
                        ("ClosetabNotebook.focus", {
                            "side": "top",
                            "sticky": "nswe",
                            "children": [
                                ("ClosetabNotebook.label", {"side":
                                  "left", "sticky": ''}),
                                ("ClosetabNotebook.close", {"side":
                                    "left", "sticky": ''}),]})]})]})])

    style.map('ClosetabNotebook.Tab', background =
        [('selected', _bgcolor), ('active', _tabbg1),
        ('!active', _tabbg2)], foreground =
        [('selected', _fgcolor), ('active', _tabfg1), ('!active', _tabfg2)])
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("1280x783+782+658")
        top.minsize(1, 1)
        top.maxsize(3409, 1896)
        top.resizable(1,  1)
        top.title("交通流量分析系统")

        self.top = top
        self.combobox = tk.StringVar()
        self.selectedButton = tk.IntVar()

        _style_code()
        PNOTEBOOK="ClosetabNotebook"
        self.PNotebook1 = ttk.Notebook(self.top)
        self.PNotebook1.place(relx=0.016, rely=0.069, relheight=0.903
                , relwidth=0.97)
        self.PNotebook1.configure(style=PNOTEBOOK)
        self.PNotebook1_t1 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t1, padding=3)
        self.PNotebook1.tab(0, text='''类型识别''', compound="right"
                ,underline='''-1''', )
        self.PNotebook1_t2 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t2, padding=3)
        self.PNotebook1.tab(1, text='''流量统计''', compound="right"
                ,underline='''-1''', )
        self.Model_Result = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.Model_Result, padding=3)
        self.PNotebook1.tab(2, text='''模型效果''', compound="left"
                ,underline='''-1''', )

        self.Frame1_1 = tk.Frame(self.PNotebook1_t1)
        self.Frame1_1.place(relx=0.887, rely=0.017, relheight=0.967
                , relwidth=0.1)
        self.Frame1_1.configure(relief='groove')
        self.Frame1_1.configure(borderwidth="2")
        self.Frame1_1.configure(relief="groove")

        self.ChooseDir = tk.Button(self.Frame1_1)
        self.ChooseDir.place(relx=0.081, rely=0.017, height=35, width=110)
        self.ChooseDir.configure(activebackground="#d9d9d9")
        self.ChooseDir.configure(font="-family {Noto Sans CJK SC} -size 7")
        self.ChooseDir.configure(text='''选择文件夹''')

        self.PreviousPic = tk.Button(self.Frame1_1)
        self.PreviousPic.place(relx=0.081, rely=0.082, height=35, width=110)
        self.PreviousPic.configure(activebackground="#d9d9d9")
        self.PreviousPic.configure(font="-family {Noto Sans CJK SC} -size 7")
        self.PreviousPic.configure(text='''上一张''')

        self.RecgnizeLabel = tk.Button(self.Frame1_1)
        self.RecgnizeLabel.place(relx=0.081, rely=0.794, height=35, width=110)
        self.RecgnizeLabel.configure(activebackground="#d9d9d9")
        self.RecgnizeLabel.configure(font="-family {Noto Sans CJK SC} -size 7")
        self.RecgnizeLabel.configure(text='''识别''')

        self.SaveLabel = tk.Button(self.Frame1_1)
        self.SaveLabel.place(relx=0.081, rely=0.86, height=35, width=110)
        self.SaveLabel.configure(activebackground="#d9d9d9")
        self.SaveLabel.configure(font="-family {Noto Sans CJK SC} -size 7")
        self.SaveLabel.configure(text='''保存''')

        self.DeleteLabel = tk.Button(self.Frame1_1)
        self.DeleteLabel.place(relx=0.081, rely=0.925, height=35, width=110)
        self.DeleteLabel.configure(activebackground="#d9d9d9")
        self.DeleteLabel.configure(font="-family {Noto Sans CJK SC} -size 7")
        self.DeleteLabel.configure(text='''销毁''')

        self.NextPic = tk.Button(self.Frame1_1)
        self.NextPic.place(relx=0.081, rely=0.146, height=35, width=110)
        self.NextPic.configure(activebackground="#d9d9d9")
        self.NextPic.configure(font="-family {Noto Sans CJK SC} -size 7")
        self.NextPic.configure(text='''下一张''')

        self.PicList = ttk.Combobox(self.Frame1_1)
        self.PicList.place(relx=0.081, rely=0.223, relheight=0.548
                , relwidth=0.887)
        self.PicList.configure(font="-family {Noto Sans CJK SC} -size 10")
        self.PicList.configure(textvariable=self.combobox)

        self.Frame1_2 = tk.Frame(self.PNotebook1_t1)
        self.Frame1_2.place(relx=0.169, rely=0.017, relheight=0.967
                , relwidth=0.705)
        self.Frame1_2.configure(relief='groove')
        self.Frame1_2.configure(borderwidth="2")
        self.Frame1_2.configure(relief="groove")

        self.Canvas = tk.Canvas(self.Frame1_2)
        self.Canvas.place(relx=0.011, rely=0.016, relheight=0.961
                , relwidth=0.975)
        self.Canvas.configure(borderwidth="2")
        self.Canvas.configure(relief="ridge")
        self.Canvas.configure(selectbackground="#d9d9d9")

        self.Frame1 = tk.Frame(self.PNotebook1_t1)
        self.Frame1.place(relx=0.016, rely=0.032, relheight=0.967
                , relwidth=0.141)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")

        self.type_amount_label = tk.Label(self.Frame1)
        self.type_amount_label.place(relx=0.057, rely=0.016, height=47
                , width=150)
        self.type_amount_label.configure(activebackground="#d9d9d9")
        self.type_amount_label.configure(anchor='w')
        self.type_amount_label.configure(compound='left')
        self.type_amount_label.configure(font="-family {Noto Sans CJK SC} -size 10")
        self.type_amount_label.configure(text='''类型/数量''')

        self.type_amount_list = ScrolledText(self.Frame1)
        self.type_amount_list.place(relx=0.057, rely=0.082, relheight=0.684
                , relwidth=0.829)
        self.type_amount_list.configure(background="white")
        self.type_amount_list.configure(font="-family {Noto Sans CJK SC} -size 6")
        self.type_amount_list.configure(insertborderwidth="3")
        self.type_amount_list.configure(selectbackground="#d9d9d9")
        self.type_amount_list.configure(wrap="none")

        self.DayMode = tk.Radiobutton(self.Frame1)
        self.DayMode.place(relx=0.057, rely=0.765, relheight=0.058
                , relwidth=0.857)
        self.DayMode.configure(activebackground="#d9d9d9")
        self.DayMode.configure(anchor='w')
        self.DayMode.configure(compound='left')
        self.DayMode.configure(font="-family {Noto Sans CJK SC} -size 9")
        self.DayMode.configure(justify='left')
        self.DayMode.configure(text='''白天模式''')
        self.DayMode.configure(variable=self.selectedButton, value=0)

        self.NightMode = tk.Radiobutton(self.Frame1)
        self.NightMode.place(relx=0.057, rely=0.819, relheight=0.074
                , relwidth=0.857)
        self.NightMode.configure(activebackground="#d9d9d9")
        self.NightMode.configure(anchor='w')
        self.NightMode.configure(compound='left')
        self.NightMode.configure(font="-family {Noto Sans CJK SC} -size 9")
        self.NightMode.configure(justify='left')
        self.NightMode.configure(text='''夜间模式''')
        self.NightMode.configure(variable=self.selectedButton, value=1, command=self.toggle_night_mode)

        self.Canvas2 = tk.Canvas(self.PNotebook1_t2)
        self.Canvas2.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Canvas2.configure(borderwidth="2")
        self.Canvas2.configure(relief="ridge")
        self.Canvas2.configure(selectbackground="#d9d9d9")

        self.TNotebook1 = ttk.Notebook(self.Model_Result)
        self.TNotebook1.place(relx=0.008, rely=0.015, relheight=0.964
                , relwidth=0.986)
        self.R_curve_Tab = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.R_curve_Tab, padding=3)
        self.TNotebook1.tab(0, text='''R曲线''', compound="left", underline='''-1'''
                ,)
        self.P_curve_Tab = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.P_curve_Tab, padding=3)
        self.TNotebook1.tab(1, text='''P曲线''', compound="left", underline='''-1'''
                ,)
        self.PR_curve_Tabs = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.PR_curve_Tabs, padding=3)
        self.TNotebook1.tab(2, text='''PR曲线''', compound="left"
                ,underline='''-1''', )
        self.F1_curve_Tab = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.F1_curve_Tab, padding=3)
        self.TNotebook1.tab(3, text='''F1曲线''', compound="left"
                ,underline='''-1''', )

        self.R_curve = tk.Canvas(self.R_curve_Tab)
        self.R_curve.place(relx=0.008, rely=0.017, relheight=0.956
                , relwidth=0.984)
        self.R_curve.configure(borderwidth="2")
        self.R_curve.configure(cursor="fleur")
        self.R_curve.configure(relief="ridge")
        self.R_curve.configure(selectbackground="#d9d9d9")

        self.P_curve = tk.Canvas(self.P_curve_Tab)
        self.P_curve.place(relx=0.008, rely=0.017, relheight=0.956
                , relwidth=0.984)
        self.P_curve.configure(borderwidth="2")
        self.P_curve.configure(relief="ridge")
        self.P_curve.configure(selectbackground="#d9d9d9")

        self.PR_curve = tk.Canvas(self.PR_curve_Tabs)
        self.PR_curve.place(relx=0.008, rely=0.017, relheight=0.956
                , relwidth=0.984)
        self.PR_curve.configure(borderwidth="2")
        self.PR_curve.configure(relief="ridge")
        self.PR_curve.configure(selectbackground="#d9d9d9")

        self.F1_curve = tk.Canvas(self.F1_curve_Tab)
        self.F1_curve.place(relx=0.008, rely=0.017, relheight=0.956
                , relwidth=0.983)
        self.F1_curve.configure(borderwidth="2")
        self.F1_curve.configure(relief="ridge")
        self.F1_curve.configure(selectbackground="#d9d9d9")
        self.PNotebook1.bind('<Button-1>',_button_press)
        self.PNotebook1.bind('<ButtonRelease-1>',_button_release)
        self.PNotebook1.bind('<Motion>',_mouse_over)

        # 根据选择的模式（白天模式或夜间模式）动态加载不同的曲线图像到Canvas中
        self.DayMode.configure(command=self.load_curves)
        self.NightMode.configure(command=self.load_curves)

        # Initialize the curves with default images
        self.load_curves()

    def load_curves(self):
        mode = "A" if self.selectedButton.get() == 0 else "B"
        base_path = f"./runs/train{mode}"

        self.load_image(self.R_curve, os.path.join(base_path, "R_curve.png"))
        self.load_image(self.P_curve, os.path.join(base_path, "P_curve.png"))
        self.load_image(self.PR_curve, os.path.join(base_path, "PR_curve.png"))
        self.load_image(self.F1_curve, os.path.join(base_path, "F1_curve.png"))

    def load_image(self, canvas, image_path):
        if os.path.exists(image_path):
            img = Image.open(image_path)
            # 使用 Image.Resampling.LANCZOS 替代 Image.ANTIALIAS
            img.thumbnail((canvas.winfo_width(), 550), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            canvas.image = photo  # 保持对图像的引用，避免被垃圾回收
        else:
            canvas.delete("all")  # 清除画布内容
            print(f"Image not found: {image_path}")

    def toggle_night_mode(self):
        if self.selectedButton.get() == 1:
            self.DayMode.deselect()  # 手动取消白天模式的选中状态
        self.load_curves()  # Reload the curves based on the selected mode

    def toggle_night_mode(self):
        if self.selectedButton.get() == 1:
            self.DayMode.deselect()  # 手动取消白天模式的选中状态

# The following code is add to handle mouse events with the close icons
# in PNotebooks widgets.
def _button_press(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        index = widget.index("@%d,%d" % (event.x, event.y))
        widget.state(['pressed'])
        widget._active = index

def _button_release(event):
    widget = event.widget
    if not widget.instate(['pressed']):
            return
    element = widget.identify(event.x, event.y)
    try:
        index = widget.index("@%d,%d" % (event.x, event.y))
    except tk.TclError:
        pass
    if "close" in element and widget._active == index:
        widget.forget(index)
        widget.event_generate("<<NotebookTabClosed>>")

    widget.state(['!pressed'])
    widget._active = None

def _mouse_over(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        widget.state(['alternate'])
    else:
        widget.state(['!alternate'])

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')
def start_up():
    TrafficAnalysis_support.main()

if __name__ == '__main__':
    TrafficAnalysis_support.main()