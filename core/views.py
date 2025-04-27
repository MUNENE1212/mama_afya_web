from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def team(request):
    team_members = [
        {"name": "Eucabeth Awino", "role": "Project Lead"},
        {"name": "Lemmis Murangiri", "role": "AI/ML Engineer"},
        {"name": "Denis Munene Ndegwa", "role": "Mobile Developer"},
        {"name": "Faith Wanjiru Mwangi", "role": "UX Researcher"},
        {"name": "Felix Kipkirui Rotich", "role": "Data Scientist"}
    ]
    return render(request, 'core/team.html', {"team": team_members})

def technical(request):
    return render(request, 'core/technical.html')

