// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;

import './DistributorNative.sol';

contract DistributorNativeFactory {

    mapping (uint => address)     public indexesToContracts;
    uint                          public contractsCount;

    function create() public returns (address) {
        DistributorNative distributorContract = new DistributorNative(msg.sender);

        indexesToContracts[contractsCount] = address(distributorContract);
        contractsCount++;

        return address(distributorContract);
    }

    function getAll() public view returns (address[] memory) {
        address[] memory distributors = new address[](contractsCount);

        for (uint i; i < contractsCount; i++) {
            distributors[i] = address(indexesToContracts[i]);
        }

        return distributors;
    }
}