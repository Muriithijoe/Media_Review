from django import forms
from .models import DailyReview
from bootstrap_modal_forms.forms import BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

class ReviewForm(BSModalForm):
    date = forms.DateField(
        error_messages={'invalid': 'Enter a valid date in YYYY-MM-DD format.'}
    )
    class Meta:
        model = DailyReview
        fields = ('media_link' , 'nation' , 'standard' , 'business_daily' , 'date')
        widgets ={'date': forms.DateInput(attrs={'class': 'datepicker'}),}

#         Approva1 = forms.CharField(required=False)
#         Approva2 = forms.CharField(required=False)
#         Approva3 = forms.CharField(required=False)
#
# date = models.DateField()
# media_link = models.TextField(validators=[URLValidator()],null=True)
# nation = models.TextField(max_length = 500)
# standard = models.TextField(max_length = 500)
