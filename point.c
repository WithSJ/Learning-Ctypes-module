#include<stdio.h>

typedef struct
{
    /* data */
    int x,y;
}Point;

Point create_point(int x,int y)
{
    Point p1;
    p1.x = x;
    p1.y = y;
    return p1;
}




void show_point(Point v1)
{
    printf("From C (%d,%d)",v1.x,v1.y);
}