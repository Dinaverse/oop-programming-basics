# 🎓 OOP Programming Basics

This repository contains fundamental exercises demonstrating **Object-Oriented Programming (OOP)** concepts in Python. These scripts were developed as part of my initiation into structured programming.

## 🧩 Concepts Demonstrated

### 1. Classes and Objects
- **`classAutoPilot.py`**: Demonstrates the creation of a class to encapsulate properties and behaviors for an autonomous system.

### 2. Encapsulation
- **`classCompte.py`**: Showcases encapsulation by managing bank account data and operations within a class structure.

### 3. Data Modeling & Encapsulation
- **\`classArticle.py\`**: Demonstrates data modeling with encapsulation. Private attributes (`__reference`, `__nom`, etc.) are protected using name mangling and accessed through getter and setter methods. It also implements business logic for managing inventory (approvisionner, vendre) and tax calculations.

### 4. Operator Overloading
- **\`TentativeConnexion.py\`**: Demonstrates operator overloading in Python by implementing \`__str__\` for custom string representation and \`__eq__\` to define custom equality logic.

### 5. Inheritance and Polymorphism
- **\`classAlerte.py\`**: Demonstrates inheritance and polymorphism by overriding \`afficher_info()\` for specialized alert types.
- **\`classAppareilReseau.py\`**: Further demonstrates inheritance where \`Serveur\` and \`Routeur\` extend the base \`AppareilReseau\` class. It showcases polymorphism by overriding \`afficher_info()\` to include device-specific details (OS/services for servers, interfaces/firmware for routers) while calling the base class method to retain common functionality.

### 6. Abstraction and Abstract Base Classes (ABC)
- **\`Employee.py\`**: Demonstrates abstraction in Python using the \`abc\` module. The base \`Employee\` class is an Abstract Base Class (ABC) with an abstract method \`get_salaire()\`. This enforces that any subclass (\`Ouvrier\`, \`Cadre\`) must implement its own salary calculation logic, ensuring a consistent interface across different employee types.

---
*Learning the foundations of robust software engineering - Dina.*


