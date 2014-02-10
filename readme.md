# DextrousFOTO
## By Adam Jeanes

## About

This web application allows for searching Instagram by hashtag and to mark certain images as favourites or to remove them, which will remove the image from the main listing. If you have mistakenly removed an image, you can click on removed images on the top bar, which will show the blocked images with a button underneath each that allows you to unblock the image. This web app also features auto hotlinking of hashtag, clicking them will cause the webapp to search for that hashtag.

##Configuration

The web app server requires a configuration file in a file called settings.json which is a sing JSON string containing your Instagram Client ID and your Instagram Secret and is laid out as such:

...
{"Client_Secret": "YOUR_CLIENT_SECRET", "Client_ID": "YOUR_CLIENT_ID"}
...

The web app is currently configured to obtain the settings from my personal server and will require changing at lines 17 and 36