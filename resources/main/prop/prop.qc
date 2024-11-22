$modelname "modelfolder/prop.mdl"

$staticprop

$model "studio" "prop.smd"

$surfaceprop  "flesh"

$contents "solid"
$cdmaterials "models\cdmaterials\"

$sequence "prop" {
	"anims\idle.smd"
	fadein 0.2
	fadeout 0.2
	fps 1
	loop
}

$collisionjoints "prop.smd"
{
	$mass 50
	$inertia 10
	$damping 0.01
	$rotdamping 5
	$rootbone "root"