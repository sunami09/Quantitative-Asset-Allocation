# Quantitative Asset Allocation: S&P 500 Index Constituent Portfolio Optimization

This Python-based financial engineering project utilizes real-time data from the S&P 500 index to construct a strategic asset allocation model for portfolio optimization.

## Overview

The project employs Python libraries such as urllib for handling URLs, json for parsing JSON data, pandas for data manipulation and analysis, and ssl for secure communication, to access and process live market data. It gathers the most recent market capitalization data for each S&P 500 constituent, calculates the weight of each stock in the index, and then determines the optimal number of shares to purchase for each equity to achieve a balanced portfolio allocation.

## API Responses

The project uses the Financial Modeling Prep API to fetch real-time data. Here's an example of the API response for the S&P 500 constituents:

```json
[
  {
    "symbol": "PANW",
    "name": "Palo Alto Networks",
    "sector": "Information Technology",
    "subSector": "Application Software",
    "headQuarter": "Santa Clara, California",
    "dateFirstAdded": "2023-06-20",
    "cik": "0001327567",
    "founded": "2005"
  },
  {
    "symbol": "AXON",
    "name": "Axon Enterprise",
    "sector": "Industrials",
    "subSector": "Aerospace & Defense",
    "headQuarter": "Scottsdale, Arizona",
    "dateFirstAdded": "2023-05-04",
    "cik": "0001069183",
    "founded": "1993"
  },
  {
    "symbol": "FICO",
    "name": "Fair Isaac",
    "sector": "Information Technology",
    "subSector": "Application Software",
    "headQuarter": "Bozeman, Montana",
    "dateFirstAdded": "2023-03-20",
    "cik": "0000814547",
    "founded": "1956"
  },
  ...
]
```

And here's an example of the API response for the quote data:

```json
[
  {
    "symbol": "PANW",
    "name": "Palo Alto Networks, Inc.",
    "price": 245.01,
    "changesPercentage": 0.8645,
    "change": 2.1,
    "dayLow": 238.87,
    "dayHigh": 248.6499,
    "yearHigh": 258.88,
    "yearLow": 132.22,
    "marketCap": 74937535510,
    "priceAvg50": 229.8716,
    "priceAvg200": 184.7445,
    "exchange": "NASDAQ",
    "volume": 3416820,
    "avgVolume": 6144908,
    "open": 239.71,
    "previousClose": 242.91,
    "eps": 0.66,
    "pe": 371.23,
    "earningsAnnouncement": "2023-08-21T00:00:00.000+0000",
    "sharesOutstanding": 305855008,
    "timestamp": 1690401600
  },
  {
    "symbol": "AXON",
    "name": "Axon Enterprise, Inc.",
    "price": 180.04,
    "changesPercentage": 0.0056,
    "change": 0.01,
    "dayLow": 176.31,
    "dayHigh": 180.765,
    "yearHigh": 229.95,
    "yearLow": 99.52,
    "marketCap": 13302308692,
    "priceAvg50": 194.401,
    "priceAvg200": 189.03735,
    "exchange": "NASDAQ",
    "volume": 627117,
    "avgVolume": 1167270,
    "open": 179.36,
    "previousClose": 180.03,
    "eps": 1.85,
    "pe": 97.32,
    "earningsAnnouncement": "2023-08-07T00:00:00.000+0000",
    "sharesOutstanding": 73885296,
    "timestamp": 1690401601
  }
  ...
]
```

## Code Explanation

The script begins by importing the necessary Python libraries and creating a secure SSL context. It then defines a function to send a request to a given URL and return the JSON data from the response.

The script fetches the S&P 500 data and quote data from the API and writes this data to JSON files. It creates a pandas DataFrame to store the fetched data and calculates the weight of each stock in the S&P 500 index and the number of shares to buy for each stock to achieve a balanced portfolio allocation.

The script then exports the DataFrame to a CSV file and an Excel file and creates a GUI to display the data.

## Portfolio Allocation

The script calculates the weight of each stock in the portfolio based on its market capitalization. This is not an equally weighted portfolio, where each stock would have the same weight. Instead, stocks with larger market capitalizations have a larger weight in the portfolio.

This approach is based on the theory that larger companies are more stable and less risky, so they should make up a larger portion of the portfolio. This can lead to better returns compared to an equally weighted portfolio.

Here's an example of the final result:

| Name                      | Symbol | Price  | Market Capitalization | Weight | Number of Shares to Buy | Portfolio Allocation |
|---------------------------|--------|--------|-----------------------|--------|-------------------------|----------------------|
| Palo Alto Networks, Inc. | PANW   | 245.01 | 74937535510           | 0.177  | 7                       | 1715.07              |
| Axon Enterprise, Inc.    | AXON   | 180.04 | 13302308692           | 0.031  | 1                       | 180.04               |
| ...                       | ...    | ...    | ...                   | ...    | ...                     | ...                  |

## Disclaimer

This tool is intended for educational and research purposes only. It is not a substitute for professional investment advice or independent factual verification. Always conduct your own due diligence or consult with a certified financial planner before making investment decisions.