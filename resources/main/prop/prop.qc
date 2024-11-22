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

$collisionmodel "models_physics.smd"
{
	$mass 50
	$inertia 1
	$damping 0
	$rotdamping 0
	$rootbone " "

}
