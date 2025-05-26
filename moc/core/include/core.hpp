#ifndef CORE_H
#define CORE_H
#include <iostream>

class Core{

public:
    Core();

    template<typename T>
    void save(const T& obj);

};

#endif