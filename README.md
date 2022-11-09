# **DigitalWatch - A web based exam administration solution**

Contributors: Henry, Suhail, Charleen, and Callum

Submission for: **HackCamp 2022** - *Western Canada's Largest Beginner-Friendly Hackathon*

## Project Description

Our project focuses on creating an web-based exam proctoring system to streamline the process used at the UBC Centre for Accessibility. We wanted to create a platform where proctors could view a dashboard of all students currently booked to take an exam, the exam status, start + end time, and more. We also recognized a need for an analog countdown timer and information system for the student. For this, we integrated an Arduino with an LED display.

## Implementation

We chose to create a MySQL database hosted on Microsoft Azure. This was the heart of our project, as it was responsible for storage of the exam information data.

Flask was the web development micro-framework of choice. We used Python, HTML, and CSS. Our webapp consisted of two functionalities: a web form and a dashboard. For the purposes of this hackathon, we decided to create a makeshift database entry form to "check-in" students with all the necessary information. In practice, this would be taken care of by existing infrastructure used by the UBC Centre for Accessibility. Additionally, we created a dashboard view of all ongoing or future examinations to be taken at the CFA.

For our desktop arduino interfacer, we used PyQt6 to create an desktop application that, in similar fashion to the webapp, all ongoing or future examinations. However, the sole purpose of this desktop application was to communicate the formatted serial information to the Arduino. Therefore, we created a GUI that allows a user to choose which exam information to upload to the Arduino. To do this, we parse the MySQL database information, take the selected query, format the information, and then serial write the information to the Arduino.

The Arduino was responsible for parsing the incoming formatted bytes and performing all calculations necessary to create a countdown. The display was configured to show the student number of the exam taker, the course for which the exam is for, and a live-updating countdown timer.