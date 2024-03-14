var contract = artifacts.require("MemberShip");

module.exports = function (deployer) {
  var initialPrice = 10000;
  deployer.deploy(contract, initialPrice);
};
