"""
@Author: Ihimu Ukpo
@License: MIT
@Email: iuu1@columbia.edu
@Description: This Python script removes invalid static meshes from actors in an Unreal Engine level.
@Version: 1.0
@Planned future updates: error handling for library opening, etc. Update script (if necessary) to Python 3.
"""

import unreal

# Get instances of unreal libraries necessary.
editor_level_lib = unreal.EditorLevelLibrary()
editor_filter_lib = unreal.EditorFilterLibrary()

# Get all the level actors
level_actors = editor_level_lib.get_all_level_actors()

# Filter the level actors by StaticMeshActor
static_mesh_actors = editor_filter_lib.by_class(level_actors, unreal.StaticMeshActor)

# Count of the number of deleted meshes
deleted_invalid_static_mesh_count = 0

# For each actor in the filtered results...
for actor in static_mesh_actors:
    actor_name = actor.get_fname()

    # Get the static mesh through the static mesh component
    actor_mesh_comp = actor.static_mesh_component
    actor_mesh = actor_mesh_comp.static_mesh
    is_valid_actor = actor_mesh != None

    # If mesh is invalid, destroy it.
    if not is_valid_actor:
        actor.destroy_actor()
        deleted_invalid_static_mesh_count += 1
        unreal.log("The Mesh Component of Actor {} is invalid and was deleted".format(actor_name))

unreal.log("Deleted {} Actors with invalid Mesh Component".format(deleted_invalid_static_mesh_count))