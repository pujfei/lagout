# How to use this project

## Prerequisites

1. You need to install Python 3.x on your computer. Download the latest Python [here]( https://www.python.org/downloads/ ).

2. Install python-pip tool following the instructions [here]( https://pip.pypa.io/en/stable/installing/ ).

3. Install the scrapy module with pip by running:

   `pip install scrapy` on Windows, or:

   `python -m pip install --user scrapy` on linux.

## Quick Demonstration

If in case you have already done the scrapy preparation stuff, all that you need is clone the repository to your local disk, and type these commands on your cmd or bash console:

```bash
cd lagout
scrapy crawl lagout
```

where lagout is the task name of the crawl project.

## Detailed Description

1. To start a new scrapy project, just run:

   `scrapy startproject lagout`

2. Now we have a scrapy project called "lagout" which is built from the scrapy built-in templates, what we need to do is create a new file in the lagout/lagout/spiders directory, let's say "lagout_spider.py". In this file, write the crawler process according to your customized purposes.
3. For further knowledge, the latest scrapy documentation is [here]( https://docs.scrapy.org/en/latest/ ), and a handy scrapy tutorial is [here]( https://docs.scrapy.org/en/latest/intro/tutorial.html ).