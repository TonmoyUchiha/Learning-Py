#include <iostream>
using namespace std;

int main() {
    int num = 10;      
    int* ptr = &num;   

    // Output the value and address
    cout << "Value of num: " << num << endl;
    cout << "Address of num: " << ptr << endl;

    // Modify the value using the pointer
    *ptr = 20;
    cout << "Modified value of num: " << num << endl;

    return 0;
}
