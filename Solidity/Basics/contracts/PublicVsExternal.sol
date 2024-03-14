// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract PublicVsExternal {
    uint value;

    function publicSet(uint x) public {
        value = x;
    }

    function externalSet(uint x) external {
        value = x;
    }

    function get() public view returns (uint) {
        return value;
    }
}
