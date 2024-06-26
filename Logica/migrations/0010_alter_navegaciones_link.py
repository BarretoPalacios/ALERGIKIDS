# Generated by Django 4.2.5 on 2023-10-20 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Logica', '0009_alter_navegaciones_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navegaciones',
            name='link',
            field=models.CharField(choices=[("{% url 'pagina_inicio' %}", 'Inicio'), ("{% url 'pagina_especialidad' %}", 'Especialidad'), ("{% url 'pagina_doctor' %}", 'Doctor'), ("{% url 'pagina_pregunta' %}", 'Preguntas'), ("{% url 'pagina_consejo' %}", 'Consejos'), ("{% url 'pagina_nosotros' %}", 'Nosotros')], max_length=200),
        ),
    ]
