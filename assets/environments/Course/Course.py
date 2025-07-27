import pychrono as chrono
import builtins

# === Global settings ===
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

shapes_dir = 'Course_shapes/'
if hasattr(builtins, 'exported_system_relpath'):
    shapes_dir = builtins.exported_system_relpath + shapes_dir

exported_items = []

# === Ground Body ===
body_0 = chrono.ChBodyAuxRef()
body_0.SetName('SLDW_GROUND')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# === Body: pillar_3-1 ===
body_1 = chrono.ChBodyAuxRef()
body_1.SetName('pillar_3-1')
body_1.SetPos(chrono.ChVectorD(1.31550280333668, -1.44997600266244, 0.347957562476324))
body_1.SetRot(chrono.ChQuaternionD(1, 0, 0, 0))
body_1.SetMass(771.720850878954)
body_1.SetInertiaXX(chrono.ChVectorD(426.393338414993, 22.5719390712824, 425.984307578066))
body_1.SetInertiaXY(chrono.ChVectorD(-5.00797540097794e-16, 0.26816981953053, -3.97846868673472e-15))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.0084511158457356, 1.27, -0.194688875818552), chrono.ChQuaternionD(1, 0, 0, 0)))
body_1.SetBodyFixed(True)

visual_mesh1 = chrono.ChTriangleMeshConnected()
visual_mesh1.LoadWavefrontMesh(shapes_dir + 'body_1_1.obj')
visual_shape1 = chrono.ChTriangleMeshShape()
visual_shape1.SetMesh(visual_mesh1)
visual_shape1.SetColor(chrono.ChColor(0.96, 0.96, 0.86))
body_1.AddVisualShape(visual_shape1)

mat_1 = chrono.ChMaterialSurfaceNSC()
body_1.GetCollisionModel().ClearModel()
collision_mesh1 = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_1_1_collision.obj', False, True)
mr1 = chrono.ChMatrix33D(); mr1[0,0] = 1; mr1[1,1] = 1; mr1[2,2] = 1
collision_mesh1.Transform(chrono.ChVectorD(0, 0, 0), mr1)
body_1.GetCollisionModel().AddTriangleMesh(mat_1, collision_mesh1, False, False, chrono.ChVectorD(0,0,0), mr1, sphereswept_r)
body_1.GetCollisionModel().BuildModel()
body_1.SetCollide(True)
exported_items.append(body_1)

# === Body: obstacle _2-1 ===
body_2 = chrono.ChBodyAuxRef()
body_2.SetName('obstacle _2-1')
body_2.SetPos(chrono.ChVectorD(-0.57913822755939, -0.618331642846517, 0.72568874190517))
body_2.SetRot(chrono.ChQuaternionD(1, 0, 0, 0))
body_2.SetMass(423.014760970138)
body_2.SetInertiaXX(chrono.ChVectorD(182.982440995468, 53.7882321435903, 231.783339983312))
body_2.SetInertiaXY(chrono.ChVectorD(0.855505481904864, -8.78288779906956e-16, -2.5149432593093e-15))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.804772195191392, 1.41867241364596, -0.383054091158211), chrono.ChQuaternionD(1, 0, 0, 0)))
body_2.SetBodyFixed(True)

visual_mesh2 = chrono.ChTriangleMeshConnected()
visual_mesh2.LoadWavefrontMesh(shapes_dir + 'body_2_1.obj')
visual_shape2 = chrono.ChTriangleMeshShape()
visual_shape2.SetMesh(visual_mesh2)
visual_shape2.SetColor(chrono.ChColor(0.96, 0.96, 0.86))
body_2.AddVisualShape(visual_shape2)

mat_2 = chrono.ChMaterialSurfaceNSC()
body_2.GetCollisionModel().ClearModel()
collision_mesh2 = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_2_1_collision.obj', False, True)
mr2 = chrono.ChMatrix33D(); mr2[0,0] = 1; mr2[1,1] = 1; mr2[2,2] = 1
collision_mesh2.Transform(chrono.ChVectorD(0, 0, 0), mr2)
body_2.GetCollisionModel().AddTriangleMesh(mat_2, collision_mesh2, False, False, chrono.ChVectorD(0,0,0), mr2, sphereswept_r)
body_2.GetCollisionModel().BuildModel()
body_2.SetCollide(True)
exported_items.append(body_2)

# === Body: pillar_1-1 ===
body_3 = chrono.ChBodyAuxRef()
body_3.SetName('pillar_1-1')
body_3.SetPos(chrono.ChVectorD(1.59126727328745, -0.570949488475453, -0.575373413809537))
body_3.SetRot(chrono.ChQuaternionD(1, 0, 0, 0))
body_3.SetMass(1316.77434795475)
body_3.SetInertiaXX(chrono.ChVectorD(736.324729816685, 56.8864362223008, 736.445270283099))
body_3.SetInertiaXY(chrono.ChVectorD(0, -9.8865298433886e-15, 0))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.254831995706842, 1.27, 0.254292586073241), chrono.ChQuaternionD(1, 0, 0, 0)))
body_3.SetBodyFixed(True)

visual_mesh3 = chrono.ChTriangleMeshConnected()
visual_mesh3.LoadWavefrontMesh(shapes_dir + 'body_3_1.obj')
visual_shape3 = chrono.ChTriangleMeshShape()
visual_shape3.SetMesh(visual_mesh3)
visual_shape3.SetColor(chrono.ChColor(0.96, 0.96, 0.86))
body_3.AddVisualShape(visual_shape3)

mat_3 = chrono.ChMaterialSurfaceNSC()
body_3.GetCollisionModel().ClearModel()
collision_mesh3 = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_3_1_collision.obj', False, True)
mr3 = chrono.ChMatrix33D(); mr3[0,0] = 1; mr3[1,1] = 1; mr3[2,2] = 1
collision_mesh3.Transform(chrono.ChVectorD(0, 0, 0), mr3)
body_3.GetCollisionModel().AddTriangleMesh(mat_3, collision_mesh3, False, False, chrono.ChVectorD(0,0,0), mr3, sphereswept_r)
body_3.GetCollisionModel().BuildModel()
body_3.SetCollide(True)
exported_items.append(body_3)

# === Body: obstacle_1-1 ===
body_4 = chrono.ChBodyAuxRef()
body_4.SetName('obstacle_1-1')
body_4.SetPos(chrono.ChVectorD(-2.06092126279835, -0.647199632988777, 0.837945601468199))
body_4.SetRot(chrono.ChQuaternionD(1, 0, 0, 0))
body_4.SetMass(346.454436844713)
body_4.SetInertiaXX(chrono.ChVectorD(220.823183995005, 17.0938153242297, 207.57793925468))
body_4.SetInertiaXY(chrono.ChVectorD(3.81943287533216e-16, 3.17179068104224e-16, 2.27274133383393e-15))
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.428832936240346, 1.50167571297629, 0.319700709047503), chrono.ChQuaternionD(1, 0, 0, 0)))
body_4.SetBodyFixed(True)

visual_mesh4 = chrono.ChTriangleMeshConnected()
visual_mesh4.LoadWavefrontMesh(shapes_dir + 'body_4_1.obj')
visual_shape4 = chrono.ChTriangleMeshShape()
visual_shape4.SetMesh(visual_mesh4)
visual_shape4.SetColor(chrono.ChColor(0.96, 0.96, 0.86))
body_4.AddVisualShape(visual_shape4)

mat_4 = chrono.ChMaterialSurfaceNSC()
body_4.GetCollisionModel().ClearModel()
collision_mesh4 = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_4_1_collision.obj', False, True)
mr4 = chrono.ChMatrix33D(); mr4[0,0] = 1; mr4[1,1] = 1; mr4[2,2] = 1
collision_mesh4.Transform(chrono.ChVectorD(0, 0, 0), mr4)
body_4.GetCollisionModel().AddTriangleMesh(mat_4, collision_mesh4, False, False, chrono.ChVectorD(0,0,0), mr4, sphereswept_r)
body_4.GetCollisionModel().BuildModel()
body_4.SetCollide(True)
exported_items.append(body_4)

# === Body: pillar_2-1 ===
body_5 = chrono.ChBodyAuxRef()
body_5.SetName('pillar_2-1')
body_5.SetPos(chrono.ChVectorD(-0.50352935330011, -1.3061538871075, 0.814368712017313))
body_5.SetRot(chrono.ChQuaternionD(1, 0, 0, 0))
body_5.SetMass(1784.14127094109)
body_5.SetInertiaXX(chrono.ChVectorD(1009.07756474951, 99.7274922317594, 1009.07756474951))
body_5.SetInertiaXY(chrono.ChVectorD(-1.46404060591131e-30, 0, 2.03631065502339e-30))
body_5.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0, 1.27, -6.51686629266461e-18), chrono.ChQuaternionD(1, 0, 0, 0)))
body_5.SetBodyFixed(True)

visual_mesh5 = chrono.ChTriangleMeshConnected()
visual_mesh5.LoadWavefrontMesh(shapes_dir + 'body_5_1.obj')
visual_shape5 = chrono.ChTriangleMeshShape()
visual_shape5.SetMesh(visual_mesh5)
visual_shape5.SetColor(chrono.ChColor(0.96, 0.96, 0.86))
body_5.AddVisualShape(visual_shape5)

mat_5 = chrono.ChMaterialSurfaceNSC()
body_5.GetCollisionModel().ClearModel()
collision_mesh5 = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_5_1_collision.obj', False, True)
mr5 = chrono.ChMatrix33D(); mr5[0,0] = 1; mr5[1,1] = 1; mr5[2,2] = 1
collision_mesh5.Transform(chrono.ChVectorD(0, 0, 0), mr5)
body_5.GetCollisionModel().AddTriangleMesh(mat_5, collision_mesh5, False, False, chrono.ChVectorD(0,0,0), mr5, sphereswept_r)
body_5.GetCollisionModel().BuildModel()
body_5.SetCollide(True)
exported_items.append(body_5)
