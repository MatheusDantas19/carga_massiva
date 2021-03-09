
from django import forms

class UploadCarga(forms.Form):
    file = forms.FileField(label="Aluno Rel")
    CHOICES = [('1', 'Português'), ('2', 'Espanhol')]
    choice_field = forms.ChoiceField(label= "Qual a linguagem da carga massiva que deseja gerar ?",widget=forms.RadioSelect, choices=CHOICES)

    def clean(self):
        file = self.cleaned_data['file']

        filename = file.name

        if filename.endswith('.csv'):
            return file
        else:
            raise forms.ValidationError("O arquivo não está no formato csv")






