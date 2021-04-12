#include<stdio.h>

typedef struct
{
    /* data */
    int x,y,z;
}Vector_Node;

void show_point(Vector_Node vec)
{
    printf("From C (%d,%d,%d)",vec.x,vec.y,vec.z);
}