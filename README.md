# inky-coffee

I have a Raspberry Pi B connected to a Pimoroni inkyWHAT e-ink display next to my coffee machine.
It's intended to let anyone who comes for a coffee in the morning know important information for the day.

Our caffeine-starved heroes should be able to see, at a glance:
* The expected weather for the day
* Any reminders or notes they've set for each other
* Happy birthday messages
* Other automated reminders (e.g. that public holidays are a thing or are coming up soon)

The inky-coffee device will rotate through images every 2 minutes.
Images are pulled from a Dropbox folder ever 2 minutes, formatted for display every 2 minutes, and then, every 2 minutes, a random image is selected.

As new images are added to the Dropbox folder, inky-coffee will convert them to something the e-ink screen can display (including resizing, cropping and dithering). It should only do this work if the image has actually changed.

Currently, images are not deleted or renamed on the pi, so it's best to keep overwriting the same image files. Eventually I plan to use timestamps to determine what should display on a given day.

## Requirements

You will need:

* A Raspberry Pi with an InkyWHAT display
* [Pimoroni Inky](https://github.com/pimoroni/inky) libraries installed
* [Dropbox-Uploader](https://github.com/andreafabrizi/Dropbox-Uploader)
* A Dropbox app setup, you'll need the key to sync files, which will live in ~/.dropbox_uploader
* This repo cloned on the Pi
* Set up your crontab with `crontab -e` using crontab.example or something like it

## crontab

See crontab.example for how I'm using this to pull files from a Dropbox folder using [Dropbox-Uploader](https://github.com/andreafabrizi/Dropbox-Uploader).

## TODO

- [ ] Configuration files and/or scripts for inky-coffee, rather than hardcoding directories in pythons scripts ;)

- [ ] Inky-coffee should iterate through available files rather than randomly selecting one

- [ ] After we do a dropbox sync, we should know if we have files to format, and we should only format new/changed files at that point in time (e.g. `sync.py` should do more heavy lifting)

- [ ] File names should have optional timestamps so we can determine what files to show on what days

- [ ] If a file is removed from the Dropbox folder, inky-coffee should likewise remove it, and any versions of it that have been formatted for display

- [ ] Better logging and optional alerting for problems

- [ ] More interesting options for display things - like the current weather or reminders from a text file, in addition to image files (though these could be done as separate scripts that generate new images to display)