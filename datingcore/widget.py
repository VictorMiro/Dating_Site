from django.forms import Widget
from django.template.loader import render_to_string


class EditorWidget(Widget):

    def render(self, name, value, attrs=None, renderer=None):
        context = {
            "name": name,
            "value": value
        }
        return render_to_string('widgets/niceeditor.html', context)
