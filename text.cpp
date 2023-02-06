#include <iostream>
#include <string>

using namespace std;

int main(){
    // int m;
    // cout<<"enter the size of row and coloum in the matrix\m";
    // cin>>m;
    // int a[m][m];
    // cout<<"enter the elements in the matix: \m";
    // for(int i = 0;i< m;i++){
    //     for(int j = 0;j< m;j++){
    //         cin>>a[i][j];
    //     }
        
    // }
    // cout<<"The elements of matrix are: \m";
    // for(int i = 0;i< m;i++){
    //     for(int j = 0;j< m;j++){
    //         cout<<a[i][j]<<" ";
    //     }
    //     cout<<endl;
    // }

    // serach for letters in char

    char str[20];
    char ch;
    int i, num = 0;

    puts("Enter a string\n");

    std::cin.getline(str, 20);

    cout<<"enterthe chareter t be search\n";

    cin>>ch;

    for(i=0;str[i]!='\0';i++){

        if(str[i] == ch){
            num++;
        }

    }
    cout<<num;
    return 0;
}