# 📰📂DownloadingAmerica📂📰

A Python script for bulk downloading individual plain text files from the [Library of Congress's Chronicling America](https://chroniclingamerica.loc.gov/).

Given a Chronicling America search result, this will download the plain text of each page into its own text file, write some of the metadata to a csv file, and create a readme that explains the search.

## Output
**YYYYMMDD_title_edition_sequence.txt**: each newspaper page's OCR text will go into a text file with a name following this format—all characters besides letters, numbers, and underscores is stripped from this title.
**metadata.csv**: filename, title (newspaper title), date, edition, sequence (e.g. 1st image in edition, 2nd, 3rd), city, county, state, page_url (this will bring you to the page's ChronAm interface)
**readme.txt**: this is intended to help you keep your data documented—it includes the (local) date and time you did the search, the number of results, URLs for the ChronAm interface & JSON file, a (rough) account of your search input, and a reminder that you used this script to do it

## Dependencies
To use this, you'll need to have Python 3 installed, and access to some kind of command line interface [I'd recommend Terminal on OS X or Anaconda on Windows].

## Instructions
Create a folder where you want your text files to live. [Your life will be easier if this folder is empty.]

Save the downloadingamerica.py file in that folder.

Using a command line interface [Terminal (Mac OS X) or Anaconda Prompt (Windows)], navigate to the folder. [For a folder named 'chronam' on the Desktop, you would type `cd Desktop/chronam`]

Run the script [type `python downloadingamerica.py`]

It will ask for a URL. Paste in the search results URL from any Chronicling America search page and hit enter. If everything goes ok, you probably won't see changes in the command prompt right away, but you should see your folder filling up with files pretty quickly.

*Do keep in mind that if you want to do multiple searches, you'll either want to delete all prior results, or move the script into a different folder!*

## Customization
I'm going to add more information about how to read and process the JSON to customize your filenames and metadata. For now, just play around or file an issue!

## Limitations & Notes
This is set up to look for OCR in English. If that field is empty for any page in the results, this will break. [I'm hoping to fix that—for now you can make sure you're doing a text search, or add 'a OR e OR i OR o OR u' if you want everything with text.] If you're looking for a different language, replace `ocr_eng` with the language of your choice.

The metadata for city, county, and state only print the first value in the record—this could be a problem if there are multiple city/county/states, or if the first value isn't the information you're looking for. In testing, I only came across papers with single values, but that is probably not universal.

This is very much in beta and has only been tested with a few different search scenarios. So far, it has been able to handle over 3k pages in a query without problems.

Some newspapers are missing key metadata which may result in blank metadata or filenaming issues.

### Next Steps
I'm open to hearing feedback if there is anything people would like to have changed. At some point I would like to parse the search query to make a nicer looking readme, but that will wait another day. Feel free to file a ticket if you have questions or suggestions!

If you're making use of this, I'd love to know! My Github username is also my Twitter handle and my Gmail address.
