# oobastats
A simple extension for oobabooga text-generation-webui that will log basic information about usage.

## Usage
Download the repo as a zip, extract the `statistics` folder to your extensions, and add `--extension statistics` to CMD_FLAGS.txt

## What is logged
Number of prompts and responses, token count of prompts and responses, character count of prompts and responses, and generation time. The logged generation time may deviate a bit from actual generation time.

## What is 'averages.jar' for?
averages.jar is a small program to calculate the average of the logged data. Run it with `java -jar averages.jar` in the same directory as your statistics.json.
