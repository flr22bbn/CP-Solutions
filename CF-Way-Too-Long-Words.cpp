#include <iostream>
#include <string>
using namespace std;
int main () {
        string word;
        int num_of_lines{};
        cin>>num_of_lines;
        
        for (int i{1};i<=num_of_lines;i++){
            cin>>word;
            if (word.length()<=10){
                cout<<word<<endl;
            }
            else{
               int g = word.length();
               int f=g-2;
                cout<<word[0]<<f<<word[word.length()-1]<<endl;
              
            }
        }
  return 0;
}
