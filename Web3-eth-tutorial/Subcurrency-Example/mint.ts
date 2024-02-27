import { Web3 } from "web3";
const SubCurrencyContract = require("./SubCurrencyContract.json");

const web3 = new Web3("http://localhost:7545");

async function mint() {
  let contract = new web3.eth.Contract(
    SubCurrencyContract.abi,
    "0x82b5a9264c54956e09AA19B37D53D1466ff64389"
  );
  let from = "0xAc4aA98D3025aA9599Be3884c85FD50299720402"; // minter
  let receiver = "0xd70A658389c81F4E2e40d8cb626a18d92864089B";
  let amount = web3.utils.toWei("1.5", "ether");

  let result = await contract.methods
    .mint(receiver, amount)
    .send({ from: from });

  console.log("Result:", result);
}

(async () => {
  await mint();
})();
