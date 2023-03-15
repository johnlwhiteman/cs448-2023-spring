.PHONY: all clean
CC=gcc

all: buffy gets heartbleed memleak naive func aslr notsonaive shellcode signme simplestack testshellcode printfv printfvW

aslr: aslr.c
	gcc -O0 -fPIE -fno-stack-protector -z execstack -g $< -o $@ 

buffy: buffy.c
	gcc -g $< -o $@

gets: gets.c
	gcc -g $< -o $@

badmem: memleak.c
	gcc -g $< -o $@

heartbleed: heartbleed.c
	gcc -g $< -o $@

naive: naive.c
	gcc -O0 -fno-pie -fno-stack-protector -z execstack $< -o $@ 

notsonaive: notsonaive.c
	gcc -O0 -fPIC -fno-stack-protector -z execstack $< -o $@ 

# sudo apt-get install gcc-multilib
#shellcode: shellcode.c
#	gcc -fno-stack-protector -z execstack -m32 $< -o $@ 

#testshellcode: testshellcode.c
#	gcc -fno-stack-protector -z execstack -m32 $< -o $@ 


#signme: signme.c
#	gcc -O0 -fno-stack-protector -z execstack $< -o $@ 

printfv: printfv.c
	gcc -g $< -o $@

printfvW: printfv.c
	gcc -Wformat -Wformat-security -g $< -o $@

printfvE: printfv.c
	gcc -Wformat -Werror=format-security -g $< -o $@

clean:
	rm -f buffy gets heartbleed memleak naive func aslr notsonaive shellcode signme simplestack testshellcode printfv printfvW
