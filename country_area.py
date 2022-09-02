def area_of_country(name, area):
	landmass = 148940000
	return "{} is {:.2%} of the total world's landmass".format(
	name,
	area / landmass
	)
