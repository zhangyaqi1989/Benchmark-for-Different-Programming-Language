obj := thermal_c thermal_f

all: $(obj)

thermal_c: thermal.c
	gcc -O3 -o thermal_c thermal.c -Wall

thermal_f: thermal.f95
	gfortran -std=f95 -O3 -o thermal_f thermal.f95

clean:
	rm $(obj)





