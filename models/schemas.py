REQUIRED_SCHEMA = {
   "header": ["pagination", "audit", "status"],
   "body": ["records"]
}
def validate_schema(data: dict):
   for key, subkeys in REQUIRED_SCHEMA.items():
       if key not in data:
           raise ValueError(f"❌ Falta la clave principal: {key}")
       for subkey in subkeys:
           if subkey not in data[key]:
               raise ValueError(f"❌ Falta la clave: {key}.{subkey}")