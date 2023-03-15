#include <stdio.h>
#include <string.h>

void show(char *);

int main(int argc, char **argv) {
    char b1[11];
    strcpy(b1, argv[1]);
    show(b1);
}

void show(char *b1) {
    printf("b1 value:      %s\n", b1);
    printf("b1 length:     11\n");
    printf("b1 address:    %p [%i]\n", (void *)b1, 0);
}
