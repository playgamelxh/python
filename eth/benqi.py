import csv
from web3 import Web3

reader_abi = [
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_router",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "inputs": [],
    "name": "accountSnapshot",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "getAccountValue",
    "outputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "account",
            "type": "address"
          },
          {
            "components": [
              {
                "internalType": "address",
                "name": "token",
                "type": "address"
              },
              {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
              }
            ],
            "internalType": "struct TokenValue[]",
            "name": "borrowTokens",
            "type": "tuple[]"
          },
          {
            "internalType": "uint256",
            "name": "borrowTotalValue",
            "type": "uint256"
          },
          {
            "components": [
              {
                "internalType": "address",
                "name": "token",
                "type": "address"
              },
              {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
              }
            ],
            "internalType": "struct TokenValue[]",
            "name": "supplyTokens",
            "type": "tuple[]"
          },
          {
            "internalType": "uint256",
            "name": "supplyTotalValue",
            "type": "uint256"
          }
        ],
        "internalType": "struct AccountValue",
        "name": "accountValue",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address[]",
        "name": "accounts",
        "type": "address[]"
      }
    ],
    "name": "getAccountsValue",
    "outputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "account",
            "type": "address"
          },
          {
            "components": [
              {
                "internalType": "address",
                "name": "token",
                "type": "address"
              },
              {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
              }
            ],
            "internalType": "struct TokenValue[]",
            "name": "borrowTokens",
            "type": "tuple[]"
          },
          {
            "internalType": "uint256",
            "name": "borrowTotalValue",
            "type": "uint256"
          },
          {
            "components": [
              {
                "internalType": "address",
                "name": "token",
                "type": "address"
              },
              {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
              }
            ],
            "internalType": "struct TokenValue[]",
            "name": "supplyTokens",
            "type": "tuple[]"
          },
          {
            "internalType": "uint256",
            "name": "supplyTotalValue",
            "type": "uint256"
          }
        ],
        "internalType": "struct AccountValue[]",
        "name": "accountsValue",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "token",
        "type": "address"
      }
    ],
    "name": "getDecimal",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "decimal",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "token",
        "type": "address"
      }
    ],
    "name": "getTokenPrice",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "price",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "token",
        "type": "address"
      }
    ],
    "name": "getUnderlyingAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "underlyingAddress",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "vwAddr",
        "type": "address"
      }
    ],
    "name": "getValue",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "tvl",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "oracle",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "router",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]
bsc_rpc_url = 'https://avalanche.drpc.org'
w3 = Web3(Web3.HTTPProvider(bsc_rpc_url))
benqi_reader_addr = Web3.to_checksum_address('0xc7cd1fc4e392d218123FB27BB79b086a7Cea21f5')
reader_contract = w3.eth.contract(benqi_reader_addr, abi=reader_abi)
# allowance = usdt_contract.functions.allowance(account_address, usdt_contract_address).call()
data_to_write = []
with open('allAddress.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    # 逐行读取内容
    i = 0
    users = []
    for line in reader:
        i += 1
        users.append(line[2])
        if(i%20 == 0 or i==5428):
            account_addresses = [Web3.to_checksum_address(address) for address in users]
            values = reader_contract.functions.getAccountsValue(account_addresses).call()
            print(i)
            for v in values:
            	data_to_write.append([v[0],v[1][0][1]/1e8,v[1][1][1]/1e8,v[1][2][1]/1e8,v[1][3][1]/1e8,v[1][4][1]/1e8,
                                      v[1][5][1]/1e8,v[1][6][1]/1e8,v[1][7][1]/1e8,v[1][8][1]/1e8,v[1][9][1]/1e8,v[1][10][1]/1e8,
                                      v[1][11][1]/1e8,v[2]/1e8,v[3][0][1]/1e8,v[3][1][1]/1e8,v[3][2][1]/1e8,v[3][3][1]/1e8,
                                      v[3][4][1]/1e8,v[3][5][1]/1e8,v[3][6][1]/1e8,v[3][7][1]/1e8,v[3][8][1]/1e8,v[3][9][1]/1e8,
                                      v[3][10][1]/1e8,v[3][11][1]/1e8,v[4]])
            users = []

with open('benqiTVL.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data_to_write)
