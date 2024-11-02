from django_components import component

@component.register("admin_header")
class AdminHeader(component.Component):

  template_name = "admin_header/template.html"