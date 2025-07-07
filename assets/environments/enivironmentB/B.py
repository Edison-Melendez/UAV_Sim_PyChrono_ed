# PyChrono model automatically generated using Chrono::SolidWorks add-in
# Assembly: 


import pychrono as chrono 
import builtins 

# Some global settings 
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

shapes_dir = 'B_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0 = chrono.ChBodyAuxRef()
body_0.SetName('SLDW_GROUND')
body_0.SetFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1 = chrono.ChBodyAuxRef()
body_1.SetName('Part2-1')
body_1.SetPos(chrono.ChVector3d(0.00999937499647294,-0.0520282369886236,0.0300706824201503))
body_1.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_1.SetMass(0.184271784185127)
body_1.SetInertiaXX(chrono.ChVector3d(0.000970902342253887,0.000138419833042299,0.000976019497119626))
body_1.SetInertiaXY(chrono.ChVector3d(-2.01782075180146e-07,-1.36319724381919e-07,7.6542860343538e-06))
body_1.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.0258200109986758,0.138037016632724,0.0243257135989926),chrono.ChQuaterniond(1,0,0,0)))
body_1.SetFixed(True)

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_1)



