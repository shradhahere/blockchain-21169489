from web3 import Web3
from decouple import config

infura_url = config('INFURA_URL')

contractAddress = Web3.toChecksumAddress(config('CONTRACT_ADDRESS'))
abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'
ownerAddress = config('OWNER_ADDRESS')

Private_Key = config('SUPER_SECRET_PRIVATE_KEY')
web3 = Web3(Web3.HTTPProvider(infura_url))
res = web3.isConnected()
if res:
    print("Connected")

    contract_instance = web3.eth.contract(address=contractAddress, abi=abi)
    symbol = contract_instance.functions.symbol().call()
    print("Symbol "+symbol)


amountInEther = "0.0001"
targetAddress = Web3.toChecksumAddress("0xac4FafdA6A3A6B48b4cDC2a896acf8D104C81d6C")

nonce = web3.eth.getTransactionCount(ownerAddress)
print(nonce)

gasPrice = web3.toWei('100', 'gwei')
value = web3.toWei(amountInEther, 'ether')

tx = {
'nonce': nonce,
'to': targetAddress,
'value': value,
'gas': 50000,
'gasPrice': gasPrice,
'chainId': 5
}

signed_tx = web3.eth.account.sign_transaction(tx, Private_Key)

tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print('tx hash: ' + tx_hash.hex())

web3.eth.waitForTransactionReceipt(tx_hash)
print('tx mined')


