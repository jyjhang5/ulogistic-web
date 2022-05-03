import re
from django import forms

class CntrnoSearchForm(forms.Form):
    cntrno = forms.CharField()

    def clean_cntrno(self):
        cntrno = self.cleaned_data['cntrno']
        # check cntrno
        if len(cntrno) != 11:
            raise forms.ValidationError("櫃號錯誤")

        if re.search("^[A-Z]{4}[0-9]{7}$", cntrno) == None:
            raise forms.ValidationError("櫃號格式錯誤")

        # TODO: check if cntrno in yard
        return cntrno