import { Web3 } from "web3";

// Set up a connection to the Ganache network
const web3 = new Web3("http://127.0.0.1:7545");

// Log the current block number to the console
web3.eth
  .getBlockNumber()
  .then((block) => {
    console.log("Last block:", block);
    // ↳ Last block: 4975299n
  })
  .catch((error) => {
    console.error("Error:", error);
  });
