#include <stdio.h>
#include <string.h>

void show(char *, char *);

int main(int argc, char **argv) {
    char b1[21] = "You can't change me!";
    char b2[21];
    strcpy(b2, argv[1]);
    show(b1, b2);
}

void show(char *b1, char *b2) {
    printf("b1 value:      %s\n", b1);
    printf("b2 value:      %s\n", b2);
    printf("b1 length:     21\n");
    printf("b2 length:     21\n");
    printf("b1 address:    %p [%i]\n", (void *)b1, 0);
    printf("b2 address:    %p [%i]\n", (void *)b2, b2 - b1);
    printf("b2+%d address:  %p [%i]\n", 21, (void *)b2 + 21, b2 + 21 - b1);
}
