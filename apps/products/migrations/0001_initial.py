# Generated by Django 4.1.6 on 2023-02-13 16:13

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')),
                ('deleted_at', models.DateTimeField(auto_now=True, verbose_name='Fecha creación')),
                ('decription', models.CharField(max_length=50, unique=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Categoría Producto',
                'verbose_name_plural': 'Categoría Productos',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCategoryProduct',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha creación')),
                ('modified_at', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha modificación')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha creación')),
                ('decription', models.CharField(db_index=True, max_length=50, verbose_name='Descripción')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Categoría Producto',
                'verbose_name_plural': 'historical Categoría Productos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalIndicator',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha creación')),
                ('modified_at', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha modificación')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha creación')),
                ('disccount_value', models.PositiveSmallIntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Indicador de oferta',
                'verbose_name_plural': 'historical Indicador de ofertas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMeasureUnit',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha creación')),
                ('modified_at', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha modificación')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha creación')),
                ('description', models.CharField(db_index=True, max_length=50, verbose_name='Descripción')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Unidad de Medida',
                'verbose_name_plural': 'historical Unidad de Medidas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='MeasureUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')),
                ('deleted_at', models.DateTimeField(auto_now=True, verbose_name='Fecha creación')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Unidad de Medida',
                'verbose_name_plural': 'Unidad de Medidas',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')),
                ('deleted_at', models.DateTimeField(auto_now=True, verbose_name='Fecha creación')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre producto')),
                ('description', models.TextField(unique=True, verbose_name='Descripción producto')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagen')),
                ('category_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='Categoría Producto')),
                ('measure_unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='Unidad de Medida')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')),
                ('deleted_at', models.DateTimeField(auto_now=True, verbose_name='Fecha creación')),
                ('disccount_value', models.PositiveSmallIntegerField(default=0)),
                ('category_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='Indicador de oferta')),
            ],
            options={
                'verbose_name': 'Indicador de oferta',
                'verbose_name_plural': 'Indicador de ofertas',
            },
        ),
        migrations.CreateModel(
            name='HistoricalProduct',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha creación')),
                ('modified_at', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha modificación')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha creación')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Nombre producto')),
                ('description', models.TextField(db_index=True, verbose_name='Descripción producto')),
                ('image', models.TextField(blank=True, max_length=100, null=True, verbose_name='Imagen')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category_product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.categoryproduct', verbose_name='Categoría Producto')),
            ],
            options={
                'verbose_name': 'historical Producto',
                'verbose_name_plural': 'historical Productos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]