from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Allergies, Analysis, Components
from .serializers import AllergySerializer, AnalysisSerializer, AnalysisPostSerializer, ComponentSerializer


class AllergiesListView(APIView):

   def get(self, request, format=None):
      allergies = Allergies.objects.all()
      serializer = AllergySerializer(allergies, many=True)
      return Response(serializer.data)


class ComponentsDetailView(APIView):

    def get_object(self, pk):
        try:
            Components.get(pk=pk)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        component = self.get_object(pk)
        serializer = ComponentSerializer(component)
        return Response(serializer.data)


class ComponentsListView(APIView):

   def get(self, request, format=None):
      components = Components.objects.all()
      serializer = ComponentSerializer(components, many=True)
      return Response(serializer.data)


class AnalysisDetailView(APIView):

   def get_object(self, pk):
      try:
         return Analysis.objects.get(pk=pk)
      except Exception:
         raise Http404

   def get(self, request, pk, format=None):
      analysis = self.get_object(pk)
      serializer = AnalysisSerializer(analysis)
      return Response(serializer.data)


class AnalysisListView(APIView):

    def component_coefficients(self, components):
        safety_percentage = 100.
        proportions = [(x+1) / len(components) for x in range(len(components))][::-1]
        component_loss = safety_percentage / sum(proportions)
        loss_coefficients = [x * component_loss for x in proportions]
        for index, coefficient in enumerate(loss_coefficients):
            loss_coefficients[index] = round(coefficient, 2)
        return loss_coefficients

    def calculate_percentage(self, components, loss_coefficients):
        safety_index = 100.
        ordered_components = list(enumerate(components))
        first_half = len(components) // 2
        for comp_tuple in ordered_components:
            first_safety = comp_tuple[1].firsthalf
            second_safety = comp_tuple[1].secondhalf
            allergies = comp_tuple[1].allergies.all()
            if first_safety and second_safety or allergies:
                safety_index -= safety_index
                break
            elif comp_tuple[0] + 1 <= first_half:
                safety_index -= first_safety * loss_coefficients[comp_tuple[0]]
            else:
                safety_index -= second_safety * loss_coefficients[comp_tuple[0]]
        return safety_index, ordered_components

    def post(self, request, format=None):
        serializer = AnalysisPostSerializer(data=request.data)
        if serializer.is_valid():
            components = []
            for component in serializer.data['components']:
                components.append(Components.objects.all().filter(
                    compname=component['compname'])[0])
            loss_coefficients = self.component_coefficients(components)
            safety_index, ordered_components = self.calculate_percentage(components, loss_coefficients)
            influences = ", ".join([comp[1].compname for comp in ordered_components[:5]])
            if safety_index <= 50.:
                verdict = "good"
            else:
                verdict = "bad"
            response = {
                "verdict": verdict,
                "percentage": safety_index,
                "influences": influences
            }
            return Response(response)