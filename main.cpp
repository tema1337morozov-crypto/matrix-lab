#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>

using namespace std;
using namespace chrono;

vector<vector<double>> load(const string& name, int& size) {
    ifstream f(name);
    f >> size;
    vector<vector<double>> m(size, vector<double>(size));
    for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            f >> m[i][j];
    return m;
}

void save(const vector<vector<double>>& m, const string& name) {
    ofstream f(name);
    int n = m.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            f << m[i][j] << " ";
        f << endl;
    }
}

vector<vector<double>> mul(const vector<vector<double>>& A, const vector<vector<double>>& B) {
    int n = A.size();
    vector<vector<double>> C(n, vector<double>(n, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            for (int k = 0; k < n; k++)
                C[i][j] += A[i][k] * B[k][j];
    return C;
}

int main() {
    int n1, n2;
    auto A = load("matrixA.txt", n1);
    auto B = load("matrixB.txt", n2);
    
    if (n1 != n2) {
        cout << "Ошибка: размеры не совпадают!" << endl;
        return 1;
    }
    
    cout << "Размер: " << n1 << "x" << n1 << endl;
    
    auto start = high_resolution_clock::now();
    auto C = mul(A, B);
    auto end = high_resolution_clock::now();
    
    auto time_ms = duration_cast<milliseconds>(end - start).count();
    double seconds = time_ms / 1000.0;
    long long ops = (long long)n1 * n1 * n1;
    double mflops = (ops / 1000000.0) / seconds;
    
    cout << "Время: " << seconds << " сек" << endl;
    cout << "Операций: " << ops << endl;
    cout << "MFLOPS: " << mflops << endl;
    
    save(C, "result.txt");
    
    cout << "\nВерификация..." << endl;
    system("python verify.py");
    
    return 0;
}