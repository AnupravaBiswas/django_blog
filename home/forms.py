from django import forms
from .models import CommentModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        # your_name =forms.CharField(max_length=20)
        # comment_text =forms.CharField(widget=forms.Textarea)
        fields =('your_name', 'comment_text')

    def __str__(self):
        return f"{self.comment_text} by {self.your_name}"
 
# class SearchForm(forms.Form):
#     title = forms.CharField(max_length=20)