from car_class import Car

car1=Car('VW',2019,'Blue',True)
car2=Car('Porsche',2029,'Red',False)
car3=Car('Maruti',2017,'Green',True)
car4=Car('Suzuki',2024,'Yellow',False)

print('The cars that I have are :')
print(f'My 1st car is {car1.model} &  is {car1.color}')
print(f'My 2nd car is {car2.model} &  is {car2.color}')
print(f'My 3rd car is for sale = {car3.for_sale}')
print(f'My 4th car is for sale = {car4.for_sale}')


car1.drive()
car4.stop()