# generate_helper.py
import os
import sys
from scan_models import scan_models

def generate_session_code(models_info, output_file):
    """Генерирует C++ код с специализациями метода save для каждого класса."""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w') as f:
        f.write("#pragma once\n")
        f.write("#include \"core.hpp\"\n")  # Убедитесь, что путь корректен

        for filename, class_name, imports, fields in models_info:
            f.write(f"#include \"{filename}\"\n")

        f.write("#include <iostream>\n")
        f.write("#include <string>\n\n")
        f.write("namespace quick {\nnamespace ultra {\n\n")
        
        for filename, class_name, imports, fields in models_info:
            # Генерируем специализацию метода save
            f.write(f"template<>\n")
            f.write(f"inline void Core::save<{class_name}>(const {class_name}& obj) {{\n")
            f.write(f'    std::cout << "Saving {class_name}:" << std::endl;\n')
            
            # Добавляем вывод полей
            for field_type, field_name in fields:
                if field_type.startswith('ONE_TO_ONE') or \
                   field_type.startswith('ONE_TO_MANY') or \
                   field_type.startswith('MANY_TO_MANY'):
                    continue
                
                f.write(f'    std::cout << "  {field_name}: " << obj.{field_name} << std::endl;\n')
            
            f.write("    // Handle dependencies here (e.g., save related objects)\n")
            f.write("}\n\n")
        
        f.write("}} // namespace quick::ultra\n")

if __name__ == "__main__":
    file_path = "build/generated/session_helper.cpp"  
    content = "Hello, World!"

    models_info = scan_models()

    if models_info:
        generate_session_code(models_info, file_path)
        print("Successfully generated session_helper.hpp")
    else:
        print("No models found to generate code")