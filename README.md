# ScraperLaRepublica
This is a web scraping project for the Colombian media La Republica

What was done was to do a web scraping to extract the links of each news that is published on the current day. We can see this code in the file escraper.py.
For this we created the following Xphats:

links= $x('//div[contains(@class, "V")]/a[contains(@class, "kicker")]/@href').map(x=>x.value)

Title = $x('//div[@class="mb-auto"]/h2/span/text()').map(x=>x.wholeText)

Summary = $x('//div[@class = "lead"]/p/text()').map(x=>x.wholeText)

Body = $x('//div[@class = "html-content"]/p[not (@class)]/text()').map(x=>x.wholeText)

The next thing that was done is for each particular link to bring the title, summary, body and save it in a folder whose name is the date of the day the download is made. This download will create a .txt file of each news in particular and thus in the future to be able to analyze the dynamics and most recurrent themes of the news published by the newspaper.
