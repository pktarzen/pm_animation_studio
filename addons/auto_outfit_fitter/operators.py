import bpy

from .utils import analyze_body, fit_clothes


class PMOF_OT_AnalyzeBody(bpy.types.Operator):
    bl_idname = "pmof.analyze_body"
    bl_label = "Analyze Body"

    def execute(self, context):

        body = context.active_object

        if body is None:
            self.report({'ERROR'}, "Select body mesh")
            return {'CANCELLED'}

        w, d, h = analyze_body(body)

        self.report(
            {'INFO'},
            f"H={h:.2f}  W={w:.2f}  D={d:.2f}"
        )

        return {'FINISHED'}


class PMOF_OT_FitClothes(bpy.types.Operator):
    bl_idname = "pmof.fit_clothes"
    bl_label = "Fit Selected Clothes"

    def execute(self, context):

        body = context.active_object

        if body is None:
            self.report({'ERROR'}, "Select body mesh")
            return {'CANCELLED'}

        fit_clothes(body)

        self.report(
            {'INFO'},
            "Clothes fitting completed"
        )

        return {'FINISHED'}
