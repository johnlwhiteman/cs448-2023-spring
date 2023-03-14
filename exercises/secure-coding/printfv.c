#include <stdio.h>
#include <string.h>

void sayHello(const char *name) {
    /* Should be printf("Hello, %s", name); */
	printf("Hello, ");
	printf(name);
	printf("\n");
}

int main(int argc, char **argv) {
	char name[64];
	strncpy(name, argv[1], sizeof(name));
	sayHello(name);
	return 0;
}
