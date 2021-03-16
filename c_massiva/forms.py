
from django import forms

class UploadAlunoRel(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'class':'filestyle','':''}),label="Aluno Rel:")
    CHOICES = [('pt', 'Português'), ('es', 'Espanhol')]
    choice = forms.ChoiceField(label= "Qual a linguagem da carga massiva que deseja gerar ?",widget=forms.RadioSelect, choices=CHOICES)

    def clean(self):
        file = self.cleaned_data['file']
        filename = file.name

        if filename.endswith('.csv'):
            return file
        else:
            raise forms.ValidationError("O arquivo não está no formato csv")

class UploadCarga(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'filestyle','multiple':True}), label="Carga Massiva:")
    # widget = forms.ClearableFileInput(attrs={'multiple': True}
    def clean(self):
        file = self.cleaned_data['file']
        filename = file.name

        if filename.endswith('.csv'):
            return file
        else:
            raise forms.ValidationError("O arquivo não está no formato csv")





