# ASCE V2365: Intro to Tibetan Civilization
Mapping geo-encoded .csv data for ASCE V2365: Intro to Tibetan Civilization Final Project

### The project can be found at [mappingtibetanculture.co](http://mappingtibetanculture.co).

#### Motivation:
One of the class assignments in our semester required us to work together as a class to locate centers of Tibetan culture around the world. I saw value in assimilating these datasets and attempting to map them to visualize the spread of Tibetan culture in the 21st century.

#### Process:
Each of the Teaching Assitants (TAs) for the course sent me the map contributions collected from their students as Excel .xls files. I first cleaned up all the data by organizing it under the following headers: `Name` of the site, `Foundation Date` (if known), `Affiliated Order`, `Street Address`, `City`, `State` and then attempted to group them by `Continent` and `Country`.

I then used [CartoDB](www.cartodb.com) to visualize the data I had. CartoDB has a very interesting functionality that allows it to geo-encode a given data set given on headers found in the tables. So using the street address, city, state and country, CartoDB was fairly accurately able to assign a latitude/longitude to each site in my table.

For this project, I focused on one region each in the United States (Bay Area), Europe (Greece/Italy) and Asia (Taiwan) to capture the widespread influence of Tibetan culture. Each of the maps used in the project are highly interactive: you can zoom in/out and click on each of the bubbles to learn more about that site. The bubbles each represent a site, color coded by the order the site is affiliated with. 
