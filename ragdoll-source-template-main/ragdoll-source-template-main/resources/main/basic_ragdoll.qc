$modelname "foldername/modelname.mdl"

$model "studio" "model.smd" {

    <THIS PART IS VERY IMPORTANT IF YOUR MODEL HAS 3D EYES.>
	eyeball "eye_right" "head_bone" -0.00000 -0.08000 00.00000 "eyeball r" 1 2 "iris_unused" (IRIS_SIZE)5
	eyeball "eye_left" "head_bone" 0.00000 -0.00000 00.00000 "eyeball l" 1 -2 "iris_unused" (IRIS_SIZE)5
    <IF NOT,REMOVE IT.>

	mouth 0 "mouth" "head_bone" 0 1 0
    <THIS PART IS VERY IMPORTANT IF YOUR MODEL HAS FACIAL FLEXES(SHAPE KEYS).>
	flexfile "model.vta" 
	{
		defaultflex frame 0
		flex "insert shape key 1" frame 1

	}

	flexcontroller insert shape key 1 range 0 1 "insert shape key 1"
	{<THIS PART IS VERY IMPORTANT IF YOUR MODEL HAS 3D EYES.>
	flexcontroller eyes range -45 45 "eyes_updown"
	flexcontroller eyes range -45 45 "eyes_rightleft"
        <IF NOT,REMOVE IT.>}
	
	%insert shape key 1 = insert shape key 1
	<IF NOT,REMOVE IT.>
}

$bodygroup "bodygroup_model"
{
	studio "bodygroup_model.smd"
}

$surfaceprop "flesh"

$contents "solid"

$mostlyopaque

$cdmaterials "models\cdmaterials\"

<IF YOUR MODELS HAS ALT SKINS,EDIT THIS>
$texturegroup "skinfamilies"
{
	{ "altskinmaterialname"  "altskinmaterialname" }
}


<THIS PART IS VERY IMPORTANT IF YOUR MODEL HAS 3D EYES.>
$attachment "eyes" "head_bone" 0.00 0.00 0.00 rotate 00 00 00
<IF NOT,REMOVE IT.>
$attachment "mouth" "head_bone" 0.00 0.00 0.00 rotate 00 00 00




$sequence "ragdoll" {
	"anims\ragdoll.smd"
	fadein 0.2
	fadeout 0.2
	fps 1
	loop
}

$collisionjoints "model_physics.smd"
{
	$mass 50
	$inertia 10
	$damping 0.01
	$rotdamping 5
	$rootbone "root bone"
	
	
	$jointconstrain "insert bone name" insert x 0.00 0.00 0.00
	$jointconstrain "insert bone name" insert y 0.00 0.00 0.00
	$jointconstrain "insert bone name" insert z 0.00 0.00 0.00
	
	}
