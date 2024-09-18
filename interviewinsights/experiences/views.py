from django.shortcuts import render, redirect
from .models import InterviewExperience

# Home page view
def home(request):
    return render(request, 'home.html')

# View to handle experience submission
def submit_experience(request):
    if request.method == 'POST':
        candidate_name = request.POST.get('candidate_name')
        college_name = request.POST.get('college_name')
        company_name = request.POST.get('company_name')
        tips_advice = request.POST.get('tips_advice')
        
        # Save the data to the database
        InterviewExperience.objects.create(
            candidate_name=candidate_name,
            college_name=college_name,
            company_name=company_name,
            tips_advice=tips_advice
        )
        
        return redirect('home')
    return render(request, 'submit_experience.html')

# View to search experiences
def search_experiences(request):
    query = request.GET.get('query')
    if query:
        experiences = InterviewExperience.objects.filter(
            models.Q(company_name__icontains=query) |
            models.Q(college_name__icontains=query)
        )
    else:
        experiences = InterviewExperience.objects.all()

    return render(request, 'search_results.html', {'experiences': experiences, 'query': query})
