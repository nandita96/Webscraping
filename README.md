# Webscraping
Scraped Data from https://data.gov.ie/ (a open source repository for datasets) and extracted desirable dataset from it.
Scaped CSV dataset from website and converted it to JSON.

There are two main ways of extracting information from a website: use the website’s API and navigating to the destination terminal to scrape the output. The other is to enter the search key on the source machine web links for scraping. 
Used two ways of web scraping data one is to parse data from HTML or XML, and another is to define the web page URL you would like to scrape. Send a request for HTTP to specified URL and save the server response in a response object. Import Beautiful soup and import Request are two libraries used.

Understanding Code:
– request.get(url) is used to get the data from url link.
– Response.content -contains the information of that website which is assigned to W3Html variable.
– With beautiful soup we have performed parsing of W3Html and result is assigned to soup variable.
– For loop is used to fetch the actual link of education and industries from the near multiple link of main website.
