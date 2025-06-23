from amplpy import AMPL

ampl = AMPL()

ampl.read(r'C:\Users\crhac\Desktop\CATTSSP\AMPL\modelo.mod')
ampl.read_data(r'C:\Users\crhac\Desktop\CATTSSP\AMPL\data.dat')

ampl.set_option('solver', 'highs')
ampl.solve()

x = ampl.get_variable('x')
df = x.get_values()

x = ampl.get_variable('x')
for i, j, val in x.get_values().to_list():
    if val > 0.5:
        print(f"Arco seleccionado: {i} -> {j}")

obj = ampl.get_objective('TotalCost')
print(f"Costo total: {obj.value()}")
