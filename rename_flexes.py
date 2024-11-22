import bpy

d = bpy.context.object.data

for b in d.shape_keys.key_blocks:        
    if "_" in b.name:
        b.name = b.name.replace("_", ".")
