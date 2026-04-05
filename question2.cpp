#include <iostream>
#include <string>
using namespace std;

int main(){
    
    int data1=3,data2=6,data3=10,data4=15;
    string q[8]={"a. data1 += 5",
                 "b. data1 = data1 + 2",  
                 "c. data2 += data1",
                 "d. data2 = data2 + data1--",
                 "e. data3 -= 2 * --data2",
                 "f. data3 *= data3 - 1",
                 "g. data4 -= data3++",
                 "h. data4 = data4 * ++data3"};
    int expression[8]={data1 += 5,
                 data1 = data1 + 2,  
                 data2 += data1,
                 data2 = data2 + data1--,
                 data3 -= 2 * --data2,
                 data3 *= data3 - 1,
                 data4 -= data3++,
                 data4 = data4 * ++data3};
    for (int i=0;i<8;i++){
        cout<<q[i]<<" = "<<expression[i]<<endl;
    }
    return 0;
}