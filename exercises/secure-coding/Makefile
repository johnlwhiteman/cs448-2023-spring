.PHONY: all clean

all: buffy gets heartbleed memleak printfv printfvW printfvE

buffy: buffy.c
	gcc -g $< -o $@

gets: gets.c
	gcc -g $< -o $@

badmem: memleak.c
	gcc -g $< -o $@

heartbleed: heartbleed.c
	gcc -g $< -o $@

printfv: printfv.c
	gcc -g $< -o $@

printfvW: printfv.c
	gcc -Wformat -Wformat-security -g $< -o $@

printfvE: printfv.c
	gcc -Wformat -Werror=format-security -g $< -o $@

clean:
	rm -f buffy gets heartbleed memleak printfv printfvW
