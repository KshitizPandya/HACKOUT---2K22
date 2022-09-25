from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def card(request):
    # a = "physical verification of registered office new initiative by mca"
    # a1 = "https://singhania.in/blog/physical-verification-of-registered-office-new-initiative-by-mca"
    b = 'shareholder has no right to litigate on behalf of its spv in contractual matters '
    b1 = 'https://singhania.in/blog/shareholder-has-no-right-to-litigate-on-behalf-of-its-spv-in-contractual-matters-'
    c = 'meity proposed changes to it rules 2021'
    c1 = 'https://singhania.in/blog/meity-proposed-changes-to-it-rules-2021'
    d = 'direction for the compulsory license of the lifesaving breast cancer drug ribociclib '
    d1 = 'https://singhania.in/blog/direction-for-the-compulsory-license-of-the-lifesaving-breast-cancer-drug-ribociclib'
    e = 'cross charging under goods and services tax act'
    e1 = 'https://singhania.in/blog/cross-charging-under-goods-and-services-tax-act'
    return render(request, 'cardnew.html', {'a':"physical verification of registered office new initiative by mca", 'a1':"https://singhania.in/blog/physical-verification-of-registered-office-new-initiative-by-mca", 'b':b, 'b1':b1, 'c':c, 'c1':c1, 'd':d, 'd1':d1, 'e':e, 'e1':e1})