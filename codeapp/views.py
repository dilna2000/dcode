from django.shortcuts import render
import sys

# Create your views here.
def index(request):
    return render(request,'index.html')
def editor(request):
    return render(request,'editor.html')
def problem_statements_list(request):
    return render(request,'problem_statements_list.html')
def problem_statement(request):
    return render(request,'test_cases.html')
def problem_statement2(request):
    return render(request,'test_cases2.html')
def problem_statement3(request):
    return render(request,'test_cases3.html')
def problem_statement4(request):
    return render(request,'test_cases4.html')
def problem_statement5(request):
    return render(request,'test_cases5.html')
def problem_statement6(request):
    return render(request,'test_cases6.html')
def problem_statement7(request):
    return render(request,'test_cases7.html')
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
        print(output)
    res = render(request,'editor.html',{"code":code_part,"output":output,"input":y})
    return res
def run_testcases(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ")
        print(input_part)
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
            #print(test['test_case1'])
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        #print(output)
    res = render(request,'test_cases.html',{"code":code_part,"output":output,"input":y})
    return res
def run_testcases2(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ")
        print(input_part)
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
            #print(test['test_case1'])
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        #print(output)
    res = render(request,'test_cases2.html',{"code":code_part,"output":output,"input":y})
    return res
def run_testcases3(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ")
        print(input_part)
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
            #print(test['test_case1'])
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        #print(output)
    res = render(request,'test_cases3.html',{"code":code_part,"output":output,"input":y})
    return res
def run_testcases4(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ")
        print(input_part)
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
            #print(test['test_case1'])
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        #print(output)
    res = render(request,'test_cases4.html',{"code":code_part,"output":output,"input":y})
    return res
def run_testcases5(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ")
        print(input_part)
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
            #print(test['test_case1'])
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        #print(output)
    res = render(request,'test_cases5.html',{"code":code_part,"output":output,"input":y})
    return res
def run_testcases6(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ")
        print(input_part)
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
            #print(test['test_case1'])
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        #print(output)
    res = render(request,'test_cases6.html',{"code":code_part,"output":output,"input":y})
    return res
def run_testcases7(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ")
        print(input_part)
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
            #print(test['test_case1'])
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        #print(output)
    res = render(request,'test_cases7.html',{"code":code_part,"output":output,"input":y})
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
            if output==outputt:
                test_case_accepted="Accepted"
            else:
                test_case_accepted="Not accepted"
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
    res = render(request,'test_cases.html',{"code":code_part,"test_case_accepted":test_case_accepted,"inputt":y,"outputt":outputt,"output1":output,"your_input":"Your Input is:","expected_output":"Expected output is:","your_output":"Your Output is:"})
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
            if output==outputt:
                test_case_accepted="Accepted"
            else:
                test_case_accepted="Not accepted"
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
    res = render(request,'test_cases2.html',{"code":code_part,"test_case_accepted":test_case_accepted,"inputt":y,"outputt":outputt,"output1":output,"your_input":"Your Input is:","expected_output":"Expected output is:","your_output":"Your Output is:"})
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
            if output==outputt:
                test_case_accepted="Accepted"
            else:
                test_case_accepted="Not accepted"
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
    res = render(request,'test_cases3.html',{"code":code_part,"test_case_accepted":test_case_accepted,"inputt":y,"outputt":outputt,"output1":output,"your_input":"Your Input is:","expected_output":"Expected output is:","your_output":"Your Output is:"})
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
            if output==outputt:
                test_case_accepted="Accepted"
            else:
                test_case_accepted="Not accepted"
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
    res = render(request,'test_cases4.html',{"code":code_part,"test_case_accepted":test_case_accepted,"inputt":y,"outputt":outputt,"output1":output,"your_input":"Your Input is:","expected_output":"Expected output is:","your_output":"Your Output is:"})
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
            if output==outputt:
                test_case_accepted="Accepted"
            else:
                test_case_accepted="Not accepted"
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
    res = render(request,'5.html',{"code":code_part,"test_case_accepted":test_case_accepted,"inputt":y,"outputt":outputt,"output1":output,"your_input":"Your Input is:","expected_output":"Expected output is:","your_output":"Your Output is:"})
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
            if output==outputt:
                test_case_accepted="Accepted"
            else:
                test_case_accepted="Not accepted"
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
    res = render(request,'6.html',{"code":code_part,"test_case_accepted":test_case_accepted,"inputt":y,"outputt":outputt,"output1":output,"your_input":"Your Input is:","expected_output":"Expected output is:","your_output":"Your Output is:"})
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
            if output==outputt:
                test_case_accepted="Accepted"
            else:
                test_case_accepted="Not accepted"
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
    res = render(request,'test_cases7.html',{"code":code_part,"test_case_accepted":test_case_accepted,"inputt":y,"outputt":outputt,"output1":output,"your_input":"Your Input is:","expected_output":"Expected output is:","your_output":"Your Output is:"})
    return res 
