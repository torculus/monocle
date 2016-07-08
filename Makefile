all: monocle

monocle: monocle.o
	g++  monocle.cpp -o monocle `pkg-config gtkmm-3.0 --cflags --libs` -std=c++11 -lX11

clean:
	rm *.o
