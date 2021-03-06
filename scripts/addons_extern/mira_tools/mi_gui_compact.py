# BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# END GPL LICENSE BLOCK #####

import bpy, os

from bpy import*
from bpy.props import *



def draw_miratools_panel_layout(self, context, layout):

        lt = context.window_manager.mirawindow

        if lt.display_miraextrude:
            box = layout.box()
            row = box.row(1)
            row.prop(lt, "display_miraextrude", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row(1)
            row.prop(lt, "display_miraextrude", text="", icon='TRIA_RIGHT')

        row.label("Extrude")
        if context.scene.mi_settings.surface_snap is False:
            row.prop(context.scene.mi_extrude_settings, "do_symmetry", text='', icon="UV_ISLANDSEL")
            if context.scene.mi_extrude_settings.do_symmetry:
                sub = row.row(1)
                sub.scale_x = 0.15
                sub.prop(context.scene.mi_extrude_settings, "symmetry_axys", text='')

        row.operator("mira.draw_extrude", text="", icon="VPAINT_HLT")

        ###
        if lt.display_miraextrude:
            ###
            box = layout.box().column(1)

            row = box.row(1)
            row.label("New Mesh Drawing")
                
            box.separator() 

            row = box.column(1)  
            row.operator("mira.draw_extrude", text="Draw Extrude", icon="VPAINT_HLT")

            row = box.row(1)
            if lt.display_help:            
                
                row.operator("wm.url_open", text="", icon='HELP').url = "https://lh3.googleusercontent.com/-tIDzK8yFnjU/VbhVbn2cfSI/AAAAAAAAIPo/mYRzdjqOki0/w530-h749-p/%25231_Draw_Extrude.png"   
            if context.scene.mi_extrude_settings.extrude_step_type == 'Asolute':
                row.prop(context.scene.mi_extrude_settings, "absolute_extrude_step", text='')
            else:
                row.prop(context.scene.mi_extrude_settings, "relative_extrude_step", text='')

            box.separator()
            
            row = box.column(1)       
            row.prop(context.scene.mi_extrude_settings, "extrude_step_type", text='Step')

            box.separator()

            row = box.column(1)
            if context.scene.mi_settings.surface_snap is False:
                row.prop(context.scene.mi_extrude_settings, "do_symmetry", text='Symmetry')

                if context.scene.mi_extrude_settings.do_symmetry:
                    row.prop(context.scene.mi_extrude_settings, "symmetry_axys", text='Axys')

            box.separator() 
            
            
# --------------------------------------------------


        if lt.display_mirasface:

            box = layout.box()
            row = box.row(1)
            row.prop(lt, "display_mirasface", text="", icon='TRIA_DOWN')
        else:
            box = layout.box()
            row = box.row(1)
            row.prop(lt, "display_mirasface", text="", icon='TRIA_RIGHT')

        row.label("Surfaces")

        row.operator("mira.poly_loop", text="", icon="MESH_GRID")
        sub = row.row(1)
        sub.scale_x = 0.15
        sub.prop(context.scene.mi_cur_surfs_settings, "spread_loops_type", text='', icon="COLLAPSEMENU")
        row.operator("mira.curve_surfaces", text="", icon="SURFACE_NCURVE")

        ###
        if lt.display_mirasface:
            ###
            box = layout.box().column(1)

            row = box.row(1)
            row.label("New Mesh Creation")
                
            box.separator()

            row = box.row(1)
            
            if lt.display_help:           
                             
                row.operator("wm.url_open", text="", icon='HELP').url = "https://lh3.googleusercontent.com/-0fzOvLD4EM8/Vb5CdYy5qKI/AAAAAAAAIVk/EkiLDYzwtVk/w780-h840-no/%25233_Poly_Loop.png"   
            row.operator("mira.poly_loop", text="Poly Loop", icon="MESH_GRID")

            box.separator()

            row = box.row(1)
            if lt.display_help:             
                           
                row.operator("wm.url_open", text="", icon='HELP').url = "https://lh5.googleusercontent.com/-o3W-ypmbxI8/Vb5gyXLJ4tI/AAAAAAAAIXc/ZsNqJR5WiWw/w746-h840-no/%25234_Curve_Surface.png"             
            row.operator("mira.curve_surfaces", text="CurveSurfaces", icon="SURFACE_NCURVE")

            box.separator()

            row = box.column(1)
            row.prop(context.scene.mi_cur_surfs_settings, "spread_loops_type", text='Points')

            box.separator() 
            

# --------------------------------------------------


        if lt.display_miradeform:

            box = layout.box()
            row = box.row(1)
            row.prop(lt, "display_miradeform", text="", icon='TRIA_DOWN')
        else:
            box = layout.box()
            row = box.row(1)
            row.prop(lt, "display_miradeform", text="", icon='TRIA_RIGHT')

        row.label("Deform")
        row.operator("mira.noise", text="", icon="RNDCURVE")
        row.prop(context.scene.mi_ldeformer_settings, "manual_update", text='', icon="DISK_DRIVE")
        row.operator("mira.linear_deformer", text="", icon="OUTLINER_OB_MESH")

        ###
        if lt.display_miradeform:
            ###
            box = layout.box().column(1)

            row = box.row(1)
            row.label("Mesh Transformation")
                
            box.separator() 
            
            row = box.row(1) 
            row.operator("mira.linear_deformer", text="LinearDeformer", icon="OUTLINER_OB_MESH")

            row = box.row(1)
            if lt.display_help:              
                           
                row.operator("wm.url_open", text="", icon='HELP' ).url = "https://lh4.googleusercontent.com/-GTuGp92YHvc/VbruOKWUTTI/AAAAAAAAIUk/LbjhscUtqHI/w611-h840-no/%25232_Deform_Mesh.png"  
            row.prop(context.scene.mi_ldeformer_settings, "manual_update", text='ManualUpdate')

            box.separator()

            row = box.row(1)
            row.operator("screen.redo_last", text = "", icon="SETTINGS")            
            row.operator("mira.deformer", text="Deformer", icon="BLANK1")
            
            row = box.column(1)            
            row.operator("mira.noise", text="NoiseDeform", icon="RNDCURVE")

            box.separator() 


# --------------------------------------------------


        if lt.display_miraguide:

            box = layout.box()
            row = box.row(1)
            row.prop(lt, "display_miraguide", text="", icon='TRIA_DOWN')
        else:
            box = layout.box()
            row = box.row(1)
            row.prop(lt, "display_miraguide", text="", icon='TRIA_RIGHT')

        row.label("CGuide")

        sub1 = row.row(1)
        sub1.scale_x = 0.75
        sub1.prop(context.scene.mi_curguide_settings, "points_number", text='')

        sub = row.row(1)
        sub.scale_x = 0.15
        sub.prop(context.scene.mi_curguide_settings, "deform_type", text='', icon="COLLAPSEMENU")
        row.operator("mira.curve_guide", text='', icon="RNA")

        ###
        if lt.display_miraguide:
            ###
            box = layout.box().column(1)

            row = box.row(1)
            row.label("Loop Manipulation")
                
            box.separator()        

            row = box.column(1)
            row.operator("mira.curve_guide", text="CurveGuide", icon="RNA")

            row = box.row(1)
            if lt.display_help:              
                
                row.operator("wm.url_open", text="", icon='HELP').url = "https://lh3.googleusercontent.com/WBih_PAVzmvuBWVuAv-iO6_ZAy1L9PdSaIm1C-AmkJkCeM8kl3te7DESf98kn3SAWVZWSLNAIg=w1920-h1080-no"    
            row.prop(context.scene.mi_curguide_settings, "points_number", text='LoopSpread')

            box.separator() 
            
            row = box.column(1)
            row.prop(context.scene.mi_curguide_settings, "deform_type", text='Type')

            box.separator() 

# --------------------------------------------------


        if lt.display_mirastretch:

            box = layout.box()
            row = box.row(1)
            row.prop(lt, "display_mirastretch", text="", icon='TRIA_DOWN')
        else:
            box = layout.box()
            row = box.row(1)
            row.prop(lt, "display_mirastretch", text="", icon='TRIA_RIGHT')

        row.label("CStretch")
        sub = row.row(1)
        sub.scale_x = 0.5
        sub.prop(context.scene.mi_cur_stretch_settings, "points_number", text='')
        row.operator("mira.curve_stretch", text="", icon="STYLUS_PRESSURE")

        ###
        if lt.display_mirastretch:
            ###
            box = layout.box().column(1)

            row = box.row(1)
            row.label("Loop Manipulation")
                
            box.separator()        

            row = box.column(1)
            row.operator("mira.curve_stretch", text="CurveStretch", icon="STYLUS_PRESSURE")

            row = box.row(1)
            if lt.display_help:              
                
                row.operator("wm.url_open", text="", icon='HELP').url = "https://lh3.googleusercontent.com/-pFQ0XaKlZY4/VcDyem3HKaI/AAAAAAAAIZI/oELrYw398oM/w530-h597-p/%25235_Curve_Stretch.png"  
            row.prop(context.scene.mi_cur_stretch_settings, "points_number", text='PointsNumber')

            box.separator() 

# --------------------------------------------------


        if lt.display_mirasettings:
            box = layout.box()
            row = box.row(1)
            row.prop(lt, "display_mirasettings", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row(1)
            row.prop(lt, "display_mirasettings", text="", icon='TRIA_RIGHT')

        row.label("Settings")
        row.prop(context.scene.mi_settings, "convert_instances", text='', icon="BOIDS")
        sub = row.row(1)
        sub.scale_x = 0.15
        sub.prop(context.scene.mi_settings, "snap_objects", text='', icon="VISIBLE_IPO_ON")
        row.prop(context.scene.mi_settings, "surface_snap", text='', icon="SNAP_SURFACE")

        ###
        if lt.display_mirasettings:
            ###
            box = layout.box().column(1)

            row = box.column(1)
            row.prop(context.scene.mi_settings, "surface_snap", text='Surface Snapping', icon ="SNAP_SURFACE")
            row.prop(context.scene.mi_settings, "convert_instances", text='Convert Instances')

            box.separator() 

            row = box.column(1)
            row.prop(context.scene.mi_settings, "snap_objects", text='SnapObjects')

            box.separator() 

            box = layout.box().column(1)

            row = box.column(1)
            row.prop(context.scene.mi_settings, "spread_mode", text='Spread')

            box.separator() 

            row = box.column(1)
            row.prop(context.scene.mi_settings, "curve_resolution", text='Resolution')

            box.separator() 

            row = box.row(1)
            row.operator("mira.curve_test", text="Curve Test")
            row.prop(context.scene.mi_settings, "draw_handlers", text='Handlers')

            box.separator() 
            
            box = layout.box().column(1)

            row = box.column(1)
            row.operator('wm.url_open', text = 'Wiki', icon='HELP').url = "https://github.com/mifth/mifthtools/wiki/Mira-Tools"

            row = box.row(1)           
            row.prop(lt, "display_help", text=" Help-URL-Buttons", icon='HELP')

            box.separator() 


class VIEW3D_MIRA_Panel_TOOLS(bpy.types.Panel):
    bl_idname = "VIEW3D_MIRA_Panel_TOOLS"
    bl_context = "mesh_edit"
    bl_label = "MiraTools"
    bl_category = 'Mira'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'    
    #bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)        
        return (context.object is not None and isModelingMode)

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_miratools_panel_layout(self, context, layout)         
        

class VIEW3D_MIRA_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_MIRA_Panel_UI"
    bl_context = "mesh_edit"
    bl_label = "MiraTools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'    
    #bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)        
        return (context.object is not None and isModelingMode)

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_miratools_panel_layout(self, context, layout)         
        



def register():
    
    bpy.utils.register_module(__name__)

def unregister():

    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()



