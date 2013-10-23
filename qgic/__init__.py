# -*- coding: utf-8 -*-
"""
    qgic
    ~~~~

    Website for the Queen's Global Innovation Conference (2013)

    blah blah blah
"""

from flask import Flask, render_template, url_for
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

assets.url = '/static'  # HACK HACK HACK
assets.auto_build = False
assets.debug = False
assets.manifest = "file:assets-manifest"

assets.register('css_screen', 'sass/screen.sass',
                filters='compass', output='css/screen.%(version)s.css')
assets.register('css_print', 'sass/print.sass',
                filters='compass', output='css/print.%(version)s.css')

assets.register('js', 'coffee/main.coffee',
                filters='coffeescript', output='js/main.%(version)s.js')


@app.route('/')
def home():
    team_members = [
        {
            'name': 'Olga Khuskivadse',
            'mug': url_for('static', filename='img/team/olga.jpg'),
            'role': 'Chair',
            'bio': [
                '',
            ],
            'contact': '',
        },
        {
            'name': 'Alicia Cuzner',
            'mug': url_for('static', filename='img/team/alicia.jpg'),
            'role': 'Speaker Coordinator',
            'bio': [
                'Alicia Cuzner graduated from Trent University in April 2013 with a Bachelor of Arts degree (B.A.) and is now enrolled in the Bachelor of Education (B.Ed) program at Queen\'s University. While at Queen\'s University she will also be enrolled in the Aboriginal Teacher Education Program, and wishes to focus her Bachelor of Education degree in Aboriginal Education and learning disabilities.',
                'Alicia was a tutor for the Learning Disabilities Association of Peterborough for the past two years, and was a Conservation Intern at Nature Canada in the summer of 2013. She is one of the Speaker Coordinators for QGIC, and is also on the planning committee for an Aboriginal based conference hosted by the Royal Ottawa Mental Health Centre. She is an active volunteer at the Odawa Native Friendship Centre and runs Education workshops at Minwaashin Lodge in Ottawa.  Alicia is a strong advocate for sustainability and a healthy environment. She believes that anyone has the power to make a positive change in global issues.',
            ],
            'contact': '',
        },
        {
            'name': 'Yaseen Khaled',
            'mug': url_for('static', filename='img/team/yaseen.jpg'),
            'role': 'Speaker Coordinator',
            'bio': [''],
            'contact': '',
        },
        {
            'name': 'Michael Piotrowski',
            'mug': url_for('static', filename='img/team/michael.jpg'),
            'role': 'Innovation Challenge Coordinator',
            'bio': [
                'At an early age Michael fell in love with the magical world of Lego. Building Spaceships and Dinosaurs he found himself enthralled by the seemingly endless possibilities for creating and innovating. This fascination grew throughout his education; he participated in numerous design competitions, built computers and robots, and designed missiles. Now entering his final year of Engineering Physics, Michael wishes to continue his studies and receive a Masters in Aerospace Engineering, with the goal of one day becoming an Astronaut. When he is not pursuing his childhood dream, Michael enjoys sailing, throwing the football around, and gracefully losing to his friends at Settlers of Catan. With his vast experience in brainstorming and problem solving, Michael looks forward to the challenge of designing an intellectually and emotionally stimulating innovation challenge as the Innovation Challenge Coordinator for the 2013 Queens Global Innovation Conference.',
            ],
            'contact': '',
        },
        {
            'name': 'Kirsten MacMillan',
            'mug': url_for('static', filename='img/team/kirsten.jpg'),
            'role': 'Workshop Coordinator',
            'bio': [
                'Kirsten is a first year engineering student at Queen’s University. Originally from Halifax, Nova Scotia, Kirsten knew she wanted to move to Kingston to go to Queen’s as early as junior high. Although she started in science, Kirsten is looking forward to the challenges of the engineering program, as it is better suited to her personal and political interests. Kirsten is interested in activism on both a local and global stage. She is looking forward to making positive changes on campus and wherever she finds herself next in the world. She recently spent 7 weeks volunteering with disabled youth in Ecuador, and it made a lasting impression. She will be coordinating the workshops during QGIC and can’t wait to get in touch with all of the innovators at Queen’s and in Kingston.',
            ],
            'contact': 'qgicworkshops@gmail.com',
        },
        {
            'name': 'Andrea D\'Amour',
            'mug': url_for('static', filename='img/team/andrea.jpg'),
            'role': 'Sponsorship & Finance',
            'bio': [
                'Andrea D\'Amour is this year’s Director of Sponsorship and Finance for Queen’s Global Innovation Conference (QGIC). She is in her fourth-year of studies as a chemical engineer at Queen’s University. She has attended QGIC in the past and is extremely excited to be part of the director team for this year’s conference. Andrea has also been a member of the Queen’s Chapter of Engineers Without Borders since her first year at Queen’s, participating as a general member and as a Director for the Fair Trade initiative. Andrea is very enthusiastic about global change and hopes to spread this energy to others through QGIC 2013. She is an avid traveller and spent the Winter 2012 semester studying abroad at the University of Strathclyde in Glasgow, Scotland. Andrea greatly enjoyed this opportunity and adventure, but is very excited to be back at Queen’s to see what her final year of studies will bring her! She hopes to see many new faces at QGIC 2013 as well as friends from years past. If you have any questions for her about last year’s conference, her exchange, sponsorship opportunities for this year’s conference, or anything else she would be more than happy to answer them.',
            ],
            'contact': 'qgicfinance@gmail.com',
        },
        {
            'name': 'Vidhur Verghese',
            'mug': url_for('static', filename='img/team/vidhur.jpg'),
            'role': 'Marketing & Media',
            'bio': [''],
            'contact': '',
        },
        {
            'name': 'Monika Szpytko',
            'mug': url_for('static', filename='img/team/monika.jpg'),
            'role': 'Logistics Director',
            'bio': [''],
            'contact': '',
        },
        # {
        #     'name': 'Phil Schleihauf',
        #     'mug': url_for('static', filename='img/facepalm.svg'),
        #     'role': 'Website',
        #     'bio': [''],
        #     'contact': '',
        # },
    ]
    return render_template('home.html', team_members=team_members)


@app.route('/register')
def register():
    return 'register here!'
