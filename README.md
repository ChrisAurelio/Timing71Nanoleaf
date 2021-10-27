# Timing71 Nanoleaf LED Illuminator
This program takes advantage of Selenium and BeautifulSoup to parse information from the [Timing71](https://timing71.org/) live timing aggregator, and illuminates Nanoleaf LED panels based on the live flag status in a motorsports event using the [NanoleafAPI](https://pypi.org/project/nanoleafapi/).
* The replay implementation was developed using Selenium because of the need to interact with website elements.
* The live implementation uses BeautifulSoup and is the more stable version. 
* The replay implementation is a proof-of-concept build that was used as a foundation for the live version. 
* Although the program is designed for Nanoleaf panels, it can easily be modified for other smart lights with their respective APIs.
