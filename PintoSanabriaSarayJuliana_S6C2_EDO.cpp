#include <iostream>
#include <cmath>
#include <iomanip>
#include <fstream>

double f(double /*t*/, double y){    
    return -y;
}
void guardar(const std::string& filename, double t, double yn, double y, double error){
    std::ofstream out(filename, std::ios::app);
    out << std::scientific << std::setprecision(6) << t << " " << yn << " " << y << " " << error << "\n";
}
void euler(double y0, double h, double tf, const std::string& suffix){
    std::string filename = "euler_h" + suffix + ".dat";
    std::remove(filename.c_str());
    double y1 = y0;
    for (double t = 0.0; t <= tf + 1e-9; t += h){
        double y = std::exp(-t);
        double error= std::fabs(y1-y);
        std::cout << t << " " << y1 << " " << y << error << "\n";
        guardar(filename, t, y1, y,error);
        y1 += h * f(t, y1);
    }
}
void rk(double y0, double h, double tf, const std::string& suffix){
    std::string filename = "rk4_h" + suffix + ".dat";
    std::remove(filename.c_str());
    double y1 = y0;
    for (double t = 0.0; t <= tf + 1e-9; t += h){
        double y = std::exp(-t);
        double error= std::fabs(y1-y);
        std::cout << t << " " << y1 << " " << y << error << "\n";
        guardar(filename, t, y1, y,error);
        double k1 = h * f(t,y);
        double k2 = h * f(t + h / 2, y + k1 / 2);
        double k3 = h * f(t + h / 2, y + k2 / 2);
        double k4 = h * f(t + h, y + k3);
        y1 += (k1 + 2*k2 + 2*k3 + k4) / 6;
    }
}

int main(){
    double tf = 2;
    double h1 = 0.1;
    double h2 = 0.01;
    double y0 = 1;

    euler(y0, h1, tf, "0.1");
    euler(y0, h2, tf, "0.01");
    std::cout << "\n";

    rk(y0, h1, tf, "0.1");
    rk(y0, h2, tf, "0.01");
    std::cout << "\n";

    return 0;
}