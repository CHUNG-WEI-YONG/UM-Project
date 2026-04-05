#include <iostream>
using namespace std;

int main(){
    int a=8,b=3,c=-5;
    cout<<"1. 2 * b + 3 * (a-c)= " << 2 * b + 3 * (a-c) << endl;
    cout<<"2. a*b/c= " << a*b/c << endl;
    cout<<"3. (a*b)%c= "<<(a*b)%c << endl;
    cout<<"4. (a*c)%b)= "<<a*(c%b) << endl;
    cout<<"5. a*(c%b)= "<<a*(c%b) << endl;
    cout<<"6. b*(a+c)*b/2= "<<b*(a+c)*a/2 << endl;
    cout<<"7. 15 + c / 6 - 2 * 6 % 5 = "<<15 + c / 6 - 2 * 6 % 5 << endl;
    cout<<"8. ((15 + c) / (6 – 2) * 6) % 5 = "<<((15 + c) / (6 - 2) * 6) % 5 
    << endl;
    return 0;
}