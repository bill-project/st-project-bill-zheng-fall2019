from flask import Flask
from flask_cors import CORS
import json
import random

app = Flask(__name__)
CORS(app)

# gpa, sat, act, ap1, ap2, ap3, ap4, ap5, ap6, ap7, ap8, ap9, ap10, ap11, ap12, ap13
input_data = [
    [4.2, 1480, 0, 5, 4, 0, 0, 4, 5, 5, 5, 5, 4, 4, 5, 5],
    [4.5, 1580, 0, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0],
    [4.0, 1500, 0, 5, 4, 0, 0, 4, 0, 4, 5, 5, 4, 4, 4, 5],
]

output_data = [
    5,
    35,
]

# Possible inputs for AP classes
APClassList = [
    "US History",
    "Calculus AB",
    "Calculus BC",
    "Statistics",
    "Physics 1",
    "Physics 2",
    "Physics C",
    "Chemistry",
    "European History",
    "Art History",
    "Psychology",
    "Spanish Language",
    "Spanish Literature",
]

# The major_map dictionary associates certain MBTI types with certain majors.
# These are used to recommend a major based off of MBTI.
# This will likely be replaced with a different algorithm later, but for now this is what we have.
major_map = {
    'INTJ' : 'Computer Science',
    'INTP' : 'Engineering',
    'ENTJ' : 'Business',
    'ENTP' : 'Environmental Science',
    'INFJ' : 'Psychology',
    'INFP' : 'Creative Writing',
    'ENFJ' : 'Theatre',
    'ENFP' : 'Architecture',
    'ISTJ' : 'Accounting',
    'ISTP' : 'Nursing',
    'ESFJ' : 'Legal Studies',
    'ESTP' : 'Culinary Arts',
    'ISFJ' : 'Nursing',
    'ISFP' : 'Fashion Design',
    'ESTJ' : 'Criminology',
    'ESFP' : 'Music'
}


# List of dictionaries, each dictionary has "name": <name of school> and "image": <image of school logo>
school_list = [
    {
        "name" : "UCLA",
        "image" : "https://static1.squarespace.com/static/59f78b7b692ebe254ac19deb/t/5a3336ebf9619a424b0ae0e7/1547854847589/?format=1500w",
    },
    {
        "name" : "UCI",
        "image" : "http://jcyte.com/beta/wp-content/uploads/2016/12/UCI-Logo@2x.png"
    },
    {
        "name" : "UIUC",
        "image" : "https://i.pinimg.com/originals/92/1d/64/921d6419779dbe07945feb669761a292.jpg"
    },
    {
        "name" : "USC",
        "image" : "https://identity.usc.edu/files/2019/01/PrimShield-Word_SmallUse_CardOnTrans.png"
    },
    {
        "name" : "UCB",
        "image" : "https://www.kellpartners.com/sites/default/files/client-logos/logo-ucberkeley.png"
    },
    {
        "name" : "ASU",
        "image" : "https://static.sustainability.asu.edu/giosMS-uploads/sites/15/2019/06/ASU_mg-logo-200x55.png"
    },
    {
        "name" : "University of Chicago",
        "image" : "https://d3qi0qp55mx5f5.cloudfront.net/shared-resources/i/template/uc_wordmark_hires.gif"
    },
    {
        "name" : "Cal State Long Beach",
        "image" : "https://micefa.org/wp-content/uploads/2017/09/CSULong-Beach-Logo-300x141.jpg"
    },
]

residence_list = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming"
]


# Uses the planned loan amount and years of payoff to generate a "loan score"
def get_suggested_loan_score(loan_amount, years_payoff):
    if loan_amount > 100000 and years_payoff > 8:
        suggested_loan_sscore = 0.5
        if loan_amount < 100000:
            suggested_loan_score = 1.5
        elif years_payoff < 8:
            suggested_loan_score = 1.5
    return suggested_loan_score


# Maybe a resource for income of each college major?
# https://www.visualcapitalist.com/visualizing-salaries-college-degrees/
@app.route("/getschool/<gpa>/<sat>/<act>/<aplist>/<mbti>/<residence>/<loan_amount>")
def get_suggested_school(gpa, sat, act, aplist, mbti, residence, loan_amount):
    gpa = float(gpa)
    sat = int(sat)
    act = int(act)
    loan_amount = float(loan_amount)
    res = random.choice(school_list)
    if mbti in major_map:  # If their mbti type is found in the major_map, recommend that
        res['major'] = major_map[mbti]
    else:  # otherwise, simply recommend science
        res['major'] = 'Science'
    res = json.dumps(res, separators = (',', ':'))
    print(res)
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0')
