# Exercise: Radamsa

## Setup

```bash
./setupRadamsa
./setupFuzzGoat
```

## Compile

```bash
cd ./fuzzgoat
make
```

## Execute

```bash
mkdir -p ./input ./output
cp ./good.json ./input/

# Manual repeat ... look for segfault
radamsa good.json > fuzzed.json
fuzzgoat fuzzed.json

# Automated
./testDriver
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
fuzzgoat output/crashes/crash-2023.03.12-12.05.05.json  # Example name
```

## Debug

```bash
gdb --args fuzzgoat ./crashes/crash-2023.03.12-12.05.05.json
run
```

## References

* [AFL](https://gitlab.com/akihe/radamsa)
* [FuzzGoat](https://github.com/fuzzstati0n/fuzzgoat)
