# HTTP / HTTPS

## Objective

* A quick demonstration showing the differences between HTTP and HTTPS.
* You will need to have Wireshark running too

## Execution

```bash
# Open a terminal and start Wireshark
wireshark -i loopback

# Open another terminal and start the containers
./shellEx

# Open a browser window and navigate to the HTTP connection
firefox http://127.0.0.1:12345

# Open another browser window and navigate to the HTTPS connection
firefox https://127.0.0.1:54321

# Click on some links for both. Observer what happens in Wireshark
# For Chrome press Ctrl+Shift+R to ensure data is fresh (avoid the not-modified)

# Interact with the HTTP container (optional)
./startEx http  # Type exit when done

# Interact with the HTTPS container (optional)
./startEx https # Type exit when done

# Stop the exercise and tear down the containers/images
./stopEx