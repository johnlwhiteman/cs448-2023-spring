#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv) {
    printf("Address: %p\n",
           __builtin_return_address(0)-0x5);
    return 0;
}
