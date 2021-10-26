
### Documentation-Downloader iterates through all pages of the Selenium homepage and retrieves the sought-after text content, returning it to a file.




## GLOBAL VARIABLES


# Selenium documentation home page

url = https://www.selenium.dev/documentation/




## IMPORT LIBRARIES


# Uses urllib to fetch the HTML
from urllib.request import urlopen


# Uses Beautiful Soup to select which text elements to include.
import bs4




# STEP 1: Trawl through the homepage to generate the list of links FROM THE TABLE OF CONTENTS.


  # STEP 1a: IDENTIFY THE BEAUTIFUL SOUP ELEMENT OF THESE LINKS
  
  
    # NEXT ACTION: FIGURE OUT WHERE IN THE HTML THE LINKS ARE.



