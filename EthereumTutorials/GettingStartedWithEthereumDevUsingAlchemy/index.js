async function main() {
	const alchemyAPIkey = "" // Set Alchemy API key here.
	if (!alchemyAPIkey) {
		console.error("Alchemy API key not set")
		return
	}
  const { createAlchemyWeb3 } = require("@alch/alchemy-web3")
  const web3 = createAlchemyWeb3("https://eth-mainnet.alchemyapi.io/v2/" + alchemyAPIkey)
  const blockNumber = await web3.eth.getBlockNumber()
  console.log("The latest block number is " + blockNumber)
}
main()
