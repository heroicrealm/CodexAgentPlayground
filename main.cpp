#include <ctime>
#include <iomanip>
#include <iostream>
#include <string>

int main() {
    std::cout << "Введите имя пользователя: " << std::flush;

    std::string username;
    if (!std::getline(std::cin, username)) {
        return 1;
    }

    if (username == "root") {
        std::cout << "Здравствуйте, root!\n";
        const std::time_t now = std::time(nullptr);
        const std::tm* local_time = std::localtime(&now);
        if (now == static_cast<std::time_t>(-1) || local_time == nullptr) {
            std::cerr << "Не удалось получить текущее время\n";
            return 1;
        }
        std::cout << "Текущее время: "
                  << std::put_time(local_time, "%Y-%m-%d %H:%M:%S") << '\n';
    } else {
        std::cout << "пользователь не найден\n";
    }

    return 0;
}
