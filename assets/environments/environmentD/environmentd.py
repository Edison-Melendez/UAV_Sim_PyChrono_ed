# PyChrono model automatically generated using Chrono::SolidWorks add-in
# Assembly: 


import pychrono as chrono 
import builtins 

# Some global settings 
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

shapes_dir = 'environmentd_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0 = chrono.ChBodyAuxRef()
body_0.SetName('SLDW_GROUND')
body_0.SetFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1 = chrono.ChBodyAuxRef()
body_1.SetName('targets-1')
body_1.SetPos(chrono.ChVector3d(0.0247466800994952,-0.0920622283625694,0.0494872334204122))
body_1.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_1.SetMass(0.234296663780861)
body_1.SetInertiaXX(chrono.ChVector3d(0.00120085178937056,0.00026194897355314,0.00127315621026146))
body_1.SetInertiaXY(chrono.ChVector3d(1.09919922453984e-05,5.78625351882856e-06,3.77258601486936e-06))
body_1.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.00539971402491222,0.145046170261709,0.00340582172789345),chrono.ChQuaterniond(1,0,0,0)))
body_1.SetFixed(True)

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Collision Model

body_1.AddCollisionModel(chrono.ChCollisionModel())

# Collision material 
mat_1 = chrono.ChContactMaterialNSC()

# Triangle mesh collision shape 
body_1_1_collision_mesh = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_1_1_collision.obj', False, True) 
mr = chrono.ChMatrix33d()
mr[0,0]=1; mr[1,0]=0; mr[2,0]=0 
mr[0,1]=0; mr[1,1]=1; mr[2,1]=0 
mr[0,2]=0; mr[1,2]=0; mr[2,2]=1 
body_1_1_collision_mesh.Transform(chrono.ChVector3d(0, 0, 0), mr) 
collshape = chrono.ChCollisionShapeTriangleMesh(mat_1,body_1_1_collision_mesh,False,False,sphereswept_r)
body_1.GetCollisionModel().AddShape(collshape)
body_1.EnableCollision(True)

exported_items.append(body_1)



