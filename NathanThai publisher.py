
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9823361
#    Student name: Nathan Thai
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  Publish Your Own Periodical
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface design and development to produce a
#  useful application for publishing a customised newspaper or
#  magazine on a topic of your own choice.  See the instruction
#  sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  You should be able to complete this assignment using
# these functions only.

# Import the function for opening a web document given its URL.
from urllib.request import urlopen

# Import the function for finding all occurrences of a pattern
# defined via a regular expression.
from re import findall

# A function for opening an HTML document in your operating
# system's default web browser. We have called the function
# "webopen" so that it isn't confused with the "open" function
# for writing/reading local text files.
from webbrowser import open as webopen

# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your publication file.
from os import getcwd

# An operating system-specific function for 'normalising' a
# path to a file to the path naming conventions used on this
# platform.  Apply this function to the full name of your
# publication file so that your program will work on any
# operating system.
from os.path import normpath
    
# Import the standard Tkinter functions.
from Tkinter import *

# Import the SQLite functions.
from sqlite3 import *

# Import the date/time function.
from datetime import datetime

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the published newspaper or magazine. To simplify marking,
# your program should publish its results using this file name.
file_name = 'publication.html'

#Create Window
publication = Tk()

#RSS feeds
breaking_news = 'http://www.nasa.gov/rss/dyn/breaking_news.rss'
solar_system = 'http://www.nasa.gov/rss/dyn/solar_system.rss'
hurricane_update = 'http://www.nasa.gov/rss/dyn/hurricaneupdate.rss'
earth_news = 'http://www.nasa.gov/rss/dyn/earth.rss'
space_station_news = 'http://www.nasa.gov/rss/dyn/shuttle_station.rss'
aeronautics_news = 'http://www.nasa.gov/rss/dyn/aeronautics.rss'

breaking_news_feed = urlopen(breaking_news).read()
solar_system_feed = urlopen(solar_system).read()
hurricane_update_feed = urlopen(hurricane_update).read()
earth_news_feed = urlopen(earth_news).read()
space_station_news_feed = urlopen(space_station_news).read()
aeronautics_news_feed = urlopen(aeronautics_news).read()

#Boolean variables
breaking_news_checked = BooleanVar()
solar_system_checked = BooleanVar()
hurricane_update_checked = BooleanVar()
earth_news_checked = BooleanVar()
space_station_news_checked = BooleanVar()
aeronautics_news_checked = BooleanVar()

#Print Button
def print_button():
    news_html = open('publication.html','w') #Creates the HTML

#Write text
    text = '''
<!DOCTYPE html>
<html>

<head>


<meta charset="UTF-8">
<title>Global Vision</title>
</head>

<body>

<h1 style='font-family:Microsoft JhengHei;
font-size:500%;text-align:center'>Global Vision
</h1>

<center><img src='http://www.brandcrowd.com/
gallery/brands/pictures/picture13501402813829.jpg' alt='Global Vision'
style='width:400px;height:330px;'></center>

<p style='font-family:Microsoft JhengHei;font-size:150%;
text-align:center;'>Konoha's Best Source of News
</p>

<p style='font-family:Microsoft JhengHei;font-size:100%;
text-align:center;'>Editor-in-Chief: Nathan Thai
</p>

'''

    text_pb.insert(END, 'Printing: Masthead... \n')

#Write to html
    news_html.write(text)
    news_html.write('<hr width = 600px size = 5px>')

#Creates lists and enables them for global use
    global links #Makes the links list global to be used in any function
    global timestamps #Makes the timestamps list global to be used in any function
    links = [] #Creates an empty list for links
    timestamps = [] #Creates an empty list for timestamps

    
#When boxes are checked
    
    stories = [breaking_news_checked.get(), solar_system_checked.get(),\
               hurricane_update_checked.get(), earth_news_checked.get(),\
               space_station_news_checked.get(), aeronautics_news_checked.get()]

#Breaking News checked
    if stories[0]:
        item = findall('(?s)<item>(.*?)</item>', breaking_news_feed)
        category = 'NASA Breaking News'
        url1 = 'http://www.nasa.gov/rss/dyn/breaking_news.rss'
        title = findall('(?s)<title>(.*)</title>', item[0])
        title = title[0]
        photo = findall('<enclosure url="(.*?)"', item[0])
        summary = findall('(?s)<description>\n*(.*)\n*</description>', item[0])
        summary = summary[0]
        date = findall('<pubDate>(.*)</pubDate>', item[0])
        text_pb.insert(END, 'Printing: Breaking News... \n')
        links.append(url1) #Add the link to list of links
        timestamp = str(datetime.now().replace()) #Current time of topic retrieval
        timestamps.append(timestamp) #Add timestamp to list of timestamps
        

#Add Breaking News to html
        news_html = open('publication.html', 'a')
        news_html.write('<h2 style="font-family:Microsoft JhengHei;\
text-align:center">' + category + '</h2>')
        news_html.write('\n' + '<h1 style="font-family:Microsoft JhengHei;\
text-align:center">' + title + '</h1>')
        news_html.write('\n' + '<center><img src=' + photo[0] + '></center>')
        news_html.write('\n' + '<h3 style="font-family:Microsoft JhengHei;\
text-align:center">' + summary + '</h3>')
        news_html.write('\n' + '<h4 style="font-family:Microsoft JhengHei;\
text-align:center"><i>' + url1 + '</i></h3>')
        news_html.write('\n' + '<h4 style="font-family:Microsoft JhengHei;\
text-align:center">' + date[0] + '</h3>')

        news_html.write('\n' + '<hr width = 600px size = 5px>' + '\n' + '\n')
        news_html.close()


#Solar System checked
    if stories[1]:
        item = findall('(?s)<item>(.*?)</item>', solar_system_feed)
        category = 'Solar System and Beyond'
        url2 = 'http://www.nasa.gov/rss/dyn/solar_system.rss'
        title = findall('(?s)<title>(.*)</title>', item[0])
        title = title[0]
        photo = findall('<enclosure url="(.*?)"', item[0])
        summary = findall('(?s)<description>\n*(.*)\n*</description>', item[0])
        summary = summary[0]
        date = findall('<pubDate>(.*)</pubDate>', item[0])
        text_pb.insert(END, 'Printing: Solar System News... \n')
        links.append(url2) #Add the link to list of links
        timestamp = str(datetime.now().replace()) #Current time of topic retrieval
        timestamps.append(timestamp) #Add timestamp to list of timestamps

#Add Solar System news to html
        news_html = open('publication.html', 'a')
        news_html.write('<h2 style="font-family:Microsoft JhengHei;\
text-align:center">' + category + '</h2>')
        news_html.write('\n' + '<h1 style="font-family:Microsoft JhengHei;\
text-align:center">' + title + '</h1>')
        news_html.write('\n' + '<center><img src=' + photo[0] + '></center>')
        news_html.write('\n' + '<h3 style="font-family:Microsoft JhengHei;\
text-align:center">' + summary + '</h3>')
        news_html.write('\n' + '<h4 style="font-family:Microsoft JhengHei;\
text-align:center"><i>' + url2 + '</i></h4>')
        news_html.write('\n' + '<h4 style="font-family:Microsoft JhengHei;\
text-align:center">' + date[0] + '</h5>')

        news_html.write('\n' + '<hr width = 600px size = 5px>' + '\n' + '\n')
        news_html.close()


#Hurricane Update checked
    if stories[2]:
        item = findall('(?s)<item>(.*?)</item>', hurricane_update_feed)
        category = 'Hurricane Breaking News'
        url3 = 'http://www.nasa.gov/rss/dyn/hurricaneupdate.rss'
        title = findall('(?s)<title>(.*)</title>', item[0])
        title = title[0]
        photo = findall('<enclosure url="(.*?)"', item[0])
        summary = findall('(?s)<description>\n*(.*)\n*</description>', item[0])
        summary = summary[0]
        date = findall('<pubDate>(.*)</pubDate>', item[0])
        text_pb.insert(END, 'Printing: Hurricane News... \n')
        links.append(url3) #Add the link to list of links
        timestamp = str(datetime.now().replace()) #Current time of topic retrieval
        timestamps.append(timestamp) #Add timestamp to list of timestamps

#Add Hurricane Update to html
        news_html = open('publication.html', 'a')
        news_html.write('\n' + '<h2 style="font-family:Microsoft JhengHei;\
text-align:center">' + category + '</h2>')
        news_html.write('\n' + '<h1 style="font-family:Microsoft JhengHei;\
text-align:center">' + title + '</h1>')
        news_html.write('\n' + '<center><img src=' + photo[0] + '></center>')
        news_html.write('\n' + '<h3 style="font-family:Microsoft JhengHei;\
text-align:center">' + summary + '</h3>')
        news_html.write('\n' + '<h4 style="font-family:Microsoft JhengHei;\
text-align:center"><i>' + url3 + '</i></h4>')
        news_html.write('\n' + '<h4 style="font-family:Microsoft JhengHei;\
text-align:center">' + date[0] + '</h5>')

        news_html.write('\n' + '<hr width = 600px size = 5px>' + '\n' + '\n')
        news_html.close()

#Earth News checked
    if stories[3]:
        item = findall('(?s)<item>(.*?)</item>', earth_news_feed)
        category = 'Earth News'
        url4 = 'http://www.nasa.gov/rss/dyn/earth.rss'
        title = findall('(?s)<title>(.*)</title>', item[0])
        title = title[0]
        photo = findall('enclosure url="(.*?)"', item[0])
        summary = findall('(?s)<description>(.*)</description>', item[0])
        summary = summary[0]
        date = findall('<pubDate>(.*)</pubDate>', item[0])
        text_pb.insert(END, 'Printing: Earth News... \n')
        links.append(url4) #Add the link to list of links
        timestamp = str(datetime.now().replace()) #Current time of topic retrieval
        timestamps.append(timestamp) #Add timestamp to list of timestamps

#Add Earth News to html
        news_html = open('publication.html', 'a')
        news_html.write('<h2 style="font-family:Microsoft JhengHei;\
text-align:center">' + category + '</h2>')
        news_html.write('\n' + '<h1 style="font-family:Microsoft JhengHei;\
text-align:center">' + title + '</h1>')
        news_html.write('\n' + '<center><img src=' + photo[0] + '></center>')
        news_html.write('\n' + '<h3 style="font-family:Microsoft JhengHei;\
text-align:center">' + summary + '</h3>')
        news_html.write('\n' + '<h4 style="font-family:Microsoft JhengHei;\
text-align:center"><i>' + url4 + '</i></h4>')
        news_html.write('\n' + '<h4 style="font-family:Microsoft JhengHei;\
text-align:center">' + date[0] + '</h5>')

        news_html.write('\n' + '<hr width = 600px size = 5px>' + '\n' + '\n')
        news_html.close()

#Space Station News checked
    if stories[4]:
        item = findall('(?s)<item>(.*?)</item>', space_station_news_feed)
        category = 'Space Station News'
        url5 = 'http://www.nasa.gov/rss/dyn/shuttle_station.rss'
        title = findall('(?s)<title>(.*)</title>', item[0])
        title = title[0]
        photo = findall('<enclosure url="(.*?)"', item[0])
        summary = findall('(?s)<description>\n*(.*)\n*</description>', item[0])
        summary = summary[0]
        date = findall('<pubDate>(.*)</pubDate>', item[0])
        text_pb.insert(END, 'Printing: Space Station News... \n')
        links.append(url5) #Add the link to list of links
        timestamp = str(datetime.now().replace()) #Current time of topic retrieval
        timestamps.append(timestamp) #Add timestamp to list of timestamps

#Add Space Station News to html
        news_html = open('publication.html', 'a')
        news_html.write('<h2 style="font-family:Microsoft JhengHei;\
text-align:center">' + category + '</h2>')
        news_html.write('\n' + '<h1 style="font-family:Microsoft JhengHei;\
text-align:center">' + title + '</h1>')
        news_html.write('\n' + '<center><img src=' + photo[0] + '></center>')
        news_html.write('\n' + '<h3 style="font-family:Microsoft JhengHei;\
text-align:center">' + summary + '</h3>')
        news_html.write('\n' + '<h4 style="font-family:Microsoft JhengHei;\
text-align:center"><i>' + url5 + '</i></h3>')
        news_html.write('\n' + '<h4 style="font-family:Microsoft JhengHei;\
text-align:center">' + date[0] + '</h3>')

        news_html.write('\n' + '<hr width = 600px size = 5px>' + '\n' + '\n')
        news_html.close()

#Aeronautics News checked
    if stories[5]:
        item = findall('(?s)<item>(.*?)</item>', aeronautics_news_feed)
        category = 'Aeronautics News'
        url6 = 'http://www.nasa.gov/rss/dyn/aeronautics.rss'
        title = findall('(?s)<title>(.*)</title>', item[0])
        title = title[0]
        photo = findall('<enclosure url="(.*?)"', item[0])
        summary = findall('(?s)<description>\n*(.*)\n*</description>', item[0])
        summary = summary[0]
        date = findall('<pubDate>(.*)</pubDate>', item[0])
        text_pb.insert(END, 'Printing: Aeronautics... \n')
        links.append(url6) #Add the link to list of links
        timestamp = str(datetime.now().replace()) #Current time of topic retrieval
        timestamps.append(timestamp) #Add timestamp to list of timestamps

#Add Aeronautics News to html
        news_html = open('publication.html', 'a')
        news_html.write('<h2 style="font-family:Microsoft JhengHei;\
text-align:center">' + category + '</h2>')
        news_html.write('\n' + '<h1 style="font-family:Microsoft JhengHei;\
text-align:center">' + title + '</h1>')
        news_html.write('\n' + '<center><img src=' + photo[0] + '></center>')
        news_html.write('\n' + '<h3 style="font-family:Microsoft JhengHei;\
text-align:center">' + summary + '</h3>')
        news_html.write('\n' + '<h4 style="font-family:Microsoft JhengHei;\
text-align:center"><i>' + url6 + '</i></h3>')
        news_html.write('\n' + '<h4 style="font-family:Microsoft JhengHei;\
text-align:center">' + date[0] + '</h3>')

        news_html.write('\n' + '<hr width = 600px size = 5px>' + '\n' + '\n')
        news_html.close()

    text_pb.insert(END, 'COMPLETED!')
    news_html = open('publication.html', 'a')
    news_html.write('''</body>
</html>''')


####Part B: SQL
#Create Record function

def record():
    connection = connect('internet_activity.db') #Connect to database
    cursor = connection.cursor()                 #Create a cursor
    cursor.execute('DELETE FROM Recent_Downloads')
    counter = 0
    for link in links:
        cursor.execute('INSERT INTO Recent_Downloads VALUES (?,?)',\
                       (timestamps[counter], link))
        counter += 1 #Next position per loop
        connection.commit() #Committing to the proposed changes
    connection.close()


##GUI
#Give Window a Title
publication.title('Publication')

#Set root window dimensions
publication.geometry('420x600')

#Set margin size
margin_size = 1

#Create Labels
columnspan= 10

lbl1 = Label(publication, text = '1.Choose your preferred topics:',\
             font = ('Arial', 20))
lbl2 = Label(publication, text = '2.Start printing your newspaper:',\
             font = ('Arial', 20))
lbl3 = Label(publication, text = '3.Watching its progess:',\
             font = ('Arial', 20))
lbl4 = Label(publication, text = '4.Open your newspaper and enjoy:',\
             font = ('Arial', 20))
lbl5 = Label(publication, text = '5. Save your internet activity:',\
             font = ('Arial', 20))

#Place Label
lbl1.grid(columnspan= 10, row=1, column=0, sticky= 'w')
lbl2.grid(columnspan= 10, row=5, column=0, sticky= 'w')
lbl3.grid(columnspan= 10, row=7, column=0, sticky= 'w')
lbl4.grid(columnspan = 10, row=9, column=0, sticky= 'w')
lbl5.grid(columnspan = 10, row=11, column=0, sticky= 'w')

#Create Checkbuttons
cb1 = Checkbutton(publication, text = 'Breaking News',\
                  variable = breaking_news_checked)
cb2 = Checkbutton(publication, text = 'Solar System',\
                  variable = solar_system_checked)
cb3 = Checkbutton(publication, text = 'Hurricane Update',\
                  variable = hurricane_update_checked)
cb4 = Checkbutton(publication, text = 'Earth News',\
                  variable = earth_news_checked)
cb5 = Checkbutton(publication, text = 'Space Station News',\
                  variable = space_station_news_checked)
cb6 = Checkbutton(publication, text = 'Aeronautics News',\
                  variable = aeronautics_news_checked)

#Place Checkbuttons
cb1.grid(row = 2, sticky= 'w', padx = 100)
cb2.grid(row = 2, sticky= 'w', padx = 250)
cb3.grid(row = 3, sticky= 'w', padx = 100)
cb4.grid(row = 3, sticky= 'w', padx = 250)
cb5.grid(row = 4, sticky= 'w', padx = 100)
cb6.grid(row = 4, sticky= 'w', padx = 250)

#Create Print button
btnP = Button(publication, text = 'Print', command = print_button)
btnP.grid(row=6, sticky= 'w', padx = 175)

#Create Progess box
text_pb = Text(publication, width= 40, height= 10)
text_pb.grid(row= 8, padx= 45, pady = 20, sticky = 'W')

#Create Read button
def read():
    html_directory = getcwd()
    html_location = html_directory + '/' + 'publication.html'
    normalised_html = normpath(html_location)
    webopen(normalised_html)
btnR = Button(publication, text = 'Read', command = read)
btnR.grid(row=10, sticky= 'w', padx = 175)

#Create Record Button
btnRE = Button(publication, text = 'Record', command = record)
btnRE.grid(row=12, stick= 'w', padx = 175)

#Wait for user input
publication.mainloop()














