from django.shortcuts import render

from django.http import HttpResponse

from django import forms

from django.views.decorators.csrf import csrf_exempt

import numpy as np

import sys

# Create your views here.
def index(request):

    context = {
        
    }

    return render(request, 'index.html', context=context)

def gauss(request):
    
    context = {
        
    }

    return render(request, 'gauss.html', context=context)

def jordan(request):
    
    context = {
        
    }

    return render(request, 'jordan.html', context=context)

def jacobi(request):
    
    context = {
        
    }

    return render(request, 'jacobi.html', context=context)

def gaussseidel(request):
    
    context = {
        
    }

    return render(request, 'gaussseidel.html', context=context)


@csrf_exempt
def resultgauss(request):

    n = request.POST['n']
    array = request.POST.getlist('array[]')

    n = int(n)

    a = np.zeros((n,n+1))

    x = np.zeros(n)

    k = 0

    string = ""

    string += "<link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'><form class='w3-container w3-card-4' action='/' method='get'><h2 class='w3-text-blue'>Metodo de Gauss</h2>"

    for i in range(n):
        for j in range(n+1):
            a[i][j] = array[k]
            k+=1

    string += "<p><label class='w3-text-blue'>Matriz Digitada: </label><br><br>"+str(a)+"<br>"

    string = string.replace('[[','[')
    string = string.replace(']]',']')
    string = string.replace(']',']')

    string += "<p><label class='w3-text-blue'>Substituições Matrizes: </label><br><h3>"

    for i in range(n):
        if a[i][i] == 0.0:
            
            return HttpResponse('Erro de divisão por zero detectada!')

        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
                string += str(a)+"<br>"

    string = string.replace('[[','[')
    string = string.replace(']]',']')
    string = string.replace(']',']<br>')

    string += "</h3><p><label class='w3-text-blue'>Resultado: </label>"
    
    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
            
        x[i] = x[i]/a[i][i]
        print(x)

    for i in range(n):
        string += '<h3>X' + str(i+1) + " = " + str(x[i])  + "</h3> "

    string += "<br><br><p><input class='w3-btn w3-blue' type='submit' value='Voltar ao Menu'></p></form>"

    return HttpResponse(string)


@csrf_exempt
def resultjordan(request):

    n = request.POST['n']
    array = request.POST.getlist('array[]')

    n = int(n)

    a = np.zeros((n,n+1))

    x = np.zeros(n)

    k = 0

    string = "<link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'><form class='w3-container w3-card-4' action='/' method='get'><h2 class='w3-text-blue'>Metodo de Jordan</h2>"

    for i in range(n):
        for j in range(n+1):
            a[i][j] = array[k]
            k+=1

    string += "<p><label class='w3-text-blue'>Matriz Digitada: </label><br><br>"+str(a)+"<br>"

    string = string.replace('[[','[')
    string = string.replace(']]',']')
    string = string.replace(']',']')

    string += "<p><label class='w3-text-blue'>Substituições Matrizes: </label><br><h3>"

    for i in range(n):
        if a[i][i] == 0.0:
            return HttpResponse('Erro de divisão por zero detectada!')
            
        for j in range(n):
            if i != j:
                ratio = a[j][i]/a[i][i]
                print(ratio)
                for k in range(n+1):
                    print(a[j][k])
                    print(a[i][k])
                    a[j][k] = a[j][k] - ratio * a[i][k]
                    string += str(a)+"<br>"
                    print(a[j][k])
                    print(a)

    string = string.replace('[[','[')
    string = string.replace(']]',']')
    string = string.replace(']',']<br>')

    for i in range(n):
        x[i] = a[i][n]/a[i][i]
        print(a[i][n])
        print(a[i][i])
        print(x[i])

    string += "</h3><p><label class='w3-text-blue'>Resultado: </label>"

    for i in range(n):
        string += '<h3>X' + str(i+1) + " = " + str(x[i])  + "</h3> "

    string += "<br><br><p><input class='w3-btn w3-blue' type='submit' value='Voltar ao Menu'></p></form>"

    return HttpResponse(string)

@csrf_exempt
def resultjacobi(request):

    string = "<link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'><form class='w3-container w3-card-4' action='/' method='get'><h2 class='w3-text-blue'>Metodo de jacobi</h2><p><label class='w3-text-blue'>Resultado: </label>"

    n = request.POST['n']

    n = int(n)

    arrayA = request.POST.getlist('arrayA[]')
    arrayB = request.POST.getlist('arrayB[]')

    aA = np.zeros((n,n))
    aB = np.zeros((n))

    k = 0

    for i in range(n):
        for j in range(n):
            aA[i][j] = arrayA[k]
            k+=1

    for i in range(n):
        aB[i] = arrayB[i]

    ITERATION_LIMIT = 500

    A = np.array(aA)
    b = np.array(aB)

    x = np.zeros_like(b)
    for it_count in range(ITERATION_LIMIT):
        if it_count != 0:
            print("Interção {0}: {1}".format(it_count, x))
            string += "<br>Interação {0}: {1}".format(it_count, x) + " \n"
        x_new = np.zeros_like(x)

        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x[:i])
            print(s1)
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            print(s2)
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
            print(x_new[i])
            if x_new[i] == x_new[i-1]:
                break

        if np.allclose(x, x_new, atol=1e-10, rtol=0.):
            break

        x = x_new

    error = np.dot(A, x) - b
    string += '<br><br>Solucao: ' + str(x) + "<br>Erro: " + str(error)

    string += "<br><br><p><input class='w3-btn w3-blue' type='submit' value='Voltar ao Menu'></p></form>"

    return HttpResponse(string)

@csrf_exempt
def resultgaussseidel(request):

    string = "<link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'><form class='w3-container w3-card-4' action='/' method='get'><h2 class='w3-text-blue'>Metodo de Gauss-Seidel</h2><p><label class='w3-text-blue'>Resultado: </label>"

    n = request.POST['n']

    n = int(n)

    arrayA = request.POST.getlist('arrayA[]')
    arrayB = request.POST.getlist('arrayB[]')

    aA = np.zeros((n,n))
    aB = np.zeros((n))

    k = 0

    for i in range(n):
        for j in range(n):
            aA[i][j] = arrayA[k]
            k+=1

    for i in range(n):
        aB[i] = arrayB[i]

    ITERATION_LIMIT = 500

    A = np.array(aA)
    b = np.array(aB)

    x = np.zeros_like(b)
    for it_count in range(1, ITERATION_LIMIT):
        x_new = np.zeros_like(x)
        print("Interação {0}: {1}".format(it_count, x))
        string += "<br>Interacao {0}: {1}".format(it_count, x) + " \n"
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1 :], x[i + 1 :])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_new, rtol=1e-8):
            break
        x = x_new

    error = np.dot(A, x) - b
    string += '<br><br>Solucao: ' + str(x) + "<br>Erro: " + str(error)

    string += "<br><br><p><input class='w3-btn w3-blue' type='submit' value='Voltar ao Menu'></p></form>"

    return HttpResponse(string)