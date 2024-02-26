var contract = artifacts.require("SubCurrencyContract");

module.exports = function (deployer) {
  deployer.deploy(contract);
};
