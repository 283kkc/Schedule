from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, EndForm
from .models import Staff, Entry
import datetime

import pdb
#pdb.set_trace()

# Create your views here.

def edit(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            staff = Staff.objects.get(pk=request.POST.get('staff'))
            # 本日出社のレコードがなければ作成する。
            try:
                entry = Entry.objects.get(staff=staff, date=datetime.date.today())
            except:
                entry = Entry.objects.create(staff=staff)
            choice = int(request.POST.get('choice'))
            entry.timestamp(choice)
            #退社するなら休憩時間を入力
            if choice == 0:
                return redirect('schedule:index')
            elif choice == 1:
                return redirect('schedule:end', pk=entry.pk)
    else:
        form = PostForm()
    return render(request, 'schedule/edit.html', {'form': form})

def end(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        form = EndForm(request.POST)
        if form.is_valid():
            entry.timeOfBreak = int(request.POST.get('timeOfBreak'))
            entry.save()
            return redirect('schedule:index')
    else:
        form = EndForm()
    return render(request, 'schedule/end.html', {'form': form})

def index(request):
    return render(request, 'schedule/index.html')

