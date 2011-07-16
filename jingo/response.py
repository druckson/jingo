import jingo
from django.template import response

loader = jingo.Loader()


def select_template(names, **kwargs):
    "Given a list of template names, returns the first that can be loaded."
    not_found = []
    for template_name in names:
        try:
            return loader.load_template(template_name, **kwargs)
        except TemplateDoesNotExist, e:
            if e.args[0] not in not_found:
                not_found.append(e.args[0])
            continue
    # If we get here, none of the templates could be loaded
    raise TemplateDoesNotExist(', '.join(not_found))


class JinjaResponse(response.TemplateResponse):
    def resolve_template(self, template):
        "Accepts a template object, path-to-template or list of paths"
        if isinstance(template, (list, tuple)):
            return select_template(template)[0]
        elif isinstance(template, basestring):
            return loader.load_template(template)[0]
        else:
            return template

