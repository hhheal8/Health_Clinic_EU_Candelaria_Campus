from django_components import component

@component.register("sidebar")
class Sidebar(component.Component):

  template_name = "sidebar/template.html"
  

  # def get_context_data(self):
  #   return {
  #     "": ,
  #   }

  # class Media:
  #   css = "sidebar/style.css"
  #   js = "sidebar/script.js"