// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract MemberShip {
    address owner;
    uint public price;
    mapping(address => uint) public registeredAddress;

    event Registration(address indexed _address, uint _value);
    event PriceChange(uint _newPrice);

    constructor(uint initialPrice) {
        owner = msg.sender;
        price = initialPrice;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not contract owner babe!");
        _;
    }

    modifier costs(uint _price) {
        require(msg.value >= _price, "Insufficient funds provided");
        _;
    }

    function register() public payable costs(price) {
        registeredAddress[msg.sender] = msg.value;
        emit Registration(msg.sender, msg.value);
    }

    function changePrice(uint _price) public onlyOwner {
        price = _price;
        emit PriceChange(_price);
    }
}
