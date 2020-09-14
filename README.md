# inky-coffee

I have a Raspberry Pi B connected to a Pimoroni inkyWHAT e-ink display next to my coffee machine.
It's intended to let anyone who comes for a coffee in the morning know important information for the day.

Our caffeine-starved heroes should be able to see, at a glance:
* The expected weather for the day
* Any reminders or notes they've set for each other
* Happy birthday messages
* Other automated reminders (e.g. that public holidays are a thing or are coming up soon)

The inky-coffee device will rotate through images every 1 minute. At the very least, it will display the day's weather forecast, and if there's any images in a shared dropbox folder, it will try to display those. If the image has a date on it, it will only show that image on the relevant date. Examples:

2020-01-11-happy-birthday-andy.png
2020-12-25-merry-christmas.png
notes.png
weather.png

As new images are added to the Dropbox folder, inky-coffee will convert them to something the e-ink screen can display (including resizing, cropping and dithering). It should only do this work if the image has actually changed.

Weather images will be automatically generated by another script (?)

## crontab

To sync files from Dropbox every 2 minutes, I'm doing:

```
*/2 * * * * /home/pi/Dropbox-Uploader/dropbox_uploader.sh -f /home/pi/.dropbox_uploader -s download ./ /home/pi/Documents/inky-coffee
```