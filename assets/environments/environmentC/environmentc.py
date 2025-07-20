import pychrono as chrono
import builtins

# Some global settings
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

shapes_dir = 'environmentc_shapes/'

if hasattr(builtins, 'exported_system_relpath'):
    shapes_dir = builtins.exported_system_relpath + shapes_dir

exported_items = []

# Ground body
body_0 = chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body (building or column)
body_1 = chrono.ChBodyAuxRef()
body_1.SetName('Part6-1')
body_1.SetPos(chrono.ChVectorD(-0.0843363733975377, -0.767458429436335, 0.565903085087532))
body_1.SetRot(chrono.ChQuaternionD(1, 0, 0, 0))
body_1.SetMass(598.023558213704)
body_1.SetInertiaXX(chrono.ChVectorD(342.130881966319, 200.841416364596, 502.315056105653))
body_1.SetInertiaXY(chrono.ChVectorD(-11.4499288240514, -40.0767993895102, -4.18839851049515))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(
    chrono.ChVectorD(-0.429345343785524, 1.29830282092817, -0.104758099830559),
    chrono.ChQuaternionD(1, 0, 0, 0)
))
body_1.SetBodyFixed(True)

# Visualization mesh
mesh_for_visualization1 = chrono.ChTriangleMeshConnected()
mesh_for_visualization1.LoadWavefrontMesh(shapes_dir + 'body_1_1.obj')

visualization_shape1 = chrono.ChTriangleMeshShape()
visualization_shape1.SetMesh(mesh_for_visualization1)
visualization_shape1.SetColor(chrono.ChColor(0.96, 0.96, 0.86))  # beige
body_1.AddVisualShape(visualization_shape1)

# Collision material
mat_1 = chrono.ChMaterialSurfaceNSC()

# Collision shape
body_1.GetCollisionModel().ClearModel()

# Load collision mesh
collision_mesh = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(
    shapes_dir + 'body_1_1_collision.obj', False, True)

# Identity rotation matrix (no rotation applied to mesh)
mr = chrono.ChMatrix33D()
mr[0, 0] = 1; mr[1, 1] = 1; mr[2, 2] = 1

# Optional: apply transformation (in this case none)
collision_mesh.Transform(chrono.ChVectorD(0, 0, 0), mr)

# Add triangle mesh for collision (no keyword args!)
body_1.GetCollisionModel().AddTriangleMesh(
    mat_1,
    collision_mesh,
    False,  # is_static
    False,  # is_convex
    chrono.ChVectorD(0, 0, 0),  # position
    mr,  # rotation
    sphereswept_r
)

#  Finalize and enable collision
body_1.GetCollisionModel().BuildModel()
body_1.SetCollide(True)

# Add to system
exported_items.append(body_1)
