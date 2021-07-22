from django.shortcuts import render,redirect
import sys
from django.db.models import Sum
from django.contrib.auth.models import User,auth
from codeapp.models import Point
 # superuser - username-dilna15
 #password-dil@2000
# Create your views here.
global total_pt
def index(request):
    return render(request,'index.html')
def editor(request):
    return render(request,'editor.html')
def problem_statements_list(request):
    return render(request,'problem_statements_list.html')
def register(request):
    username_exist= ""
    email_exist= ""
    if request.method == 'POST':
        username= request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            print("username taken")
            username_exist= "Username already exists"
        elif User.objects.filter(email=email).exists():
            print("email already exists")
            email_exist= "Email already exists"
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('login')
    return render(request,'register.html',{"username_exist":username_exist,"email_exist":email_exist})
def login(request):
    mess=""
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            mess="No user found"
    return render(request,'login.html',{"mess":mess})
def logout(request):
    auth.logout(request)
    return redirect('/')
def problem_statement(request):
    if request.user.is_authenticated:
        total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
        total_pt=total_pt['points__sum']
        if total_pt==None:
            total_pt=0
       
        return render(request,'test_cases.html',{"total_pt":total_pt})
    else:
        return redirect('login')
def problem_statement2(request):
    if request.user.is_authenticated:
        total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
        total_pt=total_pt['points__sum']
        if total_pt==None:
            total_pt=0
        return render(request,'test_cases2.html',{"total_pt":total_pt})
    else:
        return redirect('login')
    
def problem_statement3(request):
    if request.user.is_authenticated:
        total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
        total_pt=total_pt['points__sum']
        if total_pt==None:
            total_pt=0
        return render(request,'test_cases3.html',{"total_pt":total_pt})
    else:
        return redirect('login')
    
def problem_statement4(request):
    if request.user.is_authenticated:
        total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
        total_pt=total_pt['points__sum']
        if total_pt==None:
            total_pt=0
        return render(request,'test_cases4.html',{"total_pt":total_pt})
    else:
        return redirect('login')
   
def problem_statement5(request):
    if request.user.is_authenticated:
        total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
        total_pt=total_pt['points__sum']
        if total_pt==None:
            total_pt=0
        return render(request,'test_cases5.html',{"total_pt":total_pt})
    else:
        return redirect('login')
    
def problem_statement6(request):
    if request.user.is_authenticated:
        total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
        total_pt=total_pt['points__sum']
        if total_pt==None:
            total_pt=0
        return render(request,'test_cases6.html',{"total_pt":total_pt})
    else:
        return redirect('login')
   
def problem_statement7(request):
    if request.user.is_authenticated:
        total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
        total_pt=total_pt['points__sum']
        if total_pt==None:
            total_pt=0
        return render(request,'test_cases7.html',{"total_pt":total_pt})
    else:
        return redirect('login')

def run(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ")
        def input():
            a = input_part
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
    res = render(request,'editor.html',{"code":code_part,"output":output,"input":y})
    return res
def run_testcases(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ")
        
        def input():
            a = input_part
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
            #print(test['test_case1'])
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
        #print(output)
    res = render(request,'test_cases.html',{"code":code_part,"output":output,"input":y,"total_pt":total_pt})
    return res
def run_testcases2(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ")
        
        def input():
            a = input_part
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
            #print(test['test_case1'])
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
        #print(output)
    res = render(request,'test_cases2.html',{"code":code_part,"output":output,"input":y,"total_pt":total_pt})
    return res
def run_testcases3(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ")
       
        def input():
            a = input_part
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
            #print(test['test_case1'])
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
        #print(output)
    res = render(request,'test_cases3.html',{"code":code_part,"output":output,"input":y,"total_pt":total_pt})
    return res
def run_testcases4(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ")
        
        def input():
            a = input_part
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
            #print(test['test_case1'])
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
        #print(output)
    res = render(request,'test_cases4.html',{"code":code_part,"output":output,"input":y,"total_pt":total_pt})
    return res
def run_testcases5(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ")
       
        def input():
            a = input_part
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
            #print(test['test_case1'])
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
        #print(output)
    res = render(request,'test_cases5.html',{"code":code_part,"output":output,"input":y,"total_pt":total_pt})
    return res
def run_testcases6(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ")
        
        def input():
            a = input_part
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
            #print(test['test_case1'])
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
        #print(output)
    res = render(request,'test_cases6.html',{"code":code_part,"output":output,"input":y,"total_pt":total_pt})
    return res
def run_testcases7(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ")
        
        def input():
            a = input_part
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
            #print(test['test_case1'])
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
        #print(output)
    res = render(request,'test_cases7.html',{"code":code_part,"output":output,"input":y,"total_pt":total_pt})
    return res
def submit_testcases(request):
    if request.method == 'POST':
        inputt="1 2"
        outputt="3713081631934410656"
        code_part = request.POST['code_area']
        #input_part = request.POST['input_area']
        y = inputt
        inputt = inputt
        def input():
            a = inputt
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
            output=output[:-1]
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
        if output==outputt:
                test_case_accepted="Accepted"
                if Point.objects.filter(username=request.user).filter(ques_attempted=1).exists():
                    total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                    total_pt=total_pt['points__sum']
                    
                else:
                    point=Point(username=request.user,points=10,ques_attempted=1)
                    point.save()
                    total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                    total_pt=total_pt['points__sum']
                   
        else:
                test_case_accepted="Not accepted"
                total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                total_pt=total_pt['points__sum']
                if total_pt==None:
                    total_pt=0
               
    res = render(request,'test_cases.html',{"code":code_part,"test_case_accepted":test_case_accepted,"inputt":y,"outputt":outputt,"output1":output,"your_input":"Your Input is:","expected_output":"Expected output is:","your_output":"Your Output is:","total_pt":total_pt})
    return res
def submit_testcases2(request):
    if request.method == 'POST':
        inputt="10"
        outputt="12345678910"
        code_part = request.POST['code_area']
        #input_part = request.POST['input_area']
        y = inputt
        inputt = inputt
        def input():
            a = inputt
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
            output=output[:-1]            
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
               
        if output==outputt:
                test_case_accepted="Accepted"
                if Point.objects.filter(username=request.user).filter(ques_attempted=2).exists():
                    total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                    total_pt=total_pt['points__sum']
                   
                else:
                    point=Point(username=request.user,points=10,ques_attempted=2)
                    point.save()
                    total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                    total_pt=total_pt['points__sum']
                    
        else:
                test_case_accepted="Not accepted"
                total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                total_pt=total_pt['points__sum']
                if total_pt==None:
                    total_pt=0
               
    res = render(request,'test_cases2.html',{"code":code_part,"test_case_accepted":test_case_accepted,"inputt":y,"outputt":outputt,"output1":output,"your_input":"Your Input is:","expected_output":"Expected output is:","your_output":"Your Output is:","total_pt":total_pt})
    return res  
def submit_testcases3(request):

    if request.method == 'POST':
        inputt="1011 1023"
        outputt="0\n0.9882697947214076"
        code_part = request.POST['code_area']
        #input_part = request.POST['input_area']
        y = inputt
        inputt = inputt
        def input():
            a = inputt
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
            output=output[:-1]
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
        if output==outputt:
                test_case_accepted="Accepted"
                if Point.objects.filter(username=request.user).filter(ques_attempted=3).exists():
                    
                    total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                    total_pt=total_pt['points__sum']
                    
                else:
                    point=Point(username=request.user,points=10,ques_attempted=3)
                    point.save()
                    total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                    total_pt=total_pt['points__sum']
                    
        else:
                test_case_accepted="Not accepted"
                total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                total_pt=total_pt['points__sum']
                if total_pt==None:
                    total_pt=0
                
    res = render(request,'test_cases3.html',{"code":code_part,"test_case_accepted":test_case_accepted,"inputt":y,"outputt":outputt,"output1":output,"your_input":"Your Input is:","expected_output":"Expected output is:","your_output":"Your Output is:","total_pt":total_pt})
    return res  
def submit_testcases4(request):
    if request.method == 'POST':
        inputt="sss sgehrg avdjfw afgwjgwr ahfgwgwur ahfgewugqeu ahfgwugwuwrg kfwugreughwrgwgbjlgglr"
        outputt="sss-sgehrg-avdjfw-afgwjgwr-ahfgwgwur-ahfgewugqeu-ahfgwugwuwrg-kfwugreughwrgwgbjlgglr"
        code_part = request.POST['code_area']
        #input_part = request.POST['input_area']
        y = inputt
        inputt = inputt
        def input():
            a = inputt
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
            output=output[:-1]
            
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
        if output==outputt:
                test_case_accepted="Accepted"
                if Point.objects.filter(username=request.user).filter(ques_attempted=4).exists():
                    
                    total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                    total_pt=total_pt['points__sum']
                    
                else:
                    point=Point(username=request.user,points=10,ques_attempted=4)
                    point.save()
                    total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                    total_pt=total_pt['points__sum']
                   
        else:
                test_case_accepted="Not accepted"
                total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                total_pt=total_pt['points__sum']
                if total_pt==None:
                    total_pt=0
               
    res = render(request,'test_cases4.html',{"code":code_part,"test_case_accepted":test_case_accepted,"inputt":y,"outputt":outputt,"output1":output,"your_input":"Your Input is:","expected_output":"Expected output is:","your_output":"Your Output is:","total_pt":total_pt})
    return res  
def submit_testcases5(request):
    if request.method == 'POST':
        inputt="3455"
        outputt="False"
        code_part = request.POST['code_area']
        #input_part = request.POST['input_area']
        y = inputt
        inputt = inputt
        def input():
            a = inputt
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
            output=output[:-1]
            
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
        if output==outputt:
                test_case_accepted="Accepted"
                if Point.objects.filter(username=request.user).filter(ques_attempted=5).exists():
                    
                    total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                    total_pt=total_pt['points__sum']
                    
                else:
                    point=Point(username=request.user,points=10,ques_attempted=5)
                    point.save()
                    total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                    total_pt=total_pt['points__sum']
                   
        else:
                test_case_accepted="Not accepted"
                total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                total_pt=total_pt['points__sum']
                if total_pt==None:
                    total_pt=0
                
    res = render(request,'test_cases5.html',{"code":code_part,"test_case_accepted":test_case_accepted,"inputt":y,"outputt":outputt,"output1":output,"your_input":"Your Input is:","expected_output":"Expected output is:","your_output":"Your Output is:","total_pt":total_pt})
    return res  
def submit_testcases6(request):
    if request.method == 'POST':
        inputt="100"
        outputt="Not Weird"
        code_part = request.POST['code_area']
        #input_part = request.POST['input_area']
        y = inputt
        inputt = inputt
        def input():
            a = inputt
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
            output=output[:-1]
            
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
        if output==outputt:
                test_case_accepted="Accepted"
                if Point.objects.filter(username=request.user).filter(ques_attempted=6).exists():
                   
                    total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                    total_pt=total_pt['points__sum']
                   
                else:
                    point=Point(username=request.user,points=10,ques_attempted=6)
                    point.save()
                    total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                    total_pt=total_pt['points__sum']
                    
        else:
                test_case_accepted="Not accepted"
                total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                total_pt=total_pt['points__sum']
                if total_pt==None:
                    total_pt=0
                
    res = render(request,'test_cases6.html',{"code":code_part,"test_case_accepted":test_case_accepted,"inputt":y,"outputt":outputt,"output1":output,"your_input":"Your Input is:","expected_output":"Expected output is:","your_output":"Your Output is:","total_pt":total_pt})
    return res  
def submit_testcases7(request):
    if request.method == 'POST':
        inputt="9"
        outputt="0\n1\n4\n9\n16\n25\n36\n49\n64"
        code_part = request.POST['code_area']
        #input_part = request.POST['input_area']
        y = inputt
        inputt = inputt
        def input():
            a = inputt
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
            output=output[:-1]
            
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
            total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
            total_pt=total_pt['points__sum']
            if total_pt==None:
                total_pt=0
        if output==outputt:
                test_case_accepted="Accepted"
                if Point.objects.filter(username=request.user).filter(ques_attempted=7).exists():
                    
                    total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                    total_pt=total_pt['points__sum']
                    
                else:
                    point=Point(username=request.user,points=10,ques_attempted=7)
                    point.save()
                    total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                    total_pt=total_pt['points__sum']
                    
        else:
                test_case_accepted="Not accepted"
                total_pt=Point.objects.filter(username=request.user).aggregate(Sum('points'))
                total_pt=total_pt['points__sum']
                if total_pt==None:
                    total_pt=0
               
    res = render(request,'test_cases7.html',{"code":code_part,"test_case_accepted":test_case_accepted,"inputt":y,"outputt":outputt,"output1":output,"your_input":"Your Input is:","expected_output":"Expected output is:","your_output":"Your Output is:","total_pt":total_pt})
    return res 
