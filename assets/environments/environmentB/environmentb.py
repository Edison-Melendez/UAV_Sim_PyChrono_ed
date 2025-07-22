import pychrono as chrono
import builtins

# === Global settings ===
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

# === Shapes directory ===
shapes_dir = 'environmentb_shapes/'
if hasattr(builtins, 'exported_system_relpath'):
    shapes_dir = builtins.exported_system_relpath + shapes_dir

exported_items = []

# === Base Ground Reference Body ===
body_0 = chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# === Rigid Body ===
body_1 = chrono.ChBodyAuxRef()
body_1.SetName('PART6copy-1')
body_1.SetPos(chrono.ChVectorD(1.17775433620075, -0.66345478931787, 0.70572716948595947))
body_1.SetRot(chrono.ChQuaternionD(1, 0, 0, 0))
body_1.SetMass(1110.06670500994)
body_1.SetInertiaXX(chrono.ChVectorD(715.017018658678, 1916.77945460426, 2449.36792459883))
body_1.SetInertiaXY(chrono.ChVectorD(-70.3897759581321, 99.9906460281766, 0.464904551916506))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(
    chrono.ChVectorD(-0.929994054206124, 1.12218879653754, -0.167326024110134),
    chrono.ChQuaternionD(1, 0, 0, 0)))
body_1.SetBodyFixed(True)

# === Visualization Mesh ===
visual_mesh = chrono.ChTriangleMeshConnected()
visual_mesh.LoadWavefrontMesh(shapes_dir + 'body_1_1.obj')

visual_shape = chrono.ChTriangleMeshShape()
visual_shape.SetMesh(visual_mesh)
visual_shape.SetColor(chrono.ChColor(0.96, 0.96, 0.86))  # beige
body_1.AddVisualShape(visual_shape)

# === Collision Material ===
mat_1 = chrono.ChMaterialSurfaceNSC()

# === Collision Shape (Triangle Mesh) ===
body_1.GetCollisionModel().ClearModel()

collision_mesh = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(
    shapes_dir + 'body_1_1_collision.obj', False, True)

mr = chrono.ChMatrix33D()
mr[0, 0] = 1; mr[0, 1] = 0; mr[0, 2] = 0
mr[1, 0] = 0; mr[1, 1] = 1; mr[1, 2] = 0
mr[2, 0] = 0; mr[2, 1] = 0; mr[2, 2] = 1

collision_mesh.Transform(chrono.ChVectorD(0, 0, 0), mr)

body_1.GetCollisionModel().AddTriangleMesh(
    mat_1,
    collision_mesh,
    False,  # is_static
    False,  # is_convex
    chrono.ChVectorD(0, 0, 0),
    mr,
    sphereswept_r
)

body_1.GetCollisionModel().BuildModel()
body_1.SetCollide(True)

exported_items.append(body_1)
