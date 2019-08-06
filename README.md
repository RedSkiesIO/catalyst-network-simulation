## Catalyst Network Simulation
This project is to provide a simulation suite for the Catalyst Network. 

## Motivation
We split this project into three parts:
- Demonstration of security from 51% attack on the worker pools. 
- Demonstration of network latency and message propagation on the network 
- Demonstration of succesful propagation and production of peer lists during a ledger cycle to display succesful propagation. 

All of these simulations aim to allow the demonstration of the optimum parameters to be chosen when deploying the consensus mechanism demonstrated at [Insert link to Catalyst Consensus Paper]. We also demonstrate the accepted malicious node levels ($O$) that can be allowed in our network without fear of negative concequence for the network.
Message propagation and latency times 

## Code style
 
## Screenshots

## Tech/framework used

## Features

## Code Example

## Installation

This test suite requires the installation of several modules for python. It was primerally built using python 3.6. 

|Module|Install Command|Function|Link|
|---|---|---|---|
|Numpy|`pip install numpy`|	|https://numpy.org/ |
|Matplotlib|`pip install matplotlib`|	|https://matplotlib.org/ |
|Pybloom Live|`pip install pybloom-live`|Forked project from pybloom. Is used to generate bloom filters in python when looking at compressed data structures|https://github.com/joseph-fox/python-bloomfilter |
|zlib|	|	|https://www.zlib.net/	|
|glob|`pip install glob`|	|https://docs.python.org/3/library/glob.html |
|openpyxl|`pip install openpyxl`|	|https://openpyxl.readthedocs.io/en/stable/ |
|xlrd|`pip install xlrd`|	| http://www.python-excel.org/ |
|xlsx writer|`pip install XlsxWriter`|	|https://github.com/jmcnamara/XlsxWriter |

## Tests

## How to use?

## Contribute

## Credits

## License