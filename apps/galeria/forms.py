from django import forms

from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        fields = '__all__'
        labels = {
            'descricao':'Descrição',
            'data_fotografia':'Data de inserção', 
            'usuario':'Usuário'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.TextInput(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'publicada': forms.CheckboxInput(),
            'data_fotografia': forms.DateInput(attrs={'class':'form-control'}),
            'usuario': forms.SelectMultiple(attrs={'class':'form-control'}),
        }


