from django import forms


class CheckoutForm(forms.Form):
    """Optional: add shipping/notes. For minimal checkout we can leave empty or add a confirm."""
    confirm = forms.BooleanField(
        required=True,
        label='I confirm this order',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )
