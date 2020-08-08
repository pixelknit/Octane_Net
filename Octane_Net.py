
import sys
import toolutils

outputitem = None
inputindex = -1
inputitem = None
outputindex = -1

num_args = 1
h_extra_args = ''
pane = toolutils.activePane(kwargs)
if not isinstance(pane, hou.NetworkEditor):
    pane = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
    if pane is None:
       hou.ui.displayMessage(
               'Cannot create node: cannot find any network pane')
       sys.exit(0)
else: # We're creating this tool from the TAB menu inside a network editor
    pane_node = pane.pwd()
    if kwargs.has_key("outputnodename") and kwargs.has_key("inputindex"):
        outputitem = pane_node.item(kwargs["outputnodename"])
        inputindex = kwargs["inputindex"]
        h_extra_args += 'set arg4 = "' + kwargs["outputnodename"] + '"\n'
        h_extra_args += 'set arg5 = "' + str(inputindex) + '"\n'
        num_args = 6
    if kwargs.has_key("inputnodename") and kwargs.has_key("outputindex"):
        inputitem = pane_node.item(kwargs["inputnodename"])
        outputindex = kwargs["outputindex"]
        h_extra_args += 'set arg6 = "' + kwargs["inputnodename"] + '"\n'
        h_extra_args += 'set arg9 = "' + str(outputindex) + '"\n'
        num_args = 9 
    if kwargs.has_key("autoplace"):
        autoplace = kwargs["autoplace"]
    else:
        autoplace = False
    # If shift-clicked we want to auto append to the current
    # node
    if kwargs.has_key("shiftclick") and kwargs["shiftclick"]:
        if inputitem is None:
            inputitem = pane.currentNode()
            outputindex = 0
    if kwargs.has_key("nodepositionx") and             kwargs.has_key("nodepositiony"):
        try:
            pos = [ float( kwargs["nodepositionx"] ),
                    float( kwargs["nodepositiony"] )]
        except:
            pos = None
    else:
        pos = None

    if not autoplace and not pane.listMode():
        if pos is not None:
            pass
        elif outputitem is None:
            pos = pane.selectPosition(inputitem, outputindex, None, -1)
        else:
            pos = pane.selectPosition(inputitem, outputindex,
                                      outputitem, inputindex)

    if pos is not None:
        if kwargs.has_key("node_bbox"):
            size = kwargs["node_bbox"]
            pos[0] -= size[0] / 2
            pos[1] -= size[1] / 2
        else:
            pos[0] -= 0.573625
            pos[1] -= 0.220625
        h_extra_args += 'set arg2 = "' + str(pos[0]) + '"\n'
        h_extra_args += 'set arg3 = "' + str(pos[1]) + '"\n'
h_extra_args += 'set argc = "' + str(num_args) + '"\n'
            
pane_node = pane.pwd()
child_type = pane_node.childTypeCategory().nodeTypes()

if not child_type.has_key('null'):
   hou.ui.displayMessage(
           'Cannot create node: incompatible pane network type')
   sys.exit(0)

# First clear the node selection
pane_node.setSelected(False, True)

h_path = pane_node.path()
h_preamble = 'set arg1 = "' + h_path + '"\n'
h_cmd = r''' 
if ($argc < 2 || "$arg2" == "") then
   set arg2 = 0
endif
if ($argc < 3 || "$arg3" == "") then
   set arg3 = 0
endif
# Automatically generated script
# $arg1 - the path to add this node
# $arg2 - x position of the tile
# $arg3 - y position of the tile
# $arg4 - input node to wire to
# $arg5 - which input to wire to
# $arg6 - output node to wire to
# $arg7 - the type of this node
# $arg8 - the node is an indirect input
# $arg9 - index of output from $arg6

\set noalias = 1
set saved_path = `execute("oppwf")`
opcf $arg1

# Node $_obj_shopnet1 (Object/shopnet)
set _obj_shopnet1 = `run("opadd -e -n -v shopnet shopnet1")`
oplocate -x `$arg2 + 0` -y `$arg3 + 0` $_obj_shopnet1
opset -d off -r off -h off -f off -y off -t off -l off -s off -u off -F on -c on -e on -b off $_obj_shopnet1
opexprlanguage -s hscript $_obj_shopnet1
opuserdata -n '___toolcount___' -v '1' $_obj_shopnet1
opuserdata -n '___toolid___' -v 'OCT' $_obj_shopnet1
opcf $_obj_shopnet1

# Node $_obj_shopnet1_occ_target (Shop/octane_vopnet)
set _obj_shopnet1_occ_target = `run("opadd -e -n -v octane_vopnet occ_target")`
oplocate -x `$arg2 + -1.354025583145221` -y `$arg3 + 1.5693378480060187` $_obj_shopnet1_occ_target
opset -d off -r off -h off -f off -y off -t off -l off -s off -u off -F on -c on -e on -b off $_obj_shopnet1_occ_target
opexprlanguage -s hscript $_obj_shopnet1_occ_target
opuserdata -n '___toolcount___' -v '1' $_obj_shopnet1_occ_target
opuserdata -n '___toolid___' -v 'OCT' $_obj_shopnet1_occ_target
opcf $_obj_shopnet1_occ_target

# Node $_obj_shopnet1_occ_target_octane_render_target1 (Vop/octane_render_target)
set _obj_shopnet1_occ_target_octane_render_target1 = `run("opadd -e -n -v octane_render_target octane_render_target1")`
oplocate -x `$arg2 + 1.1176470290212071` -y `$arg3 + 0.28000004775822163` $_obj_shopnet1_occ_target_octane_render_target1
opset -d on -r on -h off -f off -y off -t off -l off -s off -u off -F on -c on -e on -b off -L off -M off -H on -E on $_obj_shopnet1_occ_target_octane_render_target1
opexprlanguage -s hscript $_obj_shopnet1_occ_target_octane_render_target1
opuserdata -n '___toolcount___' -v '1' $_obj_shopnet1_occ_target_octane_render_target1
opuserdata -n '___toolid___' -v 'OCT' $_obj_shopnet1_occ_target_octane_render_target1

# Node $_obj_shopnet1_occ_target_NT_CAM_THINLENS1 (octane::Vop/NT_CAM_THINLENS)
set _obj_shopnet1_occ_target_NT_CAM_THINLENS1 = `run("opadd -e -n -v octane::NT_CAM_THINLENS NT_CAM_THINLENS1")`
oplocate -x `$arg2 + -2.1752941474493799` -y `$arg3 + 7.2688235294117636` $_obj_shopnet1_occ_target_NT_CAM_THINLENS1
opset -d off -r off -h off -f off -y off -t off -l off -s off -u off -F on -c on -e on -b off -L off -M off -H on -E off $_obj_shopnet1_occ_target_NT_CAM_THINLENS1
opexprlanguage -s hscript $_obj_shopnet1_occ_target_NT_CAM_THINLENS1
opuserdata -n '___toolcount___' -v '1' $_obj_shopnet1_occ_target_NT_CAM_THINLENS1
opuserdata -n '___toolid___' -v 'OCT' $_obj_shopnet1_occ_target_NT_CAM_THINLENS1

# Node $_obj_shopnet1_occ_target_NT_KERN_PATHTRACING1 (octane::Vop/NT_KERN_PATHTRACING)
set _obj_shopnet1_occ_target_NT_KERN_PATHTRACING1 = `run("opadd -e -n -v octane::NT_KERN_PATHTRACING NT_KERN_PATHTRACING1")`
oplocate -x `$arg2 + -2.1752941474493799` -y `$arg3 + -2.519999785348773` $_obj_shopnet1_occ_target_NT_KERN_PATHTRACING1
opparm -V 18.0.499 $_obj_shopnet1_occ_target_NT_KERN_PATHTRACING1 maxsamples ( 2000 )
opset -d off -r off -h off -f off -y off -t off -l off -s off -u off -F on -c on -e on -b off -L off -M off -H on -E off $_obj_shopnet1_occ_target_NT_KERN_PATHTRACING1
opexprlanguage -s hscript $_obj_shopnet1_occ_target_NT_KERN_PATHTRACING1
opuserdata -n '___toolcount___' -v '1' $_obj_shopnet1_occ_target_NT_KERN_PATHTRACING1
opuserdata -n '___toolid___' -v 'OCT' $_obj_shopnet1_occ_target_NT_KERN_PATHTRACING1

# Node $_obj_shopnet1_occ_target_NT_ENV_TEXTURE1 (octane::Vop/NT_ENV_TEXTURE)
set _obj_shopnet1_occ_target_NT_ENV_TEXTURE1 = `run("opadd -e -n -v octane::NT_ENV_TEXTURE NT_ENV_TEXTURE1")`
oplocate -x `$arg2 + -3.3696078729395769` -y `$arg3 + 0.56500002089887857` $_obj_shopnet1_occ_target_NT_ENV_TEXTURE1
chblockbegin
chadd -t 0 0 $_obj_shopnet1_occ_target_NT_ENV_TEXTURE1 power
chkey -t 0 -v 1 -m 0 -a 0 -A 0 -T a  -F 'ch("../NT_TEX_IMAGE1/power")' $_obj_shopnet1_occ_target_NT_ENV_TEXTURE1/power
chblockend
opset -d off -r off -h off -f off -y off -t off -l off -s off -u off -F on -c on -e on -b off -L off -M off -H on -E off $_obj_shopnet1_occ_target_NT_ENV_TEXTURE1
opexprlanguage -s hscript $_obj_shopnet1_occ_target_NT_ENV_TEXTURE1
opuserdata -n '___toolcount___' -v '1' $_obj_shopnet1_occ_target_NT_ENV_TEXTURE1
opuserdata -n '___toolid___' -v 'OCT' $_obj_shopnet1_occ_target_NT_ENV_TEXTURE1

# Node $_obj_shopnet1_occ_target_NT_TEX_IMAGE1 (octane::Vop/NT_TEX_IMAGE)
set _obj_shopnet1_occ_target_NT_TEX_IMAGE1 = `run("opadd -e -n -v octane::NT_TEX_IMAGE NT_TEX_IMAGE1")`
oplocate -x `$arg2 + -7.6833333631356568` -y `$arg3 + 0.69999998807907093` $_obj_shopnet1_occ_target_NT_TEX_IMAGE1
chblockbegin
chadd -t 0 0 $_obj_shopnet1_occ_target_NT_TEX_IMAGE1 power
chkey -t 0 -v 1 -m 0 -a 0 -A 0 -T a  -F 'ch("../../../CONTROLS/hdri_pow")' $_obj_shopnet1_occ_target_NT_TEX_IMAGE1/power
chblockend
opparm -V 18.0.499 $_obj_shopnet1_occ_target_NT_TEX_IMAGE1 power ( power ) A_FILENAME ( '`chs("../../../CONTROLS/ibl_file")`' )
opset -d off -r off -h off -f off -y off -t off -l off -s off -u off -F on -c on -e on -b off -L off -M off -H on -E off $_obj_shopnet1_occ_target_NT_TEX_IMAGE1
opexprlanguage -s hscript $_obj_shopnet1_occ_target_NT_TEX_IMAGE1
opuserdata -n '___toolcount___' -v '1' $_obj_shopnet1_occ_target_NT_TEX_IMAGE1
opuserdata -n '___toolid___' -v 'OCT' $_obj_shopnet1_occ_target_NT_TEX_IMAGE1

# Node $_obj_shopnet1_occ_target_NT_TRANSFORM_3D1 (octane::Vop/NT_TRANSFORM_3D)
set _obj_shopnet1_occ_target_NT_TRANSFORM_3D1 = `run("opadd -e -n -v octane::NT_TRANSFORM_3D NT_TRANSFORM_3D1")`
oplocate -x `$arg2 + -13.872352970978794` -y `$arg3 + 2.2650000089779496` $_obj_shopnet1_occ_target_NT_TRANSFORM_3D1
opparm -V 18.0.499 $_obj_shopnet1_occ_target_NT_TRANSFORM_3D1 rotationOrder ( 0 )
opset -d off -r off -h off -f off -y off -t off -l off -s off -u off -F on -c on -e on -b off -L off -M off -H on -E off $_obj_shopnet1_occ_target_NT_TRANSFORM_3D1
opexprlanguage -s hscript $_obj_shopnet1_occ_target_NT_TRANSFORM_3D1
opuserdata -n '___toolcount___' -v '1' $_obj_shopnet1_occ_target_NT_TRANSFORM_3D1
opuserdata -n '___toolid___' -v 'OCT' $_obj_shopnet1_occ_target_NT_TRANSFORM_3D1

# Node $_obj_shopnet1_occ_target_NT_PROJ_SPHERICAL1 (octane::Vop/NT_PROJ_SPHERICAL)
set _obj_shopnet1_occ_target_NT_PROJ_SPHERICAL1 = `run("opadd -e -n -v octane::NT_PROJ_SPHERICAL NT_PROJ_SPHERICAL1")`
oplocate -x `$arg2 + -13.754705912155265` -y `$arg3 + -0.88499999698251486` $_obj_shopnet1_occ_target_NT_PROJ_SPHERICAL1
opset -d off -r off -h off -f off -y off -t off -l off -s off -u off -F on -c on -e on -b off -L off -M off -H on -E off $_obj_shopnet1_occ_target_NT_PROJ_SPHERICAL1
opexprlanguage -s hscript $_obj_shopnet1_occ_target_NT_PROJ_SPHERICAL1
opuserdata -n '___toolcount___' -v '1' $_obj_shopnet1_occ_target_NT_PROJ_SPHERICAL1
opuserdata -n '___toolid___' -v 'OCT' $_obj_shopnet1_occ_target_NT_PROJ_SPHERICAL1

# Node $_obj_shopnet1_occ_target_NT_IMAGER_CAMERA1 (octane::Vop/NT_IMAGER_CAMERA)
set _obj_shopnet1_occ_target_NT_IMAGER_CAMERA1 = `run("opadd -e -n -v octane::NT_IMAGER_CAMERA NT_IMAGER_CAMERA1")`
oplocate -x `$arg2 + -5.3371242128088596` -y `$arg3 + -2.3496928134750044` $_obj_shopnet1_occ_target_NT_IMAGER_CAMERA1
opset -d off -r off -h off -f off -y off -t off -l off -s off -u off -F on -c on -e on -b off -L off -M off -H on -E off $_obj_shopnet1_occ_target_NT_IMAGER_CAMERA1
opexprlanguage -s hscript $_obj_shopnet1_occ_target_NT_IMAGER_CAMERA1
opuserdata -n '___toolcount___' -v '1' $_obj_shopnet1_occ_target_NT_IMAGER_CAMERA1
opuserdata -n '___toolid___' -v 'OCT' $_obj_shopnet1_occ_target_NT_IMAGER_CAMERA1
opcf ..
opcf ..
opcf $_obj_shopnet1
opcf $_obj_shopnet1_occ_target
oporder -e octane_render_target1 NT_CAM_THINLENS1 NT_KERN_PATHTRACING1 NT_ENV_TEXTURE1 NT_TEX_IMAGE1 NT_TRANSFORM_3D1 NT_PROJ_SPHERICAL1 NT_IMAGER_CAMERA1 
opcf ..
opcf ..
opset -p on $_obj_shopnet1
opcf $arg1

# Node $_obj_ropnet1 (Object/ropnet)
set _obj_ropnet1 = `run("opadd -e -n -v ropnet ropnet1")`
oplocate -x `$arg2 + 2.8230681715575621` -y `$arg3 + -5.9604645663569045e-09` $_obj_ropnet1
opset -d off -r off -h off -f off -y off -t off -l off -s off -u off -F on -c on -e on -b off $_obj_ropnet1
opexprlanguage -s hscript $_obj_ropnet1
opuserdata -n '___toolcount___' -v '1' $_obj_ropnet1
opuserdata -n '___toolid___' -v 'OCT' $_obj_ropnet1
opcf $_obj_ropnet1

# Node $_obj_ropnet1_Octane_ROP1 (Driver/Octane_ROP)
set _obj_ropnet1_Octane_ROP1 = `run("opadd -e -n -v Octane_ROP Octane_ROP1")`
oplocate -x `$arg2 + -0.7069224981188853` -y `$arg3 + 1.8500000000000001` $_obj_ropnet1_Octane_ROP1
chblockbegin
chadd -t 0 0 $_obj_ropnet1_Octane_ROP1 f1
chkey -t 0 -v 1 -m 0 -a 0 -A 0 -T a  -F '$FSTART' $_obj_ropnet1_Octane_ROP1/f1
chadd -t 0 0 $_obj_ropnet1_Octane_ROP1 f2
chkey -t 0 -v 240 -m 0 -a 0 -A 0 -T a  -F '$FEND' $_obj_ropnet1_Octane_ROP1/f2
chblockend
opparm -V 18.0.499 $_obj_ropnet1_Octane_ROP1 HO_renderCamera ( '`chsop("../../CONTROLS/cam")`' ) HO_iprCamera ( '`chsop("../../CONTROLS/cam")`' ) HO_renderTarget ( ../../shopnet1/occ_target )
opset -d on -r on -h off -f off -y off -t off -l off -s off -u off -F on -c on -e on -b off $_obj_ropnet1_Octane_ROP1
opexprlanguage -s hscript $_obj_ropnet1_Octane_ROP1
opuserdata -n '___toolcount___' -v '1' $_obj_ropnet1_Octane_ROP1
opuserdata -n '___toolid___' -v 'OCT' $_obj_ropnet1_Octane_ROP1
opcf ..
opset -p on $_obj_ropnet1
opcf $arg1

# Node $_obj_CONTROLS (Object/null)
set _obj_CONTROLS = `run("opadd -e -n -v null CONTROLS")`
oplocate -x `$arg2 + 0` -y `$arg3 + -1.2942061700526706` $_obj_CONTROLS
opspareds '    group {         name    "stdswitcher4"         label   "Transform"         invisibletab          parm {             name    "xOrd"             baseparm             label   "Transform Order"             joinnext             export  none         }         parm {             name    "rOrd"             baseparm             label   "Rotate Order"             nolabel             export  none         }         parm {             name    "t"             baseparm             label   "Translate"             export  all         }         parm {             name    "r"             baseparm             label   "Rotate"             export  all         }         parm {             name    "s"             baseparm             label   "Scale"             export  none         }         parm {             name    "p"             baseparm             label   "Pivot Translate"             export  none         }         parm {             name    "pr"             baseparm             label   "Pivot Rotate"             export  none         }         parm {             name    "scale"             baseparm             label   "Uniform Scale"             export  none         }         parm {             name    "pre_xform"             baseparm             label   "Modify Pre-Transform"             export  none         }         parm {             name    "keeppos"             baseparm             label   "Keep Position When Parenting"             export  none         }         parm {             name    "childcomp"             baseparm             label   "Child Compensation"             export  none         }         parm {             name    "constraints_on"             baseparm             label   "Enable Constraints"             export  none         }         parm {             name    "constraints_path"             baseparm             label   "Constraints"             export  none         }         parm {             name    "lookatpath"             baseparm             label   "Look At"             invisible             export  none         }         parm {             name    "lookupobjpath"             baseparm             label   "Look Up Object"             invisible             export  none         }         parm {             name    "lookup"             baseparm             label   "Look At Up Vector"             invisible             export  none         }         parm {             name    "pathobjpath"             baseparm             label   "Path Object"             invisible             export  none         }         parm {             name    "roll"             baseparm             label   "Roll"             invisible             export  none         }         parm {             name    "pos"             baseparm             label   "Position"             invisible             export  none         }         parm {             name    "uparmtype"             baseparm             label   "Parameterization"             invisible             export  none         }         parm {             name    "pathorient"             baseparm             label   "Orient Along Path"             invisible             export  none         }         parm {             name    "up"             baseparm             label   "Orient Up Vector"             invisible             export  none         }         parm {             name    "bank"             baseparm             label   "Auto-Bank factor"             invisible             export  none         }     }      group {         name    "stdswitcher4_1"         label   "Render"         invisibletab          parm {             name    "tdisplay"             baseparm             label   "Display"             joinnext             export  none         }         parm {             name    "display"             baseparm             label   "Display"             export  none         }         parm {             name    "renderspace"             baseparm             label   "Output transform as render space (RIB/IFD)"             export  none         }     }      group {         name    "stdswitcher4_2"         label   "Misc"         invisibletab          parm {             name    "use_dcolor"             baseparm             label   "Set Wireframe Color"             export  none         }         parm {             name    "dcolor"             baseparm             label   "Wireframe Color"             export  none         }         parm {             name    "picking"             baseparm             label   "Viewport Selecting Enabled"             export  none         }         parm {             name    "pickscript"             baseparm             label   "Select Script"             export  none         }         parm {             name    "caching"             baseparm             label   "Cache Object Transform"             export  none         }         parm {             name    "geoscale"             baseparm             label   "Display Uniform Scale"             export  none         }         parm {             name    "geosize"             baseparm             label   "Display Scale"             export  none         }         parm {             name    "geocenter"             baseparm             label   "Display Center"             export  none         }         parm {             name    "georotate"             baseparm             label   "Display Rotate"             export  none         }         parm {             name    "displayicon"             baseparm             label   "Display"             export  none         }         parm {             name    "controltype"             baseparm             label   "Control Type"             export  none         }         parm {             name    "geocustom"             baseparm             label   "Display Custom"             export  none         }         parm {             name    "orientation"             baseparm             label   "Orientation"             export  none         }         parm {             name    "shadedmode"             baseparm             label   "Shaded Mode"             export  none         }         parm {             name    "vport_shadeopen"             baseparm             label   "Shade Open Curves In Viewport"             invisible             export  none         }         parm {             name    "vport_displayassubdiv"             baseparm             label   "Display as Subdivision in Viewport"             invisible             export  none         }         parm {             name    "shop_materialpath"             baseparm             label   "Material"             invisible             export  none         }         parm {             name    "shop_materialopts"             baseparm             label   "Options"             invisible             export  none         }     }      group {         name    "stdswitcher4_3"         label   "Octane"         invisibletab          group {             name    "octane_objprop_switcher"             label   "Properties"              parm {                 name    "octane_objprop_layer"                 label   "Object layer ID"                 type    integer                 default { "1" }                 range   { 1! 999! }             }             parm {                 name    "octane_objprop_color"                 label   "Object layer color"                 type    color                 size    3                 default { "0" "0" "0" }                 range   { 0 1 }             }             parm {                 name    "octane_objprop_baking"                 label   "Object baking group"                 type    integer                 default { "1" }                 range   { 1! 999! }             }             parm {                 name    "octane_objprop_generalVis"                 label   "General visibility"                 type    float                 default { "1" }                 range   { 0! 1! }             }             parm {                 name    "octane_objprop_cameraVis"                 label   "Camera visibility"                 type    toggle                 default { "1" }             }             parm {                 name    "octane_objprop_shadowVis"                 label   "Shadow visibility"                 type    toggle                 default { "1" }             }             parm {                 name    "octane_objprop_dirtVis"                 label   "Dirt visibility"                 type    toggle                 default { "1" }             }             parm {                 name    "octane_objprop_smoothAngle"                 label   "Smooth angle"                 type    float                 default { "89" }                 range   { 0! 180! }             }             parm {                 name    "octane_objprop_hideObject"                 label   "Hide object in render"                 type    toggle                 default { "0" }             }             parm {                 name    "octane_objprop_instacesMBFromVelocity"                 label   "Instancing MB computed from velocity attribute"                 type    toggle                 default { "0" }             }             parm {                 name    "octane_objprop_sep1"                 label   "octane_objprop_sep1"                 type    separator                 default { "" }             }             parm {                 name    "octane_objprop_objectInstanceID"                 label   "Object level instance ID"                 type    integer                 default { "-1" }                 range   { 0 10 }             }             parm {                 name    "octane_objprop_instancesIDfrom"                 label   "Instances IDs from "                 type    ordinal                 default { "0" }                 menu {                     "Cd"    "Packed RGBA values from \'Cd\' point attribute"                     "id"    "\'id\' point attribute"                 }             }         }          group {             name    "octane_objprop_switcher_1"             label   "Attributes"              parm {                 name    "octane_objprop_attr_point_float"                 label   "Point Float Attrs."                 type    string                 default { "" }                 menutoggle {                     [ "result = []                                                             " ]                     [ "geo = hou.pwd().renderNode().geometry()      " ]                     [ "for attr in geo.pointAttribs():                      " ]                     [ "        result.append(attr.name())           " ]                     [ "        result.append(attr.name())           " ]                     [ "return result                                                        " ]                     language python                 }             }             parm {                 name    "octane_objprop_attr_point_vect3"                 label   "Point Vector Attrs."                 type    string                 default { "" }                 menutoggle {                     [ "result = []                                                                " ]                     [ "geo = hou.pwd().renderNode().geometry()      " ]                     [ "for attr in geo.pointAttribs():                      " ]                     [ "        result.append(attr.name())           " ]                     [ "        result.append(attr.name())           " ]                     [ "return result                                                        " ]                     language python                 }             }             parm {                 name    "octane_objprop_attr_vertex_float"                 label   "Vertex Float Attrs."                 type    string                 default { "" }                 menutoggle {                     [ "result = []                                                               " ]                     [ "geo = hou.pwd().renderNode().geometry()      " ]                     [ "for attr in geo.vertexAttribs():             " ]                     [ "        result.append(attr.name())           " ]                     [ "        result.append(attr.name())           " ]                     [ "return result                                                        " ]                     language python                 }             }             parm {                 name    "octane_objprop_attr_vertex_vect3"                 label   "Vertex Vector Attrs."                 type    string                 default { "" }                 menutoggle {                     [ "result = []                                                              " ]                     [ "geo = hou.pwd().renderNode().geometry()      " ]                     [ "for attr in geo.vertexAttribs():             " ]                     [ "        result.append(attr.name())           " ]                     [ "        result.append(attr.name())           " ]                     [ "return result                                                        " ]                     language python                 }             }         }          group {             name    "octane_objprop_switcher_2"             label   "Light Pass Mask"              parm {                 name    "octane_objprop_lpm_sun"                 label   "Light Pass Sun"                 type    toggle                 default { "1" }             }             parm {                 name    "octane_objprop_lpm_env"                 label   "Light Pass Environment"                 type    toggle                 default { "1" }             }             parm {                 name    "octane_objprop_lpm_1"                 label   "Light Pass 1"                 type    toggle                 default { "1" }             }             parm {                 name    "octane_objprop_lpm_2"                 label   "Light Pass 2"                 type    toggle                 default { "1" }             }             parm {                 name    "octane_objprop_lpm_3"                 label   "Light Pass 3"                 type    toggle                 default { "1" }             }             parm {                 name    "octane_objprop_lpm_4"                 label   "Light Pass 4"                 type    toggle                 default { "1" }             }             parm {                 name    "octane_objprop_lpm_5"                 label   "Light Pass 5"                 type    toggle                 default { "1" }             }             parm {                 name    "octane_objprop_lpm_6"                 label   "Light Pass 6"                 type    toggle                 default { "1" }             }             parm {                 name    "octane_objprop_lpm_7"                 label   "Light Pass 7"                 type    toggle                 default { "1" }             }             parm {                 name    "octane_objprop_lpm_8"                 label   "Light Pass 8"                 type    toggle                 default { "1" }             }         }          group {             name    "octane_objprop_switcher_3"             label   "OpenSUBD"              parm {                 name    "octane_osd_level"                 label   "Subdivision level"                 type    integer                 default { "0" }                 range   { 0! 10! }             }             parm {                 name    "octane_osd_sharpness"                 label   "Subdivision sharpness"                 type    float                 default { "0" }                 disablewhen "{ octane_osd_level == 0 }"                 range   { 0! 1! }             }             parm {                 name    "octane_osd_interpolation"                 label   "Boundary interpolation"                 type    ordinal                 default { "2" }                 disablewhen "{ octane_osd_level == 0 }"                 menu {                     "none"          "None"                     "edgeOnly"      "Edge only"                     "edgeAndCorner" "Edge and corner"                     "alwaysSharp"   "Always sharp"                 }             }             parm {                 name    "octane_osd_scheme"                 label   "Subdivision scheme"                 type    ordinal                 default { "0" }                 disablewhen "{ octane_osd_level == 0 }"                 menu {                     "cc"        "Catmull-Clark"                     "loop"      "Loop"                     "bilinear"  "Bilinear"                 }             }         }          group {             name    "octane_objprop_switcher_4"             label   "Fur"              parm {                 name    "octane_objprop_fur"                 label   "Render as curves/fur object"                 type    toggle                 default { "0" }             }             parm {                 name    "octane_objprop_fur_rthick"                 label   "Curve root thickness"                 type    log                 default { "0.001" }                 disablewhen "{ octane_objprop_fur == 0 }"                 range   { 0! 1! }             }             parm {                 name    "octane_objprop_fur_tthick"                 label   "Curve tip thickness"                 type    log                 default { "0.001" }                 disablewhen "{ octane_objprop_fur == 0 }"                 range   { 0! 1! }             }             parm {                 name    "octane_objprop_fur_interp"                 label   "Hair gradient interpolation"                 type    ordinal                 default { "0" }                 disablewhen "{ octane_objprop_fur == 0 }"                 menu {                     "length"    "Length"                     "segments"  "Segments"                 }             }             parm {                 name    "octane_objprop_fur_packuv"                 label   "Pack Color/Alpha attributes in the UV map"                 type    toggle                 default { "0" }                 disablewhen "{ octane_objprop_fur == 0 }"             }             parm {                 name    "octane_objprop_fur_packc"                 label   "Prim. color attribute"                 type    string                 default { "Cd" }                 disablewhen "{ octane_objprop_fur == 0 } { octane_objprop_fur_packuv == 0 }"             }             parm {                 name    "octane_objprop_fur_packa"                 label   "Prim. alpha attribute"                 type    string                 default { "" }                 disablewhen "{ octane_objprop_fur == 0 } { octane_objprop_fur_packuv == 0 }"             }         }          group {             name    "octane_objprop_switcher_5"             label   "Tessellation"              parm {                 name    "octane_objprop_tess_ngons"                 label   "Tessellate NGons"                 type    toggle                 default { "0" }             }             parm {                 name    "octane_objprop_tess_enable"                 label   "Render as tessellated object"                 type    toggle                 default { "0" }             }             parm {                 name    "octane_objprop_tess_u"                 label   "U subdivisions"                 type    integer                 default { "1" }                 disablewhen "{ octane_objprop_tess_enable == 0 }"                 range   { 0! 16! }             }             parm {                 name    "octane_objprop_tess_v"                 label   "V subdivisions"                 type    integer                 default { "1" }                 disablewhen "{ octane_objprop_tess_enable == 0 }"                 range   { 0! 16! }             }             parm {                 name    "octane_objprop_tess_trim"                 label   "Trimming subdivisions"                 type    integer                 default { "1" }                 disablewhen "{ octane_objprop_tess_enable == 0 }"                 range   { 0! 16! }             }         }          group {             name    "octane_objprop_switcher_6"             label   "Volumes"              parm {                 name    "octane_objprop_volume_enable"                 label   "Render volume primitives"                 type    toggle                 default { "0" }             }             parm {                 name    "octane_objprop_volume_type"                 label   "Volume type"                 type    ordinal                 default { "0" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"                 menu {                     "volume"    "Volume"                     "sdf"       "SDF"                 }             }             parm {                 name    "octane_objprop_volume_absorption"                 label   "Absorption/SDF grid"                 type    string                 default { "density" }                 disablewhen "{ octane_objprop_volume_enable == 0 } { octane_objprop_volume_aux_abs == 1 }"             }             parm {                 name    "octane_objprop_volume_abs_scale"                 label   "Absorption scale"                 type    float                 default { "1" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"                 range   { 0 10 }             }             parm {                 name    "octane_objprop_volume_scattering"                 label   "Scattering grid"                 type    string                 default { "density" }                 disablewhen "{ octane_objprop_volume_enable == 0 } { octane_objprop_volume_aux_sca == 1 }"             }             parm {                 name    "octane_objprop_volume_sca_scale"                 label   "Scattering scale"                 type    float                 default { "1" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"                 range   { 0 10 }             }             parm {                 name    "octane_objprop_volume_emission"                 label   "Emission grid"                 type    string                 default { "temperature" }                 disablewhen "{ octane_objprop_volume_enable == 0 } { octane_objprop_volume_aux_emi == 1 }"             }             parm {                 name    "octane_objprop_volume_emi_scale"                 label   "Emission scale"                 type    float                 default { "1" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"                 range   { 0 10 }             }             parm {                 name    "octane_objprop_volume_vel_x"                 label   "Velocity.x grid"                 type    string                 default { "vel.x" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"             }             parm {                 name    "octane_objprop_volume_vel_y"                 label   "Velocity.y grid"                 type    string                 default { "vel.y" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"             }             parm {                 name    "octane_objprop_volume_vel_z"                 label   "Velocity.z grid"                 type    string                 default { "vel.z" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"             }             parm {                 name    "octane_objprop_volume_vel_scale"                 label   "Velocity scale"                 type    float                 default { "1" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"                 range   { 0 10 }             }             parm {                 name    "octane_objprop_volume_vel_sep1"                 label   "sep1"                 type    separator                 default { "" }             }             parm {                 name    "octane_objprop_volume_aux_x"                 label   "Additional.x grid"                 type    string                 default { "" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"             }             parm {                 name    "octane_objprop_volume_aux_y"                 label   "Additional.y grid"                 type    string                 default { "" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"             }             parm {                 name    "octane_objprop_volume_aux_z"                 label   "Additional.z grid"                 type    string                 default { "" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"             }             parm {                 name    "octane_objprop_volume_aux_abs"                 label   "Absorption from the additional vector"                 type    toggle                 default { "0" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"             }             parm {                 name    "octane_objprop_volume_aux_sca"                 label   "Scattering from the additional vector"                 type    toggle                 default { "0" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"             }             parm {                 name    "octane_objprop_volume_aux_emi"                 label   "Emission from the additional vector"                 type    toggle                 default { "0" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"             }             parm {                 name    "octane_objprop_volume_vel_sep2"                 label   "sep2"                 type    separator                 default { "" }             }             parm {                 name    "octane_objprop_volume_abs_default"                 label   "Absorption/SDF background"                 type    float                 size    3                 default { "0" "0" "0" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"                 range   { 0 10 }             }             parm {                 name    "octane_objprop_volume_emi_default"                 label   "Emission background"                 type    float                 size    3                 default { "0" "0" "0" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"                 range   { 0 10 }             }             parm {                 name    "octane_objprop_volume_sca_default"                 label   "Scattering background"                 type    float                 size    3                 default { "0" "0" "0" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"                 range   { 0 10 }             }             parm {                 name    "octane_objprop_volume_vel_default"                 label   "Velocity background"                 type    float                 size    3                 default { "0" "0" "0" }                 disablewhen "{ octane_objprop_volume_enable == 0 }"                 range   { 0 10 }             }         }          group {             name    "octane_objprop_switcher_7"             label   "OpenVDB"              parm {                 name    "octane_objprop_vdb_enable"                 label   "Render OpenVDB file"                 type    toggle                 default { "0" }             }             parm {                 name    "octane_objprop_vdb_type"                 label   "Volume type"                 type    ordinal                 default { "0" }                 disablewhen "{ octane_objprop_vdb_enable == 0 }"                 menu {                     "volume"    "Volume"                     "sdf"       "SDF"                 }             }             parm {                 name    "octane_objprop_vdb_file"                 label   "OpenVDB file"                 type    file                 default { "" }                 disablewhen "{ octane_objprop_vdb_enable == 0 }"             }             parm {                 name    "octane_objprop_vdb_absorption"                 label   "Absorption/SDF grid"                 type    string                 default { "density" }                 disablewhen "{ octane_objprop_vdb_enable == 0 }"             }             parm {                 name    "octane_objprop_vdb_abs_scale"                 label   "Absorption scale"                 type    float                 default { "1" }                 disablewhen "{ octane_objprop_vdb_enable == 0 }"                 range   { 0 10 }             }             parm {                 name    "octane_objprop_vdb_scattering"                 label   "Scattering grid"                 type    string                 default { "density" }                 disablewhen "{ octane_objprop_vdb_enable == 0 }"             }             parm {                 name    "octane_objprop_vdb_sca_scale"                 label   "Scattering scale"                 type    float                 default { "1" }                 disablewhen "{ octane_objprop_vdb_enable == 0 }"                 range   { 0 10 }             }             parm {                 name    "octane_objprop_vdb_emission"                 label   "Emission grid"                 type    string                 default { "temperature" }                 disablewhen "{ octane_objprop_vdb_enable == 0 }"             }             parm {                 name    "octane_objprop_vdb_emi_scale"                 label   "Emission scale"                 type    float                 default { "1" }                 disablewhen "{ octane_objprop_vdb_enable == 0 }"                 range   { 0 10 }             }             parm {                 name    "octane_objprop_vdb_vel_x"                 label   "Velocity/Velocity.x grid"                 type    string                 default { "" }                 disablewhen "{ octane_objprop_vdb_enable == 0 }"             }             parm {                 name    "octane_objprop_vdb_vel_y"                 label   "Velocity.y grid"                 type    string                 default { "" }                 disablewhen "{ octane_objprop_vdb_enable == 0 }"             }             parm {                 name    "octane_objprop_vdb_vel_z"                 label   "Velocity.z grid"                 type    string                 default { "" }                 disablewhen "{ octane_objprop_vdb_enable == 0 }"             }             parm {                 name    "octane_objprop_vdb_vel_scale"                 label   "Velocity scale"                 type    float                 default { "1" }                 disablewhen "{ octane_objprop_vdb_enable == 0 }"                 range   { 0 10 }             }             parm {                 name    "octane_objprop_vdb_scale"                 label   "Size units"                 type    ordinal                 default { "3" }                 disablewhen "{ octane_objprop_vdb_enable == 0 }"                 menu {                     "milimeters"    "Milimeters"                     "centimeters"   "Centimeters"                     "decimeters"    "Decimeters"                     "meters"        "Meters"                     "decameters"    "Decameters"                     "hectometers"   "Hectometers"                     "kilometers"    "Kilometers"                     "inches"        "Inches"                     "feets"         "Feets"                     "yards"         "Yards"                     "fulgongs"      "Fulgongs"                     "miles"         "Miles"                 }             }             parm {                 name    "octane_objprop_vdb_isovalue"                 label   "Isovalue"                 type    float                 default { "0.04" }                 disablewhen "{ octane_objprop_vdb_enable == 0 }"                 range   { 0 10 }             }         }          group {             name    "octane_objprop_switcher_8"             label   "Particles"              parm {                 name    "octane_objprop_particle"                 label   "Render as sphere particles"                 type    toggle                 default { "0" }             }             parm {                 name    "octane_objprop_particle_radius"                 label   "Default radius"                 type    float                 default { "0.1" }                 disablewhen "{ octane_objprop_particle == 0 }"                 range   { 0 10 }             }             parm {                 name    "octane_objprop_particle_mult"                 label   "Radius global scale"                 type    float                 default { "1" }                 disablewhen "{ octane_objprop_particle == 0 }"                 range   { 0 10 }             }             parm {                 name    "octane_objprop_particle_packuv"                 label   "Pack Color/Alpha attributes in the UV map"                 type    toggle                 default { "0" }                 disablewhen "{ octane_objprop_particle == 0 }"             }             parm {                 name    "octane_objprop_particle_packc"                 label   "Color attribute"                 type    string                 default { "Cd" }                 disablewhen "{ octane_objprop_particle == 0 } { octane_objprop_particle_packuv == 0 }"             }             parm {                 name    "octane_objprop_particle_packa"                 label   "Alpha attribute"                 type    string                 default { "" }                 disablewhen "{ octane_objprop_particle == 0 } { octane_objprop_particle_packuv == 0 }"             }         }          group {             name    "octane_objprop_switcher_9"             label   "Vectron"              parm {                 name    "octane_objprop_vectron"                 label   "Render as OSL Vectron object"                 type    toggle                 default { "0" }             }             parm {                 name    "octane_objprop_vectronPath"                 label   "OSL Vectron VOP node"                 type    oppath                 default { "" }                 disablewhen "{ octane_objprop_vectron == 0 }"                 parmtag { "opfilter" "!!VOP!!" }                 parmtag { "oprelative" "." }             }         }          group {             name    "octane_objprop_switcher_10"             label   "Light Emission"              parm {                 name    "octane_emission_enable"                 label   "Enable light emission"                 type    toggle                 default { "0" }             }             parm {                 name    "octane_emission_type"                 label   "Emission type"                 type    ordinal                 default { "0" }                 disablewhen "{ octane_emission_enable == 0 }"                 menu {                     "bb"        "Black body"                     "col"       "Color/Texture"                     "portal"    "Light portal"                 }             }             parm {                 name    "octane_emission_temp"                 label   "Color temperature"                 type    float                 default { "6500" }                 disablewhen "{ octane_emission_enable == 0 }"                 range   { 500! 12000! }             }             parm {                 name    "octane_emission_rgb"                 label   "Color RGB"                 type    color                 size    3                 default { "0" "0" "0" }                 disablewhen "{ octane_emission_enable == 0 }"                 range   { 0 1 }             }             parm {                 name    "octane_emission_power"                 label   "Power"                 type    float                 default { "100" }                 disablewhen "{ octane_emission_enable == 0 }"                 range   { 0! 10000 }             }             parm {                 name    "octane_emission_efficiency"                 label   "Efficiency"                 type    float                 default { "1" }                 disablewhen "{ octane_emission_enable == 0 }"                 range   { 0! 1! }             }             parm {                 name    "octane_emission_sr"                 label   "Sample Rate"                 type    float                 default { "1" }                 disablewhen "{ octane_emission_enable == 0 }"                 range   { 0! 100! }             }             parm {                 name    "octane_emission_normalize"                 label   "Normalize"                 type    toggle                 default { "1" }                 disablewhen "{ octane_emission_enable == 0 }"             }             parm {                 name    "octane_emission_sb"                 label   "Surface brightness"                 type    toggle                 default { "0" }                 disablewhen "{ octane_emission_enable == 0 }"             }             parm {                 name    "octane_emission_keepInstanceP"                 label   "Keep Instance Power"                 type    toggle                 default { "0" }                 disablewhen "{ octane_emission_enable == 0 }"             }             parm {                 name    "octane_emission_cast"                 label   "Visible on diffuse"                 type    toggle                 default { "1" }                 disablewhen "{ octane_emission_enable == 0 }"             }             parm {                 name    "octane_emission_castSpec"                 label   "Visible on specular"                 type    toggle                 default { "1" }                 disablewhen "{ octane_emission_enable == 0 }"             }             parm {                 name    "octane_emission_transparentEmis"                 label   "Transparent emission"                 type    toggle                 default { "1" }                 disablewhen "{ octane_emission_enable == 0 }"             }             parm {                 name    "octane_emission_castShadows"                 label   "Cast shadows"                 type    toggle                 default { "1" }                 disablewhen "{ octane_emission_enable == 0 }"             }             parm {                 name    "octane_emission_doubleSided"                 label   "Double sided"                 type    toggle                 default { "0" }                 disablewhen "{ octane_emission_enable == 0 }"             }             parm {                 name    "octane_emission_texture"                 label   "Texture/IES file"                 type    file                 default { "" }                 disablewhen "{ octane_emission_enable == 0 }"             }             parm {                 name    "octane_emission_textype"                 label   "Texture type"                 type    ordinal                 default { "0" }                 disablewhen "{ octane_emission_enable == 0 }"                 menu {                     "col"   "Color"                     "float" "Float/IES"                 }             }             parm {                 name    "octane_emission_texgamma"                 label   "Texture gamma"                 type    float                 default { "1" }                 disablewhen "{ octane_emission_enable == 0 }"                 range   { 0 10 }             }             parm {                 name    "octane_emission_texpower"                 label   "Texture HDRI power"                 type    float                 default { "1" }                 disablewhen "{ octane_emission_enable == 0 }"                 range   { 0 10 }             }             parm {                 name    "octane_emission_texinvert"                 label   "Invert texture"                 type    toggle                 default { "0" }                 disablewhen "{ octane_emission_enable == 0 }"             }             parm {                 name    "octane_emission_lightPassID"                 label   "Light pass ID"                 type    integer                 default { "1" }                 disablewhen "{ octane_emission_enable == 0 }"                 range   { 1! 8! }             }         }      }      parm {         name    "cam"         label   "cam"         type    string         default { "" }         parmtag { "script_callback_language" "python" }     }     parm {         name    "hdri_pow"         label   "HDRI Power"         type    float         default { "0" }         range   { 0 10 }         parmtag { "script_callback_language" "python" }     }     parm {         name    "ibl_file"         label   "IBL"         type    image         default { "" }         parmtag { "script_callback_language" "python" }     } ' $_obj_CONTROLS
opset -S on $_obj_CONTROLS
opparm -V 18.0.499 $_obj_CONTROLS hdri_pow ( 1 )
chautoscope $_obj_CONTROLS +tx +ty +tz +rx +ry +rz +sx +sy +sz
opset -d on -r off -h off -f off -y on -t off -l off -s off -u off -F on -c on -e on -b off -x off $_obj_CONTROLS
opexprlanguage -s hscript $_obj_CONTROLS
opcf $_obj_CONTROLS

# Node $_obj_CONTROLS_control1 (Sop/control)
set _obj_CONTROLS_control1 = `run("opadd -e -n -v control control1")`
oplocate -x `$arg2 + 0.5` -y `$arg3 + 1` $_obj_CONTROLS_control1
opparm $_obj_CONTROLS_control1  numsnappoints ( 0 )
chblockbegin
chadd -t 0 0 $_obj_CONTROLS_control1 usecolor
chkey -t 0 -v 1 -m 0 -a 0 -A 0 -T a  -F 'ch("../use_dcolor")' $_obj_CONTROLS_control1/usecolor
chadd -t 0 0 $_obj_CONTROLS_control1 colorr
chkey -t 0 -v 1 -m 0 -a 0 -A 0 -T a  -F 'ch("../dcolorr")' $_obj_CONTROLS_control1/colorr
chadd -t 0 0 $_obj_CONTROLS_control1 colorg
chkey -t 0 -v 1 -m 0 -a 0 -A 0 -T a  -F 'ch("../dcolorg")' $_obj_CONTROLS_control1/colorg
chadd -t 0 0 $_obj_CONTROLS_control1 colorb
chkey -t 0 -v 1 -m 0 -a 0 -A 0 -T a  -F 'ch("../dcolorb")' $_obj_CONTROLS_control1/colorb
chadd -t 0 0 $_obj_CONTROLS_control1 sizex
chkey -t 0 -v 1 -m 0 -a 0 -A 0 -T a  -F 'ch("../geosizex")' $_obj_CONTROLS_control1/sizex
chadd -t 0 0 $_obj_CONTROLS_control1 sizey
chkey -t 0 -v 1 -m 0 -a 0 -A 0 -T a  -F 'ch("../geosizey")' $_obj_CONTROLS_control1/sizey
chadd -t 0 0 $_obj_CONTROLS_control1 sizez
chkey -t 0 -v 1 -m 0 -a 0 -A 0 -T a  -F 'ch("../geosizez")' $_obj_CONTROLS_control1/sizez
chadd -t 0 0 $_obj_CONTROLS_control1 tx
chkey -t 0 -v 0 -m 0 -a 0 -A 0 -T a  -F 'ch("../geocenterx")' $_obj_CONTROLS_control1/tx
chadd -t 0 0 $_obj_CONTROLS_control1 ty
chkey -t 0 -v 0 -m 0 -a 0 -A 0 -T a  -F 'ch("../geocentery")' $_obj_CONTROLS_control1/ty
chadd -t 0 0 $_obj_CONTROLS_control1 tz
chkey -t 0 -v 0 -m 0 -a 0 -A 0 -T a  -F 'ch("../geocenterz")' $_obj_CONTROLS_control1/tz
chadd -t 0 0 $_obj_CONTROLS_control1 rx
chkey -t 0 -v 0 -m 0 -a 0 -A 0 -T a  -F 'ch("../georotatex")' $_obj_CONTROLS_control1/rx
chadd -t 0 0 $_obj_CONTROLS_control1 ry
chkey -t 0 -v 0 -m 0 -a 0 -A 0 -T a  -F 'ch("../georotatey")' $_obj_CONTROLS_control1/ry
chadd -t 0 0 $_obj_CONTROLS_control1 rz
chkey -t 0 -v 0 -m 0 -a 0 -A 0 -T a  -F 'ch("../georotatez")' $_obj_CONTROLS_control1/rz
chadd -t 0 0 $_obj_CONTROLS_control1 scale
chkey -t 0 -v 1 -m 0 -a 0 -A 0 -T a  -F 'ch("../geoscale")' $_obj_CONTROLS_control1/scale
chadd -t 0 0 $_obj_CONTROLS_control1 displayicon
chkey -t 0 -v 0 -m 0 -a 0 -A 0 -T a  -F 'ch("../displayicon")' $_obj_CONTROLS_control1/displayicon
chadd -t 0 0 $_obj_CONTROLS_control1 controltype
chkey -t 0 -v 0 -m 0 -a 0 -A 0 -T a  -F 'ch("../controltype")' $_obj_CONTROLS_control1/controltype
chadd -t 0 0 $_obj_CONTROLS_control1 orientation
chkey -t 0 -v 0 -m 0 -a 0 -A 0 -T a  -F 'ch("../orientation")' $_obj_CONTROLS_control1/orientation
chadd -t 0 0 $_obj_CONTROLS_control1 shadedmode
chkey -t 0 -v 0 -m 0 -a 0 -A 0 -T a  -F 'ch("../shadedmode")' $_obj_CONTROLS_control1/shadedmode
chblockend
opparm -V 18.0.499 $_obj_CONTROLS_control1 usecolor ( usecolor ) color ( colorr colorg colorb ) size ( sizex sizey sizez ) t ( tx ty tz ) r ( rx ry rz ) scale ( scale ) displayicon ( displayicon ) controltype ( controltype ) orientation ( orientation ) shadedmode ( shadedmode )
opset -d on -r on -h off -f off -y off -t off -l off -s off -u off -F on -c on -e on -b off $_obj_CONTROLS_control1
opexprlanguage -s hscript $_obj_CONTROLS_control1

# Node $_obj_CONTROLS_point1 (Sop/add)
set _obj_CONTROLS_point1 = `run("opadd -e -n -v add point1")`
oplocate -x `$arg2 + 2.5` -y `$arg3 + 1` $_obj_CONTROLS_point1
opparm $_obj_CONTROLS_point1  points ( 1 ) prims ( 1 )
opparm -V 18.0.499 $_obj_CONTROLS_point1 usept0 ( on )
opset -d off -r off -h off -f off -y off -t off -l off -s off -u off -F on -c on -e on -b off $_obj_CONTROLS_point1
opexprlanguage -s hscript $_obj_CONTROLS_point1
oporder -e control1 point1 
opcf ..
opset -p on $_obj_CONTROLS

opcf $arg1
opcf $_obj_shopnet1
opcf $_obj_shopnet1_occ_target
opwire -n $_obj_shopnet1_occ_target_NT_CAM_THINLENS1 -0 $_obj_shopnet1_occ_target_octane_render_target1
opwire -n $_obj_shopnet1_occ_target_NT_ENV_TEXTURE1 -1 $_obj_shopnet1_occ_target_octane_render_target1
opwire -n $_obj_shopnet1_occ_target_NT_IMAGER_CAMERA1 -2 $_obj_shopnet1_occ_target_octane_render_target1
opwire -n $_obj_shopnet1_occ_target_NT_KERN_PATHTRACING1 -3 $_obj_shopnet1_occ_target_octane_render_target1
opwire -n $_obj_shopnet1_occ_target_NT_TEX_IMAGE1 -0 $_obj_shopnet1_occ_target_NT_ENV_TEXTURE1
opwire -n $_obj_shopnet1_occ_target_NT_TRANSFORM_3D1 -4 $_obj_shopnet1_occ_target_NT_TEX_IMAGE1
opwire -n $_obj_shopnet1_occ_target_NT_PROJ_SPHERICAL1 -5 $_obj_shopnet1_occ_target_NT_TEX_IMAGE1
opcf ..
opcf ..
opcf $arg1
opcf $_obj_ropnet1
opcf ..
opcf $arg1
opcf $_obj_CONTROLS
opcf ..

set oidx = 0
if ($argc >= 9 && "$arg9" != "") then
    set oidx = $arg9
endif

if ($argc >= 5 && "$arg4" != "") then
    set output = $_obj_CONTROLS
    opwire -n $output -$arg5 $arg4
endif
if ($argc >= 6 && "$arg6" != "") then
    set input = $_obj_shopnet1
    if ($arg8) then
        opwire -n -i $arg6 -0 $input
    else
        opwire -n -o $oidx $arg6 -0 $input
    endif
endif
opcf $saved_path
'''
hou.hscript(h_preamble + h_extra_args + h_cmd)
