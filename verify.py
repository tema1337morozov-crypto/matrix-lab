import sys
import numpy as np

def load_matrix(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    n = int(lines[0].strip())
    matrix = []
    for line in lines[1:]:
        matrix.append([float(x) for x in line.strip().split()])
    return np.array(matrix)

def main():
    if len(sys.argv) != 4:
        print("Использование: py my_verify.py <A> <B> <C>")
        sys.exit(1)
    
    fileA, fileB, fileC = sys.argv[1], sys.argv[2], sys.argv[3]
    
    A = load_matrix(fileA)
    B = load_matrix(fileB)
    C_cpp = load_matrix(fileC)
    
    # Вычисление эталонного результата
    C_ref = np.dot(A, B)
    
    # Сравнение с учетом погрешности
    if np.allclose(C_cpp, C_ref, atol=1e-8):
        print("Верификация: УСПЕШНО (результаты совпадают с эталоном)")
        sys.exit(0)
    else:
        max_diff = np.max(np.abs(C_cpp - C_ref))
        print(f"Верификация: ОШИБКА (макс. расхождение = {max_diff:.2e})")
        sys.exit(1)

if __name__ == "__main__":
    main()
