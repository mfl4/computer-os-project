import os


class Computer:
    def __init__(self, processor, memory, storage):
        # self.os = os
        self.processor = processor
        self.memory = memory
        self.storage = storage

    # def get_os_info(self):
    #     return self.os

    def get_processor_info(self):
        return self.processor

    def get_memory_info(self):
        return self.memory

    def get_storage_info(self):
        return self.storage


# Use the os module to get system OS information
# system_os = os.system('uname -a')

# Create a Computer object with the specified specifications
pc = Computer('Intel Core i5', '8GB', '1TB')


print("My Computer System")

# os_info = pc.get_os_info()
# print(f'Operating system: {os_info}')

processor_info = pc.get_processor_info()
print(f'Processor: {processor_info}')

memory_info = pc.get_memory_info()
print(f'Memory: {memory_info}')

storage_info = pc.get_storage_info()
print(f'Storage: {storage_info}')