#include <stdio.h>

int main(){
    int num1;
    scanf("%d",&num1);
    if(num1%4==0&&num1%100!=0){
        printf("%d",1);
    }
    else if(num1%400==0){
        printf("%d",1);
    }
    else
        printf("%d",0);

    return 0;
}