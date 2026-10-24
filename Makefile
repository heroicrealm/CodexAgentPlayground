CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -Wpedantic

.PHONY: all clean

all: greeting

greeting: main.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	rm -f greeting
