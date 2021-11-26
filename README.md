# CE 4010 Applied Cryptography 
## Topic 5 - Secure and Private “intersection” of Sets 
## Contents: <br /> 
- [Introduction](#introduction)
- [Motivation](#motivation)
- [Research](#research)
- [Design](#design)
- [Development](#development)
- [Usage Of Code](#usage-of-code)

## Introduction
According to [Wikipedia](https://en.wikipedia.org/wiki/Private_set_intersection#:~:text=Private%20set%20intersection%20is%20a,the%20elements%20in%20the%20intersection.), Private set intersection: 
- is a **secure multiparty computation cryptographic** technique that allows two parties holding sets to **compare encrypted versions** of these sets in order to compute the intersection 
- In this scenario, neither party reveals anything to the counterparty except for the **elements in the intersection** <br /> 

![image](https://gateway.pinata.cloud/ipfs/QmfLafnygHJU47VpZJ5zWtzm61PoYLSfLWysBPfCEsQ4Fz)

## Motivation
Grab and Gojek want to identify the drivers who are double-dipping on both platforms while using the same
hired vehicle and the same phone number for receiving orders (assuming this behavior is against the individual contracts)

- Parties should be able to computer the intersection of two sets (phone numbers) without disclosing the sets
- No party should gain any knowledge about sets of other parties (prevent poaching of drivers in the example)
- Every party should gain the knowledge about final intersection set (the common phone numbers are revealed)
## Research
Consider whether to use symmetric cryptography (where 2 parties share the same key for encryption and decryption) or asymmetric cryptography (where 2 parties have their own private key and public key set)
- Looking at symmetric cryptography
    - Powerful as it allows fast encryption and decryption of data
    - However, in order for the 2 parties to agree on a key without physically meeting, the only way would be to send key via the internet which would be susceptible to a malicious eavesdropper
    - Second, if the 2 parties were to just use the same key, it would be computationally feasible for an eavesdropper to decrypt the ciphertext given a period of time. Even if they were to change their symmetric key, they would have to agree on another key by meeting which would be troublesome in the long run 
    - Moreover, Grab may also be performing this double dipping exercise with other ride-hailing companies like ComfortDelGro and Tada Mobility. This means that Grab has to have separate symmetric key for each communication with the other company and key storage could then become an issue for Grab
- Looking at asymetric cryptography
    - Uses two separate keys instead of one shared one: a public key and a private key
    - Highly secure because parties never need to transmit or reveal their private keys to anyone
    - **Decided to go with asymetric cryptography** <br />

![image](https://gateway.pinata.cloud/ipfs/Qmc46BXFUffsnsJkA75Z4nSt2YEct2QvgK9xLYkUw6ZKNS)

To understand how does asymetric cryptography work, we analyzed its earliest known scheme the Diffie-Hellman key exchange: <br />
You can refer to this [article](https://www.comparitech.com/blog/information-security/diffie-hellman-key-exchange/) to know more but essentially it is making use of the Discrete Logarithm Problem to send messages from one party to another. <br />

So, how do we apply to Private Set Intersection problem, Commutative Encryption comes into play: <br /> 
- It is a kind of an encryption system that enables a plaintext to be encrypted more than once using different users' public keys
- In this system, decryption is not required before the encryption/re-encryption processes, as seen in the Diffie-Hellman key exchange
- Moreover, the resulted ciphertext can be decrypted by the designated decrypters without considering the order of public keys used in the encryption/re-encryption processes 
- In other words, the order of keys used in encryption and in decryption do not affect the computational result
- Useful in real life applications such as secret sharing which is what we aim to do in our project

## Design
Using the idea of Commutative Cipher and Asymmetric Key Exchange to perform Private Set Intersection
### Approach
1. How to generate the keys - use a Python cryptographically secure library to generate a private key 
2. Next, we will use the Discrete Logarithm problem implementing it similar to how Diffie-Hellman was implemented. We can use the private key as the power raised
3. Use set of messages itself. Use a hash function before sending messages across the channel and since it is a one-way function, it provides a high level of security. After computation of the discrete logarithm, due to the exponent property; This works because - Commutative cipher (order of exponents does not matter)
4. Now, we can encrypt a list of messages in this case, in other words, the information of the hired drivers from Grab and Gojek
5. Sending the encrypted messages across to the parties and perform another encryption process again but this time with their own private keys to have doubly encrypted messages.
6. Now with the doubly encrypted sets, they can send it to each other via a Session key, and compute the intersection set between the doubly encrypted sets 
7. Grab can then do the same computational steps for its plaintext message list, same for Gojek
8. Now, they can compute the intersection between the cipher of their message list and the encrypted intersection set obtained from step 6 in their own private environment.
9. Obtain who are the drivers double-dipping!

![image](https://gateway.pinata.cloud/ipfs/Qmen8HGZxp6bzrbAunRWC9mF8wAfLASntneJNt6thwfyLU)

## Development
Development tools and stack used in project:   <br />

Code editor used:   [Visual Studio Code](https://code.visualstudio.com/) <br />
Coding Language used:   [Python](https://www.python.org/)<br />
Libraries used for Cryptography: <br />
- [*Secrets* module](https://docs.python.org/3/library/secrets.html) from Python
- [*Hashlib* module](https://docs.python.org/3/library/hashlib.html) from Python

## Usage of code
### Step 0: Prerequisite & Installation
Make sure the following are installed:
- [Git](https://gitforwindows.org/)   # Use ```git --version``` to check if git is installed
- [Python](https://www.python.org/downloads/) # Latest version: 3.10.0
- [Visual Studio Code](https://code.visualstudio.com/download) # Latest version: 1.62

### Step 1: Setup
Create a new directory in your current directory for the project: <br />
```
mkdir privateSetIntersection
cd privateSetIntersection 
```
### Step 2: Clone
Clone the github repository: <br />
```
git clone https://github.com/slim115/Private-Set-Intersection
```
Now your folder structure should look like: <br />
```
└── Private-Set-Intersection 
    ├── 4010_project_updated.py
    └── README.md
```
### Step 3: Run :rocket:
Run the Python code on Visual Studio Code or using Terminal: <br />
```
python 4010_project_updated.py
```
Output should display this:
```
Number of intersections: 4

Phone numbers: {'98765432', '95678000', '52134567', '40000000'}
```
Congratulations! We have now displayed the phone numbers of the intersection set. Private Set Intersection achieved! :smile: <br />

### Things to take note: 
Please take note Grab and Gojek sets of phone numbers have already been hardcoded
- inputs for Grab numbers: ```{"91234567", "12345678","40000000", "52134567", "11112222", "98765432", "95678000"}```
- inputs for Gojek numbers: ```{"95678000", "40000000", "68991111" "32123212", "52134567", "98765432"}```

Also, In this scenario, we are assuming that if a driver is using the same phone number, then he will be also using the same hired vehicle since it is highly likely for a driver to use the same phone but less likely for a driver to switch hired vehicle. Hence, in this protocol we will only be comparing phone numbers of the drivers from Grab and from Gojek <br />

P.S Change the numbers accordingly for a different number of intersections
