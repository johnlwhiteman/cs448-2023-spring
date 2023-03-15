#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    /* Use a string literal, can't be overwritten */
    char *password = "$3CkReTPa$sW0rd!";
    char guess[11];

    /* Use a SAFE function ... only MAX bytes */
    strncpy(guess, argv[1], sizeof(guess));
    printf("Password: [%s]\n", password);
    printf("Guess:    [%s]\n", guess);

    /* Compare the entire strings */
    if (0 == strcmp(guess, password)) {
        printf("[OK]:     *** Match ***\n");
        return 0;    }
    printf("[BAD]:    No Match\n");
    return 1;
}
