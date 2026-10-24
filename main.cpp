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
    } else {
        std::cout << "пользователь не найден\n";
    }

    return 0;
}
