from django.contrib import admin
from django.urls import path
from codeapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('editor',views.editor,name="editor"),
    path('problem-statements-list',views.problem_statements_list,name="problem_statements_list"),
    path('problem_statement',views.problem_statement,name="problem_statement"),
    path('problem_statement2',views.problem_statement2,name="problem_statement2"),
    path('problem_statement3',views.problem_statement3,name="problem_statement3"),
    path('problem_statement4',views.problem_statement4,name="problem_statement4"),
    path('problem_statement5',views.problem_statement5,name="problem_statement5"),
    path('problem_statement6',views.problem_statement6,name="problem_statement6"),
    path('problem_statement7',views.problem_statement7,name="problem_statement7"),
    path('run',views.run,name="run"),
    path('run_testcases',views.run_testcases,name="run"),
    path('run_testcases2',views.run_testcases2,name="run2"),
    path('run_testcases3',views.run_testcases3,name="run3"),
    path('run_testcases4',views.run_testcases4,name="run4"),
    path('run_testcases5',views.run_testcases5,name="run5"),
    path('run_testcases6',views.run_testcases6,name="run6"),
    path('run_testcases7',views.run_testcases7,name="run7"),
    path('submit_testcases',views.submit_testcases,name="submit_testcases"),
    path('submit_testcases2',views.submit_testcases2,name="submit_testcases2"),
    path('submit_testcases3',views.submit_testcases3,name="submit_testcases3"),
    path('submit_testcases4',views.submit_testcases4,name="submit_testcases4"),
    path('submit_testcases5',views.submit_testcases5,name="submit_testcases5"),
    path('submit_testcases6',views.submit_testcases6,name="submit_testcases6"),
    path('submit_testcases7',views.submit_testcases7,name="submit_testcases7")
]
