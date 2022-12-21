# Blockchain Project

## In this project we have our ERC20 contract created, compiled using Remix IDE and deployed on Ethereum Goerli Testnet using MetaMask account.

- Step 1: Create the solidity file for ERC20 contract
- Step 2: Compile it
- Step 3: Select "Injected Provider - Metamask" under environment section to connect to our MetaMask account and deploy it
- Step 4: Once deployed successfully, verify and publish the contract using Etherscan explorer.
- Step 5: Import Tokens in MetaMask by adding token contract address.

## Building a Python application for interacting with Ethereum Goerli Testnet and performing token distribution

## Pre-requisites

- Install Python3  
- Install PIP  
```sudo apt install python3-pip```. 
- Install web3. 
```pip install web3```. 
- Install decouple. 
```pip install python-decouple```. 
- IDE (example VS Code). 
- Install Docker desktop. 
- Optional: Setting up our infura.io account. 

## Setting up ENV file, with the following details, add your value to it, based on your account and contract.  
  
- INFURA_URL=
- CONTRACT_ADDRESS= 
- OWNER_ADDRESS=
- SUPER_SECRET_PRIVATE_KEY=
- SEED_PHRASE=
  
## Python files for performing various activities. 
  
(Make sure you have your ABI in files set correctly, based on the contract created, also you need to specify target address, the ID of the account to which transfer is to be done). 
  
For ETH transfer, run the file by using command:  
```python3 eth_transfer.py```. 
  
For transfer of token, run the python file by using command:  
```python3 token_transfer.py```. 
  
For getting the balance of the provided account, checking balance, making transactions based on requirements specified, run the following python file by using command:  
```python3 web3helpers.py```. 
  
For building a web server, run the python file by using the command:  
```python3 webserver.py```. 
  
### DOCKER. 
Use the file named "Dockerfile" in this repository, for docker setup and then we can build, run the image and push to Docker Hub. 
  
- For view running docker containers, run this command:  
```docker ps```
- For building,  
```docker build -t [name]```
- For running the docker image. 
```docker run -p 8090:8080 --name {name} -d {name}```
- To start/stop a container. 
```docker start/stop [name]```
- To run docker-compose. 
```docker-compose up```. 
  
For building and pushing the code to Docker Hub, use the follwing commands:  
- ```docker build -t [name:tag]```. 
- ```docker push [name:tag]```. 
  
Link to my DockerHub repository:  
https://hub.docker.com/repository/docker/shalinivaibhav/blockchain-21196354

- Command to pull the repo from Docker Hub : docker pull shalinivaibhav/blockchain-21196354
