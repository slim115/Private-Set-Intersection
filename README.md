# Private-Set-Intersection
According to [Wikipedia](https://en.wikipedia.org/wiki/Private_set_intersection#:~:text=Private%20set%20intersection%20is%20a,the%20elements%20in%20the%20intersection.), Private set intersection is a 
- **secure multiparty computation cryptographic** technique that allows two parties holding sets to **compare encrypted versions** of these sets in order to compute the intersection
- In this scenario, neither party reveals anything to the counterparty except for the **elements in the intersection**
## Motivation
Grab and Gojek want to identify the drivers who are double-dipping on both platforms while using the same
hired vehicle and the same phone number for receiving orders (assuming this behavior is against the individual contracts)

- Parties should be able to computer the intersection of two sets (phone numbers) without disclosing the sets
- No party should gain any knowledge about sets of other parties (prevent poaching of drivers in the example)
- Every party should gain the knowledge about final intersection set (the common phone numbers are revealed)
## Research
A commutative encryption is a kind of an encryption system that enables a plaintext to be encrypted more than once using different users' public keys. ... In other words, the order of keys used in encryption and in decryption do not affect the computational result  

Asymmetric encryption, also known as public key encryption, uses two separate keys instead of one shared one: a public key and a private key.
## Design
Using the idea of Commutative Cipher and Asymmetric Key Exchange to perform Private Set Intersection
## Development
Development tools and stack used in your project.   

Libraries used for Cryptography:
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
### Step 3: Run 
Run the Python code on Visual Studio Code or using Terminal: <br />
```
python 4010_project_updated.py
```
Output should display this:
```
Number of intersections: 4

Phone numbers: {'98765432', '95678000', '52134567', '40000000'}
```
Please take note Grab and Gojek sets of phone numbers have already been hardcoded
- inputs for Grab numbers: ```{"91234567", "12345678","40000000", "52134567", "11112222", "98765432", "95678000"}```
- inputs for Gojek numbers: ```{"95678000", "40000000", "68991111" "32123212", "52134567", "98765432"}```

Change the numbers accordingly for a different number of intersections
