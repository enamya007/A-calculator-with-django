from django.shortcuts import render

def index(request):
    result = ""
    if request.method == "POST":
        expression = request.POST.get("expression", "")
        try:
            # On utilise eval() avec prudence pour calculer la chaîne
            # Dans un projet pro, on utiliserait une librairie de parsing mathématique
            result = eval(expression)
        except Exception:
            result = "Erreur"
            
    return render(request, "calculator/index.html", {"result": result})