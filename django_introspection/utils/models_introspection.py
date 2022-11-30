import json
import os

from django.apps import apps


__all__ = [
    'models_introspection'
]


# If the file not exists or file contains no same models count,
# We override the existing file or create new file with all models and attributes of project target
def models_introspection(filename="forestadminschema.json"):
    models = apps.get_models()
    no_update = no_same_models(filename, len(models))
    if not no_update:
        return
    attr_models = {}
    for m in models:
        meta = m._meta
        attr_models[meta.object_name] = {
            'path': m.__module__, 'verbose_name': str(meta.verbose_name).encode('utf8').decode('utf8'),
            'db_table': meta.db_table, 'fields': {}
        }
        fields = meta.fields
        for f in fields:
            attr_models[meta.object_name]['fields'][f.name] = f.get_internal_type()
    models_json = json.dumps({'models': len(models), 'collections': attr_models}, indent=2)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(models_json)
    return models_json


# Check if file exist
# If file exist and get same models count, we do nothing
# And if we get not same models count, we return True
def no_same_models(filename, length):
    if not os.path.exists(filename):
        return True
    with open(filename, 'r') as f:
        read = f.read()
    if read:
        json_objects = json.loads(read)
        if json_objects['models'] == length:
            return False
    return True
