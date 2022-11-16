## Overview

DexGuru uses token lists in this repository to group tokens by tags. Check out the visual representation at https://dex.guru/tokens.
Each JSON file represents a single tag(or multiple related tags, eg. Stablecoins and Stablecoins on Ethereum) and is a list of publicly sourced tokens. Anyone is welcome to add new tokens and new tags.

Keep in mind, this is NOT investment advice, a stamp of approval, or any kind of recommendation.

## How to add a new token to a list

- Look for the JSON file in this repo with the tag name you are looking for. Please make sure that the token that you are going to add matches the tag description. See this line at beginning of JSON, eg.: 
```
  "tags": {
    "layer_2": {
      "name": "Layer 2",
      "description": "Layer 2 (L2) is a collective term to describe a specific set of Ethereum scaling solutions. L2 tokens can be used to decentralize a variety of protocol functions."
    }
```  
- Edit the JSON file. <br />
- Add an object to the JSON with the token's metadata like this <br />

```
	 {
	 "chainId": "NETWORK_CHAIN_ID",
	 "address": "TOKEN_CONTRACT_ADDRESS",
	 "symbol": "TOKEN_TICKER",
	 "name": "TOKEN_NAME",
	 "tags": ["TOKEN_TAG"]
	 }
```

- Submit your pull request
- Do not forget to add token to multiple files if you can apply more than one tag to it.

## How to add a new tag

- Add a new JSON file to this repo with the name of the new tag.
- Make sure your JSON file have description that is explain what kind of tokens belongs to this tag.

```'{
	  "name": "Meme",
	  "tags": {
	    "meme": {
	      "name": "Meme",
	      "description": "Meme coins are cryptocurrencies inspired by memes and internet jokes. Though Meme are based on memes or even internet jokes, they have cemented their position in the crypto space today. "
	    }
	  }'
```

- The structure of your JSON file should be the same as any other JSON in this repository.
- Please add at least 2 tokens to the new tag token list.
- Submit your pull request.
