CC=g++

all: monocle

monocle: monocle.o
	$(CC) -std=c++11  -I/usr/include/glibmm-3.0 monocle.cpp -o monocle `pkg-config --cflags --libs gtkmm-3.0` -lX11

clean:
	rm *.o
