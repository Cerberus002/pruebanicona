from django.shortcuts import render, redirect
from AppPrueba.models import Inscritos
from AppPrueba.forms import FormInscritos
from django.http import JsonResponse
from AppPrueba.models import Inscritos, Institucion
from .serialiazers import InscritosSerializer, InstitucionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listarParticipante(request):
    pro = Inscritos.objects.all()
    data = {'Inscritos': pro}
    return render(request, 'listarparticipante.html', data)

def agregarParticipante(request):
    form = FormInscritos()
    if request.method == 'POST':
        form = FormInscritos(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarparticipante.html', data)

def eliminarParticipante(request, id):
    pro = Inscritos.objects.get(id = id)
    pro.delete()
    return redirect('/participantes')

def actualizaParticipante(request, id):
    pro = Inscritos.objects.get(id = id)
    form = FormInscritos(instance=pro)
    if request.method == 'POST':
        form = FormInscritos(request.POST, instance=pro)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregarparticipante.html', data)

#------------------------------------------------------------
def verisncritosDb(request):
    proyecto = Inscritos.objects.all()
    data = {'Inscritos' : list(proyecto.values('id', 'nombre', 'telefono', 'fechaInscripcion', 'institucion', 'horainscripcion', 'estado', 'observacion'))}

    return JsonResponse(data)


#------------------------------------------------------------
class ListarInscrito(APIView):

    def get(self, request):
        estu = Inscritos.objects.all()
        serial = InscritosSerializer(estu, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritosSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetalleInscrito(APIView):

    def get_object(self, pk):
        try:
            return Inscritos.objects.get(pk=pk)
        except Inscritos.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        estu = self.get_object(pk)
        serial = InscritosSerializer(estu)
        return Response(serial.data)

    def put(self, request, pk):
        estu = self.get_object(pk)
        serial = InscritosSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        estu = self.get_object(pk)
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#---------------------------------------------------------------
@api_view(['GET', 'POST'])
def inscrito_list(request):
    if request.method == 'GET':
        estu = Institucion.objects.all()
        serial = InstitucionSerializer(estu, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def inscrito_detalle(request, pk):
    try:
        estu = Institucion.objects.get(id = pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializer(estu)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)