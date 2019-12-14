from flask import Flask
from flask_cors import CORS
import json
import random

app = Flask(__name__)
CORS(app)

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
    "Spanish Lieterature",
]

school_list = [
    {
        "name" : "UCLA",
        "image" : "https://reimaginingmigration.org/wp-content/uploads/2019/03/ucla-logo-square.jpg",
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
    "FLorida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illionis",
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
    "",
    "",
    "",
    "",
    "",
    "",
    ""
]


def get_suggested_loan_score(loan_amount, years_payoff):
    if loan_amount > 100000 and years_payoff > 8:
        suggested_loan_sscore = 0.5
        if loan_amount < 100000:
            suggested_loan_score = 1.5
        elif years_payoff < 8:
            suggested_loan_score = 1.5
    return suggested_loan_score


@app.route("/getschool/<gpa>/<sat>/<act>/<aplist>/<mbti>/<residence>/<loan_amount>")
def get_suggested_school(gpa, sat, act, aplist, mbti, residence, loan_amount):
    gpa = float(gpa)
    sat = int(sat)
    act = int(act)
    loan_amount = float(loan_amount)

    res = json.dumps(random.choice(school_list), separators=(',', ':'))
    print(res)
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0')