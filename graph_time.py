import subprocess
import time
import numpy as np
import matplotlib.pyplot as plt
import os

# ==============================================
# НАСТРОЙКИ (измените под себя)
# ==============================================
EXE_FILE = "mylab.exe"      # имя вашего .exe файла
SIZES = [50, 100, 150, 200, 250, 300]  # размеры матриц для теста
# ==============================================

def create_matrix_files(n):
    """Создаёт случайные матрицы размера n x n в файлах matrixA.txt и matrixB.txt"""
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    
    with open('matrixA.txt', 'w') as f:
        f.write(f"{n}\n")
        for row in A:
            f.write(" ".join(map(str, row)) + "\n")
    
    with open('matrixB.txt', 'w') as f:
        f.write(f"{n}\n")
        for row in B:
            f.write(" ".join(map(str, row)) + "\n")

def measure_time_cpp():
    """Запускает C++ программу и возвращает время выполнения умножения"""
    start = time.time()
    result = subprocess.run([EXE_FILE], capture_output=True, text=True)
    end = time.time()
    return end - start, result.stdout

# ==============================================
# ЗАПУСК ТЕСТОВ
# ==============================================
print("=" * 60)
print("Тестирование производительности умножения матриц")
print("=" * 60)

cpp_times = []

for n in SIZES:
    print(f"\nТестируем размер {n}x{n}...")
    create_matrix_files(n)
    
    # Замер времени C++
    elapsed, output = measure_time_cpp()
    cpp_times.append(elapsed)
    
    print(f"  Время: {elapsed:.4f} сек")
    
    # Показываем MFLOPS из вывода программы (если есть)
    for line in output.split('\n'):
        if 'MFLOPS' in line:
            print(f"  {line}")

# ==============================================
# СТРОИМ ГРАФИК
# ==============================================
plt.figure(figsize=(10, 6))
plt.plot(SIZES, cpp_times, 'o-', color='blue', linewidth=2, markersize=8, label='C++ (моя программа)')

plt.xlabel('Размер матрицы N', fontsize=12)
plt.ylabel('Время выполнения (секунды)', fontsize=12)
plt.title('Зависимость времени умножения матриц от размера', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)

# Сохраняем график
plt.savefig('time_graph.png', dpi=150, bbox_inches='tight')
print("\n" + "=" * 60)
print("График сохранён как: time_graph.png")
print("=" * 60)

# Показываем график
plt.show()