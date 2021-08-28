from django.http import HttpResponse
from xlsxwriter import Workbook

from universidad.models import Estudiante


def reporte_estudiantes_grupos(request):
    estudiantes = Estudiante.objects.all()
    ids_grupo = []
    for grupo_id in estudiantes.values_list('grupo_id'):
        if not ids_grupo.__contains__(grupo_id[0]):
            ids_grupo.append(grupo_id[0])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=Reporte_estudiantes.xlsx"

    book = Workbook(response, {'in_memory': True})
    worksheet_data = book.add_worksheet("Reporte Causales (COVID)")

    formato_primera_fila = book.add_format({'bold': True, 'border': 1})
    formato1 = book.add_format({'bold': True, 'border': 1, 'text_wrap': True})

    worksheet_data.merge_range('A1:H1', 'Reporte de estudiantes por grupo', formato_primera_fila)

    worksheet_data.write("A2", "Grupo", formato1)
    worksheet_data.write("B2", "Nombre y Apellidos", formato1)
    worksheet_data.write("C2", "Carnet de identidad", formato1)
    worksheet_data.write("D2", "Edad", formato1)
    worksheet_data.write("E2", "Sexo", formato1)
    worksheet_data.write("F2", "Ciudad de nacimiento", formato1)
    worksheet_data.write("G2", "Fecha de nacimiento", formato1)
    worksheet_data.write("H2", "Email", formato1)

    worksheet_data.set_column("A:A", 20)
    worksheet_data.set_column("B:B", 12)
    worksheet_data.set_column("C:C", 12)
    worksheet_data.set_column("D:D", 12)
    worksheet_data.set_column("E:E", 12)
    worksheet_data.set_column("F:F", 12)
    worksheet_data.set_column("G:G", 12)
    worksheet_data.set_column("H:H", 12)

    indice = 1

    for grupo_id in ids_grupo:
        worksheet_data.write(indice + 1, 0, estudiantes.filter(grupo_id=grupo_id).first().grupo.nombre, formato1)
        for estudiante in estudiantes.filter(grupo_id=grupo_id):
            worksheet_data.write(indice + 1, 1, str(estudiante.nombre_apellidos).decode('utf-8'), formato1)
            worksheet_data.write(indice + 1, 2, estudiante.carnet, formato1)
            worksheet_data.write(indice + 1, 3, estudiante.edad, formato1)
            worksheet_data.write(indice + 1, 4, estudiante.get_sexo(), formato1)
            worksheet_data.write(indice + 1, 5, estudiante.ciudad_nacimiento.nombre.decode('utf-8'), formato1)
            worksheet_data.write(indice + 1, 6, str(estudiante.fecha_nacimiento), formato1)
            worksheet_data.write(indice + 1, 7, estudiante.email, formato1)
            indice += 1

    book.close()
    return response
