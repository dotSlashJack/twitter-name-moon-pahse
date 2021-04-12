# Add an emoji of the moon's current phase to your twitter name field

## Files

name_updater.py used to update your twitter name, calls moon_phase.py
moon_phase.py used to generate the moon's current phase using the ephem package

dependencies: datetime and ephem

NOTE: You must fill in your twitter keys for this to work. You shoud also update the "base_twitter_name" variable to your current (or desired) twitter name, not my name!

## Usage

Recommended: schedule a taks (using crontab, etc.) to automatically run name_updater.py

Manual: run moon_phase.py from the command line to manually update your bio (must be run each day)
