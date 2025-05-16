# Makefile_PintoSanabriaSarayJuliana_S6CASA_EDO.mk

CPP = g++
CPPFLAGS = -std=c++17 -O2

TARGET = solve_edo
SRC = PintoSanabriaSarayJuliana_S6C2_EDO.cpp
PYTHON_SCRIPT = PLOTS_SarayJulianaPintoSanabria_S6CASA_EDO.py

all: run plot

$(TARGET): $(SRC)
	$(CPP) $(CPPFLAGS) -o $(TARGET) $(SRC)

run: $(TARGET)
	./$(TARGET)

plot: run
	python $(PYTHON_SCRIPT)

clean:
	rm -f $(TARGET) *.dat *.png

.PHONY: all run plot clean
