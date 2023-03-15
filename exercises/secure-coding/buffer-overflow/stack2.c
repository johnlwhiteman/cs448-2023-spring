#include <stdio.h>
#include <string.h>

void authenticate(char *, int *);
void show(char *, int);

int main(int argc, char **argv) {
    int isAuthenticated = 0;
    char password[11];
    strcpy(password, argv[1]);
    authenticate(password, &isAuthenticated);
    show(password, isAuthenticated);
    if (0 == isAuthenticated) {
        printf("Failed!\n");
        return 1;
    }
    printf("Success!\n");
    return 0;
}

void authenticate(char *password, int *isAuthenticated) {
    /* Normally checks are done here with password and
       if valid, isAuthenticated = 1 */
    return;
}

void show(char *password, int isAuthenticated) {
    printf("Password:        %s\n", password);
    printf("isAuthenticated: %d\n", isAuthenticated);
}
