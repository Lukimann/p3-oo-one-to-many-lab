class Owner:
     def  __init__(self, name):
        self.name = name

     def add_pet(self, pet):
        if not isinstance(pet, Pet):
             raise ValueError("Unknown peet.")
        pet.owner = self
        
     def pets(self):
        owner_pets = [pet for pet in Pet.all if pet.owner == self]
        return owner_pets
         
     def get_sorted_pets(self):
        def sort_key(pet):
            return pet.name

        owner_pets = self.pets()
        sorted_pets = sorted(owner_pets, key=sort_key)
        return sorted_pets

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def  __init__(self, name, pet_type, owner=None):
        if pet_type.lower() not in self.PET_TYPES:
            raise Exception(f"Invalid pet type. Allowed types are {', '.join(self.PET_TYPES)}")

        self.name = name
        self.pet_type = pet_type.lower()

        self.owner = owner

        if owner is not None and not isinstance(owner, Owner):
            raise ValueError("Owner must be an instance of the Owner class.")
        
        self.__class__.all.append(self)