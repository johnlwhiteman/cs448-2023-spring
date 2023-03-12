# Exercise: AFL

## Setup

```bash
./setupAFl
./setupFuzzGoat
```

## Compile

```bash
cd ./fuzzgoat
vi ./Makefile

#CC=gcc
CC=afl-gcc

make
```

## Execute

```bash
mkdir -p ./input ./output
cp ./good.json ./input/

# Let it run for awhile
afl-fuzz -i ./input -o ./output ./fuzzgoat @@
```

## Analyze

```bash
cd ../
afl-plot ./output ./charts
cd ./charts
firefox index.html &
```

## Reproduce

```bash
ls -al ./output/crashes
fuzzgoat output/crashes/<pick a file here>  # Should segfault
```


## References

* [AFL](https://github.com/mirrorer/afl.git)
* [FuzzGoat](https://github.com/fuzzstati0n/fuzzgoat.git)
