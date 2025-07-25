# multiplication_table.py

# Multiplication Table Generator (1 to 10)

for i in range(1, 11):
    print(f"Multiplication Table for {i}")
    
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    
    print("-" * 25)
