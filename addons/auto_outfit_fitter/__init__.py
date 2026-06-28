bl_info = {
    "name": "PM Auto Outfit Fitter",
    "author": "PM Animation Studio",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > PM Tools",
    "description": "Fit selected clothes to active body mesh",
    "category": "Object",
}

import bpy

from .operators import (
    PMOF_OT_AnalyzeBody,
    PMOF_OT_FitClothes,
)

from .ui import (
    PMOF_PT_Panel,
)


classes = (
    PMOF_OT_AnalyzeBody,
    PMOF_OT_FitClothes,
    PMOF_PT_Panel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
