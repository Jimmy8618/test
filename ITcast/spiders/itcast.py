# -*- coding: utf-8 -*-
import scrapy
from ITcast.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    # 设置name
    name = 'itcast'
    # 设定域名
    allowed_domains = ['itcast.cn']
    # 填写爬取地址
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml',]

    # 编写爬取方法
    def parse(self, response):
        # 实例一个容器保存爬取的信息
        item = ItcastItem()

        # with open("teacher.html","w") as f:
        #     f.write(response.text)
       # print response.body
       # pass
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        # 先获取每个课程的div
        node_list = response.xpath("//div[@class='li_txt']")
        for node in node_list:
            # name = node.xpath("./h3/text()").extract()
            # title = node.xpath("./h4/text()").extract()
            # info = node.xpath("./p/text()").extract()
            item['name'] = node.xpath("./h3/text()").extract()
            item['title'] = node.xpath("./h4/text()").extract()
            item['info'] = node.xpath("./p/text()").extract()

            # 返回信息
            yield item

