from .models import CarMake, CarModel


def initiate():
    makes = [
        ("NISSAN", "Great cars. Japanese technology"),
        ("Mercedes", "Great cars. German technology"),
        ("Audi", "Great cars. German technology"),
        ("Kia", "Great cars. Korean technology"),
        ("Toyota", "Great cars. Japanese technology"),
    ]
    make_by_name = {
        name: CarMake.objects.create(name=name, description=description)
        for name, description in makes
    }
    models = [
        ("NISSAN", "Pathfinder", "SUV"), ("NISSAN", "Qashqai", "SUV"), ("NISSAN", "XTRAIL", "SUV"),
        ("Mercedes", "A-Class", "SUV"), ("Mercedes", "C-Class", "SUV"), ("Mercedes", "E-Class", "SUV"),
        ("Audi", "A4", "SUV"), ("Audi", "A5", "SUV"), ("Audi", "A6", "SUV"),
        ("Kia", "Sorrento", "SUV"), ("Kia", "Carnival", "SUV"), ("Kia", "Cerato", "Sedan"),
        ("Toyota", "Corolla", "Sedan"), ("Toyota", "Camry", "Sedan"), ("Toyota", "Kluger", "SUV"),
    ]
    CarModel.objects.bulk_create([
        CarModel(name=name, type=car_type, year=2023, car_make=make_by_name[make])
        for make, name, car_type in models
    ])
