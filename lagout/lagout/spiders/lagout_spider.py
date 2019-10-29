import logging
import scrapy

logging.basicConfig(level=logging.DEBUG)


class LagoutSpider(scrapy.Spider):
    name = 'lagout'  # the project name that identifies a crawl.
    start_urls = ['https://doc.lagout.org']  # start from home page.

    # inherit the 'parse' method from its parent class,
    # and override it with your own purpose.
    def parse(self, response):
        # locate all hyper links in every page that are crawled,
        # they are either a sub-directory, or a final e-book resource link,
        # for specific, an http link ending with a suffix like pdf or e-pub.
        # https://doc.lagout.org/security/2010_gdb.pdf
        for a in response.xpath('/html/body/pre/a'):
            link = a.attrib['href']
            if link == '../':
                # ignore parent hyper links in each page,
                # for sake of avoiding dead loops.
                logging.info('skipping parent link: %s' % link)
                continue

            # reformat non parent links.
            # sub-directories are ended with a '/', the others are final resources.
            link = response.urljoin(link)

            if link[-1] != '/':
                print(link)  # here is what we want, i.e. the final e-book resources.
            else:
                # use a generator to do further crawl jobs,
                # this results in a recursive directory walk,
                # which helps us retrieving all e-book resources on this website.
                logging.info('going to sub directory: %s', link)
                yield scrapy.Request(link, callback=self.parse)
