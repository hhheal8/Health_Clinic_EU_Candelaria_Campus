from django_components import component

@component.register("admin_sidebar")
class AdminSidebar(component.Component):

  template_name = "admin_sidebar/template.html"