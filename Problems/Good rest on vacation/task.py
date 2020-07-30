# put your python code here
days = int(input())
day_food_cost = int(input())
go_flight = int(input())
day_hotel_fee = int(input())
total_flight_cost = 2 * go_flight
total_food_cost = days * day_food_cost
total_hotel_cost = (days - 1) * day_hotel_fee
amount_needed = (total_flight_cost + total_food_cost + total_hotel_cost)
print(amount_needed)