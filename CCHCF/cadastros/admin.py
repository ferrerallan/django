from django.contrib import admin
from .models import CentroCusto
from .models import Gerencia
from .models import Nucleo
from .models import Equipe
from .models import Departamento

admin.site.register(CentroCusto)
admin.site.register(Equipe)
admin.site.register(Nucleo)
admin.site.register(Departamento)
admin.site.register(Gerencia)

# Register your models here.
