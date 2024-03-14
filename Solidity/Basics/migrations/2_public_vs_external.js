var contract = artifacts.require("PublicVsExternal");

module.exports = function (deployer) {
  deployer.deploy(contract);
};
