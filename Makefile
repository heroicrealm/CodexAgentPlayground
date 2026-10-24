CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -Wpedantic

.PHONY: all test clean

all: greeting

greeting: main.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

test: greeting
	python3 tests/test_greeting.py

clean:
	rm -f greeting
