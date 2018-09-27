# 📰📂DownloadingAmerica📂📰

A Python script for bulk downloading individual plain text files from the [Library of Congress's Chronicling America](https://chroniclingamerica.loc.gov/).

Given a Chronicling America search result, this will download the plain text of each page into its own text file, write some of the metadata to a csv file, and create a readme that explains the search.

## Dependencies
To use this, you'll need to have Python 3 installed, and access to some kind of command line interface [I'd recommend Terminal on OS X or Anaconda on Windows].

## Instructions
Create a folder where you want your text files to live. [Your life will be better if this folder is empty.]

Save the downloadingamerica.py file in that folder.

Using a command line interface [Terminal (Mac OS X) or Anaconda Prompt (Windows)], navigate to the folder. [For a folder named 'chronam' on the Desktop, you would type `cd Desktop/chronam`]

Run the script (type `python downloadingamerica.py` )

It will ask for a URL. Paste in the regular results URL from any Chronicling America search result page and hit enter.

## Notes
This is very much in beta and has only been tested with a few different search scenarios. It's possible that extremely large results will break it.

Some newspapers are missing key metadata (such as page numbers) which may result in files overwriting themselves. Be sure to check your results.

### Next Steps
I'm open to hearing feedback if there is anything people would like to have changed. At some point I would like to parse the search query to make a nicer looking readme, but that will wait another day.
