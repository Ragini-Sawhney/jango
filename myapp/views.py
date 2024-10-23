from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse 
# Create your views here.
from .models import  Student  # Import the Student model
# from .models import Login
from .models import Profile

def home(request):
    names = ["ankit","kartik","kiya","monica"]
    return render(request,'home.html',{'names': names})


def about(request):
    detail=[
        {
         "name":"Ragini",
        "age":28,
        "height":5,
        "weight":40,
        "Hobby":["cricket","badminton","table tennis"]
        },
          {
        "name":"Ankit",
        "age":27,
        "height":6,
        "weight":50,
        "Hobby":["cricket","badminton","table tennis"]
        },
          {
        "name":"Rahul",
        "age":28,
        "height":5,
        "weight":55,
        "Hobby":["cricket","badminton","table tennis"]
        },
          {
        "name":"Kartik",
        "age":28,
        "height":5,
        "weight":56,
        "Hobby":["cricket","badminton","table tennis"]
        }
    ]
    return render(request,'about.html',{'detail':detail})

def contactus(request):
   
    return render(request,'contact.html')



def student_view(request):  # Rename the view function
    data=Student.objects.all()
    if request.method == "POST":
        form_data = request.POST
        first_name = form_data.get("first_name")
        last_name = form_data.get("last_name")
        age = form_data.get("age")
        discription = form_data.get("discription")  # Note: Ensure the spelling matches the model

        # Create an instance of Student and save it to the database
        s1 = Student(
            first_name=first_name,
            last_name=last_name,
            age=age,
            discription=discription  # Make sure this matches the model field name
        )
        s1.save()

        data=Student.objects.all()
        return redirect('student')


    return render(request,'student.html',{'data':data})

def delete_student(request,id):
    s1=Student.objects.filter(id=id)
    s1.delete()
    

    return redirect('student')


def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == 'POST':
        
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.age = request.POST.get('age')
        student.discription = request.POST.get('discription') 

        student.save()  
        return redirect('student')  
    
  
    return render(request, 'update_student.html', {'student': student})
   
       



# def login(request):
#     data = Login.objects.all()
    
#     if request.method == "POST":
#         form_data = request.POST
#         user_name = form_data.get("user_name")
#         email = form_data.get("email")
#         password = form_data.get("password")

#         # Check for username
#         if not user_name:
#             return render(request, 'login.html', {'data': data, 'error': 'Username is required'})

#         # Now save the new entry since user_name is valid
#         s2 = Login(  # Create a new instance of Login
#             user_name=user_name,
#             email=email,
#             password=password  # Make sure this matches the model field name
#         )
#         s2.save()  # Save to the database
        
#         data = Login.objects.all()  # Refresh data after saving

#     return render(request, 'login.html', {'data': data})


def profile(request):
    profile=Profile.objects.all()
    if request.method=='POST':
        data=request.POST
        files=request.FILES
        name=data.get('name')
        profile_picture=files.get('profile_picture')
        bio=data.get('bio')
        print(name)
        print(profile_picture)
        print(bio)
      
        Profile.objects.create(name=name,profile_picture=profile_picture,bio=bio)
        profile=Profile.objects.all()
        return redirect('profile')
    
    return render(request,'profile.html',{'profile':profile})


def home(request):
    return render(request,'index.html')

