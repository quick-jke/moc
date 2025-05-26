#ifndef CORE_H
#define CORE_H
#include <iostream>
#include "session_helper.hpp"

class Core{

public:
    Core();

    template<typename T>
    void save(const T& obj);

};

#endif