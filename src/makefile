obj := thermal_c thermal_cpp thermal_f Thermal.class

all: $(obj)

thermal_c: thermal.c
	gcc -O3 -o thermal_c thermal.c -Wall

thermal_cpp: thermal.cpp
	g++ -O3 -o thermal_cpp thermal.cpp -Wall

thermal_f: thermal.f95
	gfortran -std=f95 -O3 -o thermal_f thermal.f95

Thermal.class: Thermal.java
	javac Thermal.java

clean:
	rm $(obj)





