'''This Is A Program To Analyse The Character Of The User (Optimism/Pessimism)
And Display The Output To The User'''

#### Made By :
#### Archit Garg - 72508
#### Vedant Kohli - 72454
#### Yatharth Aggrawal - 72511

from random import*
from string import *
from swampy.Gui import*
from Tkinter import*
import tkMessageBox
import re
import os
from time import *
import Image
import ImageTk


######****************************DEFINITIONS******************************########
#################### OF CLASS AND FUNCTIONS OF THE TOKENIZER ######################
regex_strings = (
    # Emoticons:
    r"""
    (?:
      [<>]?
      [:;=8]                     # eyes
      [\-o\*\']?                 # optional nose
      [\)\]\(\[dDpP/\:\}\{@\|\\] # mouth      
      |
      [\)\]\(\[dDpP/\:\}\{@\|\\] # mouth
      [\-o\*\']?                 # optional nose
      [:;=8]                     # eyes
      [<>]?
    )"""
    ,
    # Remaining word types:
    r"""
    (?:[a-z][a-z'\-_]+[a-z])       # Words with apostrophes or dashes.
    |
    (?:[+\-]?\d+[,/.:-]\d+[+\-]?)  # Numbers, including fractions, decimals.
    |
    (?:[\w_]+)                     # Words without apostrophes or dashes.
    |
    (?:\.(?:\s*\.){1,})            # Ellipsis dots. 
    |
    (?:\S)                         # Everything else that isn't #00ffffspace.
    """
    )

word_re = re.compile(r"""(%s)""" % "|".join(regex_strings), re.VERBOSE | re.I | re.UNICODE)

emoticon_re = re.compile(regex_strings[1], re.VERBOSE | re.I | re.UNICODE)

class Tokenizer:
    def __init__(self, preserve_case=False):
        self.preserve_case = preserve_case

    def tokenize(self, s):
        # Try to ensure unicode:
        try:
            s = unicode(s)
        except DecodeError:
            s = str(s).encode('string_escape')
            s = unicode(s)
        # Tokenize:
        words = word_re.findall(s)
        return words

tok = Tokenizer(preserve_case=False)

#######****************************TOKENIZER****************************#######
#######************************* CREATION DONE *************************#######
a=0
nword=''
nott=0
done=int
positive=0
negative=0
neutral=0
hopeful=0
neg_text=0
pos_text=0
pos_sp=0
neg_sp=0
neut_text=0
presuf=[]
nstemmed=''
t=1
s=1
q=1
x=-1
txt=[]
qp=[0,0,0,0,0,0,0]
qn=[0,0,0,0,0,0,0]
content1=[]
content2=[]



#########Accessing Data Base###########

file1=open('Positive.txt')
for line in file1:
    tex1=line.strip()
    content1=content1 + tex1.split()
file1.close()

file2=open('Negative.txt')
for line in file2:
    tex2=line.strip()
    content2=content2 + tex2.split()
file2.close()

########Finished Accessing##############


def output():
    ###Final Emotion From Text :
    ###Out Of 4 - both positive and negative###
    if pos_text>15:
        pos1=4
    elif pos_text>11:
        pos1=3
    elif pos_text>7:
        pos1=2
    elif pos_text>3:
        pos1=1
    else:
        pos1=0

    if neg_text>15:
        neg1=4
    elif neg_text>11:
        neg1=3
    elif neg_text>7:
        neg1=2
    elif neg_text>3:
        neg1=1
    else:
        neg1=0


    ###Final Emotion From Suffix Prefix Game :
    ###Out Of 2 - both positive and negative###
    if pos_sp>=3:
        pos2=2
    elif pos_sp>0:
        pos2=1
    elif pos_sp==0:
        pos2=0

    if neg_sp>=3:
        neg2=2
    elif neg_sp>0:
        neg2=1
    elif neg_sp==0:
        neg2=0


    ###Final Emotion From MCQ's :
    ###Out of 4 - both positive and negative###
    pos3=positive
    neg3=negative
 

    ###NET EMOTION###
    total_pos=pos1+pos2+pos3
    total_neg=neg1+neg2+neg3
    def exi(event=NONE):
        p.destroy()
    p.fr()
    image=Image.open('123.png')
    image2=ImageTk.PhotoImage(image)
    image3=Image.open('pic2.jpg')
    image4=ImageTk.PhotoImage(image3)
    canvas=p.ca(width=1400,height=1400,bg='#F6F6F6',bd=1)
    canvas.image([-300,400],image=image4)
    canvas.image=image4

    a=float(total_pos)                    #first variable\+ve
    b=float(total_neg)			  #second variable\-ve
    s1=(a/(a+b))*360
    s2=(b/(a+b))*360
    t1=float((a/(a+b))*100)
    t2=float((b/(a+b))*100)

    item0=canvas.create_arc([640,300,390,50],width=2,fill='blue',start=0,extent=s1,stipple='gray75',activewidth=4,activefill='red')
    item1=canvas.create_arc([640,300,390,50],width=2,fill='yellow',start=s1,extent=s2,stipple='gray75',activewidth=4,activefill='red')
    canvas.place(x=-1,y=-1)
    labp=p.la(text="%d +ve"%(t1),bg='light blue',font=(10)).place(x=630,y=70)
    labn=p.la(text="%d -ve"%(t2),bg='yellow',font=(10)).place(x=630,y=300)
    head=canvas.create_text(200,50,font=('BOOKMAN OLD STYLE',32, 'bold'),justify=LEFT,fill='red',text="So who are YOU?")
        
    item2=canvas.create_text(185, 180, width=360,  font=('BOOKMAN OLD STYLE',12),justify=LEFT,fill='black',text="It was great having you spend some time with us, trying to get to know more about yourself.The following result is based on your reactions and responses to various situations, which were presented before you, during the program...")
    if (a-b)>=7:
        item3=canvas.create_text(185, 360, width=360,  font=('BOOKMAN OLD STYLE',12),justify=LEFT,fill='black',text="According to the analysis, you are a 'There is always a bright side to things' kind of a person. You always believe in a morning after every night, that difficulties are a part of life, and are often, if not always, the sign of good things coming your way. You are a sympathetic and genteel person, and often like sharing your ideals with others.")
    if (a-b)>=4 and (a-b)<=6:
        item3=canvas.create_text(185, 360, width=360,  font=('BOOKMAN OLD STYLE',12),justify=LEFT,fill='black',text="According to the analysis, you are quite optimistic. Some call it being practical. You think of the positive side of things, but then, at the same time, you are aware that a darker side exists. You think with your brain, and often make sensible and practical decisions.")
    if (a-b)>=0 and (a-b)<=3:
        item3=canvas.create_text(185, 360, width=360,  font=('BOOKMAN OLD STYLE',12),justify=LEFT,fill='black',text="You are among the ones who think a lot before doing anything. You often find a perfect balance between the pros and cons of anything, yet the final decision you make is often inclined on the optimistic side of the story. You act sensibly most of the time, and are often good at making decisions.")
    if (a-b)>=-5 and (a-b)<=-1:
        item3=canvas.create_text(185, 360, width=360,  font=('BOOKMAN OLD STYLE',12),justify=LEFT,fill='black',text="You know that the glass is half empty, and it is also what you believe, but sometimes, you tend to divert from that mindset, and look at the brighter side of the story. Though you may often have a negative side of the scene in mind, but there is always a part of you, be it a teensy bit, that makes you see the sunrise after the dark night, the heart-touching music after the silence. However, there is still scope for improvement")
    if (a-b)<=-6:
        item3=canvas.create_text(185, 360, width=360,  font=('BOOKMAN OLD STYLE',12),justify=LEFT,fill='black',text="You have a mindset that things go wrong most of the times. There is always a 'What If' attached to the decisions you make, having in mind one or the other things that could potentially go wrong. You may have a positive side to your personality, but it is not often shown in front of people, and this is possibly the thing that needs to be worked upon. Remember, it\'s our way of thinking that creates good or bad outcomes.")
        
    exit1=p.bu(text="EXIT",command=p.destroy,bd=7, bg='red', fg='white', font=('bold', 15), activebackground='red', activeforeground='white').place(x=500,y=400,width=60,height=40)


    p.bind('<Return>',exi)


def nex(event=NONE):
        global done
        if q==5 or q==15 or q==10:
           pass
        elif q>5 and q<10:
            pass
        else:
            if done==0:
                if(var.get()==1 or var.get()==2 or var.get()==3):
                    but1=p.bu(text='Next',bd=7, bg='cyan', fg='#222222', font=('bold', 15), activebackground='#222222', activeforeground='cyan', command=nexts)
                    but1.place(x=450,y=400, height=40, width=60)
                    p.bind('<Return>',nexts)
                    done=1
                else:
                    tkMessageBox.showinfo("Error","Select an Option!!!")

def analyse(stri):
    global neg_text, pos_text, neut_text, nott
    tokenized=tok.tokenize(stri)
    for word in tokenized:
        words=str(word)
        if words=='not':
            nott=1
            continue

        if var2==1:
            found=0
            for i in content1:
                if words==i:
                    if nott==1:
                        neg_text+=2
                        nott=0
                        found=1
                    else:
                        pos_text+=1
                        found=1

            if found !=1:
                for i in content2:
                    if words==i:
                        if nott==1:
                            pos_text+=1
                            nott=0
                            found=1
                        else:
                            neg_text+=2
                            found=1

            if found!=1:
                neut_text+=1
                nott=0



        if var2==2:
            found=0
            for i in content1:
                if words==i:
                    if nott==1:
                        neg_text+=1
                        nott=0
                        found=1
                    else:
                        pos_text+=2
                        found=1

            if found !=1:
                for i in content2:
                    if words==i:
                        if nott==1:
                            pos_text+=2
                            nott=0
                            found=1
                        else:
                            neg_text+=1
                            found=1

            if found!=1:
                neut_text+=1
                nott=0


        if var2==2:
            found=0
            for i in content1:
                if words==i:
                    if nott==1:
                        neg_text+=1
                        nott=0
                        found=1
                    else:
                        pos_text+=1
                        found=1
            if found!=1:
                for i in content2:
                    if words==i:
                        if nott==1:
                            neg_text+=1
                            nott=0
                            found=1
                        else:
                            pos_text+=1
                            found=1

            if found!=1:
                neut_text+=1
                nott=0         
                      



def sentiment(c):
    if c==1:
        global positive
        positive+=1
    elif c==2:
        global negative
        negative+=1
    elif c==3:
        global neutral
        neutral+=1

def hope():
    global hopeful
    hopeful+=1


def ques_pic():
    global nstemmed
    x=randint(1,5)
    if x==1:
        image1=Image.open('Pic 1.jpg')
    elif x==2:
        image1=Image.open('Pic 2.jpg')
    elif x==3:
        image1=Image.open('Pic 3.jpg')
    elif x==4:
        image1=Image.open('Pic 4.jpg')
    elif x==5:
        image1=Image.open('Pic 5.jpg')

    imag=Image.open('pic4.jpg')
    imag2=ImageTk.PhotoImage(imag)
    can1=p.ca()
    can1.image([300,-200],image=imag2)
    can1.image=imag2
    
    photo1=ImageTk.PhotoImage(image1)
    can2=p.ca(width=250,height=186)
    can2.place(x=220,y=35)
    can2.image([0,0],image=photo1)
    can2.image=photo1

    
    
    def nexstemx(event=NONE):
        global done
        global nstemmed
        if q==5 or q==15 or q==10:
            nstemmed=text.get(0.0,END)
            if len(nstemmed)>10:
                but1=p.bu(text='Next',bd=7, bg='cyan', fg='#222222', font=('bold', 15), activebackground='#222222', activeforeground='cyan', command=nexts)
                but1.place(x=450,y=430, height=40, width=60) 
                p.bind('<Return>',nexts)
            else:
                tkMessageBox.showinfo("Error","Please Fill genuinely")
    text = p.te(width=45, height=5,font=('BOOKMAN OLD STYLE',15),fg='blue')
    ques=can1.create_text(355,275,font=('GEORGIA',15, 'bold'),justify=LEFT,fill='red',text="Describe picture in few lines")
    text.place(x=80,y=295)
    but3=p.bu("Submit", command=nexstemx,bd=7, bg='cyan', fg='#222222', font=('bold', 15), activebackground='#222222', activeforeground='cyan')
    but3.place(x=160,y=430,height=40, width=80)
    p.bind('<Return>',nexstemx)

def ques_text():
    global nstemmed
    x=randint(1,5)
    cn1=p.ca()
    imag=Image.open('pic4.jpg')
    imag2=ImageTk.PhotoImage(imag)
    cn1.image([300,-200],image=imag2)
    cn1.image=imag2
    
    if x==1:
        item=cn1.create_text(350, 70, width=600,  font=('GEORGIA',15, 'bold'),justify=LEFT,fill='red',text="Question: Are foreign channels a threat to our culture? Why?\n")
    elif x==2:
        item=cn1.create_text(350, 70, width=600,  font=('GEORGIA',15, 'bold'),justify=LEFT,fill='red',text="Question: Are parents demanding on their children?\n")
    elif x==3:
        item=cn1.create_text(350, 70, width=600,  font=('GEORGIA',15, 'bold'),justify=LEFT,fill='red',text="Question: Is the team responsible for the success while the captain for the failure?\n")
    elif x==4:
        item=cn1.create_text(350, 70, width=600,  font=('GEORGIA',15, 'bold'),justify=LEFT,fill='red',text="Question: Is the Indian Education System Good?\n")
    elif x==5:
        item=cn1.create_text(350, 70, width=600,  font=('GEORGIA',15, 'bold'),justify=LEFT,fill='red',text="\nQuestion: Your time is limited, don't waste it living for someone else.' Do You Agree?\n")
    rb1=p.rb(bg='#FFFFFF', font=('BOOKMAN OLD STYLE', 10, 'bold'),text="Yes",variable=var2,value=1).place(x=160,y=150)
    rb2=p.rb(bg='#FFFFFF', font=('BOOKMAN OLD STYLE', 10, 'bold'),text="No",variable=var2,value=2).place(x=300,y=150)
    rb3=p.rb(bg='#FFFFFF', font=('BOOKMAN OLD STYLE', 10, 'bold'),text="Can't Say",variable=var2,value=3).place(x=420,y=150)
    abc=int(time())
   
    def nexstem(event=NONE):
        global done
        global nstemmed
        if q==5 or q==15 or q==10:
            nstemmed=text.get(0.0,END)
            if len(nstemmed)>10:
                but1=p.bu(text='Next',command=nexts,bd=7, bg='cyan', fg='#222222', font=('bold', 15), activebackground='#222222', activeforeground='cyan')
                but1.place(x=450,y=400,height=40, width=60)
                p.bind('<Return>',nexts)
            else:
                tkMessageBox.showinfo("Error","Please Fill genuinely")
    
    text = p.te(width=40, height=7,state='disabled', font=('BOOKMAN OLD STYLE',15),fg='blue')
    text.place(x=80,y=190)
    but3=p.bu("Submit", command=nexstem,bd=7, bg='cyan', fg='#222222', font=('bold', 15), activebackground='#222222', activeforeground='cyan')
    but3.place(x=160,y=400,height=40, width=80)
    p.bind('<Return>',nexstem)
    text.wait_variable(var2)
    text.config(state='normal')

    

def ques_pos():
    global fr2

    ##### Question - Positive #####
    global t
    global occ
    global qp
    if t==1:
        qp[t]=randint(1,15)
    else:
        global x
        x=1
        while x<t:
            if x==1:
                qp[t]=randint(1,15)
            if qp[t]==qp[x]:
                x=0
            x=x+1
    mcq(qp[t])
    t+=1
    global done
    done=0
    
    but3=p.bu(text='Submit',bd=7, bg='cyan', fg='#222222', font=('bold', 15), activebackground='#222222', activeforeground='cyan', command=nex).place(x=160,y=400, height=40, width=80)
    p.bind('<Return>',nex)
 


def ques_neg():

    ##### Question - Negative #####
    global s
    global occ
    global qn
    if s==1:
        qn[s]=randint(16,30)
    else:
        global y
        y=1
        while y<s:
            if y==1:
                qn[s]=randint(16,30)
            if qn[s]==qn[y]:
                y=0
            y=y+1
    mcq(qn[s])
    s+=1
    global done
    done=0
    but3=p.bu(text='Submit',bd=7, bg='cyan', fg='#222222', font=('bold', 15), activebackground='#222222', activeforeground='cyan', command=nex).place(x=160,y=400, height=40, width=80)
    p.bind('<Return>',nex)


def sufpreanalyse():
    global counter
    global nword
    if x==0:
        if nword=='comforts' or nword=='comfortings' or nword=='comforty' or nword=='comfortingly' or nword=='comfortable' or nword=='comfortably' or nword=='comforting' or nword=='comforted':
            counter=1
        elif nowrd=='discomforts' or nword=='uncomfortable' or nword=='uncomfortably' or nword=='discomfort' or nword=='discomforted' or nword=='discomforting':
            counter=2
    elif x==1:
        if nword=='agreeable' or nword=='agreeing' or nword=='agreed' or nword=='agrees':
            counter=1
        elif nword=='disagree' or nword=='disagreed' or nword=='disagreeing' or nword=='disagrees' or nword=='disagreeable':
            counter=2
    elif x==2:
        if nword=='lucky' or nword=='luckily' or nword=='lucks':
            counter=1
        elif nword=='unlucky' or nword=='unluckily':
            counter=2
    elif x==3:
        if nword=='propered' or nword=='properly':
            counter=1
        elif nword=='improper' or nword=='improperly' or nword=='impropered':
            counter=2
    elif x==4:
        if nword=='likeable' or nword=='likely' or nword=='liked' or nword=='liking' or nword=='likewise' or nword=='likeably':
            counter=1
        elif nword=='dislike' or nword=='disliked' or nword=='dislikeable' or nword=='unlikeable' or nword=='unlike' or nword=='unliked' or nword=='unlikely' or nword=='disliking':
            counter=2
    elif x==5:
        if nword=='tasty' or nword=='tasted' or nword=='tasting' or nword=='taster' or nword=='tasting' or nword=='tastily':
            counter=1
        elif nword=='tasteless' or nword=='distaste' or nword=='tastelessly':
            counter=2
    elif x==6:
        if nword=='legally' or nword=='legalize' or nword=='legalizing':
            counter=1
        elif nword=='illegal' or nword=='illegally' or nword=='illegalize' or nword=='illegalizing':
            counter=2
    elif x==7:
        if nword=='matured' or nword=='maturity' or nword=='maturely' or nword=='maturing':
            counter=1
        elif nword=='immature' or nword=='immatured' or nword=='immaturely' or nword=='immaturing' or nword=='immaturity':
            counter=2
    elif x==8:
        if nword=='honoured' or nword=='honourary' or nword=='honouring' or nword=='honours' or nword=='honourly':
            counter=1
        elif nword=='dishonour' or nword=='dishonourary' or nword=='dishonoured' or nword=='dishonouring' or nword=='dishonours' or nword=='dishonourly':
            counter=2
    elif x==9:
        if nword=='trusted' or nword=='trusts' or nword=='trsuting' or nword=='trustingly' or nword=='truster' or nword=='trusty' or nword=='trusties':
            counter=1
        elif nword=='distrust' or nword=='distrusted' or nword=='untrusted' or nword=='untrusts' or nword=='distrusts' or nword=='untrust' or nword=='untrusting' or nword=='distrusting' or nword=='distrustingly' or nword=='untrustingly':
            counter=2

        

def ques_sufpre():
    global x
    global counter
    global nword
    counter=0
    x=presuf[q-6]
    cn2=p.ca()
    imag=Image.open('pic3.jpg')
    imag2=ImageTk.PhotoImage(imag)
    cn2.image([300,-200],image=imag2)
    cn2.image=imag2
    text1=cn2.create_text(350, 70, width=600,  font=('GEORGIA',15, 'bold'),justify=LEFT,fill='black',text="Add suffix or prefix to form a new Word")
    def sufpre_nex(event=NONE):
        global nword
        nword=en1.get()
        nword=lower(nword)
        sufpreanalyse()
        if (nword==wordlist[x] or len(nword)<=len(wordlist[x]) or counter==0) and nword!='tasty':
            tkMessageBox.showinfo("Error","We want another word!!!")
        else:
            but1=p.bu(text='Next',command=nexts,bd=7, bg='cyan', fg='#222222', font=('bold', 15), activebackground='#222222', activeforeground='cyan')
            but1.place(x=450,y=400,height=40, width=60)
            p.bind('<Return>',nexts)

            
    wordlist=['comfort','agree','luck','proper','like','taste','legal','mature','honour', 'trust']
    ###Questions List###
    text2=cn2.create_text(350, 140, width=600,  font=('BOOKMAN OLD STYLE',25),justify=LEFT,fill='blue',text=wordlist[x])

    en1=p.en(width=40,font=('BOOKMAN OLD STYLE',15),fg='black')
    en1.place(x=120,y=200)
    but3=p.bu("Submit", command=sufpre_nex,bd=7, bg='cyan', fg='#222222', font=('bold', 15), activebackground='#222222', activeforeground='cyan')
    but3.place(x=160,y=400,height=40, width=80)
    p.bind('<Return>',sufpre_nex)
    
    
    
def mcq(a=31):
    global var
    can1=p.ca(bg='#FAFAFA')
    imag=Image.open('pic2.jpg')
    imag2=ImageTk.PhotoImage(imag)
    can1.image([300,-200],image=imag2)
    can1.image=imag2
    
    if a==1:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou've had some bad experience telling jokes before, where all you get is a polite laugh. This time, you tell a joke and everybody laughs. It is because:")
        rb1=p.rb(text="It must be a truly good joke this time",variable=var,value=3)
        rb2=p.rb(text="I happened to execute it just right, using the right timing and inflection.",variable=var,value=1)
    elif a==2:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou host a party successfully at your home. It is because:")
        rb1=p.rb(text="I was particularly charming that evening.",variable=var,value=3)
        rb2=p.rb(text="I am an excellent host.",variable=var,value=1)
    elif a==3:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou save a person from choking to death. It is because:")
        rb1=p.rb(text="I have learned the proper technique and happened to be in the right place at the right time.",variable=var,value=3)
        rb2=p.rb(text="I know what to do in a crisis situation.",variable=var,value=1)
    elif a==4:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou saw a drunk driver swerving on the road and called the police, averting a possible crime. It happened because:")
        rb1=p.rb(text="I was particularly alert",variable=var,value=1)
        rb2=p.rb(text="I happened to see the car at the moment it swerved.",variable=var,value=3)
    elif a==5:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nLast night you got asked to the dance floor repeatedly. It was because:")
        rb1=p.rb(text="I was particularly charming that evening",variable=var,value=3)
        rb2=p.rb(text="I am outgoing at parties.",variable=var,value=1)
    elif a==6:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYour friends compliment you on a great dinner. It is because:")
        rb1=p.rb(text="I got this great recipe.",variable=var,value=3)
        rb2=p.rb(text="I am an excellent cook.",variable=var,value=1)
    elif a==7:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou receive a prestigious award or recognition by your agency or peers. It is because:")
        rb1=p.rb(text="I solved an important problem or gave an important contribution.",variable=var,value=3)
        rb2=p.rb(text="I was the best employee/professional.",variable=var,value=1)
    elif a==8:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou have not had a sick day at work for two years. It is because:")
        rb1=p.rb(text="I have good genes.",variable=var,value=3)
        rb2=p.rb(text="I ate well and made sure I was well rested.",variable=var,value=1)
    elif a==9:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou made a killing on the stock market this year. It is because:")
        rb1=p.rb(text="My brother tried a new stock and it panned out.",variable=var,value=3)
        rb2=p.rb(text="My brother is top notch when it comes to investing.",variable=var,value=1)
    elif a==10:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYour employer asks for your advice on things. It is because:")
        rb1=p.rb(text="I am good at giving userful, practive advice. That is why I often get asked.",variable=var,value=1)
        rb2=p.rb(text="I am an expert in this/these areas.",variable=var,value=3)
    elif a==11:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou interviewed for a job and were 'in the flow' with your answers, getting you a second interview as a finalist. It is because:")
        rb1=p.rb(text="I felt extremely confident in the interview.",variable=var,value=3)
        rb2=p.rb(text="I interview well.",variable=var,value=1)
    elif a==12:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou win a racquetball tournament. It is because:")
        rb1=p.rb(text="I spent a lot of time honing my skills and practicing.",variable=var,value=3)
        rb2=p.rb(text="I do the best at everything I put my mind to.",variable=var,value=1)
    elif a==13:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nAfter many tries, you finally win a Rs. 10,00,000 in the lottery. It is because:")
        rb1=p.rb(text="If i play long enough chances are I will win something someday.",variable=var,value=3)
        rb2=p.rb(text="This time I happened to pick just the right numbers or picked the right place to buy the ticket.",variable=var,value=1)
    elif a==14:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou are asked to head up an important project. It is becuase:")
        rb1=p.rb(text="I am very good at what I do. When I try, I succeed.",variable=var,value=1)
        rb2=p.rb(text="I just completed an initiative that for noticed.",variable=var,value=3)
    elif a==15:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nWhen I'm honest with myself, the real reason the project I was in charge of succeeded was because:")
        rb1=p.rb(text="I kept a close watch over everyone's work and directed it.",variable=var,value=1)
        rb2=p.rb(text="Everyone devoted a lot of time and energy to it.",variable=var,value=3)



    elif a==16:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou are feeling run down lately. It is because:")
        rb1=p.rb(text="I never get a chance to relax.",variable=var,value=2)
        rb2=p.rb(text="I was busier this week than normal.",variable=var,value=3)
    elif a==17:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou do a group exercise and perform poorly compared to others. It is because:")
        rb1=p.rb(text="I am not as talented as the others.",variable=var,value=2)
        rb2=p.rb(text="I am not well rested and could not focus.",variable=var,value=3)
    elif a==18:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou gain weight over the holidays. It is because:")
        rb1=p.rb(text="Diets don't work in the long run.",variable=var,value=2)
        rb2=p.rb(text="The diet I tried didn't work.",variable=var,value=3)
    elif a==19:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou prepare a meal for your family and no one appears to like it. It is because:")
        rb1=p.rb(text="I must have missed an ingredient or rushed the meal.",variable=var,value=3)
        rb2=p.rb(text="I am not a very good cook.",variable=var,value=2)
    elif a==20:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou buy a stereo system. You work on it but can't get it to work correctly. It is because:")
        rb1=p.rb(text="I am no good at technical things.",variable=var,value=2)
        rb2=p.rb(text="The owner's manual is written poorly.",variable=var,value=3)
    elif a==21:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou forgot your spouses' anniversary. It is because:")
        rb1=p.rb(text="I am not good at remembering dates.",variable=var,value=2)
        rb2=p.rb(text="I was too pre-occupied with other things at the moment.",variable=var,value=3)
    elif a==22:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou've been fighting a lot with your spouse. It is because:")
        rb1=p.rb(text="I have been under a lot of pressure lately.",variable=var,value=2)
        rb2=p.rb(text="He\She Has been very difficult to get along with.",variable=var,value=3)
    elif a==23:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou are pretty sure you know how to get to the building where the meeting will be held but you are not sure you are on the right road.You pull over and ask for directions.You end up going the wrong direction for ten minutes before getting straightened out. You got lost because:")
        rb1=p.rb(text="The man at the gas station did not give me clear directions.",variable=var,value=3)
        rb2=p.rb(text="I missed a turn.",variable=var,value=2)
    elif a==24:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYour romantic partner wants to cool things off for a while. It is because:")
        rb1=p.rb(text="I am too self centered.",variable=var,value=2)
        rb2=p.rb(text="I did not spend enough quality time with him/her.",variable=var,value=3)
    elif a==25:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYour doctor tells you that you have to stop eating so much sigar, Your reaction is:")
        rb1=p.rb(text="I've got to start being more disciplined about this.",variable=var,value=2)
        rb2=p.rb(text="There is no way to avoid this. There is sugar in everything.",variable=var,value=3)
    elif a==26:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou have been practicing for a long time to be a good golfer but you performed poorly at an employee tournament. It is because:")
        rb1=p.rb(text="I am not good at this sport.",variable=var,value=3)
        rb2=p.rb(text="I am not a good athelete.",variable=var,value=2)
    elif a==27:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou lose your temper with a friend. It is because:")
        rb1=p.rb(text="He/She was not in a good mood that day.",variable=var,value=3)
        rb2=p.rb(text="He/She has a bad trait.",variable=var,value=2)
    elif a==28:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou run for your national association's presidency and lose. It is because:")
        rb1=p.rb(text="I didn't campaign hard enough.",variable=var,value=2)
        rb2=p.rb(text="The other candidate knew more people and was from a more populated state.",variable=var,value=3)
    elif a==29:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYour stocks are at an all time low. It is because:")
        rb1=p.rb(text="I do not understand business.",variable=var,value=3)
        rb2=p.rb(text="I did not pick good stocks.",variable=var,value=2)
    elif a==30:
        item=can1.create_text(350, 70, width=600, font=('GEORGIA',15,'bold'),justify=LEFT,fill='red',text="\nYou can't seem to save money no matter how hard you try. It is because:")
        rb1=p.rb(text="I and\or my family members are not disciplined when it comes to spending.",variable=var,value=2)
        rb2=p.rb(text="I am in a slump at the moment.",variable=var,value=3)

    rb1.config(bg='#00FF00',activebackground='#00FF00', wraplength=500,font=('BOOKMAN OLD STYLE', 12, 'bold'),justify=LEFT)
    rb1.place(x=80,y=175)
    rb2.config(bg='#00FF00',activebackground='#00FF00', wraplength=500,font=('BOOKMAN OLD STYLE', 12, 'bold'),justify=LEFT)
    rb2.place(x=80,y=230)


def nexts(event=NONE):
    global var,var2
    global fr
    global q
    global t,s
    global pos_sp, neg_sp

    if q==10 or q==5 or q==15:
        if q==10:
            global var2
            var2=3
        analyse(str(nstemmed))
    elif q<10 and q>5:
        sufpreanalyse()
        global counter
        if counter==1:
            pos_sp+=1
        elif counter==2:
            neg_sp+=1

    else:
        sentiment(var.get())
    q+=1
    var2=IntVar(0)
    var=IntVar(0)
    p.endfr()
    fr.destroy()
    fr=p.fr(bg='#FAFAFA')
    if q==10:
        ques_pic()

    elif q==5 or q==15:
        ques_text()

    elif q>5 and q<10:
        ques_sufpre()
    elif q==16:
        output()
        
    else:
        r=randint(1,2)
        if t<=4 and (s>4 or r==1):
            ques_pos()
        elif s<=4 and (t>4 or r==2):
            ques_neg()




def start(event=NONE):
    global fr
    p.endfr()
    fr.destroy()
    fr=p.fr(bg='#FAFAFA')
    p.unbind('y')
    p.unbind('n')
    ###For Randomizing Text Questions###
    list2=[1,2,3,4,5,6,7,8,9,0]
    global presuf
    presuf=sample(list2, 4)[:]
    r=randint(1,2)
    if r==1:
        ques_pos()
    elif r==2:
        ques_neg()
    
def close(event=NONE):
    if tkMessageBox.askyesno("Quit","Do You Want To Quit???"):
        p.destroy()
    

p=Gui()
p.title('Sentiment Analysis')
p.geometry(newGeometry='700x500')

fr=p.fr()
canint=p.ca(bg='green')
imag=Image.open('pic1.jpg')
imag2=ImageTk.PhotoImage(imag)
canint.image([300,-200],image=imag2)
canint.image=imag2
var=IntVar(0)
var2=IntVar(0)
but1=p.bu('YES',command=start,font=('bold',15), bg='red', fg='white', activebackground='white',activeforeground='red',bd=8).place(x=175,y=370, height=50, width=80)
p.bind('y',start)
but2=p.bu('NO',command=close,font=('bold',15), bg='red', fg='white', activebackground='white',activeforeground='red',bd=8).place(x=450,y=370, height=50, width=80)
item1=canint.create_text(350,140,text="\nWelcome!!!\n Hope You Had A Great Day Till Now.\nIf Not, We Are Gonna Make It Great With This Program!!!\n\n\nSo Shall We Begin???",font=('BOOKMAN OLD STYLE',17,'bold'),justify=CENTER,fill='white')
p.bind('n',close)
p.mainloop()
