import os

catsp_path = r'C:\Users\crhac\CATSSP\CATSSP\CGL\cgl_114.catsp'
tsp_path = catsp_path.replace('.catsp', '.tsp')
par_path = catsp_path.replace('.catsp', '.par')

with open(catsp_path, 'r') as f_in, open(tsp_path, 'w') as f_out:
    for line in f_in:
        if 'DIMENSION' in line:
            f_out.write(line)
        elif 'EDGE_WEIGHT_SECTION' in line:
            f_out.write('EDGE_WEIGHT_SECTION\n')
        else:
            f_out.write(line)

print(f'Se generó {tsp_path}')

with open(par_path, 'w') as f:
    f.write(f'PROBLEM_FILE = {os.path.basename(tsp_path)}\n')
    f.write(f'OUTPUT_TOUR_FILE = {os.path.basename(tsp_path).replace(".tsp", ".sol")}\n')
    f.write('RUNS = 10\n')

print(f'Se generó {par_path}')
