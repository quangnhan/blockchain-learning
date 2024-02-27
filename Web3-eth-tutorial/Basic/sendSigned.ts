import { Web3 } from "web3";
const web3 = new Web3("http://localhost:7545");

//make sure to copy the private key from ganache
const privateKey =
  "0x8dc63c3be4674c9b1273696b6e978f7070be4374210127a20191b90286fef39b";
const value = web3.utils.toWei("1", "ether");

async function sendSigned() {
  const accounts = await web3.eth.getAccounts();
  const fromAddress = accounts[0];
  const toAddress = accounts[1];
  // Create a new transaction object
  const tx = {
    from: fromAddress,
    to: toAddress,
    value: value,
    gas: 21000,
    gasPrice: web3.utils.toWei("10", "gwei"),
    nonce: await web3.eth.getTransactionCount(fromAddress),
  };

  // Sign the transaction with the private key
  const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);

  // Send the signed transaction to the network
  const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

  console.log("Transaction receipt:", receipt);
}
(async () => {
  await sendSigned();
})();
