#include<stdio.h>

int main(){
int x=2;
int y=3;
printf("Before swapping the value of x is %d and the value of y is %d",x,y);
x+=y;
y=x-y;
x=x-y;
printf("After swapping the value of x is %d and the value of y is %d",x,y);
return 0;
}
