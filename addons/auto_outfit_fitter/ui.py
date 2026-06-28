import bpy


class PMOF_PT_Panel(bpy.types.Panel):
    bl_label = "Outfit Fitter"
    bl_idname = "PMOF_PT_PANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'PM Tools'

    def draw(self, context):

        layout = self.layout

        layout.label(text="Body Analysis")

        layout.operator(
            "pmof.analyze_body",
            icon='MESH_CUBE'
        )

        layout.separator()

        layout.label(text="Clothing Tools")

        layout.operator(
            "pmof.fit_clothes",
            icon='MOD_CLOTH'
        )
