def profit(info):
	total_sales = info["sell_price"] * info["inventory"]
	total_costs = info["cost_price"] * info ["inventory"]
	return round(total_sales - total_cost)
