#include <iostream>
#include <functional>
#include <chrono>
#include <cmath>

void loggin_decorator(std::function<void()>&& func) {
    std::cout << "Entering function" << std::endl;
    func();
    std::cout << "Exiting function" << std::endl;
}

template<typename func>
void timing_decorator(func&& f) {
    auto start = std::chrono::high_resolution_clock::now();
    f();
    auto end   = std::chrono::high_resolution_clock::now();
    std::cout << "Elapsed time: " << std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count() << "ms" << std::endl;
}

void my_function() {
    std::cout << "Hello, World!" << std::endl;
}

// 原始函数
void example_function() {
    for (int i = 0; i < 1000000; ++i)   // 模拟耗时任务
    {
        // do something
        int j = (++i) * std::pow(999,2);
    }
}


int main()
{
    //std::function<void()> func = my_function;
    //loggin_decorator(func);

    loggin_decorator(my_function);

    timing_decorator(example_function);
    return 0;
}