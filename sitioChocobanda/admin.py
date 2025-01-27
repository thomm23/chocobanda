from django.contrib import admin

# Importa tus modelos
from .models import Integrante, Personaje, Obra, GaleriaObra, Evento, Noticia, Institucion, Multimedia, Galeria, GaleriaInstitucion, Cancion, Video, AjustesPagina

# Registrar los modelos en el admin
admin.site.register(Integrante)
admin.site.register(Personaje)
admin.site.register(Evento)
admin.site.register(Noticia)
admin.site.register(Institucion)
admin.site.register(Multimedia)
admin.site.register(Galeria)
admin.site.register(GaleriaInstitucion)
admin.site.register(Cancion)
admin.site.register(Video)
admin.site.register(AjustesPagina)

# Clase para el Inline de GaleriaObra
class GaleriaObraInline(admin.TabularInline):
    model = GaleriaObra
    extra = 1  # Para agregar un formulario vacío para una nueva imagen
    fields = ['foto', 'descripcion']
    verbose_name = "Imagen de la galería"
    verbose_name_plural = "Galería de la obra"

# Registrar el modelo Obra con su clase personalizada de admin
@admin.register(Obra) 
class ObraAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion')
    search_fields = ('titulo',)
    inlines = [GaleriaObraInline]
