from django.shortcuts import render, redirect
from .models import Student, Resource
from django.contrib.auth.decorators import login_required


@login_required

def home(request):

    query = request.GET.get('q')

    if query:

        students = Student.objects.filter(
            skill__icontains=query
        )

    else:

        students = Student.objects.all()



    total_students = Student.objects.count()


    total_skills = Student.objects.values(
        'skill'
    ).distinct().count()



    matches = []


    all_students = Student.objects.all()



    for s1 in all_students:

        for s2 in all_students:


            if (

                s1 != s2

                and

                s1.skill.lower()

                ==

                s2.need.lower()

            ):


                matches.append(

                    (

                        s1.name,

                        s2.name

                    )

                )



    notification_count = len(
        matches
    )



    skill_names = []


    skill_counts = []



    for skill in Student.objects.values(
        'skill'
    ).distinct():

        name = skill['skill']


        count = Student.objects.filter(
            skill=name
        ).count()



        skill_names.append(
            name
        )


        skill_counts.append(
            count
        )




    return render(

        request,

        'home.html',

        {

            'students':
            students,


            'total_students':
            total_students,


            'total_skills':
            total_skills,


            'matches':
            matches,


            'notification_count':
            notification_count,


            'skill_names':
            skill_names,


            'skill_counts':
            skill_counts,

        }

    )




@login_required
def add_student(request):


    if request.method == 'POST':


        name = request.POST['name']


        skill = request.POST['skill']


        need = request.POST['need']


        college = request.POST['college']



        Student.objects.create(

            user=request.user,

            name=name,

            skill=skill,

            need=need,

            college=college

        )



        return redirect('/')



    return render(
        request,
        'add_student.html'
    )

@login_required
def profile(request):

    student = Student.objects.filter(
        user=request.user
    ).first()

    return render(
        request,
        "profile.html",
        {
            "student": student
        }
    )

@login_required
def edit_profile(request):

    student = Student.objects.filter(
        user=request.user
    ).first()

    if request.method == "POST":

        student.name = request.POST["name"]
        student.college = request.POST["college"]
        student.skill = request.POST["skill"]
        student.need = request.POST["need"]

        student.save()

        return redirect("/profile/")

    return render(
        request,
        "edit_profile.html",
        {
            "student": student
        }
    )

@login_required
def resources(request):

    resources = Resource.objects.all()

    return render(
        request,
        "resources.html",
        {
            "resources": resources
        }
    )