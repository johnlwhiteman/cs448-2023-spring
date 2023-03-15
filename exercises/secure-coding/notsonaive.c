#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
	int isAuthenticated = 0;
	char buffer[7];
	strcpy(buffer, argv[1]);
	printf("isAuthenticated: %d\n", isAuthenticated);
	if (0 != isAuthenticated) {
		printf("Success!\n");
	} else {
		printf("Failed!\n");
	}
	return 0;
}
