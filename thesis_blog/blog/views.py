from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Thesis, Comment
from .forms import ThesisForm, CommentForm

def thesis_list(request):
    theses = Thesis.objects.filter(status='published').order_by('-date')
    paginator = Paginator(theses, 10)  # Show 10 theses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/thesis_list.html', {'page_obj': page_obj})

def thesis_detail(request, pk):
    thesis = get_object_or_404(Thesis, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.thesis = thesis
            comment.save()
            return redirect('thesis_detail', pk=thesis.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/thesis_detail.html', {'thesis': thesis, 'form': form})

def thesis_new(request):
    if request.method == 'POST':
        form = ThesisForm(request.POST)
        if form.is_valid():
            thesis = form.save(commit=False)
            thesis.save()
            return redirect('thesis_detail', pk=thesis.pk)
    else:
        form = ThesisForm()
    return render(request, 'blog/thesis_edit.html', {'form': form})

def thesis_edit(request, pk):
    thesis = get_object_or_404(Thesis, pk=pk)
    if request.method == 'POST':
        form = ThesisForm(request.POST, instance=thesis)
        if form.is_valid():
            thesis = form.save(commit=False)
            thesis.save()
            return redirect('thesis_detail', pk=thesis.pk)
    else:
        form = ThesisForm(instance=thesis)
    return render(request, 'blog/thesis_edit.html', {'form': form})
