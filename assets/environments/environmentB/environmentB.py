# PyChrono model automatically generated using Chrono::SolidWorks add-in
# Assembly: 


import pychrono as chrono 
import builtins 

# Some global settings 
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

shapes_dir = 'environmentB_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0 = chrono.ChBodyAuxRef()
body_0.SetName('SLDW_GROUND')
body_0.SetFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1 = chrono.ChBodyAuxRef()
body_1.SetName('Square-1')
body_1.SetPos(chrono.ChVector3d(-8.16012839610552,2.58225981643749,2.55163933029393))
body_1.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_1.SetMass(16049.5070343411)
body_1.SetInertiaXX(chrono.ChVector3d(162526.848839256,163841.5866962,9767.4784213471))
body_1.SetInertiaXY(chrono.ChVector3d(1.41506713736747e-12,-8.6281617356668e-11,420.788651621433))
body_1.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(11.6025074887558,0.560351860941242,0.736591850541093),chrono.ChQuaterniond(1,0,0,0)))
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



