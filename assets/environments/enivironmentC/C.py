# PyChrono model automatically generated using Chrono::SolidWorks add-in
# Assembly: 


import pychrono as chrono 
import builtins 

# Some global settings 
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

shapes_dir = 'C_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0 = chrono.ChBodyAuxRef()
body_0.SetName('SLDW_GROUND')
body_0.SetFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1 = chrono.ChBodyAuxRef()
body_1.SetName('Part4-1')
body_1.SetPos(chrono.ChVector3d(-0.0282549624795233,0.00789326391292871,0.00954719155333013))
body_1.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_1.SetMass(0.100112528276031)
body_1.SetInertiaXX(chrono.ChVector3d(2.79570548324636e-05,7.03658157561981e-05,5.31735273808285e-05))
body_1.SetInertiaXY(chrono.ChVector3d(-9.47293485517026e-42,5.81242574292963e-21,5.1407022784677e-38))
body_1.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.0378433981229459,0.0127,0.0260092083319216),chrono.ChQuaterniond(1,0,0,0)))
body_1.SetFixed(True)

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Collision Model

body_1.AddCollisionModel(chrono.ChCollisionModel())

# Collision material 
mat_1 = chrono.ChContactMaterialNSC()

# Collision parameters 
mat_1.SetFriction(0.6)
body_1.GetCollisionModel().SetEnvelope(0.03)
body_1.GetCollisionModel().SetSafeMargin(0.01)
mr = chrono.ChMatrix33d()
mr[0,0]=1; mr[1,0]=0; mr[2,0]=0 
mr[0,1]=0; mr[1,1]=0; mr[2,1]=1 
mr[0,2]=0; mr[1,2]=-1; mr[2,2]=0 
collshape = chrono.ChCollisionShapeBox(mat_1,0.0756867962458918,0.0520184166638432,0.0254)
body_1.GetCollisionModel().AddShape(collshape,chrono.ChFramed(chrono.ChVector3d(0.0378433981229459,0.0127,0.0260092083319216), mr))
body_1.EnableCollision(True)

exported_items.append(body_1)



