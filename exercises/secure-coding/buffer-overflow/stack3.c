#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    char password[11] = "secret";
    char guess[11];

    strcpy(guess, argv[1]);
    printf("Password: [%s]\n", password);
    printf("Guess:    [%s]\n", guess);

    if (0 == strncmp(guess, password, 11)) {
        printf("[OK]:     *** Match ***\n");
        return 0;
    }
    printf("[BAD]:    No Match\n");
    return 1;
}
