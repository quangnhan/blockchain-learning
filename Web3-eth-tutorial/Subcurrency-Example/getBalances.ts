import { Web3 } from "web3";
const SubCurrencyContract = require("./SubCurrencyContract.json");

const web3 = new Web3("http://localhost:7545");

async function getBalance() {
  let contract = new web3.eth.Contract(
    SubCurrencyContract.abi,
    "0x82b5a9264c54956e09AA19B37D53D1466ff64389"
  );
  let address = "0xd70A658389c81F4E2e40d8cb626a18d92864089B";
  let amount = await contract.methods.balances(address).call();
  console.log("Amount:", amount);
}

(async () => {
  await getBalance();
})();
