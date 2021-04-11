#include<stdio.h>

int add(int a,int b)
{
    return a+b;
}

float loopFmul(int limit)
{
    printf("\n%d\n",limit);
    int total= 1;

    for (int i = 0; i < limit; i++)
    {total *= i;}

    return total;
}