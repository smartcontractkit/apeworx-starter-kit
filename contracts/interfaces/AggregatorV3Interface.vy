# @version ^0.3.3


@external
@view
def decimals() -> uint8:
    return 0


@external
@view
def description() -> String[1000]:
    return ""


@external
@view
def version() -> uint256:
    return 0


@external
@view
def getRoundData(_roundId: uint80) -> (uint80, int256, uint256, uint256, uint80):
    return (0, 0, 0, 0, 0)


@external
@view
def latestRoundData() -> (uint80, int256, uint256, uint256, uint80):
    return (0, 0, 0, 0, 0)


# Inline interface example:
# interface AggregatorV3Interface:
#     def decimals() -> uint8: view
#     def description() -> String[1000]: view
#     def version() -> uint256: view
#     def getRoundData(_roundId: uint80) -> (uint80, int256, uint256, uint256, uint80): view
#     def latestRoundData() -> (uint80, int256, uint256, uint256, uint80): view
