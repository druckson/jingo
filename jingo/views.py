import jingo
from jingo import response
from django.views.generic import base


def direct_to_template(request, template, **kwargs):
    return jingo.render(request, template, kwargs)


class JinjaView(base.TemplateView):
    response_class = response.JinjaResponse

