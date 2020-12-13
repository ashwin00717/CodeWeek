from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
import speech_recognition as sr
import pyttsx3
import sounddevice as sd
from scipy.io import wavfile
import wavio
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponseRedirect
import sys
import pandas as pd
from SR.models import *
from django.db import connection
# from termcolor import colored
# from sty import fg, bg, ef, rs
import plotly.express as px
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "index.html", context=None)


# Python program to translate
# speech to text and text to speech
def test(request):
    if request.method == "POST":
        return redirect("www.google.com")


# @csrf_protect
def speech2text():
    # if request.method == "POST":
    # Initialize the recognizer
    r = sr.Recognizer()

    # Function to convert text to speech
    def SpeakText(command):

        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()

    # Loop infinitely for user to speak
    # while 1:

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the .wav file as source for input.
        with sr.AudioFile("output1.wav") as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            # MyText = r.recognize_wit(audio2, key="AQT65GFNUOVFYVQVMHRT4GKKS5SZOQJM")
            MyText = MyText.lower()

            print("Did you say:: " + MyText)
            with open("speech.txt", "w") as fp:
                fp.write(MyText)
            # SpeakText(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError as e:
        print("unknown error occured: {0}".format(e))


def usesounddevice(request):

    print ("### Recording voice ###")
    fs = 44100  # Sample rate
    seconds = 10  # Duration of recording
    # Records the voice
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    # Write to a .wav file
    wavio.write("output1.wav", myrecording, fs, sampwidth=2)
    print("### Converting voice to text ###")
    speech2text()
    print("### Converting text to sql ###")
    sql = text2sql()
    cur = connection.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    print("Database Result:",rows)
    #dash()
    #link = "http://127.0.0.1:8050/"
    #return HttpResponse(link)
    dash_report()
    return render(request, "index.html", context=None)
    #return HttpResponseRedirect(rows)

def loaddash(request):
    return HttpResponse("New API working")

def text2sql():
    ##########

    objkey = pd.read_csv("object_key.csv")
    logikey = pd.read_csv("logic_key.csv")

    # print(fg.blue + bg.yellow)
    with open("speech.txt", "r") as fp:
        usrreq = fp.read()
    print("usrreq:", usrreq)
    if usrreq.lower() == "goodbye":
        sys.exit("Genie: Have a great day! Thank You!!")

    # usrreq = "Which Employee has most Salary"
    # usrreq = "Which country has most number of Employee"
    usrreq_tkns = usrreq.split()
    # Filter Object Key records that has keywords from user query
    objkey_fltrd = objkey[objkey["OBJECT_KEY"].isin(usrreq_tkns)]
    # Filter Logic Key records that has keywords from user query
    logikey_fltrd = logikey[logikey["LOGIC_KEY"].isin(usrreq_tkns)]

    # if no object key or logic key is found, quit the program
    if len(objkey_fltrd) == 0 and len(logikey_fltrd) == 0:
        sys.exit("Genie: I'm Sorry, Not enough keywords found")

    # Identify corresponding list of tables (if multiple, need to join)
    x1 = objkey_fltrd.OBJECT_MASTER.unique()
    z = len(x1)

    # A0001: Logic to determine the FROM part
    if z == 1:
        from_obj = "from SR_" + (", ".join(x1))
        # print(from_obj)
    elif z == 0:
        print("no key information found")
    elif z > 1:
        print("Join logic not coded yet")
        from_obj = "from SR_" + (", ".join(x1))  # join logic needs to be added
    else:
        print("Something went wrong")
    # A0001: End

    # A0002: Logic to determine the SELECT part
    # Iterates the list of tokens from User Query against keys in Object Key table. Breaks at 1st occurence (assumed to be SELECT)

    i = 0
    # Object Keys into List
    objkeylist = objkey.OBJECT_KEY.to_list()
    # Below will pick the "matching" object key from the comparison of lists, and the 1st matching
    mtchkeylist = [i for i in usrreq_tkns if i in objkeylist]
    if len(mtchkeylist) == 0:
        sys.exit(
            "No Object Keyword available"
        )  # Temporary. Can still code for question like "Who are in US"
    selkey = mtchkeylist[0]

    # Replacing Old Code with "comparison of lists code"
    """
    for x in usrreq_tkns:
        if x in objkeylist:
            i=i+1
        if i == 1:
            selkey = x
            break
    """

    # Below will pick column name for the 1st matching keyword
    sel_obj = "SELECT " + (
        " ,".join(objkey[objkey["OBJECT_KEY"] == selkey].OBJECT_NAME)
    )
    # print (sel_obj)
    # Addressed List to track which key words are already handled. Once the Final SQL is built, all keywords (object + logic) should have been in addressed list
    addsd_list = objkey[objkey["OBJECT_KEY"] == selkey].OBJECT_KEY
    # Temporary Assumption - GROUP BY element will be same as SELECT element when there is aggregate
    grp_obj = "GROUP BY " + (
        " ,".join(objkey[objkey["OBJECT_KEY"] == selkey].OBJECT_NAME)
    )
    # A0002: End

    # Logic Keys into List
    logikeylist = logikey.LOGIC_KEY.to_list()

    # A0003: Final Query
    final_sql = sel_obj + " " + from_obj

    whr = 0
    whr = len(logikey_fltrd[logikey_fltrd["WHR_FLG"] == 1].LOGIC_KEY.unique())
    if whr > 0:
        whrnm = " ,".join(
            logikey_fltrd[logikey_fltrd["WHR_FLG"] == 1].LOGIC_NAME.unique()
        )
        final_sql = final_sql + " WHERE " + whrnm
        addsd_list = addsd_list.append(
            logikey_fltrd[logikey_fltrd["WHR_FLG"] == 1].LOGIC_KEY
        )

    agg = 0
    # From Logic Key Words assignment, identifies if Group By clause is needed or not
    # agg = len(logikey_fltrd[logikey_fltrd['LOGIC_NAME']=="group"].LOGIC_KEY.unique())
    agg = len(logikey_fltrd[logikey_fltrd["GRP_FLG"] == 1].LOGIC_KEY.unique())
    if agg > 0:
        final_sql = sel_obj + " " + from_obj + " " + grp_obj

    ordr = 0
    ordr = len(logikey_fltrd[logikey_fltrd["ORD_FLG"] == 1].LOGIC_KEY.unique())
    if ordr > 0:
        ordrnm = " ,".join(
            logikey_fltrd[logikey_fltrd["ORD_FLG"] == 1].LOGIC_NAME.unique()
        )
        final_sql = final_sql + " ORDER BY EMPL_ID " + ordrnm
        addsd_list = addsd_list.append(
            logikey_fltrd[logikey_fltrd["ORD_FLG"] == 1].LOGIC_KEY
        )

    addsd_list1 = addsd_list.to_list()
    # print(addsd_list1)

    flmtchlist = [i for i in usrreq_tkns if i in objkeylist + logikeylist]
    # print(flmtchlist)
    pndnglist = [i for i in flmtchlist if i not in addsd_list1]
    # print(pndnglist)

    final_sql = final_sql + ";"
    print("Final SQL:", final_sql)
    return final_sql
    # A0003: End

    ##############
def dash_report():
    import pandas as pd
    import plotly
    import dash
    import dash_table
    import plotly.express as px
    import dash_core_components as dcc
    import dash_html_components as html
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context

    app = dash.Dash(__name__)

    df4 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

    c = df4.columns

    fig1 = px.bar(df4, x=df4.iloc[:, 1], y=df4.iloc[:, 2], hover_data=df4.columns, color=c[3],
                  labels={'x': c[1], 'y': c[2]})

    fig2 = px.scatter(df4, x=df4.iloc[:, 1], y=df4.iloc[:, 2], height=700, hover_data=df4.columns, color=c[3],
                      size=df4.iloc[:, 4], size_max=65, log_x=True, labels={'x': c[1], 'y': c[2]})

    fig3 = px.line(df4, x=df4.iloc[:, 1], y=df4.iloc[:, 2], color=c[3], line_group=c[0], hover_name=c[0])

    fig4 = px.density_heatmap(df4, x=df4.iloc[:, 1], y=df4.iloc[:, 4], nbinsx=20, nbinsy=20,
                              labels={'x': c[1], 'y': c[4]}, hover_data=df4.columns)

    fig5 = px.density_heatmap(df4, x=df4.iloc[:, 1], y=df4.iloc[:, 4], nbinsx=10, nbinsy=10, facet_row=df4.iloc[:, 3],
                              labels={'x': c[1], 'y': c[4]}, hover_data=df4.columns)

    fig6 = px.treemap(df4, path=[df4.iloc[:, 1], df4.iloc[:, 3]], values=df4.iloc[:, 2], color=df4.iloc[:, 1],
                      color_continuous_scale=['red', 'yellow'])

    plotly.offline.plot(fig6, filename='C:\\Ashwin\\SparkCode\\projects\\CodeWeek\\genie\\SR\\templates\\fig6.html')

    ##############
