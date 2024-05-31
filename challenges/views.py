from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse  # allows us to create paths by refering to the name
from django.template.loader import render_to_string



challenges = {
    "january": "Improve a skill!",
    "february": "Have a great valentine's day with Bree!",
    "march": "Submit Web Scraper Project!",
    "april": "Submit N-Gram Model Project!",
    "may": "Submit finalized paper for publication!",
    "june": "Start internship with MS Transverse!",
    "july": "Finish Django Course!",
    "august": "Start React Course!",
    "september": "Train for GA",
    "october": "Study for MacKellar's Midterm!",
    "november": "Study for Crocetti's Exams!",
    "december": None
}
# User entered a number for the month instead of the name


def index(request):
    months = list(challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def int_monthly_challenge(request, month):
    # Reference the keys of the challenges dictionary
    months = list(challenges.keys())

    # If the user enters a number greater than the length of the dictionary, return a 404 error
    if month > len(challenges):
        return HttpResponseNotFound(str(month) + " is not a month!")

    # Accounting for indexing from 0, duh
    forward_month = months[month - 1]
    # constructs the URL path to /challenge/month
    forward_path = reverse("monthly-challenge", args=[forward_month])
    # as opposed to having it say challenges/number
    # if the main url is changed (ie challenge becomes challenges in monthly_challenges/urls.py)
    # Django will automatically adjust
    return HttpResponseRedirect(forward_path)

# Handles string cases for displaying the challenges dictionary


def monthly_challenge(request, month):
    try:
        challenge_text = challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month,

        })
    except:
        # If the full month name fails, attempt to find a match using abbreviated month names
        month = month.lower()  # Normalize input to lowercase for comparison
        for full_month in challenges.keys():
            if full_month.startswith(month):
                challenge_text = challenges[full_month]
                return render(request, "challenges/challenge.html", {
                    "text": challenge_text,
                    "month": full_month,
                })
        # If no matches are found for either full or abbreviated names, return not found message
        raise Http404()
