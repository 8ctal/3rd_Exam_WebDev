from django import forms
from .models import Note

class NoteForm(forms.ModelForm):

    class Meta: 

        model = Note

        fields = [
            'title',
            'note_body'
        ]

        labels = {
            'title':'TÍTULO',
            'note_body':'CONTENIDO'
        }

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'note_body':forms.Textarea(attrs={'class':'form-control','rows':3})
        }
    
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['title'].error_messages = {'required': 'La nota debe tener un título'}

        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'El campo {fieldname} es obligatorio'.format(
                fieldname=field.label)}