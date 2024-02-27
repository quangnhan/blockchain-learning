import { Web3 } from "web3";
const SubCurrencyContract = require("./SubCurrencyContract.json");

const web3 = new Web3("http://localhost:7545");

async function getMinter() {
  let contract = new web3.eth.Contract(
    SubCurrencyContract.abi,
    "0x82b5a9264c54956e09AA19B37D53D1466ff64389"
  );
  let minter = await contract.methods.minter().call();
  console.log("Minter:", minter);
}

(async () => {
  await getMinter();
})();
