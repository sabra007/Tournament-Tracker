# Tournament-Tracker

## Introduction
Tournaments are common - eSports, eating contests, playoff games, and chess are a few examples of sources of tournaments where people compete to be ranked, in hopes of being the best. Some tournaments are so competitive to the point that participants want to have a particular starting spot in the signups.

You will be designing a text-based application to run a tournament.

## High Level Requirements
The application user is the tournament administrator.

- Since tournaments may have a variable amount of participants, gather that up front.
- The administrator can add participants to a particular starting slot.
- In order to cancel a participant, the administrator needs to enter both the starting slot and participant name.
- The administrator can list participants in the order of their starting slots.
- The registrations should be stored in a CSV.


## Technical Requirements

- Use None to represent empty values. Do not use an empty string to represent these values.
- Participant names are a single string. Do not put first and last names in separate values.
- There will be at least 1 loop and at least 1 function.

## Stretch Goals

- Allow searching for a single participant and return their starting position.
- Separate names by first and last name. Allow printing participants and their starting spots alphabetically by last name.
- Allow saving and loading of multiple tournaments' participants lists.
- Save files in JSON to be stored in a non-relational database.

![Tournament Tracker Flowchart drawio](https://user-images.githubusercontent.com/31526195/147114340-df8443a5-def5-445e-b347-b5128bee2a3c.png)
