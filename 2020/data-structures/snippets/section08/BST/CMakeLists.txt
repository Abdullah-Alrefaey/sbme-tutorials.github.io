cmake_minimum_required(VERSION 2.8)

project(BST)

add_executable(oo oo.cpp)

add_executable(lambda lambda.cpp)

add_executable(bst bst.cpp BST.hpp)

add_executable(set set.cpp Set.hpp)

add_executable(map map.cpp Map.hpp)
