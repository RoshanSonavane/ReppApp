from django.shortcuts import render, redirect
from .models import StudentModel

def pnf(request, exception):
	return redirect("uhome")

def fb(request):
	if request.user.is_authenticated and request.method=="POST":
		na=request.user.username
		wo=request.POST.get("working")
		be=request.POST.get("beautiful")
		us=request.POST.get("useful")
		sf=request.POST.get("suggested")
		sn=request.POST.get("suggestion")

		try:
			usr=StudentModel.objects.get(name=na)
			return render(request, "fb.html",{"msg":"feedback already submitted"})
		except StudentModel.DoesNotExist:
			data=StudentModel(name=na,working=wo,beautiful=be,useful=us,suggested=sf,suggestion=sn)
			data.save()
			return render(request, "fb.html",{"msg":"thanks for ur feedback"})
			
	elif request.user.is_authenticated:
		return render(request, "fb.html")
	else:
		return redirect("uhome")

def about(request):
	return render(request,"about.html")		