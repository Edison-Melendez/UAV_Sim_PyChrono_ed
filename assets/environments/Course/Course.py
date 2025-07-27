import pychrono as chrono
import builtins

# === Global settings ===
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

# === Shapes directory ===
shapes_dir = 'Course_shapes/'
if hasattr(builtins, 'exported_system_relpath'):
    shapes_dir = builtins.exported_system_relpath + shapes_dir

exported_items = []

# === Ground Body ===
body_0 = chrono.ChBodyAuxRef()
body_0.SetName('SLDW_GROUND')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# === Helper to add rigid body ===
def add_body(name, pos, rot, mass, inertia_xx, inertia_xy, cog, visual_file, collision_file, material):
    body = chrono.ChBodyAuxRef()
    body.SetName(name)
    body.SetPos(chrono.ChVectorD(*pos))
    body.SetRot(chrono.ChQuaternionD(*rot))
    body.SetMass(mass)
    body.SetInertiaXX(chrono.ChVectorD(*inertia_xx))
    body.SetInertiaXY(chrono.ChVectorD(*inertia_xy))
    body.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(*cog), chrono.ChQuaternionD(1,0,0,0)))
    body.SetBodyFixed(True)

    # Visualization
    visual_mesh = chrono.ChTriangleMeshConnected()
    visual_mesh.LoadWavefrontMesh(shapes_dir + visual_file)
    visual_shape = chrono.ChTriangleMeshShape()
    visual_shape.SetMesh(visual_mesh)
    visual_shape.SetColor(chrono.ChColor(0.96, 0.96, 0.86))
    body.AddVisualShape(visual_shape)

    # Collision
    body.GetCollisionModel().ClearModel()
    collision_mesh = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + collision_file, False, True)
    mr = chrono.ChMatrix33D()
    mr[0,0] = 1; mr[1,1] = 1; mr[2,2] = 1
    collision_mesh.Transform(chrono.ChVectorD(0, 0, 0), mr)
    body.GetCollisionModel().AddTriangleMesh(material, collision_mesh, False, False, chrono.ChVectorD(0,0,0), mr, sphereswept_r)
    body.GetCollisionModel().BuildModel()
    body.SetCollide(True)

    exported_items.append(body)

# === Add all parts ===
add_body('pillar_3-1',
         (1.31550280333668, -1.44997600266244, 0.347957562476324),
         (1, 0, 0, 0),
         771.720850878954,
         (426.393338414993, 22.5719390712824, 425.984307578066),
         (-5.00797540097794e-16, 0.26816981953053, -3.97846868673472e-15),
         (-0.0084511158457356, 1.27, -0.194688875818552),
         'body_1_1.obj',
         'body_1_1_collision.obj',
         chrono.ChMaterialSurfaceNSC())

add_body('obstacle _2-1',
         (-0.57913822755939, -0.618331642846517, 0.72568874190517),
         (1, 0, 0, 0),
         423.014760970138,
         (182.982440995468, 53.7882321435903, 231.783339983312),
         (0.855505481904864, -8.78288779906956e-16, -2.5149432593093e-15),
         (0.804772195191392, 1.41867241364596, -0.383054091158211),
         'body_2_1.obj',
         'body_2_1_collision.obj',
         chrono.ChMaterialSurfaceNSC())

add_body('pillar_1-1',
         (1.59126727328745, -0.570949488475453, -0.575373413809537),
         (1, 0, 0, 0),
         1316.77434795475,
         (736.324729816685, 56.8864362223008, 736.445270283099),
         (0, -9.8865298433886e-15, 0),
         (0.254831995706842, 1.27, 0.254292586073241),
         'body_3_1.obj',
         'body_3_1_collision.obj',
         chrono.ChMaterialSurfaceNSC())

add_body('obstacle_1-1',
         (-2.06092126279835, -0.647199632988777, 0.837945601468199),
         (1, 0, 0, 0),
         346.454436844713,
         (220.823183995005, 17.0938153242297, 207.57793925468),
         (3.81943287533216e-16, 3.17179068104224e-16, 2.27274133383393e-15),
         (0.428832936240346, 1.50167571297629, 0.319700709047503),
         'body_4_1.obj',
         'body_4_1_collision.obj',
         chrono.ChMaterialSurfaceNSC())

add_body('pillar_2-1',
         (-0.50352935330011, -1.3061538871075, 0.814368712017313),
         (1, 0, 0, 0),
         1784.14127094109,
         (1009.07756474951, 99.7274922317594, 1009.07756474951),
         (-1.46404060591131e-30, 0, 2.03631065502339e-30),
         (0, 1.27, -6.51686629266461e-18),
         'body_5_1.obj',
         'body_5_1_collision.obj',
         chrono.ChMaterialSurfaceNSC())
