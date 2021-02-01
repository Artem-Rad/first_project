from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializater
from django.contrib.auth.models import User


def index(request):
    users = User.objects.all()

    con = {
        'users':users
    }
    return render(request,'api.html',con)

class UsersListSerializer(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class =UserSerializater

class UserViewSerializer(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializater



"""

class TasksView(View):
    template_name = 'success/tasks.html'
    form_class = TaskForm

    def get(self, request):
        tasks = Task.objects.filter(user_id=request.user.id)
        con = {
            'tasks': tasks
        }
        return render(request, self.template_name, con)

    def post(self, request):
        form = self.form_class(request.POST)
        #form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Task.objects.create(
                text=data['text'],
                priority=data['priority'],
                kind = data['kind'],
                user_id= request.user
            )
            messages.success(request, 'task added')
            return redirect('success')
        else:
            messages.error(request, 'oops')

        return render(request, self.template_name, {'form': form})

"""
"""
class DesiresListView(generics.ListCreateAPIView):
    queryset = Desires.objects.all()
    serializer_class =DesiresSerializers

class DesireView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Desires.objects.all()
    serializer_class = DesiresSerializers
"""

'''
class DesiresView(APIView):
    def get(self,request):
        desires = Desires.objects.all()
        serializer = DesiresSerializers(desires, many=True)
        return JsonResponse(serializer.data, safe=False)

class DesireView(APIView):
    def get(self,request,des_pk):
        desire = Desires.objects.get(pk=des_pk)
        serializer = DesiresSerializers(desire)
        return JsonResponse(serializer.data, safe=False)

'''
'''
@api_view(['GET'])
def get_desires(request):
    desires = Desires.objects.all()
    serializer =  DesiresSerializers(desires,many=True)
    return JsonResponse(serializer.data,safe= False)

@api_view(['GET'])
def get_desire(request,des_pk):
    desire = Desires.objects.get(pk=des_pk)
    serializer = DesiresSerializers(desire)
    return JsonResponse(serializer.data,safe=False)'''