# Exercise: AFL++

## Setup and compile

```bash
./setupAll
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
fuzzgoat output/crashes/crash-2023.03.12-12.05.05.json  # Example name
```

## Debug

```bash
gdb --args fuzzgoat ./crashes/crash-2023.03.12-12.05.05.json
run
```

## References

* [AFL](https://github.com/mirrorer/afl)
* [FuzzGoat](https://github.com/fuzzstati0n/fuzzgoat)
