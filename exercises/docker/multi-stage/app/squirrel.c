#include <stdio.h>
#include <unistd.h>

int main(int argc, char **argv, char *envp[]) {

    int i;
    for (i = 0; envp[i] != NULL; i++) {
        printf("\n%s", envp[i]);
        getchar();
    }

    if (argc > 1) {
        printf("\nThe Squirrel says: %s\n", argv[1]);
    } else {
        printf("\nThe Squirrel Done Not Have Nothing tp Say\n");
    }

    return 0;
}