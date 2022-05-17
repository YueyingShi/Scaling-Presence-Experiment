

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import csv

root = Tk()
root.title("Pitroom Survey")
root.geometry("700x800")

# Create A Main Frame
main_frame = ttk.Frame(root)
main_frame.pack(fill=BOTH, expand=1, pady=30)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(
    main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
    scrollregion=my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
second_frame = ttk.Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# title
title_label = ttk.Label(
    second_frame, text="Presence Questionnaire -- Pit Environment")
title_label.pack(padx=10, pady=10)

## ----------------------------------##
# Page frame
## ----------------------------------##

frame_info = ttk.LabelFrame(
    second_frame, text="Demograph Data", padding=(20, 10))
frame_info.pack(padx=20, pady=10, fill='both')

frame_survey = ttk.LabelFrame(
    second_frame, text="Rasch-based Presence Survey", padding=(20, 10))
frame_survey.pack(padx=20, pady=10,  fill='both')

frame_ipq = ttk.LabelFrame(
    second_frame, text="IPQ Presence Survey", padding=(20, 10))
frame_ipq.pack(padx=20, pady=10,  fill='both')


## ----------------------------------##
# Demograph
## ----------------------------------##


# entry for id
id_label = ttk.Label(frame_info, text="ParticipantID: ", width=10)
id_label.grid(row=0, column=0, sticky=W)
id_field = ttk.Entry(frame_info, width=20)
id_field.grid(row=0, column=1, columnspan=3, sticky=W)

# entry for Age
age_label = ttk.Label(frame_info, text="Age: ", width=10)
age_label.grid(row=1, column=0, sticky=W)
age_field = ttk.Entry(frame_info, width=20)
age_field.grid(row=1, column=1, columnspan=3, sticky=W)

# entry for Gender
gender_label = ttk.Label(frame_info, text="Gender: ")
gender_label.grid(row=2, column=0, sticky=W)
Genders = [
    ("Female", "female"),
    ("Male", "male"),
    ("Non-binary", "non-binary"),
    ("Perfer not to respond", "no-respond")
]
gender_radio = StringVar()
i = 1
for text, gender in Genders:
    ttk.Radiobutton(frame_info, text=text, value=gender,
                    variable=gender_radio).grid(row=2, column=i, sticky=W)
    i += 1


## ----------------------------------##
# Questionnaire
## ----------------------------------##
# yes_label = ttk.Label(frame_survey,text="Yes",width=5).grid(row=0,column=2)
# no_label = ttk.Label(frame_survey,text="No",width=5).grid(row=0,column=3)
# if pack, than alignmnet use anchor
radio_1 = IntVar()
radio_2 = IntVar()
radio_3 = IntVar()
radio_4 = IntVar()
radio_5 = IntVar()
radio_6 = IntVar()
radio_7 = IntVar()
radio_8 = IntVar()
radio_9 = IntVar()
radio_10 = IntVar()
radio_11 = IntVar()
radio_12 = IntVar()
radio_13 = IntVar()
radio_14 = IntVar()
radio_15 = IntVar()
radio_16 = IntVar()

PitRadios = [radio_1, radio_2, radio_3, radio_4, radio_5, radio_6, radio_7, radio_8, radio_9, radio_10,
          radio_11, radio_12, radio_13, radio_14, radio_15, radio_16]
# label
j = 1
for radio in PitRadios:
    label = ttk.Label(frame_survey, text=str(j)+".",
                      width=2).grid(row=j, column=0, sticky=N, pady=10)

    ttk.Radiobutton(frame_survey, text="Yes", value=1,
                    variable=radio, width=4).grid(row=j, column=2, sticky=N, pady=10)
    ttk.Radiobutton(frame_survey, text="No", value=0,
                    variable=radio, width=4).grid(row=j, column=3, sticky=N, pady=10)
    radio.set(None),
    j += 1


# Question 1
# lable_1 = ttk.Label(frame_survey, text="1.", width=2).grid(
#     row=1, column=0, sticky=N)
ttk.Label(frame_survey,
    text="At several moments during the session, I had the feeling that I could have extended my arm to touch the objects in the virtual environment. ",
    wraplength=450,
    width=52).grid(row=1, column=1, pady=10)


# Question 2
ttk.Label(frame_survey,
    text="I constantly had the feeling that the objects I saw were situated in that specific location in the real world around me.",
    wraplength=450,
    width=52).grid(row=2, column=1, pady=10)


# Question 3
ttk.Label(frame_survey,
    text="At several moments during the session, I forgot that I was in a simulation. ",
    wraplength=450,
    width=52).grid(row=3, column=1, pady=10)

# Question 4
ttk.Label(frame_survey,
    text="There were moments during the session in which I forgot I was wearing the head-mounted display.",
    wraplength=450,
    width=52).grid(row=4, column=1, pady=10)

# Question 5
ttk.Label(frame_survey,
    text="At several moments, I had a sense of walking in the virtual environment rather than using the controllers in my hands. ",
    wraplength=450,
    width=52).grid(row=5, column=1, pady=10)

# Question 6
ttk.Label(frame_survey,
    text="I was constantly sure that the environment was real and not a simulation. ",
    wraplength=450,
    width=52).grid(row=6, column=1, pady=10)

# Question 7
ttk.Label(frame_survey,
    text="At several moments during the session, I felt like I can bump into the objects in VE.",
    wraplength=450,
    width=52).grid(row=7, column=1, pady=10)

# Question 8
ttk.Label(frame_survey,
    text="At several moments I found myself walking around objects to avoid bumping into them. ",
    wraplength=450,
    width=52).grid(row=8, column=1, pady=10)

# Question 9
ttk.Label(frame_survey,
    text="I had the feeling that I needed to bend as not to bump my head against the doorpost.",
    wraplength=450,
    width=52).grid(row=9, column=1, pady=10)

# Question 10
ttk.Label(frame_survey,
    text="I was sure that I could hurt my head against the small doorpost. ",
    wraplength=450,
    width=52).grid(row=10, column=1, pady=10)

# Question 11
ttk.Label(frame_survey,
    text="I hesitated when I was asked to open the grid to fall into the pit. ",
    wraplength=450,
    width=52).grid(row=11, column=1, pady=10)

# Question 12
ttk.Label(frame_survey,
    text="When looking into the pit, I briefly had the thought that I could really fall. ",
    wraplength=450,
    width=52).grid(row=12, column=1, pady=10)

# Question 13
ttk.Label(frame_survey,
    text="I felt a bodily reaction when looking down to the bottom of the pit.",
    wraplength=450,
    width=52).grid(row=13, column=1, pady=10)

# Question 14
ttk.Label(frame_survey,
    text="I felt somehow uncomfortable when looking down to the bottom of the pit. ",
    wraplength=450,
    width=52).grid(row=14, column=1, pady=10)

# Question 15
ttk.Label(frame_survey,
    text="After the grate opened, it really felt as if I was falling.",
    wraplength=450,
    width=52).grid(row=15, column=1, pady=10)

# Question 16
ttk.Label(frame_survey,
    text="I felt a bodily reaction when hitting the bottom of the pit. ",
    wraplength=450,
    width=52).grid(row=16, column=1, pady=10)

## ----------------------------------##
# frame ipq
## ----------------------------------##

ipq_radio_1 = IntVar()
ipq_radio_2 = IntVar()
ipq_radio_3 = IntVar()
ipq_radio_4 = IntVar()
ipq_radio_5 = IntVar()
ipq_radio_6 = IntVar()
ipq_radio_7 = IntVar()
ipq_radio_8 = IntVar()
ipq_radio_9 = IntVar()
ipq_radio_10 = IntVar()
ipq_radio_11 = IntVar()
ipq_radio_12 = IntVar()
ipq_radio_13 = IntVar()
ipq_radio_14 = IntVar()

ipq_frame_1 = ttk.Frame(frame_ipq)
ipq_frame_2 = ttk.Frame(frame_ipq)
ipq_frame_3 = ttk.Frame(frame_ipq)
ipq_frame_4 = ttk.Frame(frame_ipq)
ipq_frame_5 = ttk.Frame(frame_ipq)
ipq_frame_6 = ttk.Frame(frame_ipq)
ipq_frame_7 = ttk.Frame(frame_ipq)
ipq_frame_8 = ttk.Frame(frame_ipq)
ipq_frame_9 = ttk.Frame(frame_ipq)
ipq_frame_10 = ttk.Frame(frame_ipq)
ipq_frame_11 = ttk.Frame(frame_ipq)
ipq_frame_12 = ttk.Frame(frame_ipq)
ipq_frame_13 = ttk.Frame(frame_ipq)
ipq_frame_14 = ttk.Frame(frame_ipq)

IPQRadios = [
    (ipq_radio_1,ipq_frame_1),
    (ipq_radio_2,ipq_frame_2),
    (ipq_radio_3,ipq_frame_3),
    (ipq_radio_4,ipq_frame_4),
    (ipq_radio_5,ipq_frame_5),
    (ipq_radio_6,ipq_frame_6),
    (ipq_radio_7,ipq_frame_7),
    (ipq_radio_8,ipq_frame_8),
    (ipq_radio_9,ipq_frame_9),
    (ipq_radio_10,ipq_frame_10),
    (ipq_radio_11,ipq_frame_11),
    (ipq_radio_12,ipq_frame_12),
    (ipq_radio_13,ipq_frame_13),
    (ipq_radio_14,ipq_frame_14)
    ]




Scores = [
    ("-3", -3),
    ("-2", -2),
    ("-1", -1),
    ("0", 0),
    ("+1", +1),
    ("+2", +2),
    ("+3", +3)
]

# question 1
ttk.Label(frame_ipq,
    text="How aware were you of the real world surrounding while navigating in the virtual world? (i.e. sounds, room temperature, other people, etc.)? ",
    wraplength=450,
    width=52).grid(row=1, column=1,columnspan=3)
ttk.Label(frame_ipq, text="extremely aware").grid(row=2, column=1,sticky=W)
ttk.Label(frame_ipq, text="extremely aware").grid(row=2, column=2)
ttk.Label(frame_ipq, text="extremely aware").grid(row=2, column=3,sticky=E)


# question 2
ttk.Label(frame_ipq,
    text="I was constantly sure that the environment was real and not a simulation. ",
    wraplength=450,
    width=52).grid(row=4, column=1,columnspan=3)
ttk.Label(frame_ipq, text="extremely aware").grid(row=5, column=1,sticky=W)
ttk.Label(frame_ipq, text="extremely aware").grid(row=5, column=2)
ttk.Label(frame_ipq, text="extremely aware").grid(row=5, column=3,sticky=E)

# question 3
ttk.Label(frame_ipq,
    text="I was constantly sure that the environment was real and not a simulation. ",
    wraplength=450,
    width=52).grid(row=7, column=1,columnspan=3)
ttk.Label(frame_ipq, text="extremely aware").grid(row=8, column=1,sticky=W)
ttk.Label(frame_ipq, text="extremely aware").grid(row=8, column=2)
ttk.Label(frame_ipq, text="extremely aware").grid(row=8, column=3,sticky=E)


# question 4
ttk.Label(frame_ipq,
    text="I was constantly sure that the environment was real and not a simulation. ",
    wraplength=450,
    width=52).grid(row=10, column=1,columnspan=3)
ttk.Label(frame_ipq, text="extremely aware").grid(row=11, column=1,sticky=W)
ttk.Label(frame_ipq, text="extremely aware").grid(row=11, column=2)
ttk.Label(frame_ipq, text="extremely aware").grid(row=11, column=3,sticky=E)


# question 5
ttk.Label(frame_ipq,
    text="I was constantly sure that the environment was real and not a simulation. ",
    wraplength=450,
    width=52).grid(row=13, column=1,columnspan=3)
ttk.Label(frame_ipq, text="extremely aware").grid(row=14, column=1,sticky=W)
ttk.Label(frame_ipq, text="extremely aware").grid(row=14, column=2)
ttk.Label(frame_ipq, text="extremely aware").grid(row=14, column=3,sticky=E)


# question 6
ttk.Label(frame_ipq,
    text="I was constantly sure that the environment was real and not a simulation. ",
    wraplength=450,
    width=52).grid(row=16, column=1,columnspan=3)
ttk.Label(frame_ipq, text="extremely aware").grid(row=17, column=1,sticky=W)
ttk.Label(frame_ipq, text="extremely aware").grid(row=17, column=2)
ttk.Label(frame_ipq, text="extremely aware").grid(row=17, column=3,sticky=E)


# question 7
ttk.Label(frame_ipq,
    text="I was constantly sure that the environment was real and not a simulation. ",
    wraplength=450,
    width=52).grid(row=19, column=1,columnspan=3)
ttk.Label(frame_ipq, text="extremely aware").grid(row=20, column=1,sticky=W)
ttk.Label(frame_ipq, text="extremely aware").grid(row=20, column=2)
ttk.Label(frame_ipq, text="extremely aware").grid(row=20, column=3,sticky=E)


# question 8
ttk.Label(frame_ipq,
    text="I was constantly sure that the environment was real and not a simulation. ",
    wraplength=450,
    width=52).grid(row=22, column=1,columnspan=3)
ttk.Label(frame_ipq, text="extremely aware").grid(row=23, column=1,sticky=W)
ttk.Label(frame_ipq, text="extremely aware").grid(row=23, column=2)
ttk.Label(frame_ipq, text="extremely aware").grid(row=23, column=3,sticky=E)


# question 9
ttk.Label(frame_ipq,
    text="I was constantly sure that the environment was real and not a simulation. ",
    wraplength=450,
    width=52).grid(row=25, column=1,columnspan=3)
ttk.Label(frame_ipq, text="extremely aware").grid(row=26, column=1,sticky=W)
ttk.Label(frame_ipq, text="extremely aware").grid(row=26, column=2)
ttk.Label(frame_ipq, text="extremely aware").grid(row=26, column=3,sticky=E)


# question 10
ttk.Label(frame_ipq,
    text="I was constantly sure that the environment was real and not a simulation. ",
    wraplength=450,
    width=52).grid(row=28, column=1,columnspan=3)
ttk.Label(frame_ipq, text="extremely aware").grid(row=29, column=1,sticky=W)
ttk.Label(frame_ipq, text="extremely aware").grid(row=29, column=2)
ttk.Label(frame_ipq, text="extremely aware").grid(row=29, column=3,sticky=E)


# question 11
ttk.Label(frame_ipq,
    text="I was constantly sure that the environment was real and not a simulation. ",
    wraplength=450,
    width=52).grid(row=31, column=1,columnspan=3)
ttk.Label(frame_ipq, text="extremely aware").grid(row=32, column=1,sticky=W)
ttk.Label(frame_ipq, text="extremely aware").grid(row=32, column=2)
ttk.Label(frame_ipq, text="extremely aware").grid(row=32, column=3,sticky=E)


# question 12
ttk.Label(frame_ipq,
    text="I was constantly sure that the environment was real and not a simulation. ",
    wraplength=450,
    width=52).grid(row=34, column=1,columnspan=3)
ttk.Label(frame_ipq, text="extremely aware").grid(row=35, column=1,sticky=W)
ttk.Label(frame_ipq, text="extremely aware").grid(row=35, column=2)
ttk.Label(frame_ipq, text="extremely aware").grid(row=35, column=3,sticky=E)


# question 13
ttk.Label(frame_ipq,
    text="I was constantly sure that the environment was real and not a simulation. ",
    wraplength=450,
    width=52).grid(row=37, column=1,columnspan=3)
ttk.Label(frame_ipq, text="extremely aware").grid(row=38, column=1,sticky=W)
ttk.Label(frame_ipq, text="extremely aware").grid(row=38, column=2)
ttk.Label(frame_ipq, text="extremely aware").grid(row=38, column=3,sticky=E)


# question 14
ttk.Label(frame_ipq,
    text="I was constantly sure that the environment was real and not a simulation. ",
    wraplength=450,
    width=52).grid(row=40, column=1,columnspan=3)
ttk.Label(frame_ipq, text="extremely aware").grid(row=41, column=1,sticky=W)
ttk.Label(frame_ipq, text="extremely aware").grid(row=41, column=2)
ttk.Label(frame_ipq, text="extremely aware").grid(row=41, column=3,sticky=E)





k = 1
for radio,frame in IPQRadios:
    l = 0
    for text, score in Scores:
        ttk.Radiobutton(frame, text=text, value=score,
                        variable=radio, width=3).grid(row=0, column=l)
        l += 1
    ttk.Label(frame_ipq, text=str(k)+".").grid(row=3*k-2, column=0)
    frame.grid(row=3*k, column=1, columnspan=3,pady=10)
    radio.set(None),
    k += 1



## ----------------------------------##
# Submit event
## ----------------------------------##


def updatePitroomData():
    missingdata = 0
    # Getting the current date and time
    dt = datetime.now()
    with open('pitroom.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # reader = csv.reader(file)
        # lines= len(list(reader))
        # print("the last line in file is" +  lines)
        header = ["timestamp", "id", "age", "gender", "answer_1", "answer_2", "answer_3", "answer_4", "answer_5", "answer_6",
                  "answer_7", "answer_8", "answer_9", "answer_10", "answer_11", "answer_12", "answer_13", "answer_14", "answer_15", "answer_16"]

        data = [dt, id_field.get(), age_field.get(), gender_radio.get()]
        for radio in PitRadios:
            try:
                data.append(radio.get())
                print(data)
            except TclError as te:
                data.append(".")
                print("missing data" + str(radio))
                missingdata = 1
        writer.writerow(header)
        writer.writerow(data)

    if missingdata == 0:
        messagebox.showinfo("Submit", "Submit Successfully")
    else:
        messagebox.showwarning(
            "Error", "There are questions that have not been answered")


# def updateNightData():
#     missingdata = 0
#     # Getting the current date and time
#     dt = datetime.now()
#     with open('nightroad.csv', 'a', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         # reader = csv.reader(file)
#         # lines= len(list(reader))
#         # print("the last line in file is" +  lines)
#         header = ["timestamp", "id", "age", "gender", "answer_1", "answer_2", "answer_3", "answer_4", "answer_5", "answer_6",
#                   "answer_7", "answer_8", "answer_9", "answer_10", "answer_11", "answer_12", "answer_13", "answer_14", "answer_15", "answer_16"]

#         data = [dt, id_field.get(), age_field.get(), gender_radio.get()]
#         for radio in NightRadios:
#             try:
#                 data.append(radio.get())
#                 print(data)
#             except TclError as te:
#                 data.append(".")
#                 print("missing data" + str(radio))
#                 missingdata = 1
#         writer.writerow(header)
#         writer.writerow(data)

#     if missingdata == 0:
#         messagebox.showinfo("Submit", "Submit Successfully")
#     else:
#         messagebox.showwarning(
#             "Error", "There are questions that have not been answered")

def updateIPQData():
    missingdata = 0
    # Getting the current date and time
    dt = datetime.now()
    with open('ipq.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # reader = csv.reader(file)
        # lines= len(list(reader))
        # print("the last line in file is" +  lines)
        header = ["timestamp", "id", "age", "gender", "answer_1", "answer_2", "answer_3", "answer_4", "answer_5", "answer_6",
                  "answer_7", "answer_8", "answer_9", "answer_10", "answer_11", "answer_12", "answer_13", "answer_14"]

        data = [dt, id_field.get(), age_field.get(), gender_radio.get()]
        for radio in IPQRadios:
            try:
                data.append(radio.get())
                print(data)
            except TclError as te:
                data.append(".")
                print("missing data" + str(radio))
                missingdata = 1
        writer.writerow(header)
        writer.writerow(data)

    if missingdata == 0:
        messagebox.showinfo("Submit", "Submit Successfully")
    else:
        messagebox.showwarning(
            "Error", "There are questions that have not been answered")




saveButton = ttk.Button(
    frame_survey, text="Sumit This Part", command=updatePitroomData)
saveButton.grid(row=21, column=0, columnspan=3, pady=20)

saveButton2 = ttk.Button(
    frame_ipq, text="Sumit This Part", command=updateIPQData)
saveButton2.grid(row=43, column=1, columnspan=7, pady=20)
# data = []
# for radio in Radios:
#     if not radio.get():
#         data.append(3)
#         print(data)
#     else:
#         data.append(radio.get())
#         print(data)

root.mainloop()
