import os
import pathlib
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect
from .forms import VideoForm
from .converter import toaudio
from django.contrib import messages
from .models import Video

def download(request):
    if 'salvo' in request.session:
        ultimovideo = Video.objects.last()
        nomevideo = (ultimovideo.file.name).split('.')

        path = os.path.abspath("audiotodownload.mp3")
        file_server = pathlib.Path(path)
        if not file_server.exists():
            messages.error(request, 'file not found.')
        else:
            file_to_download = open(str(file_server), 'rb')
            response = FileResponse(file_to_download, content_type='audio/mp3')
            response['Content-Disposition'] = 'attachment; filename=%s' % (nomevideo[0] + ".mp3")
            del request.session['salvo']
            return response
        raise Http404
    raise Http404



def salvar_video(request):

    form = VideoForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            imagem = form.save(commit=False)
            imagem.save()
            toaudio()
            messages.success(request, 'Video convertido com sucesso para audio.')
            request.session['salvo'] = True
            return redirect('download')


    return render(request,'index.html',{'form':form})

