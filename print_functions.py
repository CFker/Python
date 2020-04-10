def make_car(maker, model, **infos):
    car_info = {'maker': maker, 'model': model}
    for key, value in infos.items():
        car_info[key] = value
    return car_info
