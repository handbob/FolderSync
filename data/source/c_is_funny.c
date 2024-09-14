#include <stdlib.h>
#include <stdio.h>

typedef struct MySuperType
{
    char *data;
    int count;
} MySuperType;

void initMySuperType(MySuperType *self, char *data, int count)
{
    self->data = data;
    self->count = count;
}

int main(int argc, const char **argv)
{
    MySuperType *mySuperType = malloc(sizeof(MySuperType));
    initMySuperType(mySuperType, "I am String in C :)", 1000000);

    printf("pointer of address is allocated :D :%p\n", mySuperType);
    printf("data: %s\ncount: %d\n", mySuperType->data, mySuperType->count);

    free(mySuperType);
    mySuperType = NULL;

    printf("pointer of address is deallocate :D :%p\n", mySuperType)
    
    return 0;
}
