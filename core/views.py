from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def team(request):
    team = [
        {
            'name': 'Dr. Nderu',
            'role': 'Project supervisor',
            'image': 'images/team/nderu.jpg',
            'bio': 'OB/GYN with 15 years of experience in maternal health across rural Kenya. Leading the clinical validation of MamaGuardian AI.'
        },
        {
            'name': 'Eucabeth Awino',
            'role': 'Project Lead',
            'bio': 'Extensive experience in public health management...',
            'image': 'images/team/eucabeth.jpg',
        },
        {
            'name': 'Lemmis Murangiri',
            'role': 'AI/ML Engineer',
            'bio': 'Specializes in healthcare machine learning applications...',
            'image': 'images/team/lemmis.jpg',
        },
        {
            'name': 'Felix Rotich',
            'role': 'AI/ML Engineer',
            'bio': 'Specializes in healthcare machine learning applications...',
            'image': 'images/team/lemmis.jpg',
        }, 
        {
             'name': 'Faith Mwangi',
            'role': 'Project desighner',
            'bio': 'Specializes in ',
            'image': 'images/team/faith.jpg',
        },
        {
            'name': 'Denis Ndegwa',
            'role': 'Backend developer',
            'bio': 'Denis Munene Ndegwa is a data-driven engineer and machine learning enthusiast who led the backend development and containerization of the Maternal Risk Prediction API. Leveraging his skills in Python and FastAPI, Denis designed and implemented RESTful endpoints, integrated MongoDB for data persistence, and managed the entire Docker-based containerization process to ensure the application is scalable and deployable. His work focused on ensuring reliable API performance while integrating machine learning predictions to support maternal health interventions in Kenya.',
            'image': 'static/images/team/munene.jpeg',
        }
    ]

    partners = []
    

    return render(request, 'core/team.html', {'team': team, 'partners': partners})

def technical(request):
    return render(request, 'core/technical.html')

