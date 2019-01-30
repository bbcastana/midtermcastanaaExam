from django.forms import ModelForm
from .models import Candidate
from .models import Votes

class CandidateModelForm(ModelForm):
    class Meta:
        model = Candidate
        exclude = ['id']
        exclude = ['date_updated']
        exclude = ['is_active']

class VotesForm(ModelForm):
    class Meta:
        model = Votes
        exclude = ['id']
        exclude = ['Vote_date']
