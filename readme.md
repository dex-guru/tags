## Overview
DexGuru uses token lists in this repository to group tokens by tags. Check out the visual representation at https://dex.guru/tokens. 
Each JSON file represents a single tag and is a list of publicly sourced tokens. Anyone is welcome to add new tokens and new tags.

## How to add a new token to a list
* Look for the JSON file in this repo with the tag name you are looking for. 
* Edit the JSON file. <br />
* Add an object to the JSON with the token's metadata like this <br />
```
	,
	 {
	 "chainId": "NETWORK_CHAIN_ID",
	 "address": "TOKEN_CONTRACT_ADDRESS",
	 "symbol": "TOKEN_TICKER",
	 "name": "TOKEN_NAME",
	 "tags": ["TOKEN_TAG"]
	 }
```
* Submit your pull request
* Do not forget to add token to multiple files if you can apply more than one tag to it. 

## How to add a new tag
* Add a new JSON file to this repo with the name of the new tag. 
* The structure of your JSON file should be the same as any other JSON in this repository. 
* Please add at least 2 tokens to the new tag token list. 
* Submit your pull request
