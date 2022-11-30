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
    attr_models = {
        'models': len(models), 'collections': {
            m._meta.object_name: {
                'path': m.__module__,
                'verbose_name': str(m._meta.verbose_name),  # verbose_name is a proxy variable so we cast this value
                'db_table': m._meta.db_table, 'fields': {
                    f.name: f.get_internal_type() for f in m._meta.fields
                }
            } for m in models
        }
    }
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(attr_models, indent=2))
    return attr_models


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
