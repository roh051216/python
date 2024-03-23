#include <stdio.h> 

int main(){
    int h,m;
    int t;
    scanf("%d %d",&h, &m);
    scanf("%d",&t);

    h += t / 60;
    m += t % 60;

    if (m >= 60){
            ++h;
            m-= 60;
    }

    if (h >= 24){
        h-=24;
    }
    printf("%d %d\n", h,m);
    return 0;
}